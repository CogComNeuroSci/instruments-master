from psychopy import core

import time
import datetime

from time import sleep
from time import gmtime, strftime
from datetime import datetime


#####################
## Wait function 1 ##
#####################

print("# Wait function 1 #")

## The most basic function when it comes to time delay is 'time.sleep()'
## This function lets the program that you are running wait with the amount of seconds you specify between the brackets
## In the code below, we have a print function which prints every two seconds
## This type of set-up can be used to let Python do a certain action after a certain amount of time 

for i in range(5):
    time.sleep(2)
    print("I print this sentence every 2 seconds")


#####################
## Wait function 2 ##
#####################

print("# Wait function 2 #")

## Another example of the use of timing is the measurement of reaction times 
## We can define time using the datetime.now() function, which returns you the exact time based on the time of your computer
## If we measure the time two times, and we subtract the later time from the earlier time, we can also use this as a reaction time measurement
## However, we should keep in mind that the reaction time can also be measured using specific PsychoPy software, an example of this could be:
    ## trial_timer = core.Clock() 
    ## trial_timer.reset()
    ## event.getKeys(timeStamped = trial_timer)
## In that specific case, we use the function core.clock (to define a clock from this time on) to define a 'trial timer', 
## and this can be used to write away the time when a keyboard key is pressed
    ## The function 'event.getKeys' registers when a keyboard response is given
## This PsychoPy functionality can of course be very handy when collecting data, as it provides a built-in function to register reaction time
## The example below shows how we can measure passed time without PsychoPy

t1 = datetime.now()
t2 = datetime.now()

RT = t2 - t1
print(RT)


#####################
## Wait function 3 ##
#####################

print("# Wait function 3 #")

## When looking at the PsychoPy documentation, we see that some other functions involving time are offered
## An example of this is the 'core.wait()' function, which strongly resembles the time.sleep() function discussed earlier
## 'core.CountdownTimer()' is a function that can be used to count down, as the name already tells us
## When we use the extension .add on a clock, this means that we add extra time, which may come in handy when using a count down timer
## We strongly recommend to take a look at the demo on timing, which can be found in PsychoPy:
    ## Demos > Timing > clocksAndTimers.py
## The commands noted below in essence do the same: they all wait for 500 milliseconds
## The last two commands add an amount of time to the CountDown clock

t1 = datetime.now()
core.wait(0.5)
time.sleep(0.5)
core.CountdownTimer(0.5)
t2 = datetime.now()

RT = t2 - t1
print(RT)

CountDown = core.CountdownTimer()
CountDown.add(.5)


#########
## END ##
#########