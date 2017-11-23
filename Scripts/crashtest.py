# Code for crashing cars
# by Esther De Loof & Tom Verguts, nov 2017
# part 1: initialisation
from psychopy import visual
from time import sleep
import numpy as np
from numpy import random
max_time = 10 # measured in seconds
step_size=0.2
win = visual.Window([500,400])
pos_car_blue_start=(-0.5,0)
pos_car_red_start=(0.5,0)
car_blue = visual.Circle(win,lineColor="blue",fillColor="blue",pos=pos_car_blue_start,size=0.1)
car_green=visual.Circle(win,lineColor="green",fillColor="green",pos=pos_car_red_start,size=0.1)
wall_width=0.02*2 # 2% of screen width
wall_height=0.2*2 # 20% of screen height
wall=visual.Rect(win,width=wall_width,height=wall_height,lineColor="red",fillColor="red")
# part 2: driving around
time=0
crash=False
while crash == False and time<max_time:
    time=time+0.1 # 100 msec per timestep
    car_blue.pos=car_blue.pos+step_size*random.randn(2)
    car_green.pos=car_green.pos+step_size*random.randn(2)
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
# part 3: print results on screen and finish
sleep(1)
win.close()