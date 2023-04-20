##Project IEP course
##Triad Task
##Author: Vincent Hoofs

##import modules
from psychopy import visual, gui, event, core, data
import os, numpy, random, pandas, itertools

##File management & dlg box
DirectoryToWriteTo = os.getcwd() + '/TriadTaskData/' #Create data folder (if this does not yet exist) #os.getcwd() is where your script is saved
if not os.path.isdir(DirectoryToWriteTo):
    os.mkdir(DirectoryToWriteTo)

info = {'ParticipantNr': 0, 'age': 0,}

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'TriadTask') #Present a dlg box
    FileName = DirectoryToWriteTo + 'Participant' + str(info['ParticipantNr'])
    if not dlg.OK: #Quit the experiment if 'Cancel' is selected
        core.quit()
    if not os.path.isfile(FileName + '.csv'): #Only escape the while loop if ParticipantNr is unique
        AlreadyExists = False
    else:
        dlg2 = gui.Dlg(title = 'Error') #If the ParticipantNr is not unique, present an error msg
        dlg2.addText('This ParticipantNr is in use already, please select another')
        dlg2.show() #For this dlg method we need the .show() for presenting

ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info) #ExperimentHandler: a class for keeping track of multiple loops/handlers

##design & randomnization
NrOfBlocks = 3 #In each block, each triplet of TripletsList is presented once (This is based on the project instructions. This would, by the way, lead to 84 triplets in each block)
AllowedResponses = ['l','j','k']
PercentageRepeatsAllowed = 10 #How much percent of overlap is allowed between the current and previous trial? Overlap means that at least 2 words are similar
AllowedResponses.append('escape') #Just to make sure that escape can be used for quitting the task

TripletsList = list(itertools.combinations(['apple','mouse','house','fort','head','horse','client','hit','sleeve'],3)) #itertools.combinations: One of the first Google hits if searching for 'Python unique sequences'. An example of what it does here: .combinations('ABCD', 2) --> AB AC AD BC BD CD

TripletsArray = numpy.array(TripletsList)
TrialMatrix = numpy.tile('EmptyCell', (len(TripletsArray)*NrOfBlocks,TripletsArray.shape[1]+2)) #Just placeholders for now

for BlockNr in range(NrOfBlocks): #Here we fill an empty matrix with all trials of the experiment
    CurrentRowNrs = numpy.array(range(len(TripletsArray))) + (BlockNr * len(TripletsArray)) #Just a strategy to select the right lines here
    stop = True
    while stop:
        numpy.random.shuffle(TripletsArray)
        SimilarityCounter_AllLinesConsideration = 0
        for i in range(1, len(TripletsArray)): #Checking FOR EACH LINE of TripletsArray
            SimilarityCounter_TwoLinesComparison = 0
            for j in list(itertools.product(numpy.arange(TripletsArray.shape[1]),repeat=2)): #This loop is for checking for any similarities between the current and previous line. The generated list contains all possible comparisons (e.g., column 0-current line vs column 0-previous line; column 0-current line vs column 1-previous line; ...). See https://docs.python.org/3/library/itertools.html
                if TripletsArray[i,j[0]] == TripletsArray[(i-1),j[1]]: #Comparing the words of the current line (i) to those of the previous line (i-1). All possible comparisons are performed here (by contrasting each j[0] to each j[1])
                    SimilarityCounter_TwoLinesComparison += 1
            if SimilarityCounter_TwoLinesComparison > 1: #This is the case if there were at least two similarities
                SimilarityCounter_AllLinesConsideration += 1
        if SimilarityCounter_AllLinesConsideration <= (len(TripletsArray) / (100/PercentageRepeatsAllowed)): #Only escape the while loop if there is less than e.g., 10% repetition of at least 2 words between current and previous lines (for 10%, for stopping it should be below 8.4 repetitions, so 8 is max)
            stop = False
    TrialMatrix[CurrentRowNrs, 0:TripletsArray.shape[1]] = TripletsArray
    TrialMatrix[CurrentRowNrs, TripletsArray.shape[1]] = BlockNr+1 #+ 1 because Pyton starts at 0
    TrialMatrix[CurrentRowNrs, TripletsArray.shape[1]+1] = numpy.arange(len(TripletsArray))+1 #The trial nr

TrialsDataFrame = pandas.DataFrame.from_records(TrialMatrix) #Create DataFrame first
TrialsDataFrame.columns = ['WordA','WordB','WordC','BlockNr','TrialNr'] #Add column names

