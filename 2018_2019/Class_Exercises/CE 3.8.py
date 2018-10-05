# This file solves class exercise 3.8 in the IEP course 2018-2019
# Written by Tom Verguts, Nov 3, 2017

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

# note about the next code line: It's also possible to do this with one long string and several arguments in the format() argument
messageText = ( "Good morning " + name.split()[0].capitalize() + "!\n\nWe now have the scores of all " +
                str(l) + " tests that you did. You passed {:.0%}".format(tot_correct/l) + " of your courses." +
                "Your data will be written to " + directory + "student{:03d}".format(student_nr) + ".txt")
message = visual.TextStim(win, text = messageText, wrapWidth = 1.1)
message.draw()
win.flip()
time.sleep(2)
win.close()