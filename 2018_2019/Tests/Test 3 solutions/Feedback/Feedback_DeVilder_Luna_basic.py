
# import modules
from psychopy import visual, event, core, gui
import time, numpy

# create a dialog box
info = {"Naam proefpersoon":"", "Proefpersoonnummer":0, "Geslacht":["man", "vrouw", "derde gender"], "Leeftijd": 0, "Handvoorkeur":["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# initialize the window
win = visual.Window(size = [600,500], units = "norm")

# initialize the variables
nblocks = 3
ntrials = 8
key_list = ["f","j"]
### Esther: pas op, deze zijn 10 keer te lang!
SOA = numpy.array([0.16, 0.33, 0.50])
### Esther: hm, ik had gerekend op 30 en -30 ;)
oriëntatie = numpy.array([100, 70])

# deduce the correct response
CorResp     = numpy.array(["f","j"])

# allow to store the accuracy
Accuracy = numpy.repeat(-99.9,len(CorResp))

# add a default response that will be overwritten during the trial loop
Resp = numpy.repeat(0,len(CorResp))

# add a default RT that will be overwritten during the trial loop
RT = numpy.repeat(-99.9,len(CorResp))

# combine arrays in trial matrix
trials = numpy.column_stack([oriëntatie, CorResp, Resp, Accuracy, RT])

### esther: pas op, hier heb je nu nog maar twee trials per block en niet de 8 trials per blok die nodig zijn
# repeat the trial matrix for the three blocks
trials = numpy.tile(trials, (nblocks, 1))

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welkom " + info["Naam proefpersoon"] + "!\n\nDruk op de spatie om verder naar de instructies te gaan.")
Instructions    = visual.TextStim(win, text = "In dit experiment zal u de oriëntatie van een Gabor stimulus moeten inschatten\n" +
                                               "Druk op “f” als u denkt dat de Gabor naar links is gedraaid (de lijnen lopen van linksboven naar rechtsonder).\n" +
                                               "Druk op “j” als u denkt dat de Gabor naar rechts is gedraaid (de lijnen lopen van rechtsboven naar linksonder)." 
                                               , height = 0.05)
### Esther: zorg dat je proefpersonen ook op het einde van de instructies weten op welke knop ze moeten drukken om verder te gaan
Block_start     = visual.TextStim(win, text = "OK")
MessageOnSCreen = visual.TextStim(win, text = "OK")
StartGabor = visual.GratingStim(win, mask = "gauss", ori = 180, sf = 4)
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)



# Initialize a clock to measure the RT
my_clock = core.Clock()

# make a function for presenting messages on screen
def feedback_message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    MessageOnSCreen.text    = message_text
    
    ## Esther: deze drie hieronder veranderen nooit, dus je hoeft ze niet meer opnieuw in te stellen
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    MessageOnSCreen.color   = color
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

# display the welcome message
Welcome.draw()
win.flip()
### Esther: "space" hoeft niet tot een lijst omgevormd te worden 
event.waitKeys(keyList = ["space"])

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])

# display the Gabor stimuli
# in two blocks
for b in range(nblocks):
    
    # announce what block is about to start
    Block_start.text = "Blok " + str(b+1) + " zal nu starten wanneer u op spatie drukt."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    # in trials
#    for i in range(b*ntrials,(b+1)*ntrials):
    for i in range(ntrials):
        
        StartGabor.draw()
        win.flip()
        time.sleep(1)
        
        ### Esther: het is niet nodig om de Gabor stimulus op elke trial opnieuw aan te maken
        Gabor = visual.GratingStim(win, mask = "gauss", ori = 180, sf = 4)
        
        # oriëntatie Gabor
        Gabor.ori = (oriëntatie[b])
        
        # Start met aanbieding Gabor gedurende 1 seconde met een verticale oriëntatie en daarna
        # Aanbieding van de gedraaide Gabor met verschillende aanbiedingstijden
        Gabor.draw()
        
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        win.flip()
        
        # Now that the stimulus is on the screen, reset the clock
        my_clock.reset()
        
        ### Esther: hier moest de core.wait() komen!
        ### Esther: en hier moest dan de mask gepresenteerd worden
        
        # Wait for the response
        keys = event.waitKeys(keyList = ["f","j","escape"])
        
        # Register the RT
        RT = my_clock.getTime()
        
        core.wait(SOA[b])
        #time.sleep(SOA[b])
        
        # Store the response information
        ##trials = numpy.column_stack([oriëntatie, CorResp, Resp, Accuracy, RT])
        #trials[i,2] = keys[0]
        ### Esther: hier heb je waarschijnlijk problemen gehad met het opslaan van een string in een array met nummers
        
        # determine accuracy
        #trials[i,3] = int(trials[i,1] == trials[i,2])
        
        # Store the RT
        #trials[i,6] = RT
        
        StartGabor.draw()
        win.flip()
        time.sleep(1)
        
        feedback_message(message_text = "Correct!", duration = 1)
        # determine the feedback message door terug te koppelen naar accuracy
        #if int(trials[i,3]) == 1:
            #message(message_text = "Correct!", duration = 1)
        #else:
            #message(message_text = "Wrong answer!", duration = 1)
        
        # escape from the trial loop
        if keys[0] == "escape":
            break
    
    ### Esther: en hier dan nog een tweede break om ook uit de blokloop te kunnen breken


# display the goodbye message
Goodbye.draw()
win.flip()
time.sleep(1)

# Ik ben er nog niet helemaal maar ik heb alles geprobeerd wat ik kon. Ik had te weinig tijd om
# de blokstructuur volledig af te krijgen. 