# import modules
from psychopy import visual, event, core, gui
import time, numpy

info = {"Participantnummer":0, "Naam":"Unknown", "Gender":["man", "vrouw", "derde gender"], "Leeftijd":0, "Handvoorkeur":["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# initialize the window
win = visual.Window([600,500], units = "norm")

# Initialize a clock to measure RT
my_clock = core.Clock()

# initializing objects
Welcome         = visual.TextStim(win, text = "text still to be written")
Instructions    = visual.TextStim(win, height = 0.08, text = "Zo dadelijk zullen er Gabor stimuli op het scherm verschijnen."+
                                                "De bedoeling is om de oriëntatie van de figuur in te schatten.\n"+
                                                 "Druk op de linker toets (f) wanneer de Gabor naar links gedraaid is"+
                                                 " (de lijnen van de Gabor lopen van linksboven naar rechtsonder)"+
                                                 " en op de rechter toets (j) wanneer de Gabor naar rechts gedraaid is"+
                                                 " (de lijnen lopen van rechtsboven naar linksonder).\n"+
                                                 "Nog vragen?\nDruk op de spatiebalk om verder te gaan.")
Block_Message   = visual.TextStim(win, text = "text still to be written")
Feedback        = visual.TextStim(win, text = "feedback")
Goodbye         = visual.TextStim(win, text = "Je bereikte het einde van dit experiment.\nBedankt voor jouw deelname!")
Stimulus        = visual.GratingStim(win, tex = 'sin', mask = 'gauss', sf = 2, ori = 0)

# Function feedback_message
def feedback_message():
    if Response [0] == CorResp[trial]:
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Verkeerd!"
    Feedback.draw()
    win.flip()
    time.sleep(1)


# Initializing variables
nBlocks             = 3
nTrials             = 8
Block_Numbers       = [1, 2, 3]
Presentation_Time   = [0.016, 0.033, 0.050]
SF_Gabor            = [2    ,   20,     20,     20,     2,      20,     2,      2]*3
Ori_Gabor           = [-30  ,   30,     30,    -30,    30,     -30,   30,     -30]*3
CorResp             = ["f"  ,   "j",    "j",   "f",    "j",    "f",    "j",     "f"]*3
Response_Given      = numpy.repeat("key",nBlocks*nTrials)
Accuracy            = numpy.repeat(numpy.nan,nBlocks*nTrials)

# Welcome
Welcome.text = "Welkom, {0}!\nDruk op de spatiebalk om verder te gaan.".format(info["Naam"])
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# Instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = "space")

# Experiment
for b in range(nBlocks):
    Block_Message.text = "Deel {0}.\nStart het experiment door op de spatiebalk te drukken.".format(str(Block_Numbers[b]))
    Block_Message.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    for trial in range(b*nTrials,(b+1)*nTrials):
        # Mask 1
        Stimulus.sf     = SF_Gabor[trial]
        Stimulus.ori    = 0
        Stimulus.draw()
        win.flip()
        core.wait(1)
        # target
        Stimulus.sf     = SF_Gabor[trial]
        Stimulus.ori    = Ori_Gabor[trial]
        Stimulus.draw()
        
        ### Esther: dit is het goede moment om het keyboard te resetten
        
        win.flip()
        my_clock.reset()
        core.wait(Presentation_Time[b])
        TEST_TIMING = my_clock.getTime()
        print(TEST_TIMING)
        # Mask 2
        Stimulus.sf     = SF_Gabor[trial]
        Stimulus.ori    = 0
        Stimulus.draw()
        ## reset input
        event.clearEvents(eventType = "keyboard")
        ## display Mask 2
        win.flip()
        # Wachten op respons
        Response = event.waitKeys(keyList = ["f","j","escape"])
        # Escape experiment
        if Response[0] == "escape":
            break
        # Registreren van reactietijd
        RT = my_clock.getTime()
        print(RT)
        # Stockeren van responsen
        Response_Given[trial] = Response[0]
        if Response [0] == CorResp[trial]:
            Accuracy[trial] = 1
        else:
            Accuracy[trial] = 0
        feedback_message()
    if Response[0] == "escape":
            break

# Goodbye
Goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

# Close window
win.close()