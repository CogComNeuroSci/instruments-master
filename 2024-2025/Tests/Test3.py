##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##
##     Test 3: Additional singleton task      ##
##                                            ##
##   Instruments of Experimental Psychology   ##
##              Ghent University              ##
##          Academic year 2024-2025           ##
##                                            ##
##              Brent Vernaillen              ##
##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##

##   Description   ##

#   For this test, you have to implement a visual search task called the ‘additional singleton task’. 
#   In this task, participants are repeatedly exposed to 8 shapes organized along an imaginary circle. 
#   On each trial, all shapes contain a line that is either horizontal or vertical. Participants are 
#   instructed to respond as quickly as possible to the orientation of the line (‘F’ for horizontal and
#   'J’ for vertical) within the target shape, which is recognizable by its unique shape (e.g., a diamond 
#   among circles). In addition to the target shape, one of the non-target shapes will have a unique, salient 
#   color that is assumed to capture visual attention, thereby serving as the distractor. 

##------------------------------------------------------------------------------##
##                               Experiment Setup                               ##
##------------------------------------------------------------------------------##

##   Import the required modules   ##

from psychopy import visual, gui, event, core
import numpy, random

##   Participant information   ##

# What information would we like to record from the participant?
info = {'Participant number':0,  
        'Full name': 'Brent Vernaillen', 
        'Age': 0, 
        'Handedness': ['Right', 'Left', 'Both']}

# Create and present the questions
infoDlg = gui.DlgFromDict(dictionary = info, title = "Additional Singleton Task")

##   Experiment Parameters   ##

# Experiment structre
nBlocks = 2
nTrials = 10

# Timing
interTrialInterval = 0.100 # seconds
responseDeadline = 1 # Seconds

# Stimuli sizes (norm units, so both the width and the height are 2)
circleRadius = 0.05*2  # 5% of the screen size (2) is 0.1
diamondSize = 0.08*2   # 8% of the screen size (2) is 0.16
targetSize = 0.04*2    # 4% of the screen size (2) is 0.08
textSize = 0.07        # The height of text elements

# Colors
targetColor = (-1, -1, -1)                          # Black
DistractorColor = (1.0000, -0.5000, -0.5000)        # Some kind of red
nonDistractorColor = (-0.0667, 0.6549, -0.7412)     # Some kind of green
backgroundColor = (0.75, 0.75, 0.75)                # A light grey
textColor = (-1, -1, -1)                            # Black

# Responding
validKeys = ['f', 'j']      # The participant should only press F or J

# In the trials, we frequently need to randomly sample and update locations.
# Instead of working with the list of position tuples directly, it is easier to keep this
# list fixed and assign each location an ID. We can then continue with these IDs (0-7) and
# then use them to index the correct position later (this will become clear in the trial loop)
# for now, just keep in mind what posList looks like

# List with all possible locations possible locations (and respective IDs)
posList = [(0, 0.7),     # Shape 0
           (0.5, 0.5),   # Shape 1
           (0.7, 0),     # Shape 2
           (0.5, -0.5),  # Shape 3
           (0, -0.7),    # Shape 4
           (-0.5, -0.5), # Shape 5
           (-0.7, 0),    # Shape 6
           (-0.5, 0.5)]  # Shape 7

# all shape 'IDs'
# The code below is a list comprehension. It is a more efficient way of creating a list with
# numbers 0 - 7 than using an actual for loop that starts with an empty list and adds the index
# at each iteration.
posIndices = [i for i in range(8)]

# Half of the shapes will get a horizontal line (45), and half will get a vertical line (135)
lineOris = [-45, 
            -45,
            -45, 
            -45, 
            45,
            45, 
            45, 
            45]

##   Experiment Components   ##

# Window
win = visual.Window([900, 900],                 # 900x900 pixels
                    units = "norm",             # normalized coordinate system
                    color = backgroundColor)    # Correct background colour

# Response clock (used for measuring the reaction time each trial)
responseTimer = core.Clock()

# Define the typical cirlce shape
CircleStim = visual.Circle(win,
                           radius = circleRadius,
                           edges = 'circle',
                           lineColor = 'Black',     # Placeholder, will be updated later
                           fillColor = 'Black',     # Placeholder, will be updated later
                           pos = (0, 0))            # Placeholder, will be updated later

# Define the diamond (target) shape
DiamondStim = visual.Rect(win,
                          width = diamondSize,
                          height = diamondSize,
                          lineColor = nonDistractorColor,  # The distractor always has the same color
                          fillColor = nonDistractorColor,  # The distractor always has the same color
                          ori = 45,                        
                          pos = (0, 0))                    # Placeholder, will be updated later

# Define the actual target (line)
TargetStim = visual.Line(win,
                         size = targetSize,
                         lineColor = targetColor,
                         pos = (0, 0),              # Placeholder, will be updated later
                         ori = 0,                   # Placeholder, will be updated later
                         lineWidth = 5)             # In pixels!

# Define the fixation cross
FixCross = visual.TextStim(win,
                       text = '+',
                       height = textSize,
                       color = 'Black',
                       pos = (0,0))

