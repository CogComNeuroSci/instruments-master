
##De code die achter de '##' staan zijn delen die niet echt werken zoals gepland
##Deze heb ik er dan uitgelaten zodat het experiment zou kunnen werken

## Esther: OK, prima!

# importeren van de modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy as np
from numpy import random
import os
import platform

#directory
my_directory = os.getcwd()

# window aanmaken
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height],units='norm')

#variabelen aanmaken
info        = {'Name':"","Participant number": 0, "Age": 0,"Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"] } 
nblocks     = 12
nblocktrials= 60
text_width  = 0.9
my_clock    = core.Clock()
RespOptions = ["left","right",'down']

#data file management
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test4")
    directory_to_write_to = my_directory + "/data_Test4"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"]) + "_data"
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

print("OK, let's get started!")
subject_name = info["Name"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

#twee verschillende designs maken 
##hier heb ik de twee verschillende designs aangemaakt met elk hun bijhorende antwoorden -> om accuraatheid te bepalen

## Esther: pas op, in het design hieronder zijn er twee responses die verkeerd gecodeerd zijn

Design_richting=10*[{"pijltje":"<","positie":(-0.75,0),'correct':'left'},{"pijltje":"<","positie":(0,0),'correct':'down'},{"pijltje":"<","positie":(0.75,0),'correct':'left'},
                 {"pijltje":">","positie":(-0.75,0),'correct':'right'},{"pijltje":">","positie":(0,0),'correct':'down'},{"pijltje":">","positie":(0.75,0),'correct':'right'}]

Design_positie=10*[{"pijltje":"<","positie":(-0.75,0),'correct':'left'},{"pijltje":"<","positie":(0,0),'correct':'down'},{"pijltje":"<","positie":(0.75,0),'correct':'right'},
                 {"pijltje":">","positie":(-0.75,0),'correct':'left'},{"pijltje":">","positie":(0,0),'correct':'down'},{"pijltje":">","positie":(0.75,0),'correct':'right'}]

## Esther: je had hierboven ook nog de congruentie kunnen toevoegen aan je design, net zoals je de correcte response hebt toegevoegd ;)

#grafische elementen
stimulus        = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to test 4!\n"+
                                                "Push the space bar to proceed").format(subject_name))
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!").format(subject_name))
blockstart      = visual.TextStim(win,text="")


#definities
##hier heb ik twee verschillende definities in gemaakt
##Omdat 2/3 van de trials moet reageren op de richting van de pijl -> laat ik van trial nummer 1 tot en met 9 de instructies tonen 'RICHTING'
##omdat 1/3 van de trials moet reageren op de positie van de pijl -> lat ik van trial nummer 10 tot en met 12 de instructies tonen 'POSITIE'
def announce_blockstart(blocknr):
    if blocknr < 9:
        blockstart.text = ("You have to react on the direction of the arrow!\n\n"+
                            "If the arrow points to the left, you push the left arrow on your keyboard.\n\n"+
                            "If the arrow points to the right, you push the right arrow on your keyboard.\n\n"+
                           "Push the space bar to start.")
    if blocknr > 9:
        blockstart.text = ("You have to react on the position of the arrow'\n\n"+
                            "If the arrow is on the left side of the screen, you push the left arrow on your keyboard.\n\n"+
                            "If the arrow is on the right side of the screen, you push the right arrow on your keyboard.\n\n"+
                            "If the arrow is in the middle of the screen, you push the arrow pointing downwards on your keyboard.\n\n"+
                            "Push the space bar to start.")
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    

##als de instructies gegeven zijn (hierboven), dan wijs ik het juiste design toe -> zodat de correcte accuraatheid kan bepaald worden
def choose_trials(bloknr):
    
    # esther: pas op, dit had < 8 moeten zijn want python telt van 0 tot 11 in plaats van 1 tot 12
    
    # maken van de  trials
    if bloknr < 9:
        Design_block = Design_richting
    else:
        Design_block = Design_positie
    trials = data.TrialHandler(trialList = Design_block, nReps = 1, method = "random")  
    
    ## Esther: hier is het nog beter om fullRandom te gebruiken in plaats van random
    
    ## Esther: let op, je voert twee keer addLoop uit, namelijke een tweede keer in de blockloop
    
    thisExp.addLoop(trials)                                                             ##om experimenthandler te verbinden aan trialhandler #deze connectie moet gemaakt worden VOOR je loopt over trials
    return trials

#experiment starten
#welkom zeggen
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# starten van de block loop
for block in range(12):

    # maken van de trials voor in de loop
    ##beslissen welke trials
    trials = choose_trials(block)
    thisExp.addLoop(trials)
    
    #beslissen welke instructies gegeven worden
    announce_blockstart(block)
    
    #accuraatheid gelijk aan nul zetten
    acc_block = 0

    # start van de trial loop
    for trial in trials:
    
        ## zorgen dat stimulus erop komtdisplay the number on the screen
        stimulus.pos = trial["positie"]
        stimulus.text = trial["pijltje"]
        stimulus.draw()
        win.flip()
    
        ## wait for the response
        event.clearEvents(eventType="keyboard")
        
        ##de klok aanzetten
        my_clock.reset()
        
        ##de toegelaten keys als antwoord
        keys = event.waitKeys(keyList = ["up","left","right"])
 
        ## Esther: oopsie, je hebt hier up staan als mogelijke response in plaats van down zoals in je list of dictionaries
    
        ## Esther: pro tip: ik zou hier meteen de RT registreren, al is het maar in een tijdelijke variabele
        
        ##accuraatheid bepalen
        accuracy = 1*(keys[0]==trial["correct"])
        acc_block += accuracy
        
        ##conrguentie bepalen
        ###if pijltje == '<' and positie == (-0.75,0):
               ##trials='congruent'
        ###if pijltje == '>' and positie == (0,0.75):
               ##trials='incongruent'
        ##else:
               ##trials='neutraal'
        
        ##alles opslaan wat er in de data file moet komen
        trials.addData("RT",my_clock.getTime())
        trials.addData("Response",keys[0])
        trials.addData("accuracy",accuracy)
        
        ## Esther: de info hieronder hoef je niet meer toe te voegen want die wordt automatisch al toegevoegd door de trialhandler ;)
        
        trials.addData('direction arrow',trial['pijltje'])
        trials.addData('position arrow',trial['positie'])
        trials.addData('Correcte respons',trial['correct'])
        ##trials.addData('congruentie',congruency)
    
        thisExp.nextEntry()
    # einde van de trial loop
    
# goodbye zeggen aan de participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()