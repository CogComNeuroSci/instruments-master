#Bitcoin oefening

#import
from psychopy import visual
from numpy import random
import time


#windows
win=visual.Window(fullScreen=True)

#initialization
bitcoin       =1               ##Bitcoin for the changing value
x1            =-0.9           ## for x, we will make steps of 0.04
bitcoin_values=[]
text_bitcoinvalue=visual.TextStim(win)
mu= 10
sigma= 2.5
i=0


#coding
for graphs in range (3):

    increase=random.normal(mu,sigma)/100

    while bitcoin<100:
        

        #BITCOINLINE
        ##y2
        bitcoin2=bitcoin+(bitcoin*increase)
        ##x2 takes the value +.1 x1 and y2 the new value of bitcoin
        x2= x1+0.025

        ##text_bitcoinvalue
        text_value=visual.TextStim(win,text='{0:.2f} euros'.format(bitcoin),pos=(0,0.7),color=(0+bitcoin/115,0,1-bitcoin/115))

        bitcoin_values.append(((x1,bitcoin/10),(x2,bitcoin2/10)))

        ##assign new value to bitcoin and x
        bitcoin=bitcoin2
        x1=x2
        
        ##make bitcoinline
        bitcoinline=visual.ShapeStim(win,lineColor=(0+bitcoin/115,0,1-bitcoin/115)
                                    ,units='norm',vertices=bitcoin_values)
        bitcoinline.pos = (0.5, -0.5)
        
        #it's another round!
        i=i+1

        #DRAW
        text_value.draw()
        bitcoinline.draw()
        win.flip()
        time.sleep(0.1)

    bitcoin       =1               ##Bitcoin for the changing value
    x1            =-0.9           ## for x, we will make steps of 0.04
    bitcoin_values=[]
    text_bitcoinvalue=visual.TextStim(win)
