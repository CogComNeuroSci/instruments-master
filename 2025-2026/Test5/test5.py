from psychopy import visual, core, event, gui, data
import os, numpy, pandas

##dialog box
info = {'Participant number': 0}

AlreadyExists = True
while AlreadyExists:
    MyDlg = gui.DlgFromDict(dictionary = info)
    FileName = os.getcwd() + '\ParticipantData_' + str(info['Participant number'])

    if not MyDlg.OK:
        core.quit()

    if not os.path.isfile(FileName + '.csv'):
        AlreadyExists = False
    else:
        MyDlg2 = gui.Dlg()
        MyDlg2.addText('This Participant number is in use already, please select another')
        MyDlg2.show()
ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info)

win = visual.Window([800,600], color = 'lightblue')

instructions = visual.TextStim(win, text = 'Welcome to the experiment!\n\nIn each trial you will be asked to wait for a specified duration before pressing space, and to indicate whether you were presented an existing or non-existing word\n\n Press space to continue', color = 'black')
WordStim = visual.TextStim(win, pos = [0,.2], color = 'black')
number = visual.TextStim(win, pos = [0,0], color = 'black')
feedback = visual.TextStim(win, pos = [0,-.2], color = 'black')
MySliderQuestion = visual.TextStim(win, pos = [0,.2], text = 'Was this a real word?', color = 'black')
MySlider = visual.Slider(win, pos = [0,-.2], ticks = [1,2], size = [.4, .2], labels = ['yes','no'], style = 'radio', color = 'black')
BlockFeedback = visual.TextStim(win, color = 'black')
ThankYou = visual.TextStim(win, text = 'Thank you for participating!\n\n Press space to continue')

MyClock = core.Clock()

##design
NrOfBlocks = 2
NrOfTrialsPerBlock = 72

##randomnization
WordOptions = numpy.array(['car','light','table','lar','pight','mable']) #0-0-0-0-0-0-1-1-1-1-1-1-...
WordPresentationTimeOptions = numpy.array([.75,1.25]) #0-0-0-1-1-1-0-0-0-1-1-1-...
InstructedWaitOptions = numpy.array([3,5,7]) #0-1-2-0-1-2-0-1-2-0-1-2-...

UniqueTrialsArray = numpy.array(range(len(WordOptions) * len(WordPresentationTimeOptions) * len(InstructedWaitOptions))) 

words = numpy.floor(UniqueTrialsArray / (len(WordPresentationTimeOptions) * len(InstructedWaitOptions))) % len(WordOptions) #FactorB = np.floor(UniqueTrials / (NFactorC * NFactorD)) % NFactorB
WordPresentationTimes = numpy.floor(UniqueTrialsArray / len(InstructedWaitOptions)) % len(WordPresentationTimeOptions) #FactorC = np.floor(UniqueTrials / (NFactorD)) % NFactorC
InstructedWaits = numpy.floor(UniqueTrialsArray / 1) % len(InstructedWaitOptions) #FactorD = np.floor(UniqueTrials / 1) % NFactorD

UniqueTrialsArray = numpy.column_stack([words, WordPresentationTimes, InstructedWaits, numpy.arange(len(words))])
BlockTrialsArray = numpy.tile(UniqueTrialsArray, (int(NrOfTrialsPerBlock/len(UniqueTrialsArray)),1))

FullExperimentTrialsArray = numpy.ones(((NrOfBlocks * NrOfTrialsPerBlock), numpy.shape(BlockTrialsArray)[1]+1)) #Placeholder array. Wants to have tuple as input

for BlockNr in range(NrOfBlocks):
    stop = 1
    while stop:
        numpy.random.shuffle(BlockTrialsArray)
        
        if numpy.sum(numpy.diff(BlockTrialsArray[:,3]) == 0) == 0: #Later I call this UniqueTrialID
            stop = 0

    FullExperimentTrialsArray[BlockNr * len(BlockTrialsArray) : (BlockNr + 1) *  len(BlockTrialsArray) , 0:numpy.shape(BlockTrialsArray)[1] ] = BlockTrialsArray
    FullExperimentTrialsArray[BlockNr * len(BlockTrialsArray) : (BlockNr + 1) *  len(BlockTrialsArray) , numpy.shape(BlockTrialsArray)[1] ] = BlockNr + 1

