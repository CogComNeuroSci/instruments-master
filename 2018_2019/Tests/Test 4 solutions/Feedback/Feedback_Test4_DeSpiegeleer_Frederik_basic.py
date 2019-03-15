# import
from psychopy import visual, event, core, gui, data
import time, numpy, os, platform, math

# set the directory
## determine the current working directory
directory_to_write = os.getcwd()


# Esther: pas op, we hadden om een window van een bepaalde grootte gevraagd!

# initialize the window
win = visual.Window(fulscr = False, size = [1000, 700])

# initializing
stimuli     = ["<", ">"]
posities     = [-0.5, 0, 0.5]
my_clock    = core.Clock()
n_blocks    = 12
n_trials    = 60

# participant
info = {"participant number":0, "participant name" : "unkown", "age" : 0, "gender" : ["male", "female", "other"], 
        "handpreference" : ["left", "right", "ambidexter"]}

# escape

event.globalKeys.add(key="escape", func=core.quit, name="shutdown")

# Data file
## keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    ## display the gui
    infoDlg = gui.DlgFromDict(dictionary = info, title="Test4"
        , order = ["participant number", "participant name"])
    number = info["participant number"]
    
    # Esther: hier moest de folder nog aangemaakt worden
    
    ## determine the name of the file
    file_name = directory_to_write + "/Test4_subject_" + str(number)
    
    ## message and save .csv
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This name was already used. Please ask the experimenter to help you to enter a unique name.")
        myDlg2.show()
print("OK, let's get started!")

# Esther: let op: op deze manier wordt de naam van je proefpersoon ook opgeslagen in de output file!

thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


# congruency
def congruence(congruency):
    """
    stimulus.text   = stimuli[]
    stimulus.pos    = posities[]
    """
    
    # Esther: deze logica is correct!
    
    congruencyList = ["congruent", "incongruent", "neutral"]
    if pos == 0:
        congruency = congruencyList[2]
    elif stimulus.text == "<" and pos == -0.5 or stimulus.text == ">" and pos == 0.5:
        congruency = congruencyList[0]
    else: 
        congruency = congruencyList[1]

# Correct responses
def accuracy():
    
    # Esther: pas op, ik zie niet in hoe dit resulteert in 8 blokken met de ene mapping en 4 blokken met de andere mapping
    if block in range(4, 6):
        
        # Esther: die tussenstappen via conditie zijn eigenlijk overbodig
        
        conditie = numpy.array(posities)
        CorResp      = numpy.copy(conditie)
        
        # Esther: pas op, je bent hier nummer en strings door elkaar aan het gebruiken, dat levert errors op
        
        CorResp[CorResp == -0.5]       = "left"
        CorResp[CorResp == 0.5]      = "right"
        CorResp[CorResp == 0]     = "down"
    else:
        conditie = numpy.array(stimuli)
        CorResp      = numpy.copy(conditie)
        CorResp[CorResp == "<"]       = "left"
        CorResp[CorResp == ">"]      = "right"

# tekst
stimulus        = visual.TextStim(win, text="", pos= (0,0))
welcome         = visual.TextStim(win,text=(    "welcome {},\n"+
                                                "In the first condition\n"
                                                "you'll have to judge whether the stimulus\n"+
                                                "is pointing left or right.\n"+
                                                "In the other condition\n"+
                                                "you'll have to judge whether the stimulus\n"+
                                                "is positioned on the left side, in the middle or on the right side.\n"+
                                                "of the screen\n\n"+
                                                "Push the space bar to proceed.").format(info["participant name"]))
instructie1        = visual.TextStim(win,text=(    "Push left on the arrow keys for the left arrow\n"+
                                                "Push right on the arrow keys for the left arrow\n\n"+
                                                "Push the space bar to start the experiment."))
instructie2        = visual.TextStim(win,text=(    "Push left on the arrow keys when de arrow is positioned on left side\n"+
                                                "Push down on the arrow keys when de arrow is positioned in the middle\n"+
                                                "Push right on the arrow keys when de arrow is positioned on right side\n\n"+
                                                "Push the space bar to start the experiment."))
goodbye             = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"))

def instr_block():
     # Esther: pas op, ik zie niet in hoe dit resulteert in 8 blokken met de ene mapping en 4 blokken met de andere mapping
    if block in range(4, 6):
        instructie1.draw()
    else:
        instructie2.draw()
    win.flip()
    event.waitKeys(keyList = "space")

# randomisatie
def randomize():
    StimuliOptions     = numpy.array(stimuli)
    PositiesOptions = numpy.array(posities)
    ## determine the number of levels for the factor
    Nstimuli     = len(StimuliOptions)
    Nposities      = len(PositiesOptions)
    Nunique     = Nposities * Nstimuli
    ## determine the number of unique trials
    UniqueTrials = numpy.array(range(Nunique)) 
    ## make the factorial design
    Stimu = numpy.floor(UniqueTrials / Nstimuli)
    Posit = numpy.floor(UniqueTrials / Nstimuli) % Nposities
    ## combine arrays in trial matrix
    trials = numpy.column_stack([Stimu, Posit])
    
    # Esther: dit factorieel design klopt niet helemaal, close but no cigar
    
    print(trials)
    
    # Esther: inderdaad, je moet eerste even de array omzetten in een list of dictionnaries want dat is het formaat dat de trialHandler nodig heeft
    # Esther: het eenvoudigste is om een eerst de array om te zetten naar een dataframe en daarna de dataframe om te zetten naar een list of dictionnaries
    # Esther: tijdens die tussenstop kan je ook de kolomnamen toevoegen, die kan je dan gebruiken in je trialloop
    
    # de combinatie van het bovenste en hieronder is volgens mij een slechte combinatie 
    trials = data.TrialHandler(trials, nReps = 10, method = "random")
    
    # Esther: hier had je ook beter fullRandom gebruikt in de plaats van random


# welcome 
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
block = 0
while block < (n_blocks + 1):
    
    # instructions before every block
    instr_block()
    
    # randomization
    trials = randomize()
    
    
    # start of the trial loop
    for trial in trials:
        
        ## display the stimulus
        stimulus.text = trial["Stimu"]  # ik probeer hier de stimuli text en positie aan te passen door te zoeken naar de numpy.floor in randomize(), dit klopt niet
        stimulus.pos  = (trial["Posit"], 0)
        stimulus.draw()
        win.flip()
        
        # keys moeten nog aangepast worden per conditie
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["left", "right"])
        
        # Esther: bij de response opties hoort ook de optie down
        
        # de output zou hier nog moeten komen
        
        
    
    ## update the block number
    block += 1
# end of the block loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()


