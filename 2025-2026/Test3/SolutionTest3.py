##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##
##   Test 3: Christmas Tree Harvesting Task   ##
##                                            ##
##   Instruments of Experimental Psychology   ##
##              Ghent University              ##
##          Academic year 2025-2026           ##
##                                            ##
##              Brent Vernaillen              ##
##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##

## Import modules
from psychopy import visual, gui, event, core
import numpy

## Dialog box
info = {'Participant number': 0,  
        'Full name': 'brent vernaillen', 
        'Age': 0, 
        'Handedness': ['Right', 'Left', 'Both']}

# Create and present the questions
infoDlg = gui.DlgFromDict(dictionary = info, title = "Christmas Tree Experiment")

## Experiment parameters
fieldSize = 0.5 * 2
fieldColour = (0.5765, 0.2784, -0.1843)
treeSize = 0.03 * 2
treeColour = (-0.6471, -0.2078, -0.4980)

lowVar = [60, 80, 100]*2
highVar = [20, 80, 140]*2

harvestTime = 1 # Seconds
harvestPercentage = 0.2
travelTime = 1

## Experiment components

# Window
win = visual.Window([800, 800], units = 'norm', color = (0.75, 0.75, 0.75))

# Text stimuli
textStim = visual.TextStim(win,
                           text = "HO HO HO",            # Placeholder, will be updated later with the remaining time
                           height = 0.07,
                           color = 'black')

feedbackText = visual.TextStim(win,
                           text = "HO HO HO",            # Placeholder, will be updated later with the remaining time
                           height = 0.1,
                           color = 'black',
                           pos = (0, 0.75))

proceedText = visual.TextStim(win,
                           text = "Press space to continue",
                           height = 0.07,
                           color = 'black',
                           pos = (0, -0.8))

# The field stimulus
field = visual.Rect(win,
                    size = fieldSize,
                    lineColor = fieldColour,
                    fillColor = fieldColour)

# The tree stimulus
tree = visual.Polygon(win,
                      size = (treeSize, treeSize),
                      edges = 3,
                      lineColor = treeColour,
                      fillColor = treeColour)

# Travel timer
travelTimer = core.Clock()

# Reaction time timer
rtTimer = core.Clock()

## Create trial matrix
if info['Participant number'] % 2 == 0:
    startingValues = numpy.array(lowVar + highVar)   # even
    farmTypes = numpy.array(['low']*6 + ['high']*6)
else:
    startingValues = numpy.array(highVar + lowVar)   # odd
    farmTypes = numpy.array(['high']*6 + ['low']*6)

subject = numpy.repeat(info['Participant number'], len(startingValues))
residence = numpy.repeat(-10, len(startingValues))
rts = numpy.repeat(-10, len(startingValues))
harvested = numpy.repeat(-10, len(startingValues))

trialMatrix = numpy.column_stack((subject, startingValues, farmTypes, residence, rts, harvested))
print(trialMatrix)


## Welcome the participant
textStim.text = f"Welcome {info['Full name'].split(' ')[0].capitalize()}!"
textStim.draw()
proceedText.draw()

win.flip()
event.waitKeys(keyList = ['space'])

# Give instructions
textStim.text = "Your task is to collect as many Christmas trees as possible, as fast as possible"
textStim.draw()
proceedText.draw()

win.flip()
event.waitKeys(keyList = ['space'])

## Actual experiment
for trial in range(len(startingValues)):
    
    # Initialise leave
    leave = False
    nTrees = int(trialMatrix[trial, 1])
    nHarvested = 0
    nharvests = 0
    RTs = []
    totalHarvest = 0
    
    # Sample random positions
    randomX = numpy.random.uniform(-fieldSize/2, fieldSize/2, nTrees)
    randomY = numpy.random.uniform(-fieldSize/2, fieldSize/2, nTrees)
    
    treePositions = [(x, y) for x, y in zip(randomX, randomY)]
    
    # If no leave decision: keep presenting
    while not leave:
        
        # Draw the field
        field.draw()
        
        # Draw the trees
        for t in range(nTrees):
            
            # Update tree position
            tree.pos = treePositions[t]
            
            # Draw the tree
            tree.draw()
        
        # Draw harvested
        feedbackText.text = f"+ {nHarvested}!"
        feedbackText.draw()
        
        # Present everything
        win.flip()
        
        # Wait for some time
        core.wait(harvestTime)
        
        # Present the question
        textStim.text = "Press F to stay and J to leave"
        textStim.draw()
        win.flip()
        
        # Reset the clock
        rtTimer.reset()
        
        # Wait for decision
        keys = event.waitKeys(keyList = ['f', 'j', 'escape'])
        
        # Collect RT
        RT = rtTimer.getTime()
        RTs.append(RT)
        
        # Check for escape
        if keys[0] == 'escape':
            core.quit()
        
        # Check for leave
        if keys[0] == 'j':
            leave = True
        
        ## The participant decided to stay
        
        # Update the number of trees
        nHarvested = round(nTrees * harvestPercentage)
        nTrees -= nHarvested
        totalHarvest += nHarvested
        nharvests += 1
    
    ## The participant decided to leave
    
    # Present the travel time
    travelTimer.reset()
    
    while travelTimer.getTime() <= travelTime:
        
        textStim.text = f"Travelling to a new field\n{round(travelTime - travelTimer.getTime(), 2)}s left!"
        textStim.draw()
        win.flip()
    
    # if this farm is done announce the end of this farm
    if trial == 5:
        textStim.text = "That's the end of this farm"
        textStim.draw()
        win.flip()
        event.waitKeys()
    
    if trial == 11:
        textStim.text = "That's the end of this experiment"
        textStim.draw()
        win.flip()
        event.waitKeys()
    
    ## Save the data
    trialMatrix[trial, 3] = nharvests
    trialMatrix[trial, 4] = numpy.mean(RTs)
    trialMatrix[trial, 5] = totalHarvest

print(trialMatrix)

# Close the window
win.close()