from psychopy import visual, event, core, gui
import numpy, time

# create a dialog box
info = {'Participant name':'Unknown', 'Participant number':0, 'Age':0, 'Gender':['male', 'female', 'unisex'], 'Handedness':['left', 'right', 'ambidexter']}
infoDlg = gui.DlgFromDict(dictionary=info, title='Gabor experiment')
if infoDlg.OK:
    print(info)
else:
    print('User cancelled')

# initialize the window
win = visual.Window(size=[600,600], units='norm')

# initialize the variables
nBlocks = 3
nTrials = 8

# initialize the clock for RT measurement
myClock = core.Clock()

# add array of Gabor's spatial frequency
SF = numpy.array([2, 20, 2, 20, 2, 20, 2, 20])

# add array of Gabor's orientation
Ori = numpy.array([330, 30, 30, 330, 330, 330, 30, 30])

# add array of Gabor's presentation time
GaborDuration = numpy.array([.016, .033, .05])

# allow for the RT to be stored
RT = numpy.repeat(-99.9,(nBlocks*nTrials))

# allow for the response to be stored
Resp = numpy.repeat(-99.9,(nBlocks*nTrials))

# combine RT and Resp arrays into trial matrix
trials = numpy.column_stack([RT, Resp])

# repeat the trial matrix for 3 blocks
trials = numpy.tile(trials, (nBlocks))

# initialize Gabor stimulus
tiltedGabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1, 1], sf=0, ori=0)
verticalGabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1, 1], sf=0, ori =(0))

# welcome text
welcomeText = visual.TextStim(win, text = 'Welcome ' + info['Participant name'] + '!\n\nPress the space bar to continue.')
welcomeText.draw()
win.flip()
event.waitKeys(keyList = 'space')

# instructions text
instructionsText = visual.TextStim(win, text = 'In this experiment you will be presented with a so-called Gabor stimulus.\n' +
    'It is your task to determine whether the orientation of the Gabor is tilted to the left or to the right compared to the vertical Gabor that will be presented before each trial.\n' + 
    'If you think the (shortly presented) Gabor stimulus was tilted to the left, press the \'f\' key, if it was tilted to the right, press the \'j\' key. \n\n' +
    'Press the space bar to start the experiment.', height = .075)
instructionsText.draw()
win.flip()
event.waitKeys(keyList = 'space')

# block loops
for b in range (nBlocks):

    # start text of current block
    blockstartText = visual.TextStim(win, text = 'Block ' + str(b+1) + ' will start when you press the space bar')
    blockstartText.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    
    # trial loops
    for t in range(b*nTrials, (b+1)*nTrials):

        # set SF for vertical Gabor and draw it
        verticalGabor.sf = SF[t]
        verticalGabor.draw()
        win.flip()
        time.sleep(1)
        
        # set the orientation and SF the Gabor stimulus
        tiltedGabor.ori = Ori[t]
        tiltedGabor.sf = SF[t]
        
        # draw the Gabor stimulus and determine its presentation duration
        tiltedGabor.draw()
        win.flip()
        core.wait(GaborDuration[b+1])
        
        # setup and draw the post-stimulus vertical Gabor, clear keystroke buffer
        verticalGabor.sf = SF[t]
        verticalGabor.draw()
        event.clearEvents(eventType = 'keyboard')
        win.flip()
        
        # reset the clock, allow for a response to be given and deduce the RT and response
        myClock.reset()
        keys = event.waitKeys(keyList=['f','j','escape'])
        RT = myClock.getTime()
        Resp = keys[0]
        
        # store the response and RT information
        trials[t,0] = RT
        #trials[t,1] = Resp
        
        # escape from the trial loop
        if keys[0] == 'escape':
            break
        
        
# goodbye message
goodbyeText = visual.TextStim(win, text = 'Thank you for your participation, ' + info['Participant name'] + '!\n\nPress the space bar to terminate.')
goodbyeText.draw()
win.flip()
event.waitKeys(keyList = 'space')

# close the window
win.close()