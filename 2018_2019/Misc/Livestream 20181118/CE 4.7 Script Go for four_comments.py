#Bitcoin oefening

#import
from psychopy import visual
from numpy import random
import time

#windows
## Esther: just to be sure, don't start with the fullscreen option, especially when you have a while-loop
win=visual.Window(fullScreen=True)

#initialization
## Esther: basically removed everything ;)

#coding
## Esther: a for-loop is not the ideal appraoch to having four investments in a horse race against each other
## Esther: what would be a better solutions?
## Esther: also, you're missing a fourth graph
for graphs in range (3):

    ## Esther: by positioning this code here, you can remove it at the top and bottom of the script
    bitcoin       =1               ##Bitcoin for the changing value
    x1            =-0.9           ## for x, we will make steps of 0.04
    bitcoin_values=[]
    text_bitcoinvalue=visual.TextStim(win)

    ## Esther: the idea is that on each time step there is a random increase, not only for each coin
    ## Esther: also, as we are not using the mean and standard deviation anywhere else, I've just inserted them here
    increase=random.normal(10,2.5)/100

    while bitcoin<100:
        

        #BITCOINLINE
        ##y2
        bitcoin2=bitcoin+(bitcoin*increase)
        ##x2 takes the value +.1 x1 and y2 the new value of bitcoin
        x2= x1+0.025

        ##text_bitcoinvalue
        text_value=visual.TextStim(win,text='{0:.2f} euros'.format(bitcoin),pos=(0,0.7),color=(0+bitcoin/115,0,1-bitcoin/115))

        ## Esther: nice approach of storing the values: a list of tuples
        bitcoin_values.append(((x1,bitcoin/10),(x2,bitcoin2/10)))

        ##assign new value to bitcoin and x
        bitcoin=bitcoin2
        x1=x2
        
        ##make bitcoinline
        ## Esther: unfortunately, this approach does not allow for a color transition across time
        ## Esther: at this point you'll also maybe want to reconsider the data type for the bitcoin values
        bitcoinline=visual.ShapeStim(win,lineColor=(0+bitcoin/115,0,1-bitcoin/115)
                                    ,units='norm',vertices=bitcoin_values, pos = (0.5,-0.5))
        ## Esther: this line of code can already be included in the code above
        #bitcoinline.pos = (0.5, -0.5)

        #DRAW
        text_value.draw()
        bitcoinline.draw()
        win.flip()
        time.sleep(0.1)