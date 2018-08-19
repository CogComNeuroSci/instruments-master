"""
CE 9: additional explanation on the use of return in functions

Each function forms it's own small world that is blissfully ignorant of
everything that is happening outside of that function.

So if you want to adjust the information stored in the a data type
that is made outside of the function, you'll need to pass it on to
the function by including it between the brackets.

Likewise, when you calculate something inside a function and
would like to use it outside of the function, you'll need to return
that information at the end of the function.

"""

from psychopy import visual, event, core, gui

# initialize the window
win = visual.Window([500,400])

# Make the text object and insert a string
TextObject      = visual.TextStim(win, text = "")
FixationCross   = visual.TextStim(win, text = "+")

# make the function
def myfunction():
    TextObject.text = str(i)
    TextObject.draw()
    win.flip()
    core.wait(1)

# Now we will try to update the string in a loop structure.
for i in range(3):
    
    FixationCross.draw()
    win.flip()
    core.wait(1)
    
    myfunction()

## This all works very well. Your function has no difficulty with using the 
## information made outside of that function. Also, there is nothing made or adjusted
## in the function that is later needed in the for-loop, so nothing needs to be returned.

# Now let's try to calculate something in the function.

def myfunction2():
    value = i*10
    TextObject.text = str(value)
    TextObject.draw()
    win.flip()
    core.wait(1)

for i in range(3):
    
    FixationCross.draw()
    win.flip()
    core.wait(1)
    
    myfunction2()

## That works fine, but what happens when we only want to calculate the value in 
## a separate function and leave the displaying to the main loop?

execute3 = 0

if execute3 == 1:

    def myfunction3():
        value = i*10
    
    for i in range(3):
        
        FixationCross.draw()
        win.flip()
        core.wait(1)
        
        myfunction3()
        
        TextObject.text = str(value)
        TextObject.draw()
        win.flip()
        core.wait(1)

## You get this error for line 81: NameError: name 'value' is not defined
## What went wrong? We didn't return value to the for-loop! Let's try to fix it.

execute4 = 0

if execute4 == 1:
    
    def myfunction4():
        value = i*10
        return value
    
    for i in range(3):
        
        FixationCross.draw()
        win.flip()
        core.wait(1)
        
        myfunction4()
        
        TextObject.text = str(value)
        TextObject.draw()
        win.flip()
        core.wait(1)

## We still get the same error. Why?
## Because we didn't register the output of myfunction4 in the for-loop,
## hence the information of 'value' gets lost in the for-loop.
## How to fix that? We just save the output in the for-loop.

execute5 = 0

if execute5 == 1:
    
    def myfunction5():
        value = i*10
        return value
    
    for i in range(3):
        
        FixationCross.draw()
        win.flip()
        core.wait(1)
        
        stored_value = myfunction5()
        
        TextObject.text = str(stored_value) ## note the use of stored_value here
        TextObject.draw()
        win.flip()
        core.wait(1)

## That's perfect now!

## There is an alternative: instead of using return at the end of the function, 
## you can define 'value' as a global variable in your definition.
## In that way, 'value' can be used outside of the function too.

execute6 = 1


if execute6 == 1:
    
    def myfunction6():
        global value
        value = i*10
    
    for i in range(3):
        
        FixationCross.draw()
        win.flip()
        core.wait(1)
        
        myfunction6()
        
        TextObject.text = str(value)
        TextObject.draw()
        win.flip()
        core.wait(1)