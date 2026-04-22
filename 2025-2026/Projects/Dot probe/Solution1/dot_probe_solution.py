## Import modules
import os
import math
import numpy as np
import pandas as pd
from psychopy import visual, event, core, gui, data

## General variables
# Some variables for when we test the experiment:
speedy = 0                  #set to 1 for testing and 0 for subjects
full_screen = True          #set to False for testing and True for subjects

#Variable determining the length of the experiment
Nblocks = 1
Prob_congruent = .5  

## Dialog box and file creation
# create dialog box
info = {'Name': '', 'Number': 0, 'Gender':['Female', 'Male', 'X'], 'Age': 0,'Handedness':['Left', 'Right', 'Both']}

# set the directory
my_directory = os.getcwd()

# GUI and file creation
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Dot probe task")
    directory_to_write_to = my_directory + "/DotProbe"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/DotProbe_subject_" + str(info["Number"]) + "_data"
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, we got participant info")

# Guard anonimity of the participant
subject_name = info["Name"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

##Let's make the design
#Read in the file with words
words = pd.read_csv(my_directory + "/word_pairs.csv", header = None)
words = words.to_numpy()

#durations 
duration = np.array([0.5, 0.6, 0.7, 0.8, 0.9])

#positions
target_pos = [(0,-0.5), (0, 0.5)]
emotional_word_pos = [(0,-0.5), (0, 0.5)]

#responses
response           = np.array(["f","j", "escape"])

# define number of levels for the factors
Npos_target     = len(target_pos)
Npos_word       = len(emotional_word_pos)
Nduration       = len(duration)
Nresp           = len(response) 

Nunique            = Npos_target*Npos_word*Nduration
UniqueTrials       = np.arange(Nunique)

# Full factorial design
pos_target = np.floor(UniqueTrials / (Npos_word*Nduration)) % Npos_target 
pos_word  = np.floor(UniqueTrials / (Nduration))            % Npos_word
dur       = np.floor(UniqueTrials /1 )                      % Nduration

#Deduce congruence and correct responses
congruence = np.array(pos_target == pos_word)*1
CorResp = pos_target

#Combine
design       = np.column_stack([UniqueTrials, pos_target, pos_word, dur, congruence, CorResp]) 

Nwords  = np.shape(words)[0]

print("Factorial design has length: {}".format(Nunique))
print("Words have length : {}".format(Nwords))
print("Now we have to find smallest common multiple")

#Smallest common multiple of 20 and 25 is 100
Nblocktrials = 100

#Extract amount of congruent and incongruent trials based on proportion
Congruent_trials = Nblocktrials * Prob_congruent
Incongruent_trials = Nblocktrials * (1-Prob_congruent)

#Extract congruent trials and incongruent trials
Congr_design = design[design[:,4]==1,:]
print(len(Congr_design))
Incongr_design = design[design[:,4]==0,:]

#Combine them in a proportioned design
Proportioned_design = np.vstack((np.tile(Congr_design, (int(Congruent_trials/len(Incongr_design)),1)), np.tile(Incongr_design, (int(Incongruent_trials/len(Congr_design)),1))))
print(Proportioned_design)

#Repeat the design and the words (use numbers not strings) to reach 100 of each
#design_repeated    = np.tile(design, (int(Nblocktrials/Nunique),1)) #if you don't do the challenge, you can just use this line and comment lines 90 to 99
wordpairs          = np.transpose(np.tile(np.arange(Nwords), (1, int(Nblocktrials/Nwords))))

## Create psychopy visual objects
win             = visual.Window([1000,700], fullscr = full_screen, color = "black", units = "norm")
my_clock        = core.Clock()

## graphical elements
word_up             = visual.TextStim(win,text="", pos = (0, 0.5))
word_down           = visual.TextStim(win,text="", pos = (0, -0.5))
fixation            = visual.TextStim(win,text="+", pos = (0,0))
dot                 = visual.Circle(win, radius = 0.05, fillColor = "blue")

welcome            = visual.TextStim(win,text=( "Hi {},\n\n"+
                                                "Welcome to this experiment!\n\n"+
                                                "Press the space bar to proceed.").format(subject_name))
instruct           = visual.TextStim(win,text=( "First, you will see two words on the screen.\n"+
                                                "Then, a dot will appear on the location of one of the words.\n"+
                                                "Press " + response[0] + " when the dot is on the bottom, or\n"+
                                                "Press " + response[1] + " when the dot is on top. \n\n"+
                                                "To start the experiment, press the space bar."))
goodbye            = visual.TextStim(win,text=( "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"))
                                                
feedback            = visual.TextStim(win,text=( ""))

feedbacks = ["Incorrect!", "Correct!"]
                                                
#Somme added metrics, just for fun
Congruent_RT_list =     []
Incongruent_RT_list =   []
Congruent_Acc_list =    []
Incongruent_Acc_list =  []

#Also optional, but if you want a break between blocks:
Pause_message       = visual.TextStim(win,text=( "You can take a small break\n\n"+
                                                "Press space to continue."))

# execute experiment

## welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

## Experiment loops
#Just for fun we make it scalable to multiple blocks
for b in range(Nblocks):
    
    #This is optional but I present a pause message between blocks
    if b > 0:
        Pause_message.draw()
        win.flip()
        event.waitKeys(keyList = "space")
        
    # Shuffle the order of the design and of the wordpairs
    np.random.shuffle(Proportioned_design)
    np.random.shuffle(wordpairs)
    
    #Add a blocknumber to your data
    block = np.ones(Nblocktrials)*b
    
    #Step 1: Combine them in a total design
    total_design       = np.column_stack([block, Proportioned_design,  wordpairs])
    
    #Step 2: Convert them to a pandas dataframe
    trialsDF = pd.DataFrame.from_records(total_design)
    trialsDF.columns = ["Block","Trial_type", "Position_target", "Position_Emo_word", "Duration", "Congruence", "CorResp", "Wordpair"]
    #If you want you can now check it via the crosstab method 
    print(pd.crosstab(trialsDF.Duration, [trialsDF.Position_target, trialsDF.Position_Emo_word]))
    
    #Step 3: Convert to a list of dictionaries
    trial_list = pd.DataFrame.to_dict(trialsDF, orient = "records")
    
    #Step 4: Add to trial handler and experiment handler
    trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "sequential")
    thisExp.addLoop(trials)
    
    #Now the trial loop
    for trial in trials:
        
        #present fixation cross
        fixation.draw()
        win.flip()
        core.wait(1)
    
        #present emotional and neutral word at the top and bottom
        word_up.text    = words[int(trial["Wordpair"]), int(trial["Position_Emo_word"])]
        word_down.text  = words[int(trial["Wordpair"]), int(trial["Position_Emo_word"])-1]
        word_up.draw()
        word_down.draw()
        win.flip()
    
        #Wait for pre-specified time
        core.wait(duration[int(trial["Duration"])])
    
        #present the dot 
        dot.pos        = target_pos[int(trial["Position_target"])]
        dot.draw()
        
        #Make everything ready for measuring the RT
        event.clearEvents(eventType = "keyboard")
        win.flip()
        my_clock.reset()
    
        # wait for the response, if we use speedy for testing a response is given after 100 ms and always f, otherwise we wait for the participant
        if speedy:
            core.wait(.1)
            keys = ["f"]
        else:
            keys = event.waitKeys(keyList = response)
            if keys[0] == "escape":
                break
        
        #Register RT and accuracy
        RT = my_clock.getTime()
        accuracy = (keys[0] == response[int(trial["CorResp"])]) * 1
        
        feedback.text = feedbacks[accuracy]
        feedback.draw()
        win.flip()
        core.wait(.5)
    
        # store the response information in the ExperimentHandler
        trials.addData("response", keys[0])
        trials.addData("Acc", accuracy)
        trials.addData("RT", RT)
    
        #Register the metrics that we used for fun
        if trial["Congruence"] == 1:
            Congruent_RT_list.append(RT)
            Congruent_Acc_list.append(accuracy)
        else:
            Incongruent_RT_list.append(RT)
            Incongruent_Acc_list.append(accuracy)
    
        # let the ExperimentHandler proceed to the next trial
        thisExp.nextEntry()
    
    if keys[0] == "escape":
        break

## let the experimentHandler know its job is done
thisExp.close()

## say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

## Use the metrics to give some summary info
Acc_con = np.mean(np.array(Congruent_Acc_list))
Acc_incon = np.mean(np.array(Incongruent_Acc_list))
CE_ACC = (Acc_con - Acc_incon)*100

RT_con = np.mean(np.array(Congruent_RT_list))
RT_incon = np.mean(np.array(Incongruent_RT_list))
CE_RT = (RT_incon - RT_con)*1000

print("Congruency effect in terms of accuracy was: {:.2}".format(CE_ACC))
print("Congruency effect in terms of RT was: {:.2}".format(CE_RT))

win.close()
