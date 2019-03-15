from psychopy import visual, event, core, gui, data
import os, platform, math, numpy, pandas


# directory maken
my_home_directory = os.getcwd()
my_directory = my_home_directory
#if platform.system() == "Windows":
#    my_directory = "C:" + my_directory
os.chdir(my_directory) 


# window maken
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height], units = 'norm')
## UNITS IS NORM NOG DOEN!! 

# een toets om uit het experiment te geraken
for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)
    ##in case something somewhere goes wrong


# constants

## number of blocks
nBlocks = 12

## number of trials per block
nBlockTrials = 60


# make the design based on the core trial characteristics

## declare all levels of the factor
stimuli     = numpy.array([">", "<"])
position = numpy.array([(-0.25,0), (0, 0), (0.25,0)])
my_clock    = core.Clock()
info        = { "Participant number": 0, "Age": 0, "Gender": ["male", "female"], "Hand preference":["left", "right", "ambidexter"]}
extra_info = { "Name": ""}
text_width  = 0.9
nblocks = 12
nBlockTrials = 60



#dialog box maken

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = extra_info, title = "Test 4")
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    directory_to_write_to = "data"
    
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    # Esther: pas op, het is de bedoeling dat je de file opslaat in de folder data, dus je moet /data toevoegen aan je filenaam
    
    file_name = "Test4_subject_" + str(info["Participant number"])
    
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Call out for the experimenter to find a name")
        myDlg2.show()
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


# graphical elements
stimulus        = visual.TextStim(win,text="", pos = (0,0))
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Welcome {},\n"+
                                                "Push the space bar to proceed.").format(extra_info["Name"]),
                                    wrapWidth = win_width*text_width)
