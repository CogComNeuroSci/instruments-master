# Made on 6/03/2019 by Nel Tavernier for Test 4

#Importing 
from psychopy import visual, event, core, gui, data
import numpy 
from numpy import random
import os
import platform

#Set the directory and the and the dialog box info 
info = {"Participant number": "", "Participant name": "", "Age": "", 'gender':['male', 'female', 'third gender'], 'hand preference':['left', 'right', 'ambidexter']}
my_directory = os.getcwd()

# initialize window and textwidth and clock 
win_width = 1000
win_height = 700
text_width = 0.9
win = visual.Window([win_width,win_height], units = "norm")
experiment_timer = core.Clock()

#Making the data file 
already_exists = True
while already_exists:
    
    #Making a dialog 
    infoDlg = gui.DlgFromDict(dictionary=info, title="Experiment")
    number = info["Participant number"]
    name = info["Participant name"]
    
    #Deciding name directory to write to, if it doesn't exist already make it
    directory_to_write_to = my_directory + "/data"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
        
    
    # File name aanmaken 
    file_name = directory_to_write_to +"/Test4_"+"subject_" + number
    
    #Checken of deze file al bestaat of niet en anders een error weergeven 
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Use another participant number")
        myDlg2.show()

# Constants 
nBlocks = 12
nBlockTrials = 60
nReps = 10

#Graphical elements 
stimulus = visual.TextStim(win, text="")
welkom         = visual.TextStim(win,text=(    "Welkom {},\n"+
                                                "Druk op spatiebalk om verder te gaan.").format(name))
                                                
instructRichting = visual.TextStim(win, text = "Als het pijltje naar links wijst moet je op de linkse pijl op toetsenbord drukken. \n"+
"Als pijltje naar rechts wijst moet je op de rechtse pijl drukken.\n Druk op spatiebalk om verder te gaan")
instructPositie = visual.TextStim(win, text = "Als pijltje links staat moet je op linker pijl drukken.\n Als pijltje rechts staat op rechter pijl drukken. \n"+
"Als pijltje in het midden staat moet je op de naar onder wijzende pijl drukken. \n Druk op spatiebalk om verder te gaan.")
goodbye = visual.TextStim(win, text = "Bedankt om deel te nemen en tot ziens! \n Druk op spatiebalk om af te sluiten.") 


# Make the design based on the core charastheristics
pijlen = ["<", ">", "<", ">", "<", ">"]
positie = [(-0.5,0), (0,0), (0.5,0), (-0.5,0), (0,0), (0.5,0)]
design = []
congruentie = ["congruent", "neutraal", "incongruent", "incongruent", "neutraal", "congruent"]

for loop in range(6): 
    pijl = pijlen[loop]
    positi = positie[loop]
    congruent = congruentie[loop]
    design.append({"Richting": pijl, "Positie": positi, "Congruentie": congruent})
    

# create the experiment handler and hide name for privacy reasons in the file 
info.pop("Participant name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# Welkom
welkom.draw()
win.flip()
event.waitKeys(keyList = "space")

# loop over the different blocks 
for blocki in range(nBlocks): 
    
    if blocki < 8: 
        instructRichting.draw()
        win.flip()
        event.waitKeys(keyList = "space")
        richtingBlockTrials = data.TrialHandler(design, nReps = 10, method = "fullRandom")
        thisExp.addLoop(richtingBlockTrials)
        for trial in richtingBlockTrials:
            count = 0
            ## Store the trial characteristics
            richtingBlockTrials.addData("Blocknumber", blocki+1)
            richtingBlockTrials.addData("Trialnumber in experiment", count+1)
            richtingBlockTrials.addData("Response mapping", "Richting")
            
            ## Display the stimulus
            stimulus.text = trial["Richting"]
            stimulus.pos = trial["Positie"]
            stimulus.draw() 
            win.flip() 
            
            ## wait for the response 
            event.clearEvents(eventType="keyboard")
            experiment_timer.reset()
            
            ## get the response 
            response = event.waitKeys(keyList = ['left', 'right'], maxWait = 1.5)
            
            if response == None: 
                response = [""]
            
            ## get the reactiontime 
            rt = experiment_timer.getTime()
            
            ## get correct response and accuracy
            if trial["Richting"] == "<": 
                CorResp = 'left'
            else: 
                CorResp = 'right'
            
            accuracy = 0
            if response[0] == CorResp[0]: 
                accuracy = 1
                
            ## Store the responses of the participant
            richtingBlockTrials.addData("Response", response)
            richtingBlockTrials.addData("RT", rt)
            richtingBlockTrials.addData("Correct Response", CorResp)
            
            ## End of this trial 
            thisExp.nextEntry()
        
    else: 
        instructPositie.draw()
        win.flip()
        event.waitKeys(keyList = "space")
        positieBlockTrials = data.TrialHandler(design, nReps = 10, method = "fullRandom")
        thisExp.addLoop(positieBlockTrials)
        
        for trial in positieBlockTrials:
            ## Store the trial characteristics
            richtingBlockTrials.addData("Blocknumber", blocki+1)
            richtingBlockTrials.addData("Trialnumber in experiment", (trial+1)+480)
            richtingBlockTrials.addData("Response mapping", "Positie")
            
            ## Display the stimulus
            stimulus.text = trial["Richting"]
            stimulus.pos = trial["Positie"]
            stimulus.draw() 
            win.flip() 
            
            ## wait for the response 
            event.clearEvents(eventType="keyboard")
            experiment_timer.reset()
            
            ## get the response 
            response = event.waitKeys(keyList = ['left', 'right', 'down'], maxWait = 1.5)
            
            if response == None: 
                response = [""]
            ## get the reactiontime 
            rt = experiment_timer.getTime()
            
            ## get correct response and accuracy
            if trial["Positie"] == (-0.5,0): 
                CorResp = 'left'
             
            if trial["Positie"] == (0.5,0):
                CorResp = 'right'
                
            if trial["Positie"] == (0,0): 
                CorResp = 'down'
                
            accuracy = 0
            if response[0] == CorResp[0]: 
                accuracy = 1
            
            ## Store the responses of the participant
            richtingBlockTrials.addData("Response", response)
            richtingBlockTrials.addData("RT", rt)
            richtingBlockTrials.addData("Correct Response", CorResp)
            
            ## End of this trial 
            thisExp.nextEntry()
        


goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")









