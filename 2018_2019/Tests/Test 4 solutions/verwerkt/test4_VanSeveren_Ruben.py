from psychopy import data, visual, event, core, gui, os
import pandas
import numpy
#error op lijn 71: kan de naam niet uit de dialog box halen

#initializing
##clock
my_clock    = core.Clock()

##window

win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height], units = "norm")

## create a dialog box
info = { "Name":"","Participant number": "","Age?": "","Gender": ["male", "female", "third gender"],"Handedness":["right", "left", "ambidextrous"]}

# constants

## number of blocks
nBlocks = 12

## number of trials per block
nBlockTrials = 60

## number of design repetitions per block
nReps = int(nBlockTrials/(3*2))

#Determine working directory
my_directory = os.getcwd()

# make sure the data file has a novel name
already_exists = True
while already_exists:
    
    # present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test4")
    
    # construct the name of the folder that will hold the data
    directory_to_write_to = my_directory + "/data_Test4"
    
    # if the folder doesn't exist yet, make it
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    # construct the name of the data file
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"]) + "_data"
    
    # check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        
        # if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        # if the data file name has already been used, ask the participant to inser a different participant number or session number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number or session number")
        myDlg2.show()

print("OK, let's get started!")



# remove the name of the participant from the dialog box information (anonimity!)
info.pop("Name")

# extract the name of the participant from the dialog box information


# start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)



# make the design based on the core trial characteristics

## make the 3-by-2 factorial design
Arrows = (["<",">"])
Position = [(0.25,0),(0.50,0),(0.75,0)]
Design = data.createFactorialTrialList({"Arrows": Arrows},{"Position": Position})


# graphical elements

welcome         = visual.TextStim(win,text=(    "Welcome!\n"+
                                                " In this experiment you will either respond\n"+
                                                "to the position of an arrow on the screen\n"+
                                                "or to the direction it is pointing.\n\n"+
                                                "Push the space bar to proceed."),
                                    wrapWidth = win_width*text_width)
instructions1= visual.TextStim(win,text=(    "Push arrow related to pointing direction of arrow on screen \n"+
                                                "Push left when left and right when right\n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
instructions2= visual.TextStim(win, text=(   "Push left arrow if stimulus on screen is on the left\n"+
                                              "Push right arrow if stimulus on screen is on the right\n"+
                                              "Push down arrow if stimulus is in the middle of the screen\n\n"+
                                              "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)

goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)




    
# start of the trial loop
for trial in trials:
    
    ## display the number on the screen
    stimulus.Design()
    
    stimulus.draw()
    win.flip()
    
    ## wait for the response
    event.clearEvents(eventType = "keyboard")
    my_clock.reset()
    keys = event.waitKeys(keyList = RespOptions)
    RT = my_clock.getTime()
    
    ## calculate the derived properties
    CorResp = RespOptions[correct[trial["Number"]-1]]
    accuracy = (keys[0] == CorResp) * 1
    
    ## store the information in the ExperimentHandler
    trials.addData("response", keys[0])
    trials.addData("Acc", accuracy)
    trials.addData("RT", RT)
    
    ## let the ExperimentHandler proceed to the next trial
    thisExp.nextEntry()

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instructions1.draw()
win.flip()
event.waitKeys(keyList = "space")

instructions2.draw()
win.flip()
event.waitkeys(keyList = "space")

goodbye.draw()
win.flip()
event.waitkeys(keyList = "space")

core.quit()

