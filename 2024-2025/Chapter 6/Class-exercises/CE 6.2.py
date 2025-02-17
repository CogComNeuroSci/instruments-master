"""
some I/O testing in a basic "experiment"

"""

# import modules
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import visual, event, core, sound
import time, numpy

# initialize the window
win = visual.Window(size=[500,400])

# initializing
my_clock = core.Clock()
my_mouse = event.Mouse()
n_trials = 3
key_list = ["f","j"]

# hard coded stimulus onset delay and correct response
OnsetDelay  = numpy.array([1,0.5,2])
CorResp     = numpy.array(["left","left","right"]) ## right-click means double-click on a Mac

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
    
    ## clear the mouse input
    event.clearEvents(eventType = "mouse")
    
    ## display the Go message on the screen
    win.flip()

    ## reset the clock to measure the RT
    my_clock.reset() 

    ## wait for the mouse press and register it
    while numpy.sum(my_mouse.getPressed())==0:
        pass
    
    return my_mouse.getPressed()

def determine_feedback():
    ## display the accuracy feedback (predetermined)
    if (response[0]==1 and CorResp[trial]=="left") or (response[2]==1 and CorResp[trial]=="right"):
        text_correct.draw()
        current_sound = 4
        sound_adjustment = 0.2
    else:
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
mySlider = visual.Slider(win, ticks = [0, 25, 50, 75, 100], labels= ["0%", "25%", "50%", "75%", "100%"], style = "slider", size = (1.5, .1), pos = (0,-0.5))
myItem = visual.TextStim(win, text="", height=.08, units="norm")

for quest in range(2):

    ## remove any remaining ratings
    mySlider.reset() 

    if quest == 0:
        myItem.text = "How pleasant was this experiment?"
    else:
        myItem.text = "How tired do you feel?"

    ## show & update until a response has been made
    while not mySlider.getRating():
        myItem.draw()
        mySlider.draw()
        win.flip()
        if event.getKeys("escape"):
            core.quit()

    print(f"Answer to question {str(quest)}: {mySlider.getRating()}%")

# display the average RT for one second
meantime = numpy.mean(RT)
text_feedback = visual.TextStim(win, text = f"mean RT = {meantime:.1f} sec", pos = [0,0.5])
text_feedback.draw()
win.flip()
time.sleep(1)

# wrap it up
win.close()
