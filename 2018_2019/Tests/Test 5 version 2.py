"""
priming task
Tom Verguts, March 2019
variables are in English for lab-sharing purposes;
communication with participant in Dutch
novel in version 2: RT measured during target and after
"""

# import modules
from psychopy import visual, event, core, gui, data
import os

# Welcome to the subject, and ask for some data
already_exists  = True
while already_exists:
    info_subject  = {"Participant nummer": 0, "Leeftijd": 0, "Geslacht": ["Vrouw", "Man"]}
    Dlg_subject = gui.DlgFromDict(dictionary = info_subject, title = "Priming Task")
    my_directory = os.getcwd() + "/Data_priming_task_" + str(info_subject["Participant nummer"])
    if not os.path.isdir(my_directory):
        already_exists = False
    else:
        Dlg_error = gui.Dlg(title = "Error")
        Dlg_error.addText("Dit nummer is reeds gebruikt. Vraag de testleider om een nieuw nummer te zoeken.")
        Dlg_error.show()

file_name = my_directory + "/Data_priming_task_" + str(info_subject["Participant nummer"])
thisExp   = data.ExperimentHandler(dataFileName = file_name, extraInfo = info_subject)

# Participant name
info_name      = {"Naam": ""}
Dlg_Name       = gui.DlgFromDict(dictionary = info_name, title = "Gelieve je naam in te geven")

# Window definition
text_height = 0.08
win_width = 1000
win_height = 700
win = visual.Window(size = [win_width, win_height], units = "norm", color = "gray") # while testing
#win = visual.Window(fullscr=True, units = "norm", color = "gray")          # while collecting data 

# Experiment length
n_blocks       = 2
n_reps         = 2

# All durations of events, measured in seconds    
dur_fixation   = 0.5    # not a multiple of frame duration, but not so important for fixation
dur_prime      = 0.051  #
dur_blank      = 0.017  #
dur_target     = 0.170  #
dur_RT         = 2      # max RT
dur_feedback   = 1

# Experimental elements
answers     = ["f", "j", "F", "J", "escape"] # allow both letter and its capital for robustness
RT_clock    = core.Clock()

# Visual elements
fixation    = "+"
arrow_left  = "<<<<"
arrow_right = ">>>>"
stimuli     = [arrow_left, arrow_right]

fixation_cross  = visual.TextStim(win, text = fixation)
prime           = visual.TextStim(win, text = "")
target          = visual.TextStim(win, text = "")

# Communicating with your participant
too_slow        = visual.TextStim(win, text = "Probeer om sneller te reageren!")
error           = visual.TextStim(win, text = "Fout antwoord, wees nauwkeuriger!")
welcome         = visual.TextStim(win, text = "Hallo, {}!\n\n".format(info_name["Naam"].capitalize()) + 
                                                   "Welkom op dit experiment.\n\n" +
                                                   "Druk op spatie om verder te gaan.", height = text_height)
# note: Subject is not informed of the prime stimulus... although some may find out, of course
instructions    = visual.TextStim(win, text = "Elke beurt start met een kruisje in het midden van het scherm: gelieve hierop je aandacht te richten. Hierna verschijnt een pijl die ofwel naar links of naar rechts wijst.\n\n"+
                                                    "Reageer op de richting van de pijl. Gebruik hiervoor de wijsvingers van je linker- en rechterhand:\n\n"+
                                                    "Indien de pijl naar links wijst, druk op {}.\n".format(answers[0].capitalize())+
                                                    "Indien de pijl naar rechts wijst, druk op {}.\n\n".format(answers[1].capitalize())+
                                                    "Belangrijk: je moet deze taak zo snel mogelijk uitvoeren, en daarbij toch zo weinig mogelijk fouten maken.\n\n",
                                                    height = text_height)
break_text      = visual.TextStim(win, text = "Ok, {}!\n\n".format(info_name["Naam"].capitalize()) + 
                                                   "Je mag nu even pauzeren.\n\n" +
                                                   "Druk op spatie om verder te gaan.", height = text_height)
end_text        = visual.TextStim(win, text = "Ok, {}!\n\n".format(info_name["Naam"].capitalize()) + 
                                                   "Het experiment is afgelopen.\n\n" +
                                                   "Hartelijk dank voor je deelname!\n\n" + 
                                                   "Druk op spatie om het programma af te sluiten.", height = text_height)

welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instructions.draw()
win.flip()
event.waitKeys(keyList = "space")

conditions = data.createFactorialTrialList({"Prime": stimuli, "Target": stimuli})

block_nr = 0
for block in range(n_blocks):
    block_nr += 1
    trials = data.TrialHandler(conditions, nReps=n_reps, method='fullRandom')
    thisExp.addLoop(trials)
    
    for trial in trials:
        prime.text  = trial["Prime"]
        target.text = trial["Target"]
        
        event.clearEvents()
        fixation_cross.draw()
        win.flip()
        core.wait(dur_fixation)

        prime.draw()
        win.flip()
        core.wait(dur_prime)
        
        win.flip()
        core.wait(dur_blank)

        target.draw()
        win.flip()
        
        # version 2: RT measurement also during target presentation
        RT_clock.reset()
        keys = event.waitKeys(keyList = answers, maxWait = dur_target)
        win.flip() # remove target from screen
        
        if keys == None:
            keys = event.waitKeys(keyList = answers, maxWait = dur_RT - dur_target)
        RT = RT_clock.getTime()
                    
        if keys == None:   # if there was no response within the max deadline
            RT = -1
            keys = "t"

        if trial["Prime"] == trial["Target"]:
            trials.addData("Congruency", "congruent")
        else:
            trials.addData("Congruency", "incongruent")
        trials.addData("RT", RT)
        trials.addData("Response", keys[0].capitalize())
        correct_response = ["F", "J"][trial["Target"]==arrow_right]
        trials.addData("Correct Response", correct_response)
        accuracy = 1*(keys[0].capitalize()==correct_response)
        trials.addData("Accuracy", accuracy)
        if keys == "t":
            too_slow.draw()
            win.flip()
            core.wait(dur_feedback)
        elif accuracy == 0:
            error.draw()
            win.flip()
            core.wait(dur_feedback)


        thisExp.nextEntry()

    if block_nr < n_blocks:   
        break_text.draw()
        win.flip()
        event.waitKeys(keyList = "space")

end_text.draw()
win.flip()
event.waitKeys(keyList = "space")