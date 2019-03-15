#IEP Test 4 By Maya Vervoort
#Schoolyear 2018-2019

#Import modules
from psychopy import gui, core, data, visual, event
import os, numpy, pandas


#Directory
MyDir = os.getcwd()

#Define window
win = visual.Window([1000,700], units = 'norm')

#Variables
nblocks = 12
my_clock    = core.Clock()

    #Get each arrow 30 times
Stims = numpy.resize(["<", ">"], 60)
Ori = numpy.resize(["left", "right"], 60)

    #Get each position 20 times
Pos = numpy.resize([-0.75, 0, 0.75], 60)
Posi = numpy.resize(["left", "up", "right"], 60)

# Esther: dit werkt nu wel, maar wees voorzichtig met hoe dit extrapoleert naar andere situaties

    #Introduce Correct Response and Congruence to overwrite later on
CorResp = numpy.repeat(-99.9, len(Stims))
Congruence = numpy.repeat("bla", len(Stims))

    #Make the trial matrix
trials = numpy.column_stack([Stims, Ori, Pos, Posi, CorResp, Congruence])

    #Insert dialogue box
info = {"Participant number": str(0), "Name": "", "Age": str(0), "Gender": ["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"]}

    #Choose directory and file name
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    directory_to_write_to = MyDir + "/data"
    
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    file_name = directory_to_write_to + "/data_Test4_subject_" + str(info["Participant number"])
    
        #Check if file name already exists
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Insert a different Participant number")
        myDlg2.show()

#Guarantee anonimity and save participant info
subject_name = info["Name"]
info.pop("Name")

#Implement the Experiment Handler
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

#Texts
Welcome = visual.TextStim(win, text= "Welcome {0},\n".format(subject_name)+
                                        "press space to continue")

Instr = visual.TextStim(win, text = "Instructions")
Instr.text =    (   "Welcome to this experiment! \n"+
                    "In this task, you will have to decide one of two things:\n"+
                    "Either you have to make a decision about the position of the arrow on the screen \n"+
                    "Or about the way the arrow is pointing\n"+
                    "Press space to continue")

ExpBuild = visual.TextStim(win, text = "Build-up of the experiment")
ExpBuild.text =         ("The experiment consists of 12 blocks with 60 trials each\n"+
                        "Before each block, the instructions will appear on this screen\n"+
                        "concerning what you have to base your decision on.\n"+
                        "Press space to begin the experiment.")

InstrPos = visual.TextStim(win, text = "Instructions when position is important")
InstrPos.text = (   "In this block, you will have to respond to the position of the arrow. \n"+
                    "If the arrow is presented on the left side of the screen, press the left arrow on your keyboard\n"+
                    "If the arrow is presented on the right side of the screen, press the right arrow\n"+
                    "If the arrow is presented in the middle of the screen, press the arrow up\n"+
                    "Press space to start this block.")

InstrOri = visual.TextStim(win, text = "Instructions when orientation is important")
InstrOri.text =    ("In this block, you will have to respond to the orientation of the arrow. \n"+
                    "If the arrow is pointing to the left side of the screen, press the left arrow on your keyboard\n"+
                    "If the arrow is pointing to the right side of the screen, press the right arrow\n"+
                    "Press space to start this block.")

Stim = visual.TextStim(win, text = "Stimulus", pos = (-1,1))

#Show texts
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

Instr.draw()
win.flip()
event.waitKeys(keyList = "space")

ExpBuild.draw()
win.flip()
event.waitKeys(keyList = "space")

# Esther: perfecte transitie tussen arrays en de trial_list
# Esther: het enige wat ik hier nog tekort kom is een kruistabel

dataFrame = pandas.DataFrame.from_records(trials)
dataFrame.columns = ["Stimulus", "Orientation", "Position", "Position2", "CorResp", "Congruence"]

trial_list = pandas.DataFrame.to_dict(dataFrame, orient = "records")

#The actual experiment
block = 0
trialN = 0
while block < nblocks:
    #For each block the participants have to focus on position, they have to focus on orientation twice
    #So per 3 blocks, there are 2 for orientation and one for position
    if (block+1)%3 == 0:
        InstrPos.draw()
    else:
        InstrOri.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    blockTrialsHandler = data.TrialHandler(trial_list, nReps = 1, method = "random")
    thisExp.addLoop(blockTrialsHandler)
    
        #Present the Stimuli
    for trial in blockTrialsHandler:
        Stim.text = trial["Stimulus"]
        Stim.pos = ((trial["Position"]), 0)
        Stim.draw()
        win.flip()
        
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        
        keys = event.waitKeys(keyList = ["left", "right", "up"])
        
            #Define RT and Response
        RT = my_clock.getTime() 
        Response = keys[0]
        
            #Define Congruence
        if trial["Orientation"] == trial["Position2"]:
            trial["Congruence"] = "Congruent"
        else:
            trial["Congruence"] = "Incongruent"
        if trial["Position2"] == "up":
            trial["Congruence"] = "Neutral"
        
            #Define CorResp
        if (block+1)%3 == 0:
            if trial["Position2"] == "left":
                trial["CorResp"] = "left"
            if trial["Position2"] == "up":
                trial["CorResp"] = "up"
            if trial["Position2"] == "right":
                trial["CorResp"] = "right"
        else:
            if trial["Orientation"] == "left":
                trial["CorResp"] = "left"
            if trial["Orientation"] == "right":
                trial["CorResp"] = "right"
        
            #Define Accuracy
        accuracy = int(trial["CorResp"] == Response)
        Accuracy = accuracy 
        
            #Store RT, Response and Accuracy
        blockTrialsHandler.addData("RT",RT)
        blockTrialsHandler.addData("Response",Response)
        blockTrialsHandler.addData("Accuracy",accuracy)
        
            #Store block number and trialnumber in total
        blockTrialsHandler.addData("Block", block+1)
        blockTrialsHandler.addData("TrialInTotal", trialN+1)
        trialN = trialN+1
        thisExp.nextEntry()
    
    block += 1

#End of the experiment
Bye = visual.TextStim(win, text= "Thank you for participating {0}.\n".format(subject_name)+
                                        "Press space to end the experiment.")
Bye.draw()
win.flip()
event.waitKeys(keyList = "space")


win.close()
core.quit()