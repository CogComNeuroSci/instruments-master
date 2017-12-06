# Code for crashing cars
# by Esther De Loof & Tom Verguts, nov 2017

# part 1: loading modules
from psychopy import visual,event
from time import sleep
import numpy as np
from numpy import random

# part 2: initialization
n_trials = 5
max_time = 10 ## measured in seconds
step_size = 0.1*2 ## 10% of screen
step_time = 0.1
pos_car_blue_start = (-0.5,0)
pos_car_green_start = (0.5,0)
blue_counter = 0
green_counter = 0
wall_width = 0.1*2 ## 10% of screen width
wall_height = 0.2*2 ## 20% of screen height

# part 3: prepare graphic elements
win = visual.Window([500,400])
car_blue = visual.Circle(win,lineColor="blue",fillColor="blue",pos=pos_car_blue_start,size=0.1)
car_green = visual.Circle(win,lineColor="green",fillColor="green",pos=pos_car_green_start,size=0.1)
##car_blue = visual.ImageStim(win, image = "Car_blue.png", pos=pos_car_blue_start, size=0.2)
##car_green = visual.ImageStim(win, image = "Car_green.png", pos=pos_car_green_start, size=0.2)
wall = visual.Rect(win,width=wall_width,height=wall_height,lineColor="red",fillColor="red")
crash_text = visual.TextStim(win,text="Botsing!")

# part 4: driving around
for trial in range(n_trials):
    
    ## Display the trial number
    trial_text = visual.TextStim(win,text="trial "+str(trial+1)+"!")
    trial_text.draw()
    win.flip()
    sleep(0.5)
    
    ## Initialize variables for this trial
    time = 0
    crash = False
    car_blue.pos = pos_car_blue_start
    car_green.pos = pos_car_green_start
    
    while crash == False and time < max_time:
        
        ## Update variables at this moment in time
        time = time+step_time
        car_blue.pos = car_blue.pos+step_size*(2*random.randint(0,2,2)-1)
        car_green.pos = car_green.pos+step_size*(2*random.randint(0,2,2)-1)
        
        ## Check boundary conditions at this moment in time
        car_blue.pos[0] = np.maximum(car_blue.pos[0],-1)
        car_blue.pos[1] = np.maximum(car_blue.pos[1],-1)
        car_green.pos[0] = np.maximum(car_green.pos[0],-1)
        car_green.pos[1] = np.maximum(car_green.pos[1],-1)
        car_blue.pos[0] = np.minimum(car_blue.pos[0],+1)
        car_blue.pos[1] = np.minimum(car_blue.pos[1],+1)
        car_green.pos[0] = np.minimum(car_green.pos[0],+1)
        car_green.pos[1] = np.minimum(car_green.pos[1],+1)
        
        ## Display wall and cars at this moment in time
        wall.draw()
        car_blue.draw()
        car_green.draw()
        win.flip()
        sleep(step_time)
        
        ## Check wall hitting
        if np.absolute(car_blue.pos[0])<wall_width/2 and np.absolute(car_blue.pos[1])<wall_height/2:
            
            crash = True
            blue_counter += 1
            crash_text.color="blue"
            crash_text.draw()
            win.flip()
            sleep(1)
            
        if np.absolute(car_green.pos[0])<wall_width/2 and np.absolute(car_green.pos[1])<wall_height/2:
            
            crash = True
            green_counter += 1
            crash_text.color="green"
            crash_text.draw()
            win.flip()
            sleep(1)
        
        ## Escape function to get out of infinite while loop
        if "f" in event.getKeys():
            break

# part 5: print results on screen and finish
if blue_counter==0 and green_counter==0:
    feedback = "Er is niet gebotst!"
elif blue_counter==green_counter:
    feedback = "Ze zijn even vaak gebotst!"
elif blue_counter>green_counter:
    feedback = "De blauwe is vaker gebotst!"
else:
    feedback = "De groene is vaker gebotst!"
feedback_text = visual.TextStim(win,text=feedback)
feedback_text.draw()
win.flip()
sleep(3)
win.close()