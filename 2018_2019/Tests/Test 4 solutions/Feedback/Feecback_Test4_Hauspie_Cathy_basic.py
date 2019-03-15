#IMPORT MODULES
import numpy, pandas, os, platform
from psychopy import gui, visual, data, event, core

#SET THE DIRECTORY 
my_directory = os.getcwd()

#DIALOG BOX
info = {"Participant number": 0, "Name": "", "Age": 0, "Gender": ["male", "female", "third gender"], "Hand preference": ["left", "right", "ambidexter"]}

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info)
    
    # Esther: hier heb je nog een slash te kort voor data
    
    directory_to_write_to = my_directory + "data" 
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
        
    # Esther: hier hetzelfde, een extra slash was nodig
    
    file_name = directory_to_write_to + "subject_" + str(info["Participant number"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, let's get started!")

subject_name = info["Name"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

#VASTE VARIABELEN
nblocks = 12
nblocktrials = 60
my_clock = core.Clock()

#VISUAL ELEMENTS
win = visual.Window([1000,700], units = "norm")
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Push the space bar to proceed.").format(subject_name))
instructions    = visual.TextStim(win,text="")
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"))

# Esther: hint, je kon hier ook meteen de congruentie in het design gecodeerd hebben ;)

#HANDLER
DesignOr=[{"Stimulus": "<", "Position": -0.5, "Correct":"q"}, {"Stimulus": "<", "Position": 0.5, "Correct":"q"}, {"Stimulus": "<", "Position": 0, "Correct":"q"}, \
          {"Stimulus": ">", "Position": -0.5, "Correct":"m"}, {"Stimulus": ">", "Position": 0.5, "Correct":"m"}, {"Stimulus": ">", "Position": 0, "Correct":"m"}]
DesignPos = [{"Stimulus": "<", "Position": -0.5, "Correct":"q"}, {"Stimulus": "<", "Position": 0.5, "Correct":"m"}, {"Stimulus": "<", "Position": 0, "Correct":"g"}, \
             {"Stimulus": ">", "Position": -0.5, "Correct":"q"}, {"Stimulus": ">", "Position": 0.5, "Correct":"m"}, {"Stimulus": ">", "Position": 0, "Correct":"g"}]
Design = DesignOr + DesignPos

#CONGRUENCE
##convert to a data frame
dataFrame = pandas.DataFrame.from_dict(Design)
##convert to an array
array = dataFrame.values
nrows = len(array)

def congruence_function():
    Congruence = ""
    for i in range(nrows):
        if (array[i,2] == "<") and (array[i,1] == -0.5):
            Congruence = "Congruent"
        elif (array[i,2] == ">") and (array[i,1] == 0.5):
            Congruence = "Congruent"
        elif (array[i,1] == 0.0):
            Congruence = "Neutral"
        else:
            Congruence = "incongruent"
    return Congruence

#INSTRUCTIONFUNCTION
def choose_instruction(bloknr):
    
    # Esther: dit had <=8 moeten zijn
    
    if bloknr < 9:
        instructions.text = ("Responds to the direction of the arrows. \n \n" +
                            "If the arrow points left, press on the left arrow (g).\n \n" +
                            "If the arrow points right, press on the right arrow (m). \n \n" +
                            "Press the space bar to continue.")
        ResponseMapping = "Direction"
    else:
        instructions.text = ("Responds to the position of the arrows. \n"+
                            "If the arrow is on the left side of the screen, press on the left arrow (q).\n \n" +
                            "If the arrow is in the middle of the screen, press on the arrow down (g). \n \n" +
                            "If the arrow is on the right side of the screen, press on the right arrow (m). \n \n" +
                            "Press the space bar to continue.")
        ResponseMapping = "Position"
    instructions.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    return ResponseMapping

#CHOOSE TRIALS
def choose_trials(bloknr):
    # create the trials
    if bloknr < 9:
        Design_block = DesignOr
    else:
        Design_block = DesignPos
        
    # Esther: hieronder was fullRandom nog beter dan random
        
    trials = data.TrialHandler(trialList = Design_block, nReps = 10, method = "random") 
    trials.addData("ResponseMapping", Design_block)
    thisExp.addLoop(trials) 
    return trials

#GREET PARTICIPANT
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

#BLOCKLOOP
for b in range(nblocks):
    
    congruence_function()
    ResponseMapping = choose_instruction(b)
    trials = choose_trials(b)
    Congruence = congruence_function()
    
    acc_block = 0
    
    for trial in trials:
        stimulus.text = trial["Stimulus"]
        stimulus.pos = (trial["Position"], 0)
        stimulus.draw()
        win.flip()
        
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        
        keys = event.waitKeys(keyList = ["q", "m", "g"])
        RT = my_clock.getTime()
        
        ##calculate accuracy
        accuracy = 1*(keys[0]==trial["Correct"])
        acc_block += accuracy
        
        ##save everything
        trials.addData("Bloknr", b + 1)
        trials.addData("Congruentie", Congruence)
        trials.addData("TrialnrExp", (trials.thisTrialN * (b+1)))
        trials.addData("Response", keys[0])
        trials.addData("ResponseMapping", ResponseMapping)
        trials.addData("Accuracy", accuracy)
        trials.addData("RT", RT)
        
        thisExp.nextEntry()

#SAY GOODBYE
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")
