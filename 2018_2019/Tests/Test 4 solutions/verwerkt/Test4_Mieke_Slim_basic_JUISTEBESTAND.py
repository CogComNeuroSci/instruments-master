##########################################
############### TEST 4 IEP ###############
############### Mieke Slim ###############
############### 06/03/2019 ###############
##########################################

# Loading packages
from psychopy import data, visual, event, core, gui
import os, time, pandas, numpy

# Window/Clock
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height], units = "norm")
timer = core.Clock()

# GUI/Data File
## Make a dictionary for the GUI
info = {"Naam": "", "Proefpersoonnummer": str(0), "Leeftijd": str(0), "Gender": ["vrouw", "man", "derde gender"], "Handvoorkeur": ["rechtshanding", "linkshandig", "ambidexter"]}
## Determine the directory where the datafiles will be stored
my_directory = os.getcwd()
## Implement the GUI, and make sure no datafiles can be stored under the same name 
already_exists = True 
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    directory_to_write_to = my_directory + "/data"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + info["Proefpersoonnummer"] ## Make sure no datafiles can be stored under the same name, so each datafile has a unique subjectnumber in its name
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else: ## Make sure no datafiles can be stored under the same name, and make sure an error message is shown if this goes wrong
        myDlg2 = gui.Dlg(title = "Foutmelding!")
        myDlg2.addText("Dit proefpersoonnummer is reeds in gebruik, vraag de proefleider om hulp")
        myDlg2.show()
## Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = file_name) 

# Instruction texts
subject_name = info["Naam"]  ## For the welcome message
welcome         = visual.TextStim(win,text=(  "Welkom {} \n\n" +
                                              "In deze taak krijgt u elke keer een pijl op het scherm te zien\n\n"+
                                              "In sommige gevallen moet u reageren op de richting van de pijl,"+
                                              " en in andere gevallen moet u reageren op de positie van de pijl.\n\n"+
                                              "Druk op de spatiebalk om verder te gaan.").format(subject_name))
                                                
instructions_page1 =   visual.TextStim(win,text=("U kunt reageren op de pijl met de pijltjestoetsen op het toetsenbord. \n\n"+
                                                "Als u op de richting van de pijl reageert, drukt u op het pijltje naar links op uw toetsenbord, als de pijl naar links wijst,"+
                                                " en op het pijltje naar rechts als de pijl naar rechts wijst\n\n"+
                                                "Druk op de spatiebalk om verder te gaan."))
                                                
instructions_page2 = visual.TextStim(win,text=( "Als u op de positie van de pijl moet reageren, drukt u op het pijltje naar links als de pijl links op het scherm staat,"+
                                                " en op het pijltje naar rechts als de pijl rechts op het scherm staat. \n\n"+
                                                "Staat de pijl in het midden? Druk dan op het pijltje naar beneden op uw toetsenbord\n\n"+
                                                "Druk op de spatiebalk om te beginnen."))
                                                
goodbye         = visual.TextStim(win,text=(    "Dit is het einde van het experiment!\n\n"+
                                                "Laat aan de proefleider weten dat u klaar bent, en druk op de spatiebalk om af te sluiten.\n\n"+
                                                "Hartelijk dank voor uw deelname!"))

## instructions per block 
## I have named the two types of blocks 'typical' and 'atypical'. 
## In typical blocks, participants react to the direction of the arrow. In atypical blocks, participants react to the position of the arrow
typicalinstructions = visual.TextStim(win, text = ("In dit blok moet u reageren op de richting van de pijl: druk op het pijltje naar links als de pijl naar links wijst, en het pijltje naar rechts als de pijl naar rechts wijst\n\n"+
                                                   "Druk op de spatiebalk om te beginnen"))
atypicalinstructions = visual.TextStim(win, text = ("In dit blok moet je reageren op de positie van de pijl: druk op het pijltje naar links als de pijl links staat, het pijltje naar rechts als de pijl rechts staat, en het pijltje naar beneden als de pijl in het midden staat\n\n" + 
                                                   "Druk op de spatiebalk om te beginnen"))