##TrialHandler
TrialList = pandas.DataFrame.to_dict(TrialsDataFrame, orient = 'records') #Convert dataframe to list of dictionaries (this will be the input for the TrialHandler of the main experiment)

##Initialize clock, response, window, and stimuli properties
RTClock = core.Clock() #Initialize the clock

win = visual.Window(size = [1000, 1000], units = 'norm', color = 'grey')
triangle = visual.Polygon(win, edges = 3, radius = .5, lineColor = 'white', fillColor = 'grey')
circle = visual.Circle(win, radius = .05, lineColor = 'black', fillColor = 'grey')
message = visual.TextStim(win, height = .075, color = 'white')
word = visual.TextStim(win, height = .05, color = 'white')

##The actual experiment
message.text = 'Welcome to this experiment\n\nPlease indicate which word pairs are most similar by pressing \'{0}\' or \'{1}\' or \'{2}\'\n\nPress space to start'.format(AllowedResponses[0],AllowedResponses[1],AllowedResponses[2])
message.draw()
win.flip()
event.waitKeys(keyList = ['space'])

trials = data.TrialHandler(TrialList, nReps = 1, method = 'sequential') #We shouldn't randomnize! Already done!
ThisExp.addLoop(trials)

for trial in trials:
    triangle.draw()
    
    PresentedWords = [trial['WordA'],trial['WordB'],trial['WordC']]
    random.shuffle(PresentedWords) #To make sure that the order of words in TripletsList is not deciding where the words are displayed on the screen

    for i in range(len(PresentedWords)):
        word.text = PresentedWords[i]
        word.pos = [[-.5,0,.5][i],[-.3,.55,-.3][i]] #Y and X position of the words, the first is at [-.5,-.3], ...
        word.draw()
        trials.addData(['LeftBottomWord','MidTopWord','RightBottomWord'][i], word.text)
    
    PresentedLetters = AllowedResponses[0:3]
    random.shuffle(PresentedLetters) #To make sure that the response buttons are shuffled ('i','j','k')

    for i in range(len(PresentedLetters)):
        circle.pos = [[-.225,0,.225][i],[.1,-.25,.1][i]] #X and Y position of the circles
        circle.draw()
        word.text = PresentedLetters[i] #The letters 'l','j','k'
        word.pos = circle.pos #To make sure that the presented letter and the surrounding circle have the same coordinates
        word.draw()
        trials.addData(['LeftSideResponseKey','MidBottomResponseKey','RightSideResponseKey'][i], word.text)
    
    win.flip()
    
    RTClock.reset()
    keys = event.waitKeys(keyList = AllowedResponses, maxWait = 1.5)
    RT = round(RTClock.getTime()*1000) #In ms

    if keys: #We need a statement as this, otherwise we'll get issues if maxWait is exceeded and no response has been performed
        if keys[0] == 'escape': #Leave the trial loop if escape is pressed (and since this is the only loop, it will terminate the entire experiment)
            break
        trials.addData('PerformedResponse', keys[0])
        
        RespondedWithWhichResponseKey = ['LeftSideResponseKey', 'MidBottomResponseKey', 'RightSideResponseKey'][PresentedLetters.index(keys[0])] #In this particular trial, to which of the three circles has been responded?
        MostAlike = [[PresentedWords[0] + '_' + PresentedWords[1]],[PresentedWords[0] + '_' + PresentedWords[2]],[PresentedWords[1] + '_' + PresentedWords[2]]][PresentedLetters.index(keys[0])] #Just some bookkeeping for the data file. Which words in this trial where considered most similar?

        trials.addData('RespondedToWhichResponseKey', RespondedWithWhichResponseKey)
        trials.addData('MostAlike', MostAlike)
    else:
        RT = -999 #Will overwrite the value of RT in case of a too-late response
        trials.addData('PerformedResponse', 'None')
        trials.addData('MostAlike', 'NotApplicable')

    trials.addData('RT', RT) #Write RT to data file

    ThisExp.nextEntry() #Let the ExperimentHandler proceed to the next trial (now it knows that next .addData() calls correspond to the next trial)

    if (trials.thisN+1) % len(TripletsArray) == 0: #To decide when a break is offered to the participant
        if (trials.thisN+1)/len(TripletsArray) == NrOfBlocks:
            message.text = 'This is the end of the experiment\n\nThank you for participating!\n\nPress space to finish' #No break after the last block has finished
        else:
            message.text = 'This was block nr {0} of {1} blocks in total\n\nYou can take a break now\n\nPress space to continue'.format(trial['BlockNr'],NrOfBlocks)
        message.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])

ThisExp.close() #Let the ExperimentHandler know that it's finished
win.close()