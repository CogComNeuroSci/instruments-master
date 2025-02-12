##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##
##     Test 3: Serial Reaction time task      ##
##                                            ##
##   Instruments of Experimental Psychology   ##
##              Ghent University              ##
##          Academic year 2024-2025           ##
##                                            ##
##              Brent Vernaillen              ##
##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##

##   Description   ##

#   For this test, you have to implement a serial reaction time task. In this task, participants 
#   see 6 squares next to each other and each trial a target appears in one of the 6 locations. Participants 
#   have to press one of 6 corresponding buttons as fast as possible. What participants don’t know however 
#   is that there is a fixed sequence in which the targets appear (e.g., 2-1-5-4-3-6). If participants 
#   implicitly learn this sequence, we expect their reaction times to decrease over time. As we want to 
#   distinguish learning from practice effects, we also include a block with a random sequence, which allows 
#   us to explore a difference in reaction time decreases between a structured and a random block.

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
infoDlg = gui.DlgFromDict(dictionary = info, title = "Serial Reaction Time Task")

##   Experiment Parameters   ##

# Experiment structre
nBlocks = 2
seqReps = 2
isi = 0.1

# The sequence for the structured block
sequence = [1, 0, 4, 3, 2, 5]

# Stimuli sizes and positions (norm units, so both the width and the height are 2)
squareSize = 0.08*2   # 8% of the screen size (2) is 0.16

squareLocs = [(-0.5, 0),        # 0
              (-0.3, 0),        # 1
              (-0.1, 0),        # 2
              (0.1, 0),         # 3
              (0.3, 0),         # 4
              (0.5, 0)]         # 5

circleRadius = 0.025*2  # 2% of the screen size (2) is 0.1
textSize = 0.07        # The height of text elements

# Colors
backgroundColor = (0.75, 0.75, 0.75)                # A light grey
textColor = (-1, -1, -1)                            # Black
targetColor = (-0.0667, 0.6549, -0.7412)     # Some kind of green

# Responding
validKeys = ['d', 'f', 'g', 'h', 'j', 'k']      # key 0, 1, 2, 3, 4, 5

##   Experiment Components   ##

# Window
win = visual.Window([900, 900],                 # 900x900 pixels
                    units = "norm",             # normalized coordinate system
                    color = backgroundColor)    # Correct background colour

# Location square
locationSquare = visual.Rect(win,
                             pos = (0, 0),            # Placeholder, will be updated later
                             lineColor = 'Black',
                             fillColor = None,
                             height = squareSize,
                             width = squareSize)

# Define the typical cirlce shape
targetDot = visual.Circle(win,
                          radius = circleRadius,
                          edges = 'circle',
                          lineColor = targetColor,     # Placeholder, will be updated later
                          fillColor = targetColor,     # Placeholder, will be updated later
                          pos = (0, 0))            # Placeholder, will be updated later

# Text stims for instructions and stuff
textElement = visual.TextStim(win, 
                              'Shrubbery', 
                              color = textColor, 
                              height = textSize)

proceedText = visual.TextStim(win, 
                              'Press space to proceed', 
                              color = textColor, 
                              height = textSize,
                              pos = (0, -0.8))

# RT timer
rtTimer = core.Clock()

## trial matrix
structureSeq = sequence*seqReps     # The same list repeated
randomSeq = sequence*seqReps        # Identical
numpy.random.shuffle(randomSeq)     # But shuffled (randomized)

# Determine the order based on the participant number
if info['Participant number'] % 2:                          # Even
    ItemPosition = structureSeq + randomSeq
else:                                                       # Odd
    ItemPosition = randomSeq + structureSeq

# Empty columns
Response = numpy.repeat('Shrubbery', len(ItemPosition))
ReactionTime = numpy.repeat(-1, len(ItemPosition))

# The correct response determined via a list comprehension
# We fill the list by each time taking the respective key (print the list to see this!)
CorResp = [validKeys[int(i)] for i in ItemPosition]

# Stack together
trialMatrix = numpy.column_stack([ItemPosition,
                                  Response,
                                  ReactionTime,
                                  CorResp])

##-----------------------------------------------------------------------------##
##                            The actual experiment                            ##
##-----------------------------------------------------------------------------##

# Welcome and instructions
textElement.text = "Welcome"
textElement.draw()
proceedText.draw()
win.flip()
event.waitKeys(keyList = ['space']) # Wait for key press

textElement.text = "Press the corresponding buttons as fast as possible"
textElement.draw()
proceedText.draw()
win.flip()
event.waitKeys(keyList = ['space']) # Wait for key press

# The number of times a dot appears
nTrials = int(len(ItemPosition)/2)

## Block Loop
for block in range(nBlocks):
    
    # announce block start
    textElement.text = f"Block {block+1}/{nBlocks} will start now"
    textElement.draw()
    proceedText.draw()
    
    win.flip()
    event.waitKeys(keyList = ['space']) # Wait for key press
    
    ## Trial loop
    for trial in range(nTrials):
        
        ## One trial
        # Draw the location squares
        for loc in squareLocs:
            locationSquare.pos = loc
            locationSquare.draw()
        
        # Draw the target in the current location
        targetDot.pos = squareLocs[int(trialMatrix[block*nTrials + trial, 0])]
        targetDot.draw()
        
        # Flip and reset the timer!
        win.flip()
        rtTimer.reset()
        
        # Wait for a response, only allowing the corresponding button
        keys = event.waitKeys(keyList = trialMatrix[block*nTrials + trial, 3])
        RT = rtTimer.getTime()
        
        # Draw the location squares
        for loc in squareLocs:
            locationSquare.pos = loc
            locationSquare.draw()
        
        # Flip and wait for the intertrial interval
        win.flip()
        core.wait(isi)
        
        # Store the response and RT
        trialMatrix[block*nTrials + trial, 1] = keys[0]
        trialMatrix[block*nTrials + trial, 2] = RT
    
    # announce blreak or end
    if block != nBlocks - 1:
        textElement.text = f"Take a break :)\nYour average reaction time was {round(numpy.mean([float(x) for x in trialMatrix[block*nTrials:block*nTrials+nTrials, 2]])*1000)} ms"
    else:
        textElement.text = f"The end \nYour average reaction time was {round(numpy.mean([float(x) for x in trialMatrix[block*nTrials:block*nTrials+nTrials, 2]])*1000)} ms"
    
    textElement.draw()
    proceedText.draw()
    
    win.flip()
    event.waitKeys(keyList = ['space']) # Wait for key press

# Check the data of this experiment
print(trialMatrix)
win.close()