# Design
## the arrows:
Pijltjes = ['<-', '->']
## positioning:
left = (-0.5, 0.0)
middle = (0.0,0.0)
right = (0.5, 0.0)
Positie = [left, middle, right]
## Make the factorial design
Design = data.createFactorialTrialList({"Arrow": Pijltjes, "Position": Positie})

## Number of blocks, trials per block, and repititions in each block
nBlocks = 12
nBlockTrials = 60
nReps = int(nBlockTrials) / (2 * 3)         ## it is a 2x3 design (two possible directions of the arrow X three possible positions of the arrow)

# Display a welcome message and the unstructions
welcome.draw()
win.flip()
event.waitKeys(keyList = 'space')
instructions_page1.draw()
win.flip()
event.waitKeys(keyList = 'space')
instructions_page2.draw()
win.flip()
event.waitKeys(keyList = 'space')


# Begin experiment
for block in range(nBlocks):
    ## Implement the TrialHandler, and communicate to the ExperimentHandler
    blockTrialHandler = data.TrialHandler(Design, nReps = nReps, method = "fullRandom")
    thisExp.addLoop(blockTrialHandler)    
    ## Determine which blocks will be 'typical' (8 of the 12 blocks), and 'atypical' (4 of the 12 blocks)
    if (block + 1) % 3 == 0: 
        instructions = 'atypical' 
        atypicalinstructions.draw()
        win.flip()
        event.waitKeys(keyList = 'space')
    else:
        instructions = 'typical'
        typicalinstructions.draw()
        win.flip()
        event.waitKeys(keyList = 'space') 
    for trial in blockTrialHandler:
        ## Add the personal data of the participant to the datafile (apart from the participant's name)
        blockTrialHandler.addData('Subject', info['Proefpersoonnummer'])
        blockTrialHandler.addData('Gender', info['Gender'])        
        blockTrialHandler.addData('Age', info['Leeftijd'])
        blockTrialHandler.addData('Handedness', info['Handvoorkeur'])  
        ## Add the block number and block type (typical versus atypical) to the datafile
        blockTrialHandler.addData('Block', block + 1)
        blockTrialHandler.addData('Instructions', instructions)
        ## Display the trial
        stimulus = visual.TextStim(win, text = trial['Arrow'], pos = trial['Position'])
        stimulus.draw()
        event.clearEvents(eventType = 'keyboard')
        win.flip()
        timer.reset()
        if instructions == 'typical': ## in the typical blocks, two response keys are possible (two directions to which the arrow can point)
            response = event.waitKeys(keyList = ['left', 'right'])
        else: ## in the atypical blocks, three response keys are possible (three possible positions of the screen)
            response = event.waitKeys(keyList = ['left', 'right', 'down'])
        ## register the rt per trial
        rt = timer.getTime()
        ## add the participants response and rt per trial to the datafile
        blockTrialHandler.addData('RT', rt)
        blockTrialHandler.addData('Response', response[0])
        ## Determine the concruency per trial
        if (trial['Arrow'] == "<-" and trial['Position'] == left) or (trial['Arrow'] == "->" and trial['Position'] == right):
            Congruence = "congruent"
        elif (trial['Arrow'] == "<-" and trial['Position'] == right) or (trial['Arrow'] == "->" and trial['Position'] == left):
            Congruence = "incongruent"
        else:
            Congruence = "neutral"
        ## Determine which response is the correct one per trial 
           ## In 'typical' blocks:
        if instructions == "typical":
            if trial['Arrow'] == "<-":
                CorResp = 'left'
            else:
                CorResp = 'right'
           ## In 'atypical blocks':
        else: 
            if trial['Position'] == left:
                CorResp = 'left'
            elif trial['Position'] == middle:
                CorResp = 'down'
            else:
                CorResp = 'right'
        ## Determine the accuracy of the participant's response per trial
        accuracy = 0
        if response[0] == CorResp:
            accuracy = 1
        ## Add the correct response, accuracy, and congruence of per trial to the datafile
        blockTrialHandler.addData('Congruence', Congruence)
        blockTrialHandler.addData('Correct Response', CorResp)
        blockTrialHandler.addData('Accuracy', accuracy)
        ## Move onto the next trial
        thisExp.nextEntry()

# Goodbye message
goodbye.draw()
win.flip()
event.waitKeys(keyList = 'space')

# Closing
win.close()
core.quit()