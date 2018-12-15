#TEST 3 BY HELENA CORENS ~ 12/12/2018

from psychopy import visual, event, core, gui 
import time, numpy, random

####################
##   ESSENTIALS   ##
####################

# CREATE DIALOG BOX: registreren gegevens van participant
## NIET VERGETEN: ELEMENTEN INVOEGEN BIJ numpy.column_stack!!!!!! indien gevraagd 
info = {"Naam":".", "Participant nummer":0, "Leeftijd":0, 
        "Gender":["man", "vrouw","derde gender"], 
        "Handsvoorkeur":["links","rechts", "ambidexter"]}

infoDlg = gui.DlgFromDict(dictionary=info, title="Orientatie experiment")
if infoDlg.OK:  
    print(info)
else:
    print("User Cancelled")

naam = info["Naam"]
ppnummer = info["Participant nummer"]

# INITIALIZE THE WINDOW
win = visual.Window(size=[600,500], units = "norm")

# INITIALIZE OTHER
clock = core.Clock()

###############################
##   WELCOME & INSTRUCTIONS  ## 
###############################

# WELCOME SCREEN
Welcome         = visual.TextStim(win, text = "Gegroet {0}! Welkom op dit experiment. \n \nDruk op de spatiebalk om door te gaan.".format(naam))
Welcome.draw()
win.flip()
event.waitKeys(keyList=['space'])

# INSTRUCTION SCREEN
Instruction     = visual.TextStim(win, text = "Zodadelijk zal u een Gabor stimulus zien. Het is de bedoeling dat je deze orientatie gaat inschatten.\n\n"+
                                              "Wanneer de Gabor naar links is gedraaid (lijnen lopen van linksboven naar rechtsonder), duw dan op f.\n"+
                                              "Wanneer de Gabor naar rechts is gedraaid (lijnen lopen van linksboven naar rechtsonder), duw dan op de j.\n\n"+
                                              "Druk op de spatiebalk als u er klaar voor bent")
Instruction.draw()
win.flip()
event.waitKeys(keyList=['space'])

########################
##   INITIALISATION   ## 
########################
# Initialize trails gabor
rotation_trials = numpy.array([30, 30, 30, 30, -30, -30, -30, -30])
sf_trials = numpy.array([2, 20, 2, 20, 2, 20, 2,20,])
##Sf_trials geschranst om te zorgen dat verschillende combinaties sf en rotatie even vaak voorkomen

# Correct Response --> was ik nog aan bezig maar niet genoeg tijd
## CorResp = numpy.copy(rotation_trials)
## CorResp[CorResp == 30]     = "j"
## CorResp[CorResp == -30]   = "f"
## print(CorResp = numpy.copy(rotation_trials))

# Make trial matrix for output:
trials = numpy.column_stack([rotation_trials,sf_trials])

# Initialize info of time for blocks
timeblock1 = 16
timeblock2 = 33
timeblock3 = 50
time_blocks=([16,33,50])

# Initialise info for loop
blocks = 3 ##1 = 16ms/ 2 = 33ms/ 3 = 50ms
ntrails = 8
Accuratesse = [ ]
RTList = [ ]
clock = core.Clock()
counter = 0

# FUNCTIONS

def BLOCKLOOP(): 
#    block_time = ([16,33,50)]
    blocknummer = visual.TextStim(win, text = "Blok {0} begint zo dadelijk. Druk op de spatiebalk als je er klaar voor bent.".format(i+1))
    blocknummer.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])

def GABOR_VERTICAAL():
    gabor_vert = gabor = visual.GratingStim(win, tex="sin", mask="gauss", sf= 10, size=[1.0, 1.0], ori = 0)
    gabor.draw()
    win.flip()
    core.wait(1)

########################
##   DISPLAY TRIALS   ##
########################

for i in range(blocks):
    
    BLOCKLOOP()
    
    for x in range(ntrails):
        ## Voor elke trial een verticale Gabor die 1 seconde wordt getoond
        GABOR_VERTICAAL()
        
        ## trials 
        gabor = visual.GratingStim(win, tex="sin", mask="gauss", size=[1.0, 1.0], sf= trials[x, 1], ori = trials[x,0])
        gabor.draw()
        
        ## verschillenden core.wait() voor elke block maar weet niet goed hoe dit best op te lossen
        #for t in range (blocks):
        #    core.wait(0)
        #   if t = 0:
        #       core.wait(0.016)
        #   elif t = 1:
        #       core.wait(0.033)
        #   else t = 2:
        #       core.wait(0.05)
        
        ## clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        ## Display gabor on screen
        win.flip()
        
        clock.reset()
        
        ## response:
        ### Omdat ik merk dat ik elke keer moet antwoorden vooraleer de volgende trial komt, dacht ik om 
        ### waitKeys naar getKeys te veranderen maar dan krijg ik error ivm 'ESCAPE FROM TRIAL LOOP'
        keys = event.waitKeys(keyList = ["f","j", "escape"])
        
        ## register Reaction Time
        RT = clock.getTime()
        print(RT)
        
        ## ESCAPE FROM TRIAL LOOP
        if keys[0] == "escape":
            break

# display the goodbye message
Goodbye         = visual.TextStim(win, text = "Het experiment is afgelopen. Goodbye ", pos = (0), height = 0.2) 
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()
