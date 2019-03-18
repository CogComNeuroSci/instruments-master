#test4 Robbe Sevenhant

#Import modules
import numpy
from psychopy import visual, gui, event, core, data
import os
import random, pandas


# GUI
info_details = {'Participant nummer':0, 'Naam participant':'Voornaam', 'Geslacht':['Vrouw', 'Man', 'Andere'], 'Leeftijd':0, 'Handvoorkeur':['Rechts', 'Links', 'Ambidexter']}

# Working directory
my_directory = os.getcwd()

# New file for every new participant
already_exists = True
while already_exists:

    # Dialog box 
    infoDlg = gui.DlgFromDict(dictionary = info_details, title = 'Test 4')
    Subject = '{0:03d}'.format(int(info_details['Participant nummer']))


    # Folder
    directory_to_write_to = my_directory + '/data'
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)

    # File name
    file_name = directory_to_write_to + '/Test4_subject_' + str(Subject)
    if not os.path.isfile(file_name):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = 'Error')
        myDlg2.addText('Probeer een andere participant nummer')
        myDlg2.show()

# Remove name for anonymity but keep for greeting
pp_name = info_details['Naam participant']
info_details.pop('Naam participant')

#Define window
win = visual.Window([1000,700])

#text
welkom            = visual.TextStim(win, text = "Welkom " + pp_name + ", druk op spatie om verder te gaan")
pijlInstructies   = visual.TextStim(win, text = "Als het pijltje naar rechts wijst druk dan op de rechter pijltjestoets.\n"+ "Als het pijltje naar links wijst druk dan op de linker pijltjestoets. Druk op spatie om verder te gaan.")
positieInstructies= visual.TextStim(win, text = "Als het pijltje in het midden van het scherm is druk op de onderste pijltjestoets, \n"+ "als het rechts op het scherm komt druk op de rechter pijltjestoets \n"+ "en als het links komt op de linkerpijltjestoets. Druk op spatie om verder te gaan.")
afscheid          = visual.TextStim(win, text = "bedankt voor u deelname, dit is het einde van het experiment")

## Esther: pro tip: splits je tekst op over verschillende lijntjes zodat je script wat beter leesbaar is

#posities op scherm
links  = (-0.5,0)
midden = (0,0)
rechts = (0.5,0)

#variables
nblocks = 12
ntrials = 60
#aanmaken van klok
my_clock    = core.Clock()

# number of design repetitions per block
nReps = int(ntrials/(3*2))

respOpt = ("left","down", "right")

richtingpijltjes = numpy.array ([ "<-", "->"])
posities = numpy.array ([links, midden, rechts])

Design = data.createFactorialTrialList({"pijltjes": richtingpijltjes, "positie": posities})

#stimulus aanmaken

#Stimulus = visual.TextStim(win, text = "pijltjes", pos = "positie")   werkt niet

# make the design for one block

## Esther: de pandas code hieronder was waarschijnlijk een aanzet om crosstables te maken

## convert to a data frame to easily add dummy columns
dataFrame = pandas.DataFrame.from_dict(Design)
dataFrame["StimType"] = range(dataFrame.shape[0])

## each block consists of 60 trials
trials = pandas.concat([dataFrame]*nReps, ignore_index = True)

## extract the trial indices
index = list(trials.index)

#display welcom text
welkom.draw()
win.flip()
event.waitKeys(keyList = ["space"])


# make the trial stucture for the entire experiment
 
## Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = file_name)

## Esther: jammer dat je hier niet meteen de gegevens van de proefpersoon opslaat in de output file

##loop over the 12 blocks to randomize each block separtely
for blocknr in range(nblocks):
    
    #make the design for a block
    ##random trial order
    blockTrials = data.TrialHandler(Design, nReps = nReps, method = "fullRandom")
    
    ##add the block to the experimenthandler
    thisExp.addLoop(blockTrials)
    
    # esther: pas op, dit had < 8 moeten zijn ipv < 9
    
    ##zorgen dat 2/3 ze op 2/3 van de blokken op de pijltjes reageren en 1/3 op positie
    if (blocknr) < 9:
        pijlInstructies.draw()
        win.flip()
        event.waitKeys(keyList = ["space"])
    else:
        positieInstructies.draw()
        win.flip()
        event.waitKeys(keyList = ["space"])
        
        ## Esther: oei pas op, je hebt hier de trial loop genest in de else statement van hierboven dus enkel de positietrials zullen uitgevoerd worden
        
        for trial in blockTrials:
            
            
            #tekenen van de stimuli
            Stimulus.text = trial["richtingpijltjes"]       ## ESther: hier moest je "pijltjes" gebruiken in plaats van "richtingpijltjes"
            Stumulus.pos  = trial["positie"]
            
            Stimulus.draw()
            win.flip()
            event.clearEvents(eventType="keyboard")
            my_clock.reset()
            keys= event.waitKeys(keyList= respOpt)
            
            RT= my_clock.getTime()
            Response = keys[0]
            
            #tijdop maar zo moet het:
            #accuracy = int(trial["CorResp"] == Response)
            
            ## Esther: in de code hieronder moest je verwijzen naar blockTrials in plaats van blockTrialsHandler
            
            blockTrialsHandler.addData("RT",RT)
            blockTrialsHandler.addData("Response",Response)
            #blockTrialsHandler.addData("Accuracy",accuracy)
            
            
            
            ##store the block number
            blockTrials.addData("Block",blocknr+1)
            
            ## proceed to the next trial
            thisExp.nextEntry()

#neem afscheid en sluit het venster
afscheid.draw()
win.flip()
event.waitKeys(keyList = ["space"])
win.close()
core.quit()








