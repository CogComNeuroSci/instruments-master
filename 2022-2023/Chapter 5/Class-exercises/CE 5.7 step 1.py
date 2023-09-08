"""
some I/O testing in a basic "experiment"

"""

# import modules
from psychopy import prefs
prefs.hardware['audioLib'] = ['pyo']
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
sound_duration = 1.5
right_sound = sound.Sound("A", octave=4, secs=sound_duration, stereo=True)
wrong_sound = sound.Sound("A", octave=3, secs=sound_duration, stereo=True)

# perform three trials
for trial in range(n_trials):

    ## display the first message and wait a second (or two)
    text_ready.draw()
    win.flip()
    time.sleep(OnsetDelay[trial])

    ## draw the Go message on the back buffer
    text_go.draw()
    
    ## clear the mouse input
    event.clearEvents(eventType = "mouse")
    
    ## display the Go message on the screen
    win.flip()

    ## reset the clock to measure the RT
    my_clock.reset() 

    ## wait for the mouse press and register it
    mouseResponses = [0,0,0]
    while numpy.sum(mouseResponses)==0:
        mouseResponses = my_mouse.getPressed()
    
    ## register the time
    RT[trial] = my_clock.getTime()

    ## display the accuracy feedback (predetermined)
    if (mouseResponses[0]==1 and CorResp[trial]=="left") or (mouseResponses[2]==1 and CorResp[trial]=="right"):
        text_correct.draw()
        sound_to_play = right_sound
    else:
        text_error.draw()
        sound_to_play = wrong_sound
    win.flip()
    sound_to_play.play()
    time.sleep(sound_duration)

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

    print(f"Answer to question {str(quest)}: {myRatingScale.getRating()}%")

# display the average RT for one second
meantime = numpy.mean(RT)
text_feedback = visual.TextStim(win, text = f"mean RT = {meantime:.1f} sec", pos = [0,0.5])
text_feedback.draw()
win.flip()
time.sleep(1)

# wrap it up
win.close()