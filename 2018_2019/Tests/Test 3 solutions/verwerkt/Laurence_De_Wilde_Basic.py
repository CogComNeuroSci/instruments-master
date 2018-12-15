# importeren modules
from __future__ import division
from psychopy import visual, event, core, gui
import time



# window aanmaken 
win_width = 600
win_height = 500
win = visual.Window(size = [win_width,win_height], units = "norm")


#gegevens test verzamelen (initializing)
n_blocks    = 3
n_trials    = 8
text_width  = 1
my_clock    = core.Clock()



# maken dialoogvenster
def check_input_device():
    info = {"name":"", "Participant number":0,"age":"","gender":["man","vrouw","neutraal"], "handvoorkeur":["links","rechts","ambidexter"]}
    gui.DlgFromDict(dictionary = info)
    return info
participant_info = check_input_device()



# stimuli op scherm brengen
welkom          = visual.TextStim(win,text=(    "Welkom {},\n"+
                                                "Druk op de spatiebalk om te beginnen.").format(participant_info["name"]),
                                                wrapWidth = win_width*text_width)


instruct        = visual.TextStim(win,text=(    "Druk op de letter f als de gabor, \n"+
                                                "naar links gedraaid is (de lijnen, \n"+
                                                "lopen van linksboven naar rechtsonder.\n\n"+
                                                "Druk op de letter j als de gabor, \n"+
                                                "naar rechts gedraaid is (de lijnen, \n"+
                                                "lopen van rechtboven naar linksonder. \n\n"
                                                "Druk op de spatiebalk, \n"+
                                                "om met het experiment te starten."),
                                                wrapWidth = win_width*text_width)

blockstart      = visual.TextStim(win,text=(   "Als je op de spatiebalk drukt, start blok "),
                                                wrapWidth = win_width*text_width)

afscheid         = visual.TextStim(win,text=(   "Dit is het einde van het experiment. \n\n"+
                                                 "Bedankt om deel te nemen!"),
                                                 wrapWidth = win_width*text_width)


# welkom en instructie
welkom.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start blockloop
for block in range(n_blocks):
    
        blockstart.text = ( "Welcome to part {} of 2!\n\n"+
                            "Push the space bar to start.").format(block+1)
        blockstart.draw()
        win.flip()
        event.waitKeys(keyList = "space")
        
        # start of the trial loop
        for trial in range(n_trials):
            
            ## gabors tonen
            masked_gabor = visual.GratingStim(win, ori = 90)
            turned_gabor = visual.GratingStim(win, ori = 45 or 135)
            masked_gabor.draw() 
            win.flip()
            core.wait(1)
            turned_gabor.draw()
            win.flip()
            core.wait(0.016)


            ## wachten op reactie
            event.clearEvents(eventType="keyboard")
            my_clock.reset()
            while my_clock.getTime() < 0.016:
                keys = event.getKeys(keyList = ["f","j", "esc"])
                if len(keys) != 0:
                    break

            ## Escape functie
            if "esc" in keys:
                break
