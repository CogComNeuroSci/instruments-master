from psychopy import gui, data, visual, core, event
import os, numpy, random, pandas

##File management & dlg box
DirectoryToWriteTo = os.getcwd() + '/RSVP_Data/' #Create data folder (if this does not yet exist) #os.getcwd() is where your script is saved
if not os.path.isdir(DirectoryToWriteTo):
    os.mkdir(DirectoryToWriteTo)

info = {'ParticipantNr': 0, 'age': 0, 'gender' : ['male','female','x']} #Dictionary for dlg box ... I collect all data here that is typically needed for a method section in a paper

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'RSVP') #Present a dlg box
    FileName = DirectoryToWriteTo + 'Participant_' + str(info['ParticipantNr'])
    if not dlg.OK: #Quit the experiment if 'Cancel' is selected
        core.quit()
    if not os.path.isfile(FileName + '.csv'): #Only escape the while loop if ParticipantNr is unique
        AlreadyExists = False
    else:
        dlg2 = gui.Dlg(title = 'Error') #If the ParticipantNr is not unique, present an error msg
        dlg2.addText('This ParticipantNr is in use already, please select another')
        dlg2.show() #For this dlg method we need the .show() for presenting

ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info) #To use the ExperimentHandler (a class for keeping track of multiple loops/handlers)

##Design

NrOfBlocks = 4 #This is not used for scaling purposes, only to decide the timing of the breaks... The break takes place at 'trials.thisN == ((TotalNrOfTrials/NrOfBlocks)-1)'
TotalNrOfTrials = 404 #This is used for scaling purposes
NrOfTrialsPerPracticeBlock = 16
FixationCrossColors = numpy.array(['blue','red','black','green'])
Letters = ['k','l','d','s']
LettersAndButtons = Letters + ['space','escape'] #Please note that in this way the 'continue button' (information screens) is always the same as the 'none-response' (experiment)... What this means exactly gets clear if you scroll down

FullExperimentFixationCross = numpy.tile(numpy.vstack(numpy.arange(len(FixationCrossColors))), (int((TotalNrOfTrials/len(FixationCrossColors))),1))

FullExperimentAllTrialInformation = numpy.ones((TotalNrOfTrials,15))  #Placeholders for the fixation cross + 14 digits
FullExperimentAllTrialInformation[numpy.arange(TotalNrOfTrials),0:1] = FullExperimentFixationCross #[[0][1][2][3][0]...]... Later used with stim.text = '+' and stim.color = FixationCrossColors[int(trial['FixationCrossColor'])]

for line in numpy.arange(len(FullExperimentAllTrialInformation)): #With each iteration, we select a new trial for which we want to create the information (each line represents one trial (= one sequence))
    for column in range(1, FullExperimentAllTrialInformation.shape[1]): #Within this trial (/line), we now start selecting the integers that should be presented
        while True:
            FullExperimentAllTrialInformation[line,column] = random.randint(1,9)
            if not FullExperimentAllTrialInformation[line,column] == FullExperimentAllTrialInformation[line,(column-1)]: #Ask for a new random integer as long as this does not differ from the preceding one
                break

RowsToBeReplaced = []
for ReplaceRow in range(int((0.95 * len(FullExperimentAllTrialInformation)))): #For 95% for the trials/lines, we want to replace one of the digits by a letter
        while True:
            NewRowNr = random.randint(0,(len(FullExperimentAllTrialInformation)-1)) #-1 because Python starts at 0 and the last line nr is thus nr 23... We randomly select a line that needs digit-by-letter-replacement
            if not NewRowNr in RowsToBeReplaced:
                RowsToBeReplaced.append(NewRowNr) #Keep asking for a new line nr in case this line nr was chosen before already
                break
for row in RowsToBeReplaced:
    FullExperimentAllTrialInformation[row, random.choice([1, 3, 6])] = random.choice([111,222,333,444]) #This replacement can take place at position 1,3 or 6, and this is chosen randomly... If you scroll down you can see how these nrs (111/222/333/444) are transferred into 'k'/'l'/'d'/'s'

##Dataframe
FullExperimentAllTrialInformation_DataFrame = pandas.DataFrame.from_records(FullExperimentAllTrialInformation)
FullExperimentAllTrialInformation_DataFrame.columns = ['FixationCrossColor','digit1','digit2','digit3','digit4','digit5','digit6','digit7','digit8','digit9','digit10','digit11','digit12','digit13','digit14']

