import time, datetime
from datetime import datetime
from psychopy import core, event


#####################
## Wait function 1 ##
#####################

print("# Wait function 1 #")

## The most basic function when it comes to time delay is 'time.sleep()'.
## This function lets the program that you are running wait for the number of seconds you specify between the brackets.
## In the code below, we have a print function which is executed every two seconds.
## This type of setup can be used to let Python do a certain action after a certain amount of time.

for i in range(5):
    time.sleep(2)
    print("I print this sentence every 2 seconds")


#####################
## Wait function 2 ##
#####################

print("# Wait function 2 #")

## Another example of the use of timing is the measurement of reaction times.
## We can define time using the datetime.now() function, which returns you the exact time based on the time of your computer.
## If we measure the time twice, and we subtract the later time from the earlier time, we can also use this as a reaction time measurement.
## However, we should keep in mind that the reaction time can also be measured using specific PsychoPy functions (the core functions), an example of this could be:

trial_timer = core.Clock() 
trial_timer.reset()
time.sleep(2)
key = event.getKeys(timeStamped = trial_timer)
print("Your reaction time is {0:.2f} seconds.".format(trial_timer.getTime()))


## In that specific case, we use the function core.clock (to define a clock that start counting from the moment you call it into life) to define a 'trial_timer', 
## and this can be used to write away the time when a keyboard key is pressed.
    ## The function 'event.getKeys' registers when a keyboard response is given.
## This PsychoPy functionality can of course be very handy when collecting data, as it provides a built-in function to register reaction time.
## The example below shows how we can measure passed time without PsychoPy.

t1 = datetime.now()
time.sleep(2)
t2 = datetime.now()

RT = t2 - t1
print(RT)


#####################
## Wait function 3 ##
#####################

print("# Wait function 3 #")

## When looking at the PsychoPy documentation, we see that some other functions involving time are offered.
## An example of this is the 'core.wait()' function, which strongly resembles the time.sleep() function discussed earlier.
## 'core.CountdownTimer()' is a function that can be used to count down, as the name already tells us.
## When we use the extension .add() on a clock, this means that we add extra time, which may come in handy when using a count down timer.
## We strongly recommend to take a look at the demo on timing, which can be found in PsychoPy:
    ## Demos > timing > clocksAndTimers.py
## The commands noted below in essence do the same: they all wait for 500 milliseconds.
## Does the resulting RT equal 1 second?

t1 = datetime.now()
core.wait(0.5)
time.sleep(0.5)
t2 = datetime.now()

RT = t2 - t1
print(RT)

## These last two commands add an amount of time to the CountDown clock

CountDown = core.CountdownTimer()
CountDown.add(0.5)
while CountDown.getTime() > 0:
    print("Still {0:.2f} seconds to go.".format(CountDown.getTime()))
    core.wait(0.05)


#########
## END ##
#########