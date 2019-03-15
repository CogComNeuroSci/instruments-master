#import modules
from psychopy import visual, core, gui, event, data
import time, numpy, pandas, os

# initialize window 
win_width       = 1000
win_height      = 700
win             = visual.Window(size = [win_width, win_height], units = "norm")


# data file management

## GUI : info die moet worden gevraagd
info           = {"Name": "Incognito","Participant Number": str(0), "gender":["male", "female", "X"], "Age":str(0), "Hand preference": ["left", "right", "ambidexter"]}

## Set the directory
My_directory   = os.getcwd() 

## file name
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    # Choose the directory and add "data"
    directory_to_write_to = My_directory + "/data"
    
    ## Als de folder nog niet bestaat, maak deze dan aan
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    #Choose file name and add the particpant number out of the GUI 
    file_name = My_directory + "/Test4_subject_" + str(info["Participant Number"])
    
    ##Als file name al bestaat maak dan een nieuwe aan
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This Participant number was already used. Enter a new participant number.")
        myDlg2.show()

thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

## Haal de naam uit de file om de anonimiteit de garanderen 
pp_name = info["Name"]
info.pop("Name")

# initialize variables
nblocks            = 12
ntrials            = 60

##60 trials: 2 pijltjes en met elk 50% kans
arrows             = numpy.resize(["<", ">"],60)
arrows_answer      = numpy.resize(["left", "right"],60)

##60 trials: 3 posities met elk 20%
positions          = numpy.resize([-0.75, 0, 0.75],60)
positions_answer   = numpy.resize(["left", "down", "right"], 60)

# initialize a clock
my_clock           = core.Clock()
# initialize a clock to measure the RT
my_clock_RT        = core.Clock()

# graphical elements
stimulus                         = visual.TextStim(win,text="")
blockstart                       = visual.TextStim(win,text="")
welcome                          = visual.TextStim(win,text=(
                                                "Welkom op het experiment {}!\n"+
                                                "Je zult tijdens het experiment pijltjes < of > zien op verschillende plaatsen.\n"+
                                                "Soms zul je op de richting van het pijltje moeten reageren en soms op de positie.\n\n"+
                                                "Tijdens het experiment zal worden aangegeven wanneer je wat moet doen. \n\n\n" +
                                                "Druk op de spatiebalk om verder te gaan.").format(pp_name), height = 0.09)

instructions_arrow               = visual.TextStim(win,text=("Als het pijltje naar links wijst (<) moet je op het linkerpijltje van je klavier drukken"+
                                                "Indien het naar rechts wijst (>) moet je op het rechterpijltje van je klavier drukken. \n\n"+
                                                "Druk op de spatiebalk om verder te gaan."), height = 0.09)

instructions_positions           = visual.TextStim(win,text=("Als het pijltje aan de linkerkant van het scherm staat, moet je op je linkerpijltje duwen."+
                                                "Als het pijltje in het midden van het scherm staat moet je op het pijltje naar beneden duwen. \n\n"+
                                                "Als het pijltje aan de rechterkant van het scherm staat moet je op het pijltje rechts duwen. \n\n\n"+
                                                "Druk op de spatiebalk om verder te gaan."), height = 0.09)

goodbye                         = visual.TextStim(win,text=(    "Dit is het einde van het experiment.\n\n"+
                                                "Bedankt voor je deelname!"), height = 0.09)


#Display the welcome message
welcome.draw()
win.flip()
##Druk op spatiebalk om verder te gaan
k = event.waitKeys(keyList = ['space'])


#Implementeer een eenvoudige versie van de trials
for b in range(nblocks):
    
    ## in 1/3 van de blokken op richting van de pijltjes reageren
    if(b+1)%3 == 0:
        instructions_arrow.draw()
    ## in 2/3 van de blokken op de positie van de pijltjes reageren
    else:
        instructions_positions.draw()
    win.flip()
    ## Druk op de spatiebalk om verder te gaan
    k = event.waitKeys(keyList = ['space'])
    
    # randomization
    trial_list = data.createFactorialTrialList({"Richting": arrows, "Orientatie":positions})
    
    #Create trials
    trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "random")
    thisExp.addLoop(trials)
    
    # start the trialloop
    for trial in trials:
        stimulus.text    = trial["Richting"]
        stimulus.pos     = (trial["Orientatie"],0)
        
        ## clear the keyboard before the display of the response
        event.clearEvents(eventType = "keyboard")
        stimulus.draw()
        win.flip()
        ## reset the clock after the win.flip()
        my_clock.reset()
        
        #wait for the response
        keys        = event.waitKeys(keyList = ["left","down","right"])
        
        # register the RT
        RT          = my_clock.getTime()
        print(RT)
        
        #Store RT
        trials.addData("RT",RT)
        
        thisExp.nextEntry()

#        if(b+1)%3 == 0:
#            # determine accuracy 
#            ACC = int(keys[0] == arrows_answer[trial])
#        else:
#            # determine accuracy 
#            ACC = int(keys[0] == positions_answer[trial])


#Display the goodbye message
goodbye.draw()
win.flip()
time.sleep(1)
win.close()