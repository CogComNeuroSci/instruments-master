## Test 3: Marie Vandemoortele
# importing modules
from psychopy import visual, event, core, gui
import time, numpy

# create a dialog box
info = {'Participant number': 0, 'Name': 'unknown', 'Age' :0, 'Gender':['male', 'female', 'Other'], 'Handedness': ['Left', 'Right', 'ambidexter'] }
dlg = gui.DlgFromDict(dictionary= info,title="Participant info", order = ['Name', 'Participant number', 'Age', 'Gender', 'Handedness'])
thisInfo = dlg
p_number = info['Participant number']
name = info['Name']

#define functie gui box
def gui_box():
    if dlg.OK:
        printstatement = print(info)
    else:
        printstatement = print('User Cancelled')
    return printstatement

# initialze a window 
win = visual.Window([600,500], units = 'norm')

# welcome message
def welcomescreen():
    welcome= visual.TextStim(win, text='Hello {0}! Welcome to this experiment. \n\nPress the spacebar to continue'.format(name))
    welcome.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#define instructions
def instructions():
    instr= visual.TextStim(win, text= 'Press \'f\' if the Gabor is turned to the left. \n\nPress \'j\' if the Gabor is turned to the right.\n\nPress spacebar to continue.')
    instr.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

# define correct response
def determineCorResp():
    if gabor.ori == -30:
        CorResp = 'f'
    else:
        CorResp = 'j'
    return CorResp

# define feedback message
def feedback_message(CorResp):
    if keys[0] == CorResp:
        feedback = 'Correct!'
        AC= 1
    else:
        feedback = 'Wrong!'
        AC= 0
    feedback_text = visual.TextStim(win, text= feedback)
    feedback_text.draw()
    win.flip()
    core.wait(1)
    return AC 

def goodbyescreen():
    goodbye = visual.TextStim(win, text= 'Thanks for participating! Goodbye {0}!\n\n\nPress the spacebar to quit.'.format(name))
    goodbye.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.close()

#initialize the variables
nblocks      = 3
ntrials      = 8
duration     = numpy.array([0.016, 0.033, 0.050])
orientation  = numpy.array([30, 30, 30, 30, -30, -30, -30, -30])
spatialfreq  = numpy.array([2,2,20,20,2,2,20,20])
my_clock     = core.Clock()
accuratesse  = [ ]
RTList       = [ ]
ResponseList = [ ]


# initialize the gabor stimulus
gabor1 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')
gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')

gui_box()
welcomescreen()
instructions()

for b in range(nblocks):
    time  = duration[b]
    block = visual.TextStim(win, text = 'Block {} will start if you press the spacebar'.format(b+1))
    block.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    for t in range(ntrials):

        gabor1.draw()
        win.flip()
        core.wait(1)

        gabor.ori = orientation[t]
        gabor.sf  = [spatialfreq[t], 0]
        gabor.draw()
        win.flip()
        core.wait(time)

        gabor1.draw()
        # clear the keyboard input; to make sure 'f' & 'j' are the only response options
        event.clearEvents(eventType = "keyboard")
        win.flip()
        my_clock.reset()
        keys = event.waitKeys(keyList = ['f', 'j', 'escape'])
        RT   = my_clock.getTime()
        resp = keys[0]
        
        #escape from the loop
        if keys[0] == 'escape':
            break
        
        RTList.append(RT)
        ResponseList.append(resp)
        CorResp = determineCorResp()
        AC   = feedback_message(CorResp)
        accuratesse.append(AC)
        
        # Stores the response key of the partipant along with his reaction time (RT)
        trials = numpy.column_stack((ResponseList, RTList))

    win.flip()

goodbyescreen()

#print(RTList)
#print(ResponseList)
print(trials)