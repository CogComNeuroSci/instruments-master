##import modules
from psychopy import visual, gui, event, data, core
import numpy, pandas, os, string

##File management and dlg box
DirectoryToWriteTo = os.getcwd() + '/AGData/'
#Create data folder (if this does not yet exist)
if not os.path.isdir(DirectoryToWriteTo):
    os.mkdir(DirectoryToWriteTo)

info = {'ParticipantNr': numpy.random.randint(0,999)}
#ParticipantNr proposes a random number such that the experimenter (you) has to change this less often

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'AG')
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
print('Writing to ', FileName)

##Parameters of the experiment
readTimeTraining = 3
readTime = 6

##Read in the stimuli
training = pandas.read_csv("stimuli/learning_phase.txt", sep=" ")
test = pandas.read_csv("stimuli/test_phase.txt", sep=",")
test.columns = ["stim", "ans"]

###Design and randomization
##First for training phase
nTrainingBlocks = 2
#declare all levels of the factor
Stimuli = training.values
NStimuli = len(Stimuli)
Attempts = numpy.repeat(0, NStimuli)
#to allow all data (both from training and testing phase) to be saved in one file, we need these extra columns:
Correct = numpy.repeat('k', NStimuli)
Accuracy = numpy.repeat(-99, NStimuli)
RT = numpy.repeat(-99, NStimuli)
TrialsMatrix = numpy.column_stack([Stimuli, Attempts, Correct, Accuracy, RT])
#Step 2: Pandas dataframe
TrialsDataFrame = pandas.DataFrame.from_records(TrialsMatrix)
TrialsDataFrame.columns = ['Stimulus', 'Attempts', 'Correct', 'Accuracy', 'RT']
#Step 3: list, needed as input for the TrialHandler
TrialList = pandas.DataFrame.to_dict(TrialsDataFrame, orient = 'records')
#Step 4: TrialHandler
trainingTrials = data.TrialHandler(TrialList, nReps = nTrainingBlocks, method = 'random')
#add the trialhandler to the experimenthandler
ThisExp.addLoop(trainingTrials)


###create all stimuli
win = visual.Window(size = [800, 600], units = 'norm', color = 'grey')
RTClock = core.Clock() #clock to measure RTs

message = visual.TextStim(win, height = .1, color = 'white')
stimulus = visual.TextStim(win, height = .1, color = 'black')
box = visual.Rect(win, width = .4, height = .1, fillColor = 'green')

allowed_responses = list(string.ascii_lowercase)
allowed_responses.append('return') 
allowed_responses.append('backspace')
clock = core.Clock()

##Beginning of the actual experiment
##Welcome message
message.text = 'Welcome to this task!\n\nPress any key to continue'
message.draw()
win.flip()
event.waitKeys()

###Training phase
##Instructions
message.text = 'For the training round, you need to type in the sequence you just observed. Press enter to submit your answer. \n\nPress any key to continue'
message.draw()
win.flip()
event.waitKeys()

def trainingAnswer():
    """
    function that execute one answer attempt
    """
    #first show the stimulus
    message.text = trial['Stimulus']
    message.color = "white"
    box.color = "DarkCyan"
    box.draw()
    message.draw()
    win.flip()
    core.wait(readTimeTraining)
    #let them answer
    box.color = "DarkTurquoise"
    box.draw()
    win.flip()
    answer = ""
    keys = event.waitKeys(keyList = allowed_responses)
    while keys[-1] != "return":
        if keys[-1] == 'backspace': 
            answer = answer[:-1] #the answer loses its last character
        else:
            answer += keys[-1].upper() #we want to show the answer in upper case
        message.text = answer
        box.draw()
        message.draw()
        win.flip()
        keys = event.waitKeys(keyList = allowed_responses)
    return answer

for trial in trainingTrials:
    counter = 1
    answer = trainingAnswer()
    while answer != trial["Stimulus"]: #attempts only stop when answer is correct
        counter += 1
        #show negative feedback
        message.text = "Incorrect. Try again"
        message.color = "red"
        message.draw()
        win.flip()
        core.wait(1)
        #repeat
        answer = trainingAnswer()
        
        
    #once outside of the while loop: the answer is correct
    message.text = "Correct"
    message.color = "green"
    message.draw()
    win.flip()
    core.wait(1)
    #save number of attempts
    trial["Attempts"] = counter
    ThisExp.nextEntry()


###Testing phase
###Design and randomization
nTestingBlocks = 1
##For the testing phase
#declare all levels of the factor
Stimuli = test["stim"].values
NStimuli = len(Stimuli)
Correct = test["ans"].values #these values are 0 or 1
Correct = ['f' if item == 0 else 'j' for item in Correct] #we replace 0 with 'f' and 1 with 'j'
Accuracy = numpy.repeat(0, NStimuli)
RT = numpy.repeat(-99, NStimuli)
#to allow all data (both from training and testing phase) to be saved in one file, we need these extra columns:
Attempts = numpy.repeat(0, NStimuli)
TrialsMatrix = numpy.column_stack([Stimuli, Attempts, Correct, Accuracy, RT])
print(TrialsMatrix)
#Step 2: Pandas dataframe
TrialsDataFrame = pandas.DataFrame.from_records(TrialsMatrix)
TrialsDataFrame.columns = ['Stimulus', 'Attempts', 'Correct', 'Accuracy', 'RT']
TrialsMatrix = numpy.column_stack([Stimuli, Correct, Accuracy, RT])
#Step 3: list, needed as input for the TrialHandler
TrialList = pandas.DataFrame.to_dict(TrialsDataFrame, orient = 'records')
#Step 4: TrialHandler
testingTrials = data.TrialHandler(TrialList, nReps = nTestingBlocks, method = 'random')
#add the trialhandler to the experimenthandler
ThisExp.addLoop(testingTrials)

##Instructions
message.color = 'white'
message.text = "There is an underlying rule that generated the sequences you just practiced. For the test phase, you will have to judge whether the presented sequences obey this rule.\n Press 'f' if yes, 'j' if no. \n\nPress any key to continue"
message.draw()
win.flip()
event.waitKeys()

allowed_responses = ["f", "j", "escape"]

##Start test rounds
for trial in testingTrials: 
    #show stimulus
    message.text = trial['Stimulus']
    message.color = "white"
    box.color = "DarkCyan"
    box.draw()
    message.draw()
    win.flip()
    
    clock.reset()
    keys = event.waitKeys(keyList = allowed_responses, maxWait=readTime) #maximum time is 6s
    trial["RT"] = round(clock.getTime() * 1000) #to save the RT in ms
    
    if keys == None: #this happens when maxWait is exceeded
        message.text = "Too slow"
        message.color = "red"
        trial["Accuracy"] = 0
    elif keys[-1] == "escape":
        break #end the testing phase
        
    elif keys[-1] == trial["Correct"]:
        message.text = "Correct"
        message.color = "green"
        trial["Accuracy"] = 1
    else:
        message.text = "Wrong"
        message.color = "red"
        trial["Accuracy"] = 0
    message.draw()
    win.flip()
    core.wait(1)
    ThisExp.nextEntry()