#In the next lines you are going to use the dataframe in combination with .iloc. For more informtion see https://discovery.cs.illinois.edu/guides/DataFrame-Fundamentals/dataframe-loc-vs-iloc/ AND https://stackoverflow.com/questions/65836268/valueerror-boolean-array-expected-for-the-condition-not-object
RandomPracticeRowNrList = []
for PracticeRow in range(0, NrOfTrialsPerPracticeBlock):
    while True:
        RandomPracticeRowNr = random.choice(numpy.arange(len(FullExperimentAllTrialInformation)))
        if not RandomPracticeRowNr in RandomPracticeRowNrList:
            RandomPracticeRowNrList.append(RandomPracticeRowNr) #We're creating a list with randomly selected practice trials
            break

TrialListPractice = pandas.DataFrame.to_dict(FullExperimentAllTrialInformation_DataFrame.iloc[RandomPracticeRowNrList], orient = 'records') #We can use .iloc in combination with dataframes. This strategy helps to select practice trials (alternative strategy: slicing in combination with 'list of dicts'). I consider the .iloc strategy as nicer, because with slicing you end up with selecting adjacent trials, now we have more freedom
TrialListMain = pandas.DataFrame.to_dict(FullExperimentAllTrialInformation_DataFrame, orient = 'records')

RTClock = core.Clock() #Initialize the clock

win = visual.Window(fullscr = True, units = 'norm')
stim = visual.TextStim(win, text = '')

RatingScale1 = visual.RatingScale(win, low = 0, high = 1, marker = 'slider', textSize = 1,
    tickMarks = [0, 1], stretch = 1.5, showValue = False,
    labels = ['Yes', 'No'])
RatingScale2 = visual.RatingScale(win, low = 0, high = 3, marker = 'slider',  textSize = 1,
    tickMarks = [0, 1, 2, 3], stretch = 1.5, showValue = False,
    labels = ['Yellow', 'Green', 'Black', 'Red'])

stim.text = f'Welcome to this experiment!\n\nYou will see sequences of 14 numbers.\n\nIf a letter is included,\nplease indicate this letter at the end of\nthe sequence by pressing the\ncorresponding key.\n\nIf you did not see any letter in the sequence, press {LettersAndButtons[-2]}.\n\nGood luck!\n\nPress space to start practicing' 
stim.draw()
win.flip()
event.waitKeys(keyList = LettersAndButtons[-2])

