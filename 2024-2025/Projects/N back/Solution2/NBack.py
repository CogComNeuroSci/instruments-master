from psychopy import gui, visual, data, core, event
import os, numpy, random, pandas

#Data file
info = {'PartNr': random.randint(1,999999)}
MyDlg = gui.DlgFromDict(dictionary = info)

if not MyDlg.OK: #Don't continue if pressing 'cancel'
    core.quit()

thisExp = data.ExperimentHandler(dataFileName = os.getcwd()+'/data/PartNr' + str(info['PartNr']), extraInfo = info)

#Randomnization
SingleDigitArray = numpy.repeat(numpy.arange(8), 5) #8 -> the sequence contains 8 nrs... 5 -> we repeat each letter 5 times
TrialNrPerBlock = 2 #You can adapt this, E.g., 2 means two times N2back sequence in a block

AllDigitsArray=numpy.ones((1,40)) #First line will be deleted later, this is just something that we can vstack to ... This will contain the digit array
NBackArray=numpy.ones((1,1)) #First line will be deleted later, this is just something that we can vstack to ... This will contain info on 'how many back'
for i in numpy.random.permutation([1, 2, 3]): #Will shuffle 1,2,3 and only use each value once
    for j in range(1, TrialNrPerBlock+1):
        while not sum(numpy.array(numpy.array(SingleDigitArray[:-i]) - numpy.array(SingleDigitArray[i:]))==0) == round(.3*(5*len(['a','b','c','d','e','f','g','h']))): #First part of statement: For e.g., N1Back: you compare the sequence without the last value to the sequence without the first value
            random.shuffle(SingleDigitArray) #We shuffle again in case there isn't the exact right nr of 'hits'
        AllDigitsArray=numpy.vstack((AllDigitsArray,SingleDigitArray))
        NBackArray=numpy.vstack((NBackArray,i))
    random.shuffle(SingleDigitArray)

AllDigitsArray = AllDigitsArray[1:] #Deleting the first line
NBackArray = NBackArray[1:] #Deleting the first line

FullMatrix = numpy.ones((len(AllDigitsArray),2), dtype = object) #dtype should be this way if you want to place the sequence array within a single cell of the FullMatrix array later (ValueError: setting an array element with a sequence)
FullMatrix[:,0] = NBackArray.squeeze() #Squeeze because otherwise you had 'ValueError: could not broadcast input array from shape (3,1) into shape (3,)'

for i in range(len(AllDigitsArray)): #This is just a trick to get the long sequences within one cell of the array
    FullMatrix[i, 1] = AllDigitsArray[i, :]

DF = pandas.DataFrame.from_records(FullMatrix) #Array (/matrix) -> DF
DF.columns = ['NBack', 'digit']
DICT = pandas.DataFrame.to_dict(DF, orient = 'records') #Df -> List of dictionaries
trials = data.TrialHandler(DICT, nReps = 1, method = 'sequential') #Sequential because it was already randomnized

thisExp.addLoop(trials)

#Initializing all what is needed
win = visual.Window(fullscr=1)
msg = visual.TextStim(win)
MyClock = core.Clock()

#The experimental procedure
for trial in trials:
    msg.text = f"Press the button if the letter is the same as {int(trial['NBack'])} back"
    msg.draw()
    win.flip()
    event.waitKeys(keyList= ['space'])

    LetterList = []
    for SeqCount, i in enumerate(trial['digit']): #SeqCount just adds up, 0-1-2-... ; i just gets the values of the digits array
        keys = []

        msg.text = ['a','b','c','d','e','f','g','h'][int(i)]
        trials.addData('letter', msg.text)
        msg.draw()
        win.flip()

        MyClock.reset()
        while MyClock.getTime() < 0.5 and not keys: #feels a bit weird, but the keys list get emptied after each iteration, which is why I leave the while loop directly after registering a response
            keys = event.getKeys(keyList = ['space', 'escape']) #waitKeys would also be a possible strategy instead of the looping here

        if keys:
            RT = round(MyClock.getTime() * 1000)
            core.wait(abs(0.5 - MyClock.getTime())) #to ensure that it remains .5 seconds on the screen, the abs() is to prevent crashing if pressing close to the .5 seconds deadline
            trials.addData('resp', keys[-1])
            if keys[-1] == 'escape':
                core.quit()
        else:
            RT = -999
            trials.addData('resp', 'NoResponse')
        trials.addData('RT', RT)

        LetterList.append(msg.text)
        trials.addData('SequenceSoFar', LetterList)
        
        accuracy = ''
        if SeqCount - int(trial['NBack']) > -1: #Only after some trials, there can be hits
            if LetterList[SeqCount - int(trial['NBack'])] == LetterList[SeqCount] and keys: #If hit and pressed -> correct
                accuracy = 'correct'
            elif LetterList[SeqCount - int(trial['NBack'])] == LetterList[SeqCount] and not keys: #If hit and not pressed -> error
                accuracy = 'error'
            elif not LetterList[SeqCount - int(trial['NBack'])] == LetterList[SeqCount] and not keys: #If no hit and not pressed -> correct
                accuracy = 'correct'
            elif not LetterList[SeqCount - int(trial['NBack'])] == LetterList[SeqCount] and keys: #If no hit and pressed -> error
                accuracy = 'error'
        else:
            if keys:
                accuracy = 'error'
                trials.addData('resp', keys[0])
            else:
                accuracy = 'correct'
        trials.addData('accuracy', accuracy)

        win.flip() #empty screen
        core.wait(0.5)

        thisExp.nextEntry()

win.close()