#Import modules
from psychopy import visual, core, gui, event
import time, numpy

#Dialog Box
### Esther: het is nog beter 
info = {"name": "unknown", "participant number": "", "age": "", "gender": ["male", "female", "third gender"], "hand preference": ["left", "right", "ambidexter"]}
Box = gui.DlgFromDict(info)
if Box.OK:
    print(info)
else:
    print("user cancelled")

#Initialize window
win = visual.Window([600,500], units = "norm")

#Initialize the variables
nblocks           = 3
ntrials           = 8
my_clock          = core.Clock()
my_clock_stimulus = core.Clock()
DurationGabor     = [0.016, 0.033, 0.05]
SfGabor           = ([2, 2, 2, 2, 20, 20, 20, 20]*nblocks)
OriGabor          = ([30, 330, 30, 330, 30, 330, 30, 330]*nblocks)
SfAndOri          = numpy.column_stack([SfGabor, OriGabor])

#Initialize the graphic elements
VerticalGabor = visual.GratingStim(win, tex = "sin", ori = 0, mask = "circle")
Gabor         = visual.GratingStim(win, tex = "sin", ori = 0, mask = "circle")

#Store responses
Resp        = numpy.repeat("0", ntrials)
CorrectResp = numpy.repeat("0", ntrials)
trials      = numpy.column_stack([Resp, CorrectResp])
## repeat the trial matrix for the three blocks
trials      = numpy.tile(trials, (nblocks,1))

#Correct response function
def Corresp_function(Ori = 0):
    if Ori == 330:
        CorResp = "f"
    elif Ori == 30:
        CorResp = "j"
    return CorResp

#Feedbackfunction
def feedback_message():
    if trials[i,0] == trials[i,1]:
        fbtext = "Correct!"
    else:
        fbtext = "Verkeerd antwoord!"
    
    fb = visual.TextStim(win, text = fbtext)
    fb.draw()
    win.flip()
    core.wait(1)

#Messagefunction
MessageOnSCreen = visual.TextStim(win, text = "OK")
def message(message_text = "", response_key = "space", duration = 0, color = "white"):
    
    MessageOnSCreen.text    = message_text
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

#Welcome
message(message_text = "Welkom {0}. Druk op spatie om verder te gaan.".format(info["name"]), response_key = "space")

#Instructies
message(message_text = "Druk op f wanneer de Gabor naar links gedraaid is (de lijnen lopen van linksboven naar rechtsonder).\n" +
                       "Druk op j wanneer de Gabor naar rechts gedraaid is (de lijnen lopen van rechtsboven naar linksonder).\n" +
                       "Druk op spatie om verder te gaan", response_key = "space")

#Blockloop
for b in range(nblocks):
    message(message_text = "Dit is blok {0}. \n Druk op spatie om verder te gaan".format(b+1))
    
    for i in range(b*ntrials, (b+1)*ntrials): 
        ##Verticale gaborstimulus
        VerticalGabor.draw()
        win.flip()
        core.wait(1)
        
        ##GaborStim
        Gabor.sf  = SfAndOri[i,0]
        Gabor.ori = SfAndOri[i,1]
        
        Gabor.draw()
        event.clearEvents(eventType = "keyboard")
        win.flip()
        
        my_clock_stimulus.reset()
        my_clock.reset()
        core.wait(DurationGabor[b])
        
        ##Toon de verticale stimulus opnieuw
        VerticalGabor.draw()
        win.flip()
        
        ##hoe lang werd stimulus gepresenteerd
        SP = my_clock_stimulus.getTime()
        
        ##wacht op respons
        keys = event.waitKeys(keyList = ["j", "f", "escape"])
        
        if keys[0] == "escape": ##ontsnappen uit trialloop
            break
        
        RT = my_clock.getTime() ##wat was de reactietijd
        
        ##Correcte respons afleiden
        CorResp = Corresp_function(Ori = SfAndOri[i,1])
        
        ##Resp + corresp opslaan
        trials[i,0] = keys[0]
        trials[i,1] = CorResp
        
        ##feedback
        feedback_message()
    
    ##Ontsnappen uit blockloop
    if keys[0] == "escape":
        break

#Goodbye
message(message_text = "Het experiment is nu gedaan. \nBedankt voor je deelname. \nDruk op spatie om af te sluiten", response_key = "space")

#Close the window
win.close()

print(trials)