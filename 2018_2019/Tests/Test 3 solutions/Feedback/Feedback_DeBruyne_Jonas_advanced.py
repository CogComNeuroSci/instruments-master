# import modules
from psychopy import visual, event, core, gui
import time, numpy, random

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
    if Response [0] == Matrix[trial,3]:
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

SF_Gabor            = numpy.array([2, 20])
Ori_Gabor           = numpy.array([-30, 30])

## MATRIX
Subject                     = numpy.repeat(info["Participantnummer"],nBlocks*nTrials)
Ori                         = numpy.repeat(numpy.nan, nBlocks*nTrials)
SpaFre                      = numpy.repeat(numpy.nan, nBlocks*nTrials)
Correct_Response            = numpy.repeat("CorKey", nBlocks*nTrials)
Reaction_Time               = numpy.repeat(numpy.nan, nBlocks*nTrials)
Response_Given              = numpy.repeat("RespKey",nBlocks*nTrials)
Accuracy                    = numpy.repeat(numpy.nan,nBlocks*nTrials)
Effectieve_Presentatietijd  = numpy.repeat(numpy.nan,nBlocks*nTrials)
Geplande_Presentatietijd    = numpy.repeat(numpy.nan,nBlocks*nTrials)

Matrix = numpy.column_stack([Subject, Ori, SpaFre, Correct_Response, Reaction_Time, Response_Given, Accuracy, Effectieve_Presentatietijd,Geplande_Presentatietijd])

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
        # Store planned presentation time
        Matrix[trial,8]=Presentation_Time[b]
        
        # Mask 1
        Stimulus_sf     = random.choice(SF_Gabor)
        Stimulus.sf     = Stimulus_sf
        Stimulus.ori    = 0
        Stimulus.draw()
        win.flip()
        core.wait(1)
        
        # target
        Stimulus.sf     = Stimulus_sf
        Stimulus_ori    = random.choice(Ori_Gabor)
        Stimulus.ori    = Stimulus_ori
        
        ## Aanvullen eigenschappel trial in matrix
        Matrix[trial, 2] = Stimulus_sf
        Matrix[trial, 1] = Stimulus_ori
        
        if Stimulus_ori == -30:
            Matrix[trial, 3] = "f"
        elif Stimulus_ori == 30:
            Matrix[trial, 3] = "j"
        
        Stimulus.draw()
        
        ### Esther: OK!
        ## reset input
        event.clearEvents(eventType = "keyboard")
        
        ## display target
        win.flip()
        
        ## reset clock
        my_clock.reset()
        
        ## Aanbiedingstijd instellen en aanvullen in matrix
        core.wait(Presentation_Time[b])
        TEST_TIMING = my_clock.getTime()
        Matrix[trial,7] = TEST_TIMING
        
        # Mask 2
        Stimulus.sf     = Stimulus_sf
        Stimulus.ori    = 0
        Stimulus.draw()
        ## reset input
        
        ## display Mask 2
        win.flip()
        
        ### Esther: dit is een beter moment om de presentatietijd te meten
        
        # Wachten op respons
        Response = event.waitKeys(keyList = ["f","j","escape"])
        
        # registreren Response
        Matrix[trial, 5] = Response[0]
        
        # Escape experiment
        if Response[0] == "escape":
            break
        
        # Registreren van reactietijd
        RT = my_clock.getTime()
        Matrix[trial, 4] = RT
        
        # Stockeren van responsen
        Response_Given[trial] = Response[0]
        
        # Stockeren van accuracy
        if (Response [0] == "f" and Stimulus_ori == -30) or (Response[0] == "j" and Stimulus_ori == 30):
            Matrix[trial, 6] = 1
        else:
            Matrix[trial, 6] = 0
        feedback_message()
    ## Escape
    if Response[0] == "escape":
            break

# Print Matrix
print(Matrix)

# Goodbye
Goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

# Close window
win.close()