instruct_locatie        = visual.TextStim(win,text=(    "Push left ('<') when the arrow is located left\n"+
                                                "Push right ('>') when the arrow is located right\n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
instruct_richting        = visual.TextStim(win,text=(    "Push left ('<') when the arrow points left\n"+
                                                "Push right ('>') when the arrow points right\n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)



## IK WEET DAT IK NU VERDER MOET MET EEN EXPERIMENT HANDLER OMDAT IK HET ZO WOU OPSLAAN DOOR DE GUI MAAR DIT LUKTE ME NIET!!

# Esther: dat hoeft niet persé want via een ExperimentHandler en TrialHandler aanpak kan je niet de kruistabellen maken in pandas ;)
    

## determine the number of levels for the factor
Nstimuli = len(stimuli)
Nposition = len(position)
Nunique = Nstimuli * Nposition

## determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 


## make the 4-by-4 factorial design
pijltjes = numpy.floor(UniqueTrials / Nstimuli)
positie = numpy.floor(UniqueTrials / 1) %  Nposition

# Esther: het design dat je bekomt is niet het 2*3 design dat we gevraagd hadden ;)

### combine arrays in trial matrix
## de 3e kollom is oplopend van 0 tot 5
Design = numpy.column_stack([pijltjes, positie, UniqueTrials])
##[[0. 0. 0.]
## [0. 1. 1.]
## [1. 2. 2.]
## [1. 0. 3.]
## [2. 1. 4.]
## [2. 2. 5.]]


# make the design for one block
## number of design repetitions per block
nReps = int(nBlockTrials/Nunique)
# = 10


## repeat the design ten times
blockTrials = numpy.tile(Design, (nReps, 1))


# make the trial stucture for the entire experiment

## number of trials in the experiment
ntrials = nBlocks * nBlockTrials
## = 720

## make empty trial matrix
## nu willen we 6 kolommen
trials = numpy.ones((ntrials,5)) * numpy.nan




# fill in the random trial order per block

## loop over the 12 blocks to randomize each block separately
for blocki in range(nBlocks):

    ## suggest a shuffle
    ## blockTrials is de 60 trials in iedere block
    numpy.random.shuffle(blockTrials)
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    ## = 12 blokken met ieder 60 trials 

    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:3] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 2] = blocki+1
    
    # Esther: dit moest >= 8 geweest zijn
    
    ## correct response
    if blocki >= 7:
        trials[currentTrials, 3] = trials[currentTrials, 0]     ## correct antwoord bepaald door de pijl richting
    else:
        trials[currentTrials, 3] = trials[currentTrials, 1] ## NOG AANPASSEN!!!! GEEN IDEE HOE, DENK ZOIETS ALS HIERONDER MAAR HET LUKT NIET 
    
#        ## als het pijlje in het midden staat, druk dan...
#        if trials[currentTrials, 1] == 0:
#            trials[currentTrials, 3] = x
#        ## als het pijlje links staat, druk dan...
#        if trials[currentTrials, 1] == -0.25:
#            trials[currentTrials, 3] = <
#        ## als het pijlje rects staat, druk dan...
#        else: 
#            trials[currentTrials, 3] = >
#    
## HIER WOU IK HET NUMMER PER BLOK OPGESLAGEN HEBBEN MAAR LUKTE NIET, EN TE WEINIG TIJD
    #trialnummer per blok er in zetten
    #trials[currentTrials, 4] = int(currentTrials/12)

print(trials)



# presenteren van het experiment

#welkom heten
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")


# instructies per blok
## de blokken 1 tot 8 (0 tot 7) willen we deze instructie geven = 2/3
for i in range(nBlocks):
    if i > 7:
        instruct_locatie.draw()
    else:
        instruct_richting.draw()
    win.flip()
    event.waitKeys(keyList = "space")

print(trials)
#ECHTE EXPERIMENT

## HIER MOET IK NOG EEN MANIER VINDEN OM DE STIMULI TE PRESENTEREN
## WEET DAT trial[0] NIET GAAT WERKEN WANT HIJ WEET NIET WAAR HET TE GAAN HALEN


block = 0
while block < (nBlocks + 1):
    for trial in trials:
        
        ## display the stimulus
        stimulus.text = trial[0]
        stimulus.pos = trial[1]
        stimulus.draw()
        win.flip()
        
        
        ## wait for the response
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = [">","<"])
        
        # Esther: dit waren niet de pijltjes die we gevraagd hadden

        RT = my_clock.getTime() 

        ## je gebruikt keys[0] zodat alleen de eerste respons van de pp wordt op genomen en er dus niets verloren gaat
        Response = keys[0]
        ## CorResp IS NOG NIET GEDEFINIEERD OMDAT IK NOG NIET WEET HOE, HEB OP REGEL 162 GEPROBEERD MAAR MISLUKT
        #accuracy = int(trial["CorResp"] == Response)
        print(accuracy)
        acc_block =  acc_block + accuracy
        Accuracy = accuracy 
        
        # Esther: je kan hier inderdaad niet verder doen met de infrastructuur voor de TrialHandler en ExperimentHanlder hier
        
        ## IN EEN TRIAL HANDLER ZOU IK DIT DOEN! 
        ## HIER WEET IK HET NIET + TE WEINIG TIJD
        blockTrialsHandler.addData("RT",RT)
        blockTrialsHandler.addData("Response",Response)
        blockTrialsHandler.addData("Accuracy",accuracy)
        
    # end of the trial loop
    
    # update the block number
    block += 1
 #end of the block loop

# dag zeggen
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")


# Esther: goed dat je hier probeert om de crosstables te maken, maar het is wel wat vijgen na pasen gezien de trials al allemaal uitgevoerd zijn ;)

# Validation and export

## creating pandas dataframe from numpy array
trials = pandas.DataFrame.from_records(trials)

## name the columns
trials.columns = ["Stimulus", "Positie", "Blocknummer","CorResp", "TrialPerBlock"]

print(trials)

## cross table validation
print("Block randomization")
## cross table validation
print(pandas.crosstab([trials.Stimulus, trials.Positie], trials.Blocknummer))


## export
trials.to_csv(path_or_buf = "Test4_subect_subject_", index = False)

