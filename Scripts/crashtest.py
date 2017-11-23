# Code for crashing cars
# by Esther De Loof & Tom Verguts, nov 2017
# part 1: initialisation
from psychopy import visual,event
from time import sleep
import numpy as np
from numpy import random
n_trials = 5
max_time = 10 # measured in seconds
step_size=0.1
win = visual.Window([500,400])
pos_car_blue_start=(-0.5,0)
pos_car_green_start=(0.5,0)
blue_counter=0
green_counter=0
car_blue = visual.Circle(win,lineColor="blue",fillColor="blue",pos=pos_car_blue_start,size=0.1)
car_green=visual.Circle(win,lineColor="green",fillColor="green",pos=pos_car_green_start,size=0.1)
wall_width=0.1*2 # 10% of screen width
wall_height=0.2*2 # 20% of screen height
wall=visual.Rect(win,width=wall_width,height=wall_height,lineColor="red",fillColor="red")
bots_text = visual.TextStim(win,text="Botsing!!")

# part 2: driving around
for loop in range(n_trials):
    trial_text = visual.TextStim(win,text="trial "+str(loop+1)+"!")
    trial_text.draw()
    win.flip()
    sleep(0.5)
    time=0
    crash=False
    car_blue.pos=pos_car_blue_start
    car_green.pos=pos_car_green_start
    while crash == False and time<max_time:
        time=time+0.05 # time scale
        car_blue.pos=car_blue.pos+step_size*(2*random.randint(0,2,2)-1)
        car_green.pos=car_green.pos+step_size*(2*random.randint(0,2,2)-1)
        # check boundary conditions
        car_blue.pos[0]=np.maximum(car_blue.pos[0],-1)
        car_blue.pos[1]=np.maximum(car_blue.pos[1],-1)
        car_green.pos[0]=np.maximum(car_green.pos[0],-1)
        car_green.pos[1]=np.maximum(car_green.pos[1],-1)
        car_blue.pos[0]=np.minimum(car_blue.pos[0],+1)
        car_blue.pos[1]=np.minimum(car_blue.pos[1],+1)
        car_green.pos[0]=np.minimum(car_green.pos[0],+1)
        car_green.pos[1]=np.minimum(car_green.pos[1],+1)
        wall.draw()
        car_blue.draw()
        car_green.draw()
        win.flip()
        # check wall hitting
        if np.absolute(car_blue.pos[0])<wall_width/2 and np.absolute(car_blue.pos[1])<wall_height/2:
            crash = True
            blue_counter += 1
            bots_text.color="blue"
            bots_text.draw()
            win.flip()
            sleep(1)
        if np.absolute(car_green.pos[0])<wall_width/2 and np.absolute(car_green.pos[1])<wall_height/2:
            crash = True
            green_counter += 1
            bots_text.color="green"
            bots_text.draw()
            win.flip()
            sleep(1)
        sleep(0.1)    
    if "f" in event.getKeys():
        break
    
# part 3: print results on screen and finish
win.flip()
if blue_counter==0 and green_counter==0:
    to_print = "Er is niet gebotst!"
elif blue_counter==green_counter:
    to_print = "Ze zijn even vaak gebotst!"
elif blue_counter>green_counter:
    to_print = "De blauwe is vaker gebotst!"
else:
    to_print = "De groene is vaker gebotst!"
text = visual.TextStim(win,text=to_print)
text.draw()
win.flip()
sleep(1)
win.close()