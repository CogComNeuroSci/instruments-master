from psychopy import gui, visual, core, data, event
import random, numpy, pandas

DlgDict = {'PPNr': random.randint(0,999)}
MyDlg = gui.DlgFromDict(DlgDict)
if not MyDlg.OK:
    core.quit()

win = visual.Window([1000,800], units = 'norm')
msg = visual.TextStim(win)
tb = visual.TextBox2(win, text = '', letterHeight= .1, size = [.5,.2], borderColor= 'black', alignment = 'center')
ResponseTimer = core.Clock()
ThisExp = data.ExperimentHandler(dataFileName = 'ParticipantData/' + str(DlgDict['PPNr']))

#Feel free to make the lists longer, but in this way it's easier to verify that things are working fine
TrainingList = ['PVV','TXS','TSXS']#,'PTTVV','PTVPS','PVPXVV','TSSSXS','TXTVPS','PTTTVPS','PTVPXVV','PVPXVPS','TSSXXVV','TSXXTVV','TXXTVPS','PVPXTVPS','TSSSXXVV','TSSXXVPS','TSXXTVPS','TXXTTTVV','TXXVPXVV']
TrainingList2 = list(TrainingList)
TestList = TrainingList + ['TXV','TTVV']#,'PSXS','TXPV','PVTVV','PTTPS','XXSVT','TXXVX','TXVPS','TPTXS','PTTTVT','TSXXPV','SXXVPS','PTVVVV','VPXTVV','PTVPPPS','SVPXTVV','PVTTTVV','VSTXVVS','TXXTVPT','PTTTVPVS','TSSXXVSS','PVXPVXPX','PTVPXVSP','PXPVXVTT']
random.shuffle(TrainingList), random.shuffle(TrainingList2), random.shuffle(TestList)

WordShown = numpy.array(TrainingList + TrainingList2 + TestList)
MemberOf = numpy.array(['MemberOfTraininglist' if i in TrainingList else 'NoMemberOfTraininglist' for i in WordShown])
CorrectResponse = numpy.array([i.lower() for i in WordShown[0:len(TrainingList)+len(TrainingList2)]] + ['f' if i == 'MemberOfTraininglist' else 'j' for i in MemberOf[len(TrainingList)+len(TrainingList2):]])
response = numpy.repeat('', len(WordShown))

matrix = numpy.column_stack([WordShown, MemberOf, CorrectResponse, response, numpy.copy(response), numpy.copy(response), numpy.copy(response)])
df = pandas.DataFrame.from_records(matrix)
df.columns = ['WordShown', 'MemberOf', 'CorrectResponse', 'response', 'ResponseMemory', 'MainPhaseAccuracy', 'RT']
ListOfDicts = pandas.DataFrame.to_dict(df, orient = 'records')

def WordShow(AgainMsg = ''):
    msg.text = AgainMsg + trial['WordShown']
    msg.draw()
    win.flip()
    if not phase == 'main':
        core.wait(3)
        win.flip()
    else:
        ResponseTimer.reset()

for i, phase in enumerate(['PracticeBlock1','PracticeBlock2','main']):

    msg.text = ['We start practicing, please retype the word you just saw.', 'We continue practicing, you can have a break now.', 'The words that you just saw were based on a particular rule. We will now also include new words that you didn’t see before. All of these new ones follow another rule. Press ‘f’ for words following the original rule, press ‘j’ for the ones following another rule (the new words)'][i] + '\n\nPress space to start'
    msg.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    trials = [data.TrialHandler(ListOfDicts[0:len(TrainingList)], nReps = 1, method = 'sequential'), data.TrialHandler(ListOfDicts[len(TrainingList):len(TrainingList)+len(TrainingList2)], nReps = 1, method = 'sequential'), data.TrialHandler(ListOfDicts[len(TrainingList)+len(TrainingList2):], nReps = 1, method='sequential')][i]
    ThisExp.addLoop(trials)

    for trial in trials:
        WordShow()

        while True:
            if not phase == 'main':
                tb.text = trial['response'].upper()
                tb.draw()
                win.flip()

                keys = event.waitKeys(keyList = [chr(i) for i in range(97, 123)]+['return','backspace'])[0]
                if not keys == 'return' and not keys == 'backspace':
                    trial['response'] += keys
                elif keys == 'backspace':
                    trial['response'] = trial['response'][:-1]
                else:
                    trial['ResponseMemory'] += "_" + trial['response']
                    if trial['CorrectResponse'] == trial['response']:
                        break
                    else:
                        WordShow('Again: ')
                        trial['response'] = ''
            else:
                trial['response'] = event.waitKeys(keyList=['f','j'], maxWait = 6)
                if trial['response']:
                    trial['RT'] = str(round(ResponseTimer.getTime() * 1000))
                    trial['MainPhaseAccuracy'] = ['error','correct'][trial['CorrectResponse'] == trial['response'][0]]
                else:
                    trial['RT'] = 'NoResponse'
                    trial['MainPhaseAccuracy'] = 'too late'
                msg.text = trial['MainPhaseAccuracy']
                msg.draw()
                win.flip()
                core.wait(1)
                break
        ThisExp.nextEntry()

win.close()
core.quit()