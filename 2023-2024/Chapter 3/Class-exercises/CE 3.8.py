# This file solves class exercise 3.8 in the IEP course
# Written by Tom Verguts, Nov 3, 2017
# Contributions by various students in 2018-2019

# this is an imaginary score sheet for a student on four courses.
# Max score on each course is 20.

# import modules
from psychopy import visual
import time, numpy

# initializing
name        = "jasper francken"
student_nr  = 2
scores      = numpy.array([12, 13, 9, 18])
directory   = "/Users/tom/Documents/student_data/"  ## you'll want to insert a path for your own directory

# total of correct items
tot_correct = sum(scores>9)
l           = len(scores)

# initialize the window
win = visual.Window([800,400])

# a first possible approach:
messageText = ( "Good morning " + name.split()[0].capitalize() + "!\n\nWe now have the scores of all " +
                str(l) + f" tests that you did. You passed {tot_correct/l:.0%}" + " of your courses." +
                "Your data will be written to " + directory + f"student{student_nr:03d}" + ".txt")

# a second possible approach: It's also possible to do this with one long string and several arguments in the format() argument
messageText = ( f"Good morning {name.split()[0].capitalize()}!\n\nWe now have the scores of all {l} tests that you did. You passed {tot_correct/l:.0%} of your courses. " +
                f"Your data will be written to {directory}student{student_nr:03d}.txt")

# a third very neat approach if you want to keep the overview
greet           = "Good morning, "+ name.split()[0].capitalize() + "!"
courses         = "We now have the scores of all " + str(l) + " courses that you did. "
succes          = f"You passed {tot_correct/l:.0%} of your courses. "
written         = f"Your data wil be written to {directory}{student_nr:03d}. "
messageText     = greet +'\n\n' + courses + succes + written

# display the message on the screen
message = visual.TextStim(win, text = messageText, wrapWidth = 1.1)
message.draw()
win.flip()
time.sleep(2)
win.close()