## Data matrix for storing the data 
DistrLoc = numpy.repeat(-1, nBlocks * nTrials)
TargLoc = numpy.repeat(-1, nBlocks * nTrials)
Response = numpy.repeat('Shrubbery', nBlocks * nTrials)
Accuracy = numpy.repeat(-1, nBlocks * nTrials)
ReactionTime = numpy.repeat(-1, nBlocks * nTrials)

dataMatrix = numpy.column_stack([DistrLoc,
                                 TargLoc,
                                 Response,
                                 Accuracy,
                                 ReactionTime])

# Text stims for instructions and stuff
textElement = visual.TextStim(win, 
                              'Shrubbery', 
                              color = textColor, 
                              height = textSize)

feedbackText = visual.TextStim(win, 
                              'Shrubbery', 
                              color = textColor, 
                              height = textSize)

proceedText = visual.TextStim(win, 
                              'Press space to proceed', 
                              color = textColor, 
                              height = textSize,
                              pos = (0, -0.8))

##   THE ACTUAL EXPERIMENT   ##

# Welcome the participant (only first name, capitalized)
textElement.text = f"Welcome to this experiment, {info['Full name'].split()[0].capitalize()}!"
textElement.draw()
proceedText.draw()

win.flip()
event.waitKeys(keyList = ['space'])

# Present instructions
textElement.text = "In this task, you will repeatedly see 8 shapes organized along an imaginary circle. Each trial there will be 7 circles and 1 diamond, and each shape will contain a line that is either horizontal or vertical. Your task is to respond as fast as possible to the orientation of the line within the diamond shape by pressing 'f' for horizontal and 'j' for vertical. Importantly, each trial, all shapes will be green, except for one circle that will be red. this is the distractor, which can be safely ignored."
textElement.draw()
proceedText.draw()

win.flip()
event.waitKeys(keyList = ['space'])

##   Block Loop   ##

for block in range(nBlocks):
    
    # announce block start
    textElement.text = f"Block {block+1}/{nBlocks} will start now"
    textElement.draw()
    proceedText.draw()
    
    win.flip()
    event.waitKeys(keyList = ['space']) # Wait for key press
    
    ##   Trial Loop   ##
    
    for trial in range(nTrials):
        
        ##   One trial   ###
        
        # Select random target and distractor location
        targetLocation, distractorLocation = numpy.random.choice(posIndices, 2, replace = False)
        
        # Next we define the neutral locations (no distractor or target)
        neutralLocs = posIndices.copy()
        neutralLocs.remove(distractorLocation)
        neutralLocs.remove(targetLocation)
        
        # With both the target and distractor location chosen, we proceed to draw everything
        # First, we draw the non-distractor circles
        for loc in neutralLocs:
            CircleStim.pos = posList[loc]
            CircleStim.color = nonDistractorColor # Should be green
            CircleStim.draw()
        
        # Second, we draw the target diamond
        DiamondStim.pos = posList[targetLocation]
        DiamondStim.draw() # hard-coded green
        
        # Third, we draw the distractor shape
        CircleStim.pos = posList[distractorLocation]
        CircleStim.color = DistractorColor
        CircleStim.draw() # hard-coded red
        
        # Fourth, we shuffle and draw the lines
        numpy.random.shuffle(lineOris)
        
        # for each of the lines, we set simultaneously the orientation and the position
        for orientation, position in zip(lineOris, posList):
            TargetStim.ori, TargetStim.pos = orientation, position
            TargetStim.draw()
        
        # Finally we add the fixation cross
        FixCross.draw()
        
        # Present everything on the screen and flip screen
        win.flip()
        responseTimer.reset() # Correct time to reset timer!
        
        # Wait for a response for a maximum of 1 seconds
        keys = event.waitKeys(maxWait = responseDeadline, 
                              keyList = validKeys)
        
        RT = responseTimer.getTime()
        
        # In case no key was pressed, manually make the variable keys a list containing the string 'No response'
        if not keys:
            keys = ['No response']
        
        # Determine correct response
        if lineOris[targetLocation] == 45: # If the orientation of the target line was 45 (i.e., horizontal)
            correctResponse = 'f'
        else:
            correctResponse = 'j'
        
        # Save the relevant data
        dataMatrix[trial + block*nTrials, 0] = distractorLocation                 # This trial distr loc
        dataMatrix[trial + block*nTrials, 1] = targetLocation                     # This trial target loc
        dataMatrix[trial + block*nTrials, 2] = keys[0]                            # This trial key pressed
        dataMatrix[trial + block*nTrials, 3] = int(keys[0] == correctResponse)    # This trial corResp
        dataMatrix[trial + block*nTrials, 4] = round(RT*1000)                     # This trial RT
        
        # Finally, remove all but the fixation cross and present ITI
        FixCross.draw()
        win.flip()
        core.wait(0.1)
    
    # If it is not the last block, present a break
    if block != nBlocks-1:
        textElement.text = "This is a break"
        proceedText.draw()
    
    # Else announce the end
    else:
        textElement.text = "This is the end of the experiment. Thank you for participating!\n\n\nPress space to end this session."
    
    textElement.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])

# Check saved data
print(dataMatrix)