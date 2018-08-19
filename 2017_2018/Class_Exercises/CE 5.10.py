# This file solves class exercise 5.10 in the IEP course 2017-2018
# Written by Tom Verguts, Nov 3, 2017

# this is an imaginary score sheet for a student on four courses.
# Max score on each course is 20.

# import modules
from __future__ import division
from psychopy import visual, event

# initializing
name        = "jasper francken"
student_nr  = 2
scores      = [12, 13, 9, 18]
directory   = "/Users/tom/Documents/student_data/"  ## you'll want to insert a path for your own directory

# initialize the window
win = visual.Window([800,400])

# here starts a (not necessarily the best) solution
# note about the next code line: cleaner code is possible if one uses a for-loop or numpy,
# but neither have been discussed yet in class
# Remember, True + True = 2
tot_correct = (scores[0]>9)+(scores[1]>9)+(scores[2]>9)+(scores[3]>9)
l = len(scores)

# note about the next code line: It's also possible to do this with one long string and several arguments in the format() argument
text1 = ("Good morning " + name.split()[0].capitalize() +"!\n\nWe now have the scores of all "+
        str(l)+" tests that you did. You passed {:.0%}".format(tot_correct/l)+" of your courses."+
        "Your data will be written to "+directory+"student{:03d}".format(student_nr)+".txt")
t1 = visual.TextStim(win,text=text1,wrapWidth=1.1)
t1.draw()
win.flip()

# next line keeps the screen active until the f key is pressed
while not "f" in event.getKeys():
    pass
win.close()