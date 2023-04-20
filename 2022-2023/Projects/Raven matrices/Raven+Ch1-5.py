#Challenge1: Let the user select the answer with the mouse
#Challenge2: Subjects receive feedback after every trial on their accuracy, 
#and receive feedback on their overall accuracy after the test.
#Challenge3: The feedback is implemented by quickly flashing the correct answer 
#in green (red) ink in case of correct (wrong) answer
#Challenge4: After every fifth item, present a rating scale querying a subject’s confidence 
#in his/her answer. Also record the confidence judgments on those trials in the data file.
#Challenge5: To check order effects in the test, construct two versions of the test. 
#One with the standard order (1, 2, 3, 4, …) and one with odd and even items swapped (2, 1, 4, 3, …). 
#Subjects with an odd subject number receive the standard version.

##import modules
from psychopy import visual, gui, event, data, core
import numpy, pandas, os

##File management and dlg box
DirectoryToWriteTo = os.getcwd() + '/RavenData/'
#Create data folder (if this does not yet exist)
if not os.path.isdir(DirectoryToWriteTo):
    os.mkdir(DirectoryToWriteTo)

info = {'ParticipantNr': numpy.random.randint(0,999)} 
#ParticipantNr proposes a random number such that the experimenter (you) has to change this less often

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'Raven')
    FileName = DirectoryToWriteTo + 'Participant' + str(info['ParticipantNr'])
    #If cancel is selected, the experiment is quitted
    if not dlg.OK: 
        core.quit()
    #Only leave the while loop if the ParticipantNr is unique
    if not os.path.isfile(FileName + '.csv'): 
        AlreadyExists = False
    #If the ParticipanatNr has been used, show an error gui
    else:
        dlg2 = gui.Dlg(title = 'Error')
        dlg2.addText('This ParticipantNr is already in use, please select another')
        dlg2.show()

#we create the experimenthandler with the created name and the participant's (anonymous) info
ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info)

##Design and randomization
MaxTime = 1*60 #MaxTime is expressed in seconds. For true experiment, this should be 60*60
WaitTime = 0.2 #the time the program waits after a click before allowing a second click
MessageTime = 2
Nunique = 48

#To create our design, we follow the 4-variable class streamline
#we create a function to swap the order of our stimuli
def swap(array):
    for i in range(int(len(array)/2)):
        array[2*i], array[2*i+1] = array[2*i+1], array[2*i]
    return array

#Step 1: numpy arrays
Stimuli = numpy.arange(1, Nunique + 1)
#for odd numbers, the standard order is used
if info["ParticipantNr"]%2 == 0: #for even numbers, we swap the order
    Stimuli = swap(Stimuli)
Answers = numpy.repeat(0, Nunique)
RT = numpy.repeat(-99.99, Nunique)
#to give feedback, we need to know which answer is correct
#Since the solutions are not given, I just define what's correct myself
Correct = numpy.array([int((i-1)%8)+1 for i in Stimuli]) 
Accuracy = numpy.repeat(-99, Nunique)
#include space to save confidence judgements
Confidence = numpy.repeat(-999, Nunique)
TrialsMatrix = numpy.column_stack([Stimuli, Answers, RT, Correct, Accuracy, Confidence])
print(TrialsMatrix)
#Step 2: Pandas dataframe
TrialsDataFrame = pandas.DataFrame.from_records(TrialsMatrix)
TrialsDataFrame.columns = ['Question', 'Answer', 'RT', 'Correct', 'Accuracy', 'Confidence']
#Step 3: list, needed as input for the TrialHandler
TrialList = pandas.DataFrame.to_dict(TrialsDataFrame, orient = 'records')
#Step 4: TrialHandler
trials = data.TrialHandler(TrialList, nReps = 1, method = 'sequential') #no randomization in the original version
#add the trialhandler to the experimenthandler
ThisExp.addLoop(trials)

##Create all stimuli needed in the experiment
win = visual.Window(size = (1800, 800), units = 'norm', color = 'grey')
mouse = event.Mouse()
CounterClock = core.Clock() #clock to track how long we're in the experiment
RTClock = core.Clock() #clock to measure RTs

message = visual.TextStim(win, height = .1, color = 'white')
question = visual.ImageStim(win, image = None, pos = (-.4, 0), size = 1.1)
answer = visual.ImageStim(win, image = None, pos = (.56, 0), size = .8)
#for interactions with mouse, we create boxes on top of each answer option
#we make them green, but put to opacity to 0 to make them initially invisible/see-through
box1 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.253, .162))
box2 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.45, .162))
box3 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.65, .162))
box4 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.845, .162))
box5 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.255, -.195))
box6 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.45, -.195))
box7 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.65, -.195))
box8 = visual.Rect(win, width = .153, height = .29, fillColor = 'green', opacity = 0, pos = (.845, -.195))

ratingScale = visual.RatingScale(win, low=1, high=5, markerStart=3, marker="slider")

##Beginning of the actual experiment
##Welcome message
message.text = 'Welcome to the Raven Progressive Matrices Task!\n\nPress any key to continue'
message.draw()
win.flip()
event.waitKeys()

##Instructions
message.text = 'Select which pattern is missing. Respond by pressing the correct pattern.\n\nPress any key to continue'
message.draw()
win.flip()
event.waitKeys()

