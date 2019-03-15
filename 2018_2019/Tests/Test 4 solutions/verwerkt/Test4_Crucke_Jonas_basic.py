#importeren

from psychopy import data, visual, event, core, gui, os

import random, numpy, pandas


#dialog box

info = {"First Name": "...","Participant number": 0, "Age": 0, "Sex":"M,F,X", "Handpreference":"L,R,Ambidextrous"}


#data file maken en benoemen

data_file = "Test4_subject_{0}".format(info["Participant number"])
directory_to_write_to = os.getcwd() + "/data/"

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(info, title = u"Participant Gegevens")
    number = str(info["Participant number"])
    filename = directory_to_write_to + data_file + number
    if not os.path.isfile(filename + ".csv"):
        already_exists = False

thisExp = data.ExperimentHandler(dataFileName = filename)


# constants

## number of blocks
nBlocks = 12

## number of trials per block
nBlockTrials = 60


#core trial characteristics
##all levels of each factor
arrow=numpy.array(["<",">"])
arrow_position=numpy.array(["(-0.75,0)","(0,0)","(0.75,0)"])

##determine number of levels
NArrow = len(arrow)
NArrow_position=len(arrow_position)
NUnique=NArrow*NArrow_position

##number of unique trials
UniqueTrials = numpy.array(range(NUnique)) 

# make the 2-by-3 factorial design
arrow_options = numpy.floor(UniqueTrials / NArrow)
arrow_position_options = numpy.floor(UniqueTrials / 1) %  NArrow_position

## combine arrays in trial matrix
Design = numpy.column_stack([arrow_options, arrow_position_options])


# make the design for one block

## number of design repetitions per block
nReps = int(nBlockTrials/NUnique)

## repeat the 2-by-3 design ten times
blockTrials = numpy.tile(Design, (nReps, 1))


# make the trial stucture for the entire experiment

## number of trials in the experiment
ntrials = nBlocks * nBlockTrials

## make empty trial matrix
trials = numpy.ones((ntrials,3)) * numpy.nan


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:2] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 2] = blocki+1





#window
win=visual.Window(size=(1000,700),units="norm")

#interactie met proefpersoon
welkomtekst=visual.TextStim(win, text="Welkom, {0}! \nOm verder te gaan naar de instructies druk op spatie.".format(info["First Name"]))
introductie=visual.TextStim(win, text="Tijdens de trials van dit experiment zal je een oordeel moeten vellen over de orientatie of de positie van pijltjes. \nDruk op spatie om verder te gaan.")
instructies_positie=visual.TextStim (win, text="In de positie blokken druk je op de linkerpijl wanneer de pijl links staat, ongeacht de orientatie en op de rechterpijl wanneer de pijl rechts staat.\nIn de positie blokken is het ook mogelijk dat er een pijltje in het midden staat, dan druk op de pijl naar beneden op je toetsenbord.\nDruk op spatie om het experiment te starten.")
instructies_orientatie=visual.TextStim(win, text=".Wanneer er in de orientatie blokken een pijltje naar links wijst druk je op de linkerpijl toets op het toetsenbord.\nWanneer het pijltje naar rechts wijst druk je op de rechterpijl toets op het toetsenbord.\nDruk op spatie om verder te gaan.")
afscheid=visual.TextStim(win, text="Bedankt voor uw deelname, {0}! n\Tot ziens!".format(info["First Name"]))


#drawen
welkomtekst.draw()
win.flip()
event.waitKeys(keyList="space")
introductie.draw()
win.flip()
event.waitKeys(keyList="space")
instructies_positie.draw()
win.flip()
event.waitKeys(keyList="space")
instructies_orientatie.draw()
win.flip()
event.waitKeys(keyList="space")


#block
for block in range (10):
    pijltjes=visual.TextStim(win,text=random.choice(arrow), pos=random.choice(arrow_position))
    pijltjes.draw()






















afscheid.draw()
win.flip()
event.waitKeys(keyList="space")
win.close()


