# Code for catching butterflies
# by Esther De Loof & Tom Verguts, dec 2017

# part 1: loading modules
from psychopy import visual,event,core
from time import sleep
import numpy as np
from numpy import random

# part 2: initialization
n_trials = 5
max_time = 10 ## measured in seconds
step_size = 0.1*2 ## 10% of screen
step_time = 0.1
pos_bfly_blue_start = (-0.5,0)
pos_bfly_green_start = (0.5,0)
blue_counter = 0
green_counter = 0
my_clock = core.Clock()
colors = ["blue","green"]

# part 3: prepare graphic elements
win = visual.Window([500,400])
bfly_blue = visual.Circle(win,lineColor="blue",fillColor="blue",pos=pos_bfly_blue_start,size=0.1)
bfly_green = visual.Circle(win,lineColor="green",fillColor="green",pos=pos_bfly_green_start,size=0.1)
catcher = visual.Circle(win, radius=30, edges=13, units='pix')
target_text = visual.TextStim(win,text="")
slow_text = visual.TextStim(win,text="Too slow!")
catch_text = visual.TextStim(win,text="Caught!")
mouse = event.Mouse()

# part 4: flying around
for trial in range(n_trials):
    
    ## Display the trial number
    trial_text = visual.TextStim(win,text="trial "+str(trial+1)+"!")
    trial_text.draw()
    win.flip()
    sleep(0.5)
    
    ## Display which butterlfy to catch
    target = random.choice(colors)
    target_text.text = "Catch the {0} butterfly!".format(target)
    target_text.draw()
    win.flip()
    sleep(1)
    
    ## Initialize variables for this trial
    time = 0
    catch = False
    bfly_blue.pos = pos_bfly_blue_start
    bfly_green.pos = pos_bfly_green_start
    
    while catch == False:
        
        ## Update variables at this moment in time
        time = time+step_time
        bfly_blue.pos = bfly_blue.pos+step_size*(2*random.randint(0,2,2)-1)
        bfly_green.pos = bfly_green.pos+step_size*(2*random.randint(0,2,2)-1)
        
        ## Check boundary conditions at this moment in time
        bfly_blue.pos[0] = np.maximum(bfly_blue.pos[0],-1)
        bfly_blue.pos[1] = np.maximum(bfly_blue.pos[1],-1)
        bfly_green.pos[0] = np.maximum(bfly_green.pos[0],-1)
        bfly_green.pos[1] = np.maximum(bfly_green.pos[1],-1)
        bfly_blue.pos[0] = np.minimum(bfly_blue.pos[0],+1)
        bfly_blue.pos[1] = np.minimum(bfly_blue.pos[1],+1)
        bfly_green.pos[0] = np.minimum(bfly_green.pos[0],+1)
        bfly_green.pos[1] = np.minimum(bfly_green.pos[1],+1)
        
        ## Reset the clock to catch the butterfly in 0.1 seconds
        my_clock.reset() 
        
        while my_clock.getTime() < step_time and catch == False:
            
            ## Register the position of the mouse
            catcher.pos = mouse.getPos() * win.size / 2  # follow the mouse
            
            ## Display butterflies at this moment in time
            bfly_blue.draw()
            bfly_green.draw()
            catcher.draw()
            win.flip()
            
            ## Check whether the butterflies are caught
            if bfly_blue.overlaps(catcher) and target == "blue":
                catch = True
                blue_counter += 1
                catch_text.color="blue"
                catch_text.draw()
                win.flip()
                sleep(1)
                
            if bfly_green.overlaps(catcher) and target == "green":
                catch = True
                green_counter += 1
                catch_text.color="green"
                catch_text.draw()
                win.flip()
                sleep(1)
                
        ## Escape the while loop when the time is up
        if time >= max_time:
            slow_text.draw()
            win.flip()
            sleep(1)
            break
            
        ## Escape function to get out of infinite while loop
        if "f" in event.getKeys():
            break

# part 5: print results on screen and finish
if blue_counter==0 and green_counter==0:
    feedback = "Er zijn geen vlinders gevangen!"
elif blue_counter==green_counter:
    feedback = "Ze zijn even vaak gevangen!"
elif blue_counter>green_counter:
    feedback = "De blauwe is vaker gevangen!"
else:
    feedback = "De groene is vaker gevangen!"
feedback_text = visual.TextStim(win,text=feedback)
feedback_text.draw()
win.flip()
sleep(3)
win.close()