for phase in ['practice','main']:
    if phase == 'practice':
        trials = data.TrialHandler(TrialListPractice, nReps = 1, method = 'random') #Shuffles the rows
    else:
        stim.text = f'This is the end of the practice phase.\n\nPress {LettersAndButtons[-2]} to continue with the main experiment'
        stim.draw()
        win.flip()
        event.waitKeys(keyList = LettersAndButtons[-2])
        trials = data.TrialHandler(TrialListMain, nReps = 1, method = 'random') #Shuffles the rows
    ThisExp.addLoop(trials)
    
    for trial in trials:
        stim.text = '+'
        stim.color = FixationCrossColors[int(trial['FixationCrossColor'])] #We now constructed the colored fixation cross at the start of the trial
        stim.draw()
        win.flip()
        core.wait(2)
        PresentedSequence = []
        CorResp = ''
        for DigitDraw in range(14):
            stim.color = 'white'
            stim.text = int([trial['digit1'],trial['digit2'],trial['digit3'],trial['digit4'],trial['digit5'],trial['digit6'],trial['digit7'],trial['digit8'],trial['digit9'],trial['digit10'],trial['digit11'],trial['digit12'],trial['digit13'],trial['digit14']][DigitDraw])
            if not int(stim.text) < 10: #To transfer the 111-... to letters 
                stim.text = LettersAndButtons[(int(stim.text[:1])-1)].upper() #-1 because 1-2-3-4 should be 0-1-2-3 ... So for these occasions, we overwrite the stim.text again
                CorResp = stim.text.lower() #No capital... CorResp is only overwritten in a trial in case there is a 111/222/333/444 in the sequence
            stim.draw()
            win.flip()
            core.wait(.9)
            win.flip() #Just so that we have an empty screen directly after (nothing being drawn right now)
            core.wait(.1)
            PresentedSequence.append(stim.text) #We are going to write this to the datafile later, we now have replaced the 111/222/... with letters

        stim.text = 'What letter did you see?'
        stim.draw()
        win.flip()

        RTClock.reset()
        keys = event.waitKeys(keyList = LettersAndButtons) #All responses should be registered (4 letters, space, escape)
        RT = round(RTClock.getTime() * 1000) #In ms

        CorResp = 'space' if CorResp == '' else CorResp #CorResp was not overwritten (i.e., CorResp = '') in case that there was no letter present in the sequence
        if keys[0] == LettersAndButtons[-1]: #Escape button
            break
        elif keys[0] in LettersAndButtons[:4]:
            stim.text = keys[0].upper() #Should be one of the letters
        stim.draw()
        win.flip() #If k,l,d or s was pressed, we're now displaying that particular button press on the screen
        core.wait(0.5)
        
        if keys[0] == LettersAndButtons[-2]: #spacebar was pressed
            stim.text = 'None'
            stim.draw()
            win.flip() #if the spacebar was pressed, we're now showing the corresponding text (i.e., 'None')
            core.wait(1)
            if keys[0] == CorResp:
                stim.text = 'Correct' #A bit of an ugly solution to have the right accuracy information in the data file. We're not drawing and flipping this! Purely for admin (see for-loop with AddData later)... Spacebar was pressed and this was correct
            else:
                stim.text = 'Error' #The ugly solution once more... Spacebar was pressed and this was incorrect
        elif keys[0] == CorResp: #it was not the spacebar that was pressed
            stim.text = 'Correct' #the correct button of this selection was pressed: k,l,d or s
            stim.draw()
            win.flip()
            core.wait(0.5)
        else: #it was again not the spacebar that was pressed
            stim.text = 'Error' #the incorrect button of this selection was pressed: k,l,d or s
            stim.draw()
            win.flip()
            core.wait(0.5)

        win.flip()
        core.wait(1.5)
        
        if trials.thisN > 0 and trials.thisN == ((TotalNrOfTrials/NrOfBlocks)-1): #To have the breaks at the right moments
            stim.text = f'You can have a break now. Press {LettersAndButtons[-2]} to continue with next block'
            stim.draw()
            win.flip()
            event.waitKeys(keyList = LettersAndButtons[-2])

        for AddData in [trials.addData('ExperimentPhase', phase), trials.addData('FixationColor', FixationCrossColors[int(trial['FixationCrossColor'])]), trials.addData('PresentedSequence', PresentedSequence), trials.addData('Response', keys[0]), trials.addData('CorrectResponse', CorResp), trials.addData('Accuracy', stim.text.split()[-1]),  trials.addData('RT',RT)]:
            AddData #This statement is to have all relevant information in the data file of each participant

        ThisExp.nextEntry() #Let the experiment handler know that it should write a new line in the data file

    if keys[0] == LettersAndButtons[-1]:
        break

if not keys[0] == LettersAndButtons[-1]: #If not doing so, you'll see the ratingscale questions after escaping the experiment
    RatingScale1.reset()
    while RatingScale1.noResponse:
        stim.text = 'Did you feel or think during the experiment that you performed better or worse after different colors?'
        stim.draw()
        RatingScale1.draw()
        win.flip()
    trials.addData('Rating_BetterPerformanceAfterParticularColor?', ['Yes','No'][int(RatingScale1.getRating())])

    if RatingScale1.getRating() == 0:
        RatingScale2.reset()
        while RatingScale2.noResponse:
            stim.text = 'After which color(s) did you feel/think you performed better?'
            stim.draw()
            RatingScale2.draw()
            win.flip()
        trials.addData('Rating_FeelBetterAfterParticularColor?', ['Yellow', 'Green', 'Black', 'Red'][int(RatingScale2.getRating())])

        RatingScale2.reset()
        while RatingScale2.noResponse:
            stim.text = 'After which color(s) did you feel/think you performed worse?'
            stim.draw()
            RatingScale2.draw()
            win.flip()
        trials.addData('Rating_WorsePerformanceAfterParticularColor?', ['Yellow', 'Green', 'Black', 'Red'][int(RatingScale2.getRating())])

win.close()
core.quit()