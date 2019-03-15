#TEST 4 BY HELENA CORENS ~ 06/03/2019

from psychopy import visual, event, core, gui, data
import time, numpy, os

# SET DIRECTORY
#my_directory = "/Users/HC/Documents/PSYCHO 3/IEP"
#os.chdir(my_directory) + "/data/"

# current working directory
directory_to_write = os.getcwd()

# DIALOG BOX:
info = {"Naam": "","Participant nummer":0, "Leeftijd":0, 
        "Gender":["man", "vrouw","derde gender"], 
        "Handsvoorkeur":["links","rechts", "ambidexter"]}
 
# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Test 4")
    name = info["Naam"]
    number = info["Participant nummer"]
    
    ## Esther: pas op, dit is niet de correcte manier om de subfolder data aan te maken
    
    subject_directory = directory_to_write + "/Test_4_""/Subject_" + str(number)
    if not os.path.isdir(subject_directory):
        os.mkdir(subject_directory)
    file_name = subject_directory + "/subject_nr_" + str(number) + "_data.txt"
    print(file_name)
    
    ## Esther: dit is niet exact de filename die we gevraagd hebben, zetten de puntjes goed op de i
    ## Esther: let ook op, je voegt hier de extensie .txt toe aan de filename. Psychopy zal daar dan zelf de extensie .csv aan plakken en je file check hieronder zal niet werken
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Dit participanten nummer is reeds gebruikt. Gelieve een andere participanten nummer in te geven.")
        myDlg2.show()

## Esther: pas op, je verwijdert hier niet info over de naam van de proefpersoon uit info, dus die staat in je output file
        
print("OK, laten we er aan beginnen!")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)
 
# INITIALIZE WINDOW
win = visual.Window([1000, 700],units = "norm")

# INITIALIZE OTHER
clock = core.Clock()

# GRAPHICAL ELEMENTS
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text=(    "Gegroet {},\n"+
                                                "Welkom op dit experiment!\n"+
                                                "Bij deze taak zal je moeten kijken naar pijltjes.\n"+
                                                "Lees de instructies goed. Er zijn 2 soorten instructies: ofwel zal u zich moeten focussen op de richting van het pijltje \n" +
                                                "ofwel op locatie van het pijltje. +\n"+
                                                "Druk op de spatiebalk om verder te gaan.").format(info["Name"]))
instructie_Position        = visual.TextStim(win,text=(  "Welke richting geeft het pijltje aan?\n"+
                                                "Gebruik de horizontale pijltjes toetsen om de richting aan te wijzen.\n\n"+
                                                "Duw op de spatiebalk indien u er klaar voor bent."))

Instructie_Location        = visual.TextSTim(win,text=( "Waar op het scherm bevind het pijltje zich?\n"+
                                                "Gebruik de pijltjes toetsen om de locatie van het pijltje aan te wijzen.\n" +
                                                "Staat het pijltje op de linkerkant van het scherm, duw dan op het linker pijltje.\n"+
                                                "Staat het pijtlje in het midden, duw dan op het onderste pijltje. \n"+
                                                "Staat het pijltje op de rechterkant van het scherm, duw dan op het rechter pijltje. \n"+
                                                "Duw op de spatiebalk indien u er klaar voor bent."))

goodbye         = visual.TextStim(win,text=(    "Het experiment is afgelopen.\n\n"+
                                                "Danku voor u deelname!"))

# INITIALIZING
blocks    = 12
trails = 60
Stimuli = numpy.array[">",">",">",">",">",">",">",">",">",">",
                     ">",">",">",">",">",">",">",">",">",">",
                     ">",">",">",">",">",">",">",">",">",">",
                     "<","<","<","<","<","<","<","<","<","<",
                     "<","<","<","<","<","<","<","<","<","<",]

Position = numpy.array[(0,-1), (0,0), (0,1),(0,-1), (0,0), (0,1),(0,-1), (0,0), (0,1),
                        (0,-1), (0,0), (0,1),(0,-1), (0,0), (0,1),(0,-1), (0,0), (0,1),
                        (0,-1), (0,0), (0,1),(0,-1), (0,0), (0,1),(0,-1), (0,0), (0,1)
                        (0,-1), (0,0), (0,1)]

# Esther: hm, wat een vreem aantal opties voor zowel stimuli als voor positie, wat was hierbij je denkwijze?

Congruence = numpy.array(["Incongruent", "Congruent"])

#Correct_Resp = 
#Block_Number =
#TrialNr_Block =
#TrialNr_Exp =

#RT = 
#Respons =
#Accuracy =

trials = numpy.Collumn_Stack([Stimuli, Position])
 
# Export as a tab separated file
numpy.savetxt(thisExp, trials, delimiter = '\t') 


# FUNCTIONS

def BLOCKLOOP(): 
    blocknummer = visual.TextStim(win, text = "Blok {0} begint zo dadelijk. Druk op de spatiebalk als je er klaar voor bent.".format(i+1))
    blocknummer.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])

# initialize graphical elements
MessageOnSCreen = visual.TextStim(win, text = "OK")
Stim     = visual.TextStim(win, text = "<")

def message(message_text = "", response_key = "space", duration = 0, pos = "", color = "white"):
    
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

def perform_trial():
    # draw the stimulus on the back buffer
    Stroop_stim.draw()
    
    # clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    
    # display the stimulus on the screen
    win.flip()
    
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    
    # Wait for the response
    keys = event.waitKeys(keyList = [">","<","escape","tab"])
    
    # Register the RT
    RT = my_clock.getTime()
    
    if keys == None:
        keys = [0]
    
    return keys, RT

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instructie.draw()
win.flip()
event.waitKeys(keyList = "space")

for i in range(blocks):
    
    BLOCKLOOP()
    
    for x in range(trails):
        perform_trail() 
        Stroop_stim.draw()


# display the goodbye message
goodbye.draw()
win.flip()
core.wait(2)

# close the experiment window
win.close()



