from psychopy import visual, event, core, gui, data
import time, numpy
import os

nblocks     = 12
ntrials     = 60
Centrekeys  = (0,0)
Rightkeys   = (0,250)
blockdirection  
blockposition 

nReps = int(nBlockTrials/(2*3))

CorResp





if position == 0
    Instructions.Text = (                       "In this experiment you will see arrows < or > \n" +
                                                "presented in a random order and on a random position left, centre or on the right of the window.\n\n" +
                                                "You have to respond to the direction of the arrows or to the position\n" +
                                                "You can use the following four response buttons (left, down and right arrows\n" +"If the arrow is presented at the left part of the window, press “Leftarrow”.\n" +
                                                "If the arrow is presented at the centre part of the window, press “Downarrow”.\n" +
                                                "If the arrow is presented at the right part of the window, press “Rightarrow”.\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                                "Any questions?", height = 0.05)
                                                "Press spacebar to continue"
else
    Instruction.Text = (                        "In this experiment you will see arrows < or > \n" +
                                                "presented in a random order and on a random position left, centre or on the right of the window.\n\n" +
                                                "You have to respond to the direction of the arrows or to the position\n" +
                                                "You can use the following four response buttons (left, down and right arrows\n" +"If this arrow < is presented, press “Leftarrow”.\n" +
                                                "If this arrow > is presented, press “Rightarrow”.\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                                "Any questions?", height = 0.05)
                                                "Press spacebar to continue"


my_clock = core.Clock()

event.waitKeys(keyList = "space")
event.waitKeys(keyList = "space")
        my_clock.reset()
        RT = my_clock.getTime()