##validate the randomization
FullExperimentTrialsArrayDataFrame = pandas.DataFrame.from_records(FullExperimentTrialsArray) #Create DataFrame first. This DataFrame is needed for the crosstab and for creating the dictionairy input (i.e., TrialListMainExperiment) of the TrialHandler of the main experiment
FullExperimentTrialsArrayDataFrame.columns = ['words', 'WordPresentationTimes', 'InstructedWaits', 'UniqueTrialID', 'BlockNr'] #Add column names to FullExperimentTrialsArrayDataFrame
print(pandas.crosstab([FullExperimentTrialsArrayDataFrame.words, (FullExperimentTrialsArrayDataFrame.WordPresentationTimes)], [FullExperimentTrialsArrayDataFrame.InstructedWaits])) #Print the cross table validation

##TrialHandler
TrialsDataFrame = pandas.DataFrame.from_records(FullExperimentTrialsArray)
TrialsDataFrame.columns = ['words', 'WordPresentationTimes', 'InstructedWaits', 'UniqueTrialIdentifier', 'BlockNr']
TrialList = pandas.DataFrame.to_dict(TrialsDataFrame, orient = 'records')
trials = data.TrialHandler(TrialList, nReps = 1, method = 'sequential')

##def functions
def EscFunc(check):
    if check == 'escape':
        core.quit()

##exp instructions
instructions.draw()
win.flip()
resp = event.waitKeys(keyList = ['space','escape'])
EscFunc(resp[0])

AbsPerfError_ExistingWords = []
AbsPerfError_NonExistingWords = []

##trial presentation
for trial in trials:
    for TrialBuilder in ['Word', 'Word+InstructedWait', 'Word+InstructedWait+Feedback']:
        WordStim.text = WordOptions[int(trial['words'])] 
        WordStim.draw() 
        if TrialBuilder == 'Word':
            win.flip()
            core.wait(WordPresentationTimeOptions[int(trial['WordPresentationTimes'])])
        elif TrialBuilder == 'Word+InstructedWait':
            number.text = InstructedWaitOptions[int(trial['InstructedWaits'])]
            number.draw()
            win.flip()
            MyClock.reset()
            resp = event.waitKeys(keyList = ['space', 'escape'])
            AbsPerfError = abs(int(number.text)*1000-round(MyClock.getTime()*1000))
            EscFunc(resp[0])
        elif TrialBuilder == 'Word+InstructedWait+Feedback':
            number.draw()
            feedback.text = f'you were off {AbsPerfError} ms'
            feedback.draw() 
            win.flip()
            core.wait(2)
    
    ##slider
    MySlider.reset()
    while not MySlider.getRating():
        MySliderQuestion.draw()
        MySlider.draw()
        win.flip()

    ##Data collection    
    ThisExp.addData('BlockNr', trial['BlockNr'])
    ThisExp.addData('word', WordStim.text)
    ThisExp.addData('WordDuration', WordPresentationTimeOptions[int(trial['WordPresentationTimes'])])
    
    ThisExp.addData('SpecWaitTime', number.text)
    ThisExp.addData('AbsPerfError', AbsPerfError)
    
    ActualWordExistence = 'no'
    for CheckedWord in ['car','light','table']:
        if WordStim.text == CheckedWord:
            ActualWordExistence = 'yes'
            break
    ThisExp.addData('ActualWordExistence', ActualWordExistence)
    
    ThisExp.addData('RespondedWordExistence', MySlider.getRating())
    ThisExp.addData('accuracy', ['no','yes'][ActualWordExistence == MySlider.getRating()])

    ##block feedback
    if ActualWordExistence == 'yes':
        AbsPerfError_ExistingWords.append(AbsPerfError)
    else:
        AbsPerfError_NonExistingWords.append(AbsPerfError)

    if (trials.thisN + 1) == NrOfTrialsPerBlock:
        BlockFeedback.text = f'For existing words, your were off {round(numpy.mean(AbsPerfError_ExistingWords))} ms on average\n\nFor non-existing words, you were off {round(numpy.mean(AbsPerfError_NonExistingWords))} ms on average\n\n Press space to continue'
        BlockFeedback.draw()
        win.flip()
        resp = event.waitKeys(keyList = ['space','escape'])
        EscFunc(resp[0])
    
    ThisExp.nextEntry()

##thank you
ThankYou.draw()
win.flip()
resp = event.waitKeys(keyList = ['space','escape'])
EscFunc(resp[0])

ThisExp.close()
win.close()
core.quit()