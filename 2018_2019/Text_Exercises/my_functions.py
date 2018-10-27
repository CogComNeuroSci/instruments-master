# a homemade squaring function
def square_function(number):
    return number*number

# a homemade power function
def power_function(number, power):
    return number**power

# a homemade function to display a fixation cross
def fixationCross(window, duration):
    
    # import the necessary modules
    from psychopy import visual
    import time
    
    # display the fixation cross
    fixation = visual.TextStim(window, text = "+")
    fixation.draw()
    window.flip()
    time.sleep(duration)