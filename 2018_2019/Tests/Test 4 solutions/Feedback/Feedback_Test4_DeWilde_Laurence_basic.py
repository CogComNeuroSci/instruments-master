
from psychopy import visual, event, core, gui, data
import os, platform, math, numpy, pandas

## data file management ##

#create a dialog box
info = {"name": "", "participant number": 0, "age": 0, "gender": ["male", "female", "third gender"], "hand preference": ["left", "right", "ambidexter"]}

# determine the current working directory
directory_to_write = os.getcwd()

# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Data")
    name    = info["name"]
    number  = info["participant number"]
    age = info["age"]
    gender = info["gender"]
    hand= info["hand preference"]
    
    # Esther: pas op, dit is niet de folder naam die we gevraagd hadden
    
    # determine the name of the subject directory
    subject_directory  = directory_to_write + "/data" + "/nr_" + str(number)
    
    # if the directory doesn't exist yet, make it now
    if not os.path.isdir(subject_directory):
        os.mkdir(subject_directory)
    
    # Esther: dit else statement moest uitgevoed worden bij de file naam, niet de folder
    else:
        infoDlg2 = gui.Dlg(title = "Error")
        infoDlg2.addText("Try another participant number")
        infoDlg2.show()
    
    # Esther: de locatie van de file naam ontbreekt
    
    # determine the file name
    file_name = "Test4_" + "subject_" + str(number)
    print(file_name)
    if not os.path.isfile(file_name + ".csv"):
        already_exists = False


# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height], units = "norm")

# initializing
stimuli     = ["<", ">"]
text_width  = 1
my_clock    = core.Clock()
nBlocks = 12
nBlockTrials = 60

# graphical elements

# Esther: dit is zeker niet de correcte manier om de pijltjes toe te voegen aan de text stimulus, het derde argument staat niet op zijn plaats
stimulus        = visual.TextStim(win,text="<",">")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "In deze taak zal je pijlen te zien krijgen\n"+
                                                "ze kunnen een andere richting en positie hebben.\n\n"+
                                                "druk op de spatiebalk om verder te gaan").format(info["name"]),
instruct        = visual.TextStim(win,text=(    "druk op het linkerpijltje op uw toetsenbord\n"+
                                                "als de pijl links op het scherm staat.\n"+
                                                "Druk in op het pijltje naar beneden als het in het midden staat,\n"+
                                                "en druk op het rechter pijltje als het rechts staat.\n\n"+
                                                "druk op de spatie om verder te gaan.")
goodbye         = visual.TextStim(win,text=(    "Dit is het einde van het experiment.\n\n"+
                                                "Bedankt om deel te nemen!"),
# Esther: tracht het soort syntaxfouten zoals hierboven te vermijden zodat je code nog runt

# Esther: er was geen oefenblok gevraagd
def announce_blockstart():
    if block == 0:
        blockstart.text = ("Welkom bij het oefenblok!\n\n"+
                           "Druk op spatie om te starten.")
    else:
        blockstart.text = ( "Welkom bij deel {}\n\n"+
                            "Druk op spatie om te starten.").format(block)
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")

##randomisatie
# make the design based on the core trial characteristics
Options = numpy.array(["<", ">"])
Positions = numpy.array([[-1,0], [0,0], [1,0]])

# Esther: werken met arrays in arrays is om problemen vragen, gebruik liever één waarde per kolom in plaats van geneste structuren

## determine the number of levels for the factor
Nrichting = len(Options)
Npositie = len(Positions)
Nunique = Nrichting * Nrichting

# determine the congruency and even out the congruent and incongruent trials

# Esther: kan < gelijk zijn aan [-1,0] ? :D
## deduce the congruence
CongruenceBoolean = numpy.array("<" == [-1,0]) or (">" == [1,0])
Congruence = CongruenceBoolean*1

UnCongruenceBoolean = numpy.array("<" == [-1,0]) or (">" == [1,0])
UnCongruence = CongruenceBoolean*1


## determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

# Esther: de code hieronder resulteert niet in het factorieel design dat je nodig hebt

## make the 2-by-3 factorial design
PijlRichting = numpy.floor(UniqueTrials / Nrichting)
PijlPositie = numpy.floor(UniqueTrials / 1) %  Npositie

## combine arrays in trial matrix
Design = numpy.column_stack([PijlRichting, PijlPositie])

# make the design for one block
## number of design repetitions per block
nReps = int(nBlockTrials/Nunique)

## repeat the 2-by-3 design five times
blockTrials = numpy.tile(Design, (nReps, 1))

# make the trial stucture for the entire experiment
## number of trials in the experiment
ntrials = nBlocks * nBlockTrials

## make empty trial matrix
trials = numpy.ones((ntrials,3)) * numpy.nan


# fill in the random trial order per block

## loop over the 12 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:2] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 2] = blocki+1


def output():
    global acc
    if block > 0:
        trials.addData("response", keys[0])
        trials.addData("RT", my_clock.getTime())
        
        if keys[0] == trial["CorAns"]:
            trials.addData("ACC", 1)
        else:
            trials.addData("ACC", 0)
            
        thisExp.nextEntry()
    else:
        if keys[0] == trial["CorAns"]:
            acc += 1

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
block = 0
while block < (n_blocks + 1):
    
    # announce the block start
    announce_blockstart()
    
    # randomization
    trials = randomize()
    
    # accuracy tracker
    acc = 0
    
    # start of the trial loop
    for trial in trials:
        
        ## display the stimulus
        stimulus.text = trial["Stimulus"]
        stimulus.draw()
        win.flip()
        
        ## wait for the response
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["",""])
        
        ## register the output
        output()
        
    # end of the trial loop
    
    # Esther: deze voorwaarde voor het updaten van het bloknummer is niet correct
    # update the block number
    if (block == 0 and acc == 4) or block > 0:
        block += 1
# end of the block loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()



