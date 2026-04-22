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
Nunique = 48
AllowedResponses = [str(i) for i in range(1,9)] #only 1 - 8 is allowed as a response
AllowedResponses.append('escape')

#To create our design, we follow the 4-variable class streamline
#Step 1: numpy arrays
Stimuli = numpy.arange(1, Nunique + 1) 
Answers = numpy.repeat(0, Nunique)
RT = numpy.repeat(-99.99, Nunique)
Accuracy = numpy.repeat(-99, Nunique)
TrialsMatrix = numpy.column_stack([Stimuli, Answers, RT, Accuracy])
#Step 2: Pandas dataframe
TrialsDataFrame = pandas.DataFrame.from_records(TrialsMatrix)
TrialsDataFrame.columns = ['Question', 'Answer', 'RT', 'Accuracy']
#Step 3: list, needed as input for the TrialHandler
TrialList = pandas.DataFrame.to_dict(TrialsDataFrame, orient = 'records')
#Step 4: TrialHandler
trials = data.TrialHandler(TrialList, nReps = 1, method = 'sequential') #no randomization in the original version
#add the trialhandler to the experimenthandler
ThisExp.addLoop(trials)

##Create all stimuli needed in the experiment
win = visual.Window(fullscr = True, units = 'norm', color = 'grey')
CounterClock = core.Clock() #clock to track how long we're in the experiment
RTClock = core.Clock() #clock to measure RTs

message = visual.TextStim(win, height = .1, color = 'white')
question = visual.ImageStim(win, image = None, pos = (-.4, 0), size = 1.1)
answer = visual.ImageStim(win, image = None, pos = (.56, 0), size = .8)

##Beginning of the actual experiment
##Welcome message
message.text = 'Welcome to the Raven Progressive Matrices Task!\n\nPress any key to continue'
message.draw()
win.flip()
event.waitKeys()

##Instructions
message.text = 'Select which pattern is missing. Respond via the numerical keys.\n\nPress any key to continue'
message.draw()
win.flip()
event.waitKeys()

#start the timer! the 'real' experiment begins
CounterClock.reset()

for trial in trials:
    #The experiment is finished after 60min or after completing all questions
    if CounterClock.getTime() >= MaxTime:
        message.text = 'Your time is up!! \n\nPress any key to continue'
        message.pos = (0, 0)
        message.draw()
        win.flip()
        event.waitKeys()
        break #we will leave the trial loop

    #show the trial
    message.text = 'Which pattern is missing?'
    message.pos = (0, 0.8)
    question.image = 'stimuli/questions/item' + str(int(trial['Question'])) + '.jpg'
    answer.image = 'stimuli/answers/answer' + str(int(trial['Question'])) + '.jpg'
    message.draw()
    question.draw()
    answer.draw()
    win.flip()
    
    RTClock.reset()
    keys = event.waitKeys(keyList = AllowedResponses)
    RT = round(RTClock.getTime()*1000) #in ms
    if keys[0] == 'escape':
        break
        
    #save the answers
    trial['Answer'] = keys[0]
    trial['RT'] = RT

    #inform the experiment handler that this trial is over
    ThisExp.nextEntry()

##Goodbye message
message.text = 'Thank you for participating, you will hear your results later from us via mail.\n\nPress any key to exit.'
message.pos = (0,0)
message.draw()
win.flip()
event.waitKeys()