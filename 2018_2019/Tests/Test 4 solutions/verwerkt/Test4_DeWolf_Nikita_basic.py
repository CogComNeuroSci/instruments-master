#Test 4 2018-2019, March 6th
#Made by Nikita De Wolf, number 01608179

#import modules
from __future__ import division
from psychopy import visual, event, core, data, gui
import os, platform, math, pandas
import numpy
from numpy import random

#set directory
my_directory = os.getcwd()

#initialize the window
win = visual.Window(size= [700, 1000], color = (-1, -1, -1), units= "norm")

#Create a dialog box that registers the name, number, gender, age and hand preference of the participant
#Data file creation
info = {"Participant number": str(0), "Name": "", "Gender": ["Woman", "Man", "Other"], "Hand Preference": ["left handed", "right handed", "ambidextrous"]}

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test4")
    
    directory_to_write_to = my_directory + "/data_Test4"
    
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"]) 
    
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Oops! This number already exists. Please insert another number.")
        myDlg2.show()

print("OK, we can start!")

#Guarantee anonimity of the participant
subject_name = info["Name"]
info.pop("Name")

#Initialize ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

## 12 blocks
## 60 trials per block
#initialize variables
my_clock = core.Clock()
nblocks = 12
ntrials = 60
participant = info["Participant number"] 
Stimulus = visual.TextStim(win, text = "Stim")

##BALANCED DESIGN!!


#Make a function called 'message' for later use
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    MessageOnScreen.text = message_text
    MessageOnScreen.height = height
    MessageOnScreen.pos = pos
    MessageOnScreen.color = color
    
    MessageOnScreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

#Stimuli
Direction = numpy.array(["<", ">"])
Position = numpy.array([1/4, 2/4, 3/4])
Stimuli = numpy.append([Direction], [Position])

#Allow to store the correct response
CorResp = numpy.repeat("", len(Stimuli))

#Allow to store the accuracy
Accuracy = numpy.repeat(-99.9, len(Stimuli))

#Default RT that will be overwritten
RT = numpy.repeat(numpy.nan, len(CorResp))

#Default Response that will be overwritten
Resp = numpy.repeat(0, len(CorResp))

#Put the variables in a column
trials = numpy.column_stack([Stimuli, CorResp, Accuracy, RT, Resp])
print(trials)

#Initialize the instructions for either when the participants should focus on the direction of the arrow (2/3), or when they should focus on the position of the arrow (1/3)
Instr = visual.TextStim(win, text = "Instructions")
Instr.text =    ("Carefully read the instructions during this experiment, as they will change across blocks.\n\n" +
                "In this block, you will see an arrow (< or >).\n" 
                "The arrow can be pointed in the left direction or right direction \n"+
                "You have to respond to the direction of the arrow. \n"+
                "This means, that when the arrow is directed to the left side (<), you respond with the arrow on your keyyboard that is also pointing out to the left side (<).\n"+
                "When the arrow is pointed to the right side (>), you respond using the right arrow on your keyboard.\n" +
                "When in doubt, contact the experimenter.\n"+
                "Press the spacebar when you're ready to continue")

Instr2 = visual.TextStim(win, text = "Instructions")
Instr2.text=    ("Carefully read the instructions during this experiment, as they will change across blocks.\n\n" +
                "In this block, you will see an arrow (< or >).\n" 
                "The arrow can be in the middle of the screen, to the left or the right of the screen \n"+
                "You have to respond to their location. By this, we mean that when the arrow is on the left side of the screen (<), you respond with the left arrow in your keyboard. \n"+
                "When the arrow is in the middle, you react with the arrow on your keyboard that goed downwards.\n"+
                "Finally, when the arrow is to the right side of the screen (>), you respond again by pressing the arrow on the right of your keyboard.\n"+
                "When the arrow is pointed to the right side (>), you respond using the right arrow on your keyboard.\n" +
                "When in doubt, please contact the experimenter.\n"+
                "Press the spacebar when you're ready to continue")


#deduce the Congruence
##Nog te bepalen dat wanneer het pijltje naar links wijst en links op het scherm staat, deze trials congruent zijn. 
##Trials waarbij het pijltje naar rechts wijst en rechts staan, zijn ook congruente trials.
## Als het pijltje in het midden staat, is de trial neutraal (niet congruent en niet incongruent)


#Starting the Experiment: drawing the instructions and waiting for the spacebar to be pressed
Instr.draw()
win.flip()
event.waitKeys(keyList = "space")

#make a definition for a trials
def perform_trial():
    #draw stimulus (back buffer)
    Stimulus.draw()
    
    #clear keyboard input
    event.clearEvents(eventType = "keyboard")
    
    #display stimulus on screen, so the stimulus appears
    win.flip()
    
    #reset the clock
    my_clock.reset()
    
    #wait for the response
    keys= event.waitKeys(keyList = ["keyboard"]
    
    #Register the RT
    RT = my_clock.getTime() ##neemt de tijd van wanneer de proefpersoon een toets indrukt
    
    if keys == None:
        keys = [0]
    return keys, RT

##function to deduce correct response 
##def determine_CorResp(target = "arrow"):
##    if target =="<":
##        CorResp = ""
##    elif target == ">":
##        CorResp = ""
    
##    return CorResp

#keep track of average RT and Accuracy
averageRT = [ ]
averageACC = [ ]

#display a personalized welcome message
message(message_text = "Welcome" + info["Name"] +"!\n\nPress the spacebar to continue.", response_key = "space")

#Display the actual Stimuli# 12 blocks
for b in range(nblocks):
    #reset instructions
    InstrType = "None"
    
    #task instruction 
    InstrType = which_type[b]
    
    #display instructions
    if InstrType == "Direction":
        Instructi
    elif InstrType == "Position":
        Ins
    #announce that the experiment is going to start
    message(message_text = "The experiment is about to start. Press the space bar to start block" + str(b+1) + ".",  response_key = "space")
    
    for i in range(b*ntrials, (b+1)*ntrials): ##zo gaat die varieren van trial op trial binnen de blockloop
        #store RT and response info
        trials[i,4] = keys[0] ##de eerste key dat men indrukt wordt als definitief respons geregistreerd door python
        trials[i,2] = int(trials[i,3] == trials[i,4]) ## de accuratesse is de gelijkstelling van de correcte respons met de actuele respons
        trials[i,3] = RT

#informatie toevoegen van de trialhandler naar de experimentalhandler
    blockTrialsHandler.addData("RT",RT)
    blockTrialsHandler.addData("Response",Response)
    blockTrialsHandler.addData("Accuracy",accuracy)

        blockTrialsHandler.addData("Block", block+1)
        thisExp.nextEntry()

#Close the window at the end
win.close()
core.quit()

"""sorry ik kom wederom te kort in tijd. het eerste deel van het experiment van de dialog box ging perfect 
maar ik kan het niet meer genoeg fixen dat het experiment runt door tijdsnood"""