#function to show a trial screen
def show_trial(reset = False):
    if reset: #then no green box is shown and all boxes 'wait' in green
        box1.color = 'green'
        box2.color = 'green'
        box3.color = 'green'
        box4.color = 'green'
        box5.color = 'green'
        box6.color = 'green'
        box7.color = 'green'
        box8.color = 'green'
        box1.opacity = 0
        box2.opacity = 0
        box3.opacity = 0
        box4.opacity = 0
        box5.opacity = 0
        box6.opacity = 0
        box7.opacity = 0
        box8.opacity = 0
        
    message.draw()
    question.draw()
    answer.draw()
    box1.draw()
    box2.draw()
    box3.draw()
    box4.draw()
    box5.draw()
    box6.draw()
    box7.draw()
    box8.draw()
    win.flip()

def check_clicked():
    clicked = False #becomes true if a stimili is clicked
    #a trial only ends when one of the stimili is clicked
    # loop until detect a click inside one of the boxes:
    while clicked == False:
        show_trial()
        #check if anything is clicked
        #the clicked box becomes visible
        if mouse.isPressedIn(box1):
            box1.opacity = 0.5
            Answer = 1
            clicked = True
        elif mouse.isPressedIn(box2):
            box2.opacity = 0.5
            Answer = 2
            clicked = True
        elif mouse.isPressedIn(box3):
            box3.opacity = 0.5
            Answer = 3
            clicked = True
        elif mouse.isPressedIn(box4):
            box4.opacity = 0.5
            Answer = 4
            clicked = True
        elif mouse.isPressedIn(box5):
            box5.opacity = 0.5
            Answer = 5
            clicked = True
        elif mouse.isPressedIn(box6):
            box6.opacity = 0.5
            Answer = 6
            clicked = True
        elif mouse.isPressedIn(box7):
            box7.opacity = 0.5
            Answer = 7
            clicked = True
        elif mouse.isPressedIn(box8):
            box8.opacity = 0.5
            Answer = 8
            clicked = True
    mouse.clickReset()    
    return Answer

#function to show feedback
def feedback(correct, answered):
    #the correct answer will be shown,
    #if the correct answer is the answered answer
    if correct == answered: #the box above this answer is green
        color = 'green'
    else: #else the box is red
        color = 'red'
    
    if correct == 1:
        box1.color = color
        box1.opacity = 0.5
    elif correct == 2:
        box2.color = color
        box2.opacity = 0.5
    elif correct == 3:
        box3.color = color
        box3.opacity = 0.5
    elif correct == 4:
        box4.color = color
        box4.opacity = 0.5
    elif correct == 5:
        box5.color = color
        box5.opacity = 0.5
    elif correct == 6:
        box6.color = color
        box6.opacity = 0.5
    elif correct == 7:
        box7.color = color
        box7.opacity = 0.5
    elif correct == 8:
        box8.color = color
        box8.opacity = 0.5
        
    question.draw()
    answer.draw()
    box1.draw()
    box2.draw()
    box3.draw()
    box4.draw()
    box5.draw()
    box6.draw()
    box7.draw()
    box8.draw()
    win.flip()
    

#start the timer! the 'real' experiment begins
CounterClock.reset()

NCorrect = 0 #counter to save the overal accuracy
Ndone = 0 #counter to save how many questions you've answered
for trial in trials:
    #The experiment is finished after 60min or after completing all questions
    if CounterClock.getTime() >= MaxTime:
        message.text = 'Your time is up!! \n\nPress any key to continue'
        message.pos = (0, 0)
        message.draw()
        win.flip()
        event.waitKeys()
        break #we will leave the trial loop
    
    #the trial
    message.text = 'Which pattern is missing?'
    message.pos = (0, 0.8)
    question.image = 'questions/item' + str(int(trial['Question'])) + '.jpeg'
    answer.image = 'answers/answer' + str(int(trial['Question'])) + '.jpeg'
    show_trial(reset = True) #we want all opacities to be back to 0
    
    RTClock.reset()
    first_click = check_clicked()
    core.wait(WaitTime)
    second_click = check_clicked()
    #a response is only recorded once a box is clicked twice
    while first_click != second_click:
        show_trial(reset = True) #the green box around the choice dissapears
        core.wait(WaitTime)
        first_click = check_clicked()
        core.wait(WaitTime)
        second_click = check_clicked()
        
    RT = round(RTClock.getTime()*1000) #in ms
    
    #before showing the feedback, ask a confidence judgement for every fifth trial
    if (Ndone+1)%5 == 0:
        message.text = 'How confident are you of this answer?'
        message.draw()
        ratingScale.draw()
        win.flip()
        while ratingScale.noResponse:
            message.draw()
            ratingScale.draw()
            win.flip()
        trial['Confidence'] = ratingScale.getRating()
        ratingScale.reset() 
        
    #feedback
    feedback(trial['Correct'], second_click)
    core.wait(MessageTime)
    if second_click == trial['Correct']:
        trial['Accuracy'] = 1
        NCorrect += 1
    else: 
        trial['Accuracy'] = 0
    
    #save the answers
    Ndone += 1
    trial['RT'] = RT
    trial['Answer'] = second_click
    ThisExp.nextEntry()

#show the overal accuracy
message.text = "You had " + str(round(NCorrect/Ndone * 100)) + "% correct."
message.draw()
win.flip()
core.wait(MessageTime)