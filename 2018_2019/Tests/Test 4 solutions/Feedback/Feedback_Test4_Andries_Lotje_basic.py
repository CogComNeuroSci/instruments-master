#test 4 Lotje Andries (6/3/2019)

#import
from psychopy import visual, event, core, gui, data
import numpy 
import os
import pandas
import numpy

# install window
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height], units = "norm")

#dialogbox
info = {"Participant number":0, "Participant name":"", "Gender":["male", "female", "third gender"], "Age":0, "Handedness":["right", "left", "ambidextrous"]}

## set the directory
my_directory = os.getcwd()

#data file management
## nieuwe naam
already_exists = True
while already_exists:
    ## presenteren dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    # Esther: wat je hier nodig had was /data
    
    ## naam datafolder
    directory_to_write_to = my_directory + "data_Test4_subject"
    
    ## aanmaken indien niet bestaat
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    ## naam geven
    file_name = directory_to_write_to + "/Test4_subjest" + str(info["Participant number"]) + "_data"
    ## al gebruikt
    if not os.path.isfile(file_name + ".csv"):
        ## start als nummer nog niet niet bestaat
        already_exists = False
    else:
        ## wanneer nummer al bestaat
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

#constants
nBlocks=12
nTrials=60
stimuli= numpy.array([">", "<"])
## 3 posities waar pijltje op kan verschijnen, weet dat het niet klopt maar tijdelijke oplossing
position= numpy.array([0.50, -0.50,0])
CorResp = numpy.array([])

# Esther: voor de aankondigingen: zorg dat de proefpersoon altijd weet op welke knoppen ze moeten drukken

# visuals
Welcome         = visual.TextStim(win, text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.")
Instructions    = visual.TextStim(win, text = "OK", height = 0.05)
Block_start     = visual.TextStim(win, text = "OK")
Stimuli_start         = visual.TextStim(win, text= "OK", height = 0)
Goodbye         = visual.TextStim(win, text = "Thank you, goodbye!")

# initialize a clock to measure the RT
my_clock_RT = core.Clock()

# initialize a clock to verify the presentation duration
my_clock_check = core.Clock()

# verwelkoming tonen
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# intstructies tonen
Instructions.draw()
win.flip()
event.waitKeys(keyList = "space")

#Instructions in 2/3 van het experiment
Instructions.text = ("In this experiment you will see arrows on different places on the screen, press the arrowkeys in the same way as the arrow is presented.\n"+ 
"For instance '>' this arrow points to the right so press the right arrow key ->")
#Instructions in 1/3 van het experiment
instrustions.text = ("In this experiment you will see arrows on different places on the screen, press the arrowkey sin the same way as the position from the arrow on the screen.\n" + 
"For instance  when this '>' arrow is presented on the left parts of the screen press the left arrowkey\n"+"When the arrow is presented in the middle of the screen press the down arrowkeys")

# Esther: gezien stimuli en positions een andere lengte hebben kan je ze zeker niet combineren in één array

#combine arrays
factors = numpy.column_stack([stimuli, position])
CorResp = numpy.array([])

#the blocks
for blocki in range (nBlocks):
    numpy.random.shuffle(factors)
    Block_start.text = "Block " + str(blocki+1) + " will start when you press the space bar."
    Block_start.draw()
    for i in range(len(factors)):
        Stimuli_start.text= stimuli
        Stimuli_start.height = position
        Stimuli_start.draw
        core.wait(1)
        event.clearEvents(eventType = "keyboard")
        win.flip()
        my_clock_RT.reset()
        my_clock_check.reset()
#        ## weet dat dit (addData) bij trialhandlers hoort en dus niet binnen dit past, maar wou het toch laten staan)
#        keys = event.waitKeys(keyList = ["left","up", "right", "down"])
#        trials.addData("response", keys[0])
#        trials.addData("RT", my_clock.getTime())
#        
#        ##accuraatheid
#        if keys [0] == stimuli '>':
#            trials.addData("ACC", 1)
#        els: 
#            trials.addData("ACC", 0)
    win.flip()
    event.waitKeys(keyList = "space")

#correct response
for stimuli in range (position):
    
    # Esther: pas op, een syntax fout hier omdat er maar 1 = staat in plaats van 2 (==)
    if stimuli = ">":
        CorResp= numpy.append(CorResp, [0])
    else:
        CorResp= numpy.append(CorResp, [2])

#ik zou eerst trials moeten aanmaken maar weet niet wat ik er in moet zetten 
# creating pandas dataframe from numpy array
trials = pandas.DataFrame.from_records(trials)

# name the columns
trials.columns = ["stimuli", "position", "Congruence", "CorResp", "BlockNumber", "Resp", "Trialnumber_block", "Trialnumber_exp"]

# display the goodbye message
Goodbye.draw()
win.flip()
core.wait(1)
event.waitKeys(keyList = "space")

# close the experiment window
win.close()

# cross table validation
print("Block randomization")
print(pandas.crosstab(trials.stimuli, [trials.position, trials.Block]))
print("Block instructions")
print(pandas.crosstab(trials.Instruction, trials.Block))
print("Correct answers")
print(pandas.crosstab(trials.CorAns, [trials.Instruction, trials.stmuli]))
print(pandas.crosstab(trials.CorAns, [trials.Instruction, trials.position]))

# export
trials.to_csv(path_or_buf = "data_Test4_subject.csv", index = False)
#ik weet dat er heel veel niet klopt, ik snap de principes wel maar vind het moeilijk om toe te passen