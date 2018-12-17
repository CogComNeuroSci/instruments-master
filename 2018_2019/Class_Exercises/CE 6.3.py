"""
some I/O testing in a basic "experiment"

"""

# import modules
from psychopy import prefs
prefs.general['audioLib'] = ['pyo']
from psychopy import visual, event, core, sound, gui
import time, numpy

# create a dialog box
info = {"Participant number":0, "Participant name":"Unknown", "Gender":["male", "female"], "Age":0, "Device":["keyboard", "mouse"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Generic Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# initialize the window
win = visual.Window(size=[500,400])

# initializing
my_clock = core.Clock()
my_mouse = event.Mouse()
n_trials = 3

# hard coded stimulus onset delay and correct response
OnsetDelay  = numpy.array([1,0.5,2])
if device == "keyboard":
    CorResp = numpy.array(["f","f","j"]) ## right-click means double-click on a Mac
elif device == "mouse":
    CorResp = numpy.array(["left","left","right"]) ## right-click means double-click on a Mac

# add a default RT that will be overwritten during the trial loop
RT = numpy.repeat(-99.9,n_trials)

# graphical elements
text_ready      = visual.TextStim(win,text="are you ready...?")
text_go         = visual.TextStim(win,text="Go!")
text_correct    = visual.TextStim(win,text="correct :-)")
text_error      = visual.TextStim(win,text="wrong :-(")

# feedback sound elements
sound_duration = 0.25
sound_to_play = sound.Sound("A", octave=1, secs=sound_duration, stereo=True)

# define some custome functions
def get_ready():
    ## display the first message and wait a second (or two)
    text_ready.draw()
    win.flip()
    time.sleep(OnsetDelay[trial])

def target_and_response():
    ## draw the Go message on the back buffer
    text_go.draw()
    
    ## clear the keyboard or mouse input
    if device == "keyboard":
        event.clearEvents(eventType = "keyboard")
    elif device == "mouse":
        event.clearEvents(eventType = "mouse")
    
    ## display the Go message on the screen
    win.flip()

    ## reset the clock to measure the RT
    my_clock.reset() 

    ## wait for the keyboard or mouse press and register it
    if device == "keyboard":
        keys = event.waitKeys(keyList = ["f","j"])
        response = keys[0]
    elif device == "mouse":
        while numpy.sum(my_mouse.getPressed())==0:
            pass
        response = my_mouse.getPressed()
    
    return response

def determine_feedback():
    ## display the accuracy feedback (predetermined)
    accuracy = -1
    if device == "keyboard":
        if response == CorResp[trial]:
            accuracy = 1
        else:
            accuracy = 0
    elif device == "mouse":
        if (response[0]==1 and CorResp[trial]=="left") or (response[2]==1 and CorResp[trial]=="right"):
            accuracy = 1
        else:
            accuracy = 0
    
    if accuracy == 1:
        text_correct.draw()
        current_sound = 4
        sound_adjustment = 0.2
    elif accuracy == 0:
        text_error.draw()
        current_sound = 3
        sound_adjustment = -0.2
    
    return current_sound, sound_adjustment

def play_feedback(current_sound = 0, sound_adjustment = 0.1):
    ## display the message and play the sound
    win.flip()
    for soundi in range(5):
        current_sound = current_sound + sound_adjustment
        sound_to_play = sound.Sound("A", octave=current_sound, secs=sound_duration, stereo=True)
        sound_to_play.play()
        time.sleep(sound_duration)


# perform three trials
for trial in range(n_trials):
    
    ## get them ready
    get_ready()
    
    ## start actual trial
    response = target_and_response()
    
    ## they have pressed something
    RT[trial] = my_clock.getTime()
    
    ## check what feedback must be given to this response
    current_sound, sound_adjustment = determine_feedback()
    
    ## present the feedback 
    play_feedback(current_sound, sound_adjustment)

# probe the pleasantness and tiredness of the participant
myRatingScale = visual.RatingScale(win, low=0, high=100, marker="slider",
    tickMarks=[0, 25, 50, 75, 100], stretch=1.5, tickHeight=1.5,  # singleClick=True,
    labels=["0%", "25%", "50%", "75%", "100%"])
myItem = visual.TextStim(win, text="", height=.08, units="norm")

for quest in range(2):

    ## remove any remaining ratings
    myRatingScale.reset() 

    if quest == 0:
        myItem.text = "How pleasant was this experiment?"
    else:
        myItem.text = "How tired do you feel?"

    ## show & update until a response has been made
    while myRatingScale.noResponse:
        myItem.draw()
        myRatingScale.draw()
        win.flip()
        if event.getKeys("escape"):
            core.quit()

    print("Answer to question {0}: {1}%".format(str(quest), myRatingScale.getRating()))

# display the average RT for one second
meantime = numpy.mean(RT)
text_feedback = visual.TextStim(win, text = "mean RT = {0:.1f} sec".format(meantime), pos = [0,0.5])
text_feedback.draw()
win.flip()
time.sleep(1)

# wrap it up
win.close()
