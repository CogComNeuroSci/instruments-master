"""Test 4 IEP 06/03/2019: Chapter 7 & Chapter 8
Clara Van Isterdael - 01600474
Participants get to see an arrow (< or >) on either the left, right or middle of the screen
2/3 of the time, they must react to the orientation of the arrow. 1/3  of the time to the position on the screen"""


#door tijdsgebrek, kon ik de taak niet afwerken
#ik heb besloten om mij eerst te focussen op Data File management & randomisaties (aangezien dit mij voor deze test het belangrijkst leek
#jammer genoeg heb ik hierdoor geen visuele elementen kunnen invoeren... 

#import modules
import os, numpy, time, pandas
from psychopy import gui, visual, core, event, data

##Install GUI and store data  (Data File Management)
# create a dialog box
info = {"Naam":"Onbekend", "Proefpersoonnummer":0, "Leeftijd": 0, "Gender":["", "Man", "Vrouw", "Derde gender"], "Handvoorkeur": ["", "Links", "Rechts", "Ambidexter"]}

#determine the current working directory
directory_to_write_to = os.getcwd() + "\\data\\"
if not os.path.isdir(directory_to_write_to):
    os.mkdir(directory_to_write_to)

# keep asking for a new name when the data file already exists
already_exists = True

while already_exists:
 # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Pijltjestaak", order = ["Naam", "Proefpersoonnummer", "Leeftijd", "Gender", "Handvoorkeur"])
    
    # determine the name of the subject file
    filename  = directory_to_write_to + "Test4_subject_" + str(info["Proefpersoonnummer"])
    
# verify whether this file name already exists
    if not os.path.isfile(filename+ ".csv"):
        already_exists = False

    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
# instead of a list of strings of seperate letters, Gender & Handvoorkeur should be one string
info["Gender"]= "".join(info["Gender"])
info["Handvoorkeur"]="".join(info["Handvoorkeur"])

#store the participant name for further use
name        = info["Naam"]

#delete name of the file for anonimity
info.pop("Naam")

#introduce experimentHandler
thisExp = data.ExperimentHandler(dataFileName = filename, extraInfo = info)

##Randomizations
##initialise the constants

#number of blocks 
nBlocks = 12

#number of trials per block
nBlockTrials = 60

##Make the experiment design based on the core trial characteristics
ArrowOrient = numpy.array(["<",">"])
ArrowPos    = numpy.array([0.25,0.75,0.5]) #we will fill these number in in place of the horizontal coordinates of the stimulus position

#determine the number of levels for the factor
Npos = len(ArrowPos)
Norient = len(ArrowOrient)
Nunique = Npos*Norient

#determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique))

#Make a 2-by-3 factorial design
Orientation = numpy.floor(UniqueTrials/ Npos)
Position = numpy.floor(UniqueTrials)%Npos

#deduce the other trial characteristics
CongruenceLevels = numpy.array(["Incongruent", "Congruent"])
Congruence = numpy.array(Orientation == Position)


#Combine arrays into trial matrix
Design = numpy.column_stack([Orientation, Position, Congruence])

#deduce congruence
for i in range(len(Congruence)):
    if Design[i,1]==2.:
        Design[i,2]=2. #0 means incongruent, 1 means congruent, 2 means neutral

##make the design for one block

#number of design repititions per block
nReps = int(nBlockTrials/Nunique)

#repeat the 2*3 design 10 times
blockTrials = numpy.tile(Design, (nReps, 1))

##Make the trial structure for the entire experiment
#number of trials in the experiment
ntrials = nBlocks*nBlockTrials

#make an empty trial matrix
trials = numpy.ones((ntrials,11))*numpy.nan 
#11 columns because it will store: 1. block number 2. trial number within the block 3. trial number in the experiment 4.arrow orientation 5. arrow position 6. congruence 7.response mapping (orientation vs. position) 8. correct response 9. given  response 10. accuracy 11. RT

##Fill in the random trial order per block
#loop over the 12 blocks to randomise each block seperately
for blocki in range(nBlocks):
    #randomize trial order
    numpy.random.shuffle(blockTrials)
    
    # trial number within the whole experiment for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    # fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 0] = str(blocki+1)
    
    #fill in the trial number within the block
    trials[currentTrials,1]= numpy.array(range(nBlockTrials))
    
    #fill in the trial number within the whole experiment
    trials[currentTrials,2]= currentTrials
    
    # store the trials for this block in the experiment array
    trials[currentTrials, 3:6] = blockTrials

    # store the response mapping and correct response
    if blocki%3==0:
        trials[currentTrials, 6] = 0 #1/3d of the trials, participants must respond to position
        trials[currentTrials,7]= trials[currentTrials,4]
    else:
        trials[currentTrials, 6] = 1 #the other blocks, they must response to orientation
        trials[currentTrials,7]= trials[currentTrials,3]


# creating pandas dataframe from numpy array
trials = pandas.DataFrame.from_records(trials)

# name the columns
trials.columns = ["block number", "trial number within the block", "trial number in the experiment", "arrow orientation", "arrow position", "congruence", "response mapping", "correct response", "given  response", "accuracy", "RT"]

# export
trials.to_csv(path_or_buf = directory_to_write_to + "Test4_subject_" + str(info["Proefpersoonnummer"]) +"output_arrays.csv", index = False)
