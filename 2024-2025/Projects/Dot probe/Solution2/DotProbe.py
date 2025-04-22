import random, numpy, pandas
from psychopy import gui, visual, data, core, event

###dlg box to obtain participant nr (for datafile)
info = {'PartNr': random.randint(1,999)}
MyDlg = gui.DlgFromDict(info)
if not MyDlg.OK:
    core.quit()

###initialising all the psychopy elements
win = visual.Window(size = [800,600], units = 'norm')
dot = visual.Circle(win, radius = .05, color = 'blue')
stim = visual.TextStim(win)
ResponseButtons = ['f','j']
RespClock = core.Clock()

###randomnisation
WordPairs = [['Parked','Suffer'],['Dried','Wound'],['Physics','Attacks'],['Clarets','Panicky'],['Wagons','Horror'],['Data','Dead'],['Detail','Afraid'],
['Hill','Evil'],['Remarks','Disease'],['Crew','Bomb'],['Approximate','Catastrophe'],['Racket','Lethal'],['Pupils','Terror'],['Tent','Trap'],['Edited','Coffin'],['Note','Fear'],
['Check','Enemy'],['Furniture','Destroyed'],['Campus','Damage'],['Pond','Harm'],['Saddle','Cancer'],['Cars','Shot'],['League','Danger'],['Laws','Pain'],['Lists','Dying']]

PossibleDotLocations, PossibleTrialDurations, PossibleWordOrdering = [.5, -.5], [.5,.6,.7,.8,.9], ['standard','reversed']

TopWord = numpy.array([])
BottomWord, EmoTrack, duration, DotPosition = numpy.copy(TopWord), numpy.copy(TopWord), numpy.copy(TopWord), numpy.copy(TopWord)

for DotLocation in PossibleDotLocations:
    for TrialDuration in PossibleTrialDurations:
        for WordOrder in PossibleWordOrdering:
                for WordPair in WordPairs:
                        if WordOrder == 'standard':
                            TopWord, BottomWord, EmoTrack = numpy.append(TopWord, WordPair[0]), numpy.append(BottomWord, WordPair[1]), numpy.append(EmoTrack, 'EmoBottom')
                        else:
                            TopWord, BottomWord, EmoTrack  = numpy.append(TopWord, WordPair[1]), numpy.append(BottomWord, WordPair[0]), numpy.append(EmoTrack, 'EmoTop')
                        duration, DotPosition = numpy.append(duration, TrialDuration), numpy.append(DotPosition, DotLocation)

CorrectResponse = numpy.copy(DotPosition)
CorrectResponse[CorrectResponse == .5] = 0 #doesn't allow to replace by strings here
CorrectResponse[CorrectResponse == -.5] = 1

### preparing the trials
#initialize the experimenthandler
ThisExp = data.ExperimentHandler(dataFileName = 'Participant_' + '1', extraInfo = info) #without this, no datafile

#1D arrays -> trial matrix
matrix = numpy.column_stack([TopWord, BottomWord, EmoTrack, duration, DotPosition, CorrectResponse])

#trial matrix -> data frame
df = pandas.DataFrame.from_records(matrix)
df.columns = ['TopWord', 'BottomWord', 'EmoTrack', 'duration', 'DotPosition', 'CorrectResponse']

#data frame -> list of dicts
TrialList = pandas.DataFrame.to_dict(df, orient = 'records')

#the list of dicts is the input for the trialhandler
trials = data.TrialHandler(TrialList, nReps = 1, method = 'fullRandom')

#add trialhandler to experimenthandler
ThisExp.addLoop(trials)

def TrialBuilding(a, b):
    stim.text, stim.pos = a, b
    stim.draw() #the def function is so that stim.draw() doesn't need to be typed below multiple times

### running the actual experiment
for trial in trials:
    TrialBuilding('+', [0,0])
    win.flip()
    core.wait(1)

    TrialBuilding(trial['TopWord'], [0, PossibleDotLocations[0]])
    TrialBuilding('+', [0, 0])
    TrialBuilding(trial['BottomWord'], [0, PossibleDotLocations[1]])
    win.flip()
    core.wait(float(trial['duration']))

    dot.pos = [0, trial['DotPosition']]
    dot.draw()
    win.flip()

    RespClock.reset()
    RespInfo = event.waitKeys(keyList = ResponseButtons, timeStamped = RespClock)
    trials.addData('response', RespInfo[0][0])
    trials.addData('ResponseTime', round(RespInfo[0][1]*1000))
    trials.addData('accuracy', ['error','correct'][RespInfo[0][0] == ResponseButtons[int(float(trial['CorrectResponse']))]])

    ThisExp.nextEntry() #to move to the next line in the data output

win.close()