# import modules
from psychopy import visual, event, core, gui, data
import numpy, pandas
import os

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing
nBlocks = 2#12
nBlockTrials = 4 #60
text_width = 0.9
stimuli = ["<", ">"]
position = [-0.5,0,0.5]
#Design = data.createFactorialTrialList({"Arrows": stimuli, "Position": position})
#
## convert to a data frame to easily add dummy columns
#Balanced = pandas.DataFrame.from_dict(Design)
#Balanced["Congruence"] = -1
#Balanced["Balanced"] = 1
#Balanced["CorAns"] = Balanced["Arrows"]
#Balanced["StimType"] = range(Balanced.shape[0])
#
## determine the correct response button
#Balanced["CorAns"].replace(["<",">"], ["left","right"], inplace = True)

## deduce the congruence
#Balanced.loc[Balanced["stimuli"] == Balanced["position"], "Congruence"] = 1
#Balanced.loc[Balanced["stimuli"] != Balanced["position"], "Congruence"] = 0

RespOptions = ["left", "right", "down"]
my_clock    = core.Clock()
info        = {"Participant number": 0, "Name": ":'(", 'gender':['male', 'female', 'other'], 'age':0, 'hand preference':['right', 'left', 'ambidextrous']}


# make sure the data file has a novel name
already_exists = True
while already_exists:
#    
    # present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Arrow task")
#    
#    # construct the name of the folder that will hold the data
    directory_to_write_to = my_directory + "/data"
#    data_file = os.getcwd() + '/data/' + 'experimental_data'
#    # if the folder doesn't exist yet, make it
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
#    # construct the name of the data file
    file_name = directory_to_write_to  + "/data" +  "Test4" + "_subject_" + str(info["Participant number"])
#    
#    # check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
#        
#        # if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
#        
    else:
#        
#        # if the data file name has already been used, ask the participant to inser a different participant number or session number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number or session number")
        myDlg2.show()


# extract the name of the participant from the dialog box information
subject_name = info["Name"]

# graphical elements
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to this task!\n"+
                                                "You'll have to judge whether the arrow\n"+
                                                "is facing left or right.\n\n"+
                                                "Push the space bar to proceed.").format(subject_name),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (left key) for arrows that point to the left\n"+
                                                "Push right (right key) for arrows that point to the right\n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

# remove the name of the participant from the dialog box information (anonimity!)
info.pop("Name")
#
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)
#
# randomization step 1: Within-subjects design
Design = [{"Arrow": "<", "Position": -0.5}, {"Arrow": "<", "Position": 0}, {"Arrow": "<", "Position": 0.5}, {"Arrow": ">", "Position": -0.5}, {"Arrow": ">", "Position": 0}, {"Arrow": ">", "Position": 0.5} ]
#
#
#count = 0
# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")
# start of the block loop
for block in range(nBlocks):
#    
#    # announce the block start
    blockstart.text = ( "Welcome {} to block {}!\n\n"+
                        "Push the space bar to start.").format(subject_name, block+1)
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    Design = data.createFactorialTrialList({"StimulusNumber": range(len(stimuli))})
    Design = [dict(item, Arrow = stimuli[item["StimulusNumber"]])                            for item in Design]
    Design = [dict(item, position_stim = position[item["StimulusNumber"]])                            for item in Design]
    Design = [dict(item, Arrow_Direction     = round(item["StimulusNumber"]/1))                            for item in Design]

    Design = [(dict(item, CorAns = "right") if (item["Arrow_Direction"] == 1) else dict(item, CorAns = "left"))  for item in Design]
#    print('new')
#    print(Design)
#    # create the trials
    trials = data.TrialHandler(trialList = Design, nReps = 3, method = "random") #30
    thisExp.addLoop(trials)
#    
#    
#    # start of the trial loop
    for trial in trials:
#    #    count +=1
#    #    print(count)
#        ## display the stimulus
        stimulus.text = trial["Arrow"]
        stimulus.pos = (trial["position_stim"], 0)
        stimulus.draw()
        win.flip()
#        
#        ## wait for the response
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["left","right"])
#        
#        ## register the output
        trials.addData("response", keys[0])
        trials.addData("RT", my_clock.getTime())
        
        if keys[0] == trial["CorAns"]:
            trials.addData("ACC", 1)
        else:
            trials.addData("ACC", 0)
        thisExp.nextEntry()
#
#
#    # end of the trial loop
# end of the block loop
# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()
#
## creating pandas dataframe from numpy array
#trials = pandas.DataFrame.from_records(trials)
#
## name the columns
#trials.columns = ["ColorWord", "FontColor", "StimType", "Block", "Instruction", "CorAns"]
#print(pandas.crosstab(trials.ACC, [trials.response, trials.Block]))
#
#
#try with arrays
#
#stimuli = numpy.array(["<", ">"])
#position = numpy.array([-0.5,0,0.5])

# ┬─┬ノ( º _ ºノ)     (╯°□°）╯︵ ┻━┻
