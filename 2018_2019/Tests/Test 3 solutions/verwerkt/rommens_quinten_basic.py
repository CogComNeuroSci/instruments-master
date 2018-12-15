from psychopy import visual, event, core, gui
import time, numpy

win = visual.Window(size = [600,500], units = 'norm')

#GUI
info = {"Naam": "Unknown", "Proefpersoonnummer": 0, "Leeftijd": 0, "Gender": ["Man", "Vrouw", "Ander"], "Handvoorkeur": ["Links", "Rechts", "Ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor test")

#informatie
ppnnaam = info["Naam"]
ppnnummer = info["Proefpersoonnummer"]
nblocks = 3
ntrials = 8

#stimuli
welcome = visual.TextStim(win, text = "Welkom {0}. \n\nDuw op spatie om verder te gaan.".format(ppnnaam.split() [0]))
instructions = visual.TextStim(win)
instructions.text = ("Straks krijgt u een Gabor-stimulus te zien die naar een bepaalde kant zal uitwijken.\n\nIndien de uitwijking een oriëntatie heeft naar links, duw op de 'F'-toets.\n\n Indien de stimulus een oriëntatie heeft naar rechts, duw op de 'J'-toets.\n\nDuw op spatie om te starten.")
gaborverticaal = visual.GratingStim(win, mask = 'circle', ori = 0)
gabor = visual.GratingStim(win, mask = 'circle')


#arrays
presentatietijd = numpy.array([0.016, 0.033, 0.050])
orientatie = numpy.array([-30, 30])
spatfreq = numpy.array([2, 20])
CorResp = numpy.array(["f","j","f","j","f","j","f","j"])

#Welkom + Instructies
welcome.draw()
win.flip()
event.waitKeys(keyList = ["space"])

instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#klok (stimulus check & response time)
my_clock_SC = core.Clock()
my_clock_RT = core.Clock()


#trials

for b in range(nblocks):
    
    block_start = visual.TextStim(win, text = "Block " + str(b+1) + " zal beginnen als je op spatie duwt.")
    block_start.draw()
    win.flip()
    keys = event.waitKeys(keyList = ["space"])
    
    for trials in range(ntrials):
        
        def feedback_message(string):
            if keys[0] == CorResp[trials]:
                feedbacktekst = "Correct!"
            else:
                    feedbacktekst = "Verkeerd antwoord!"
            feedback = visual.TextStim(win, text = feedbacktekst)
            return feedback.draw()

        
        gabor.ori = orientatie[trials%2]
        if trials < ntrials/2:
            gabor.sf = spatfreq[0]
            gaborverticaal.sf = spatfreq[0]
        else:
            gabor.sf = spatfreq[1]
            gaborverticaal.sf = spatfreq[1]
        
        #drawing the gabor stimuli + timing
        gaborverticaal.draw()
        win.flip()
        core.wait(1)
        
        gabor.draw()
        win.flip()
        my_clock_SC.reset()
        core.wait(presentatietijd[b])
        SC = my_clock_SC.getTime()
        print("Presentatietijd = {0}".format(SC))
        
        
        gaborverticaal.draw()
        win.flip()
        my_clock_RT.reset()
        keys = event.waitKeys(keyList = ("f", "j", "escape"))
        RT = my_clock_RT.getTime()
        print(keys)
        print("Response time = {0}".format(RT))
        
        
        #escape from trial
        if keys[0] == "escape":
            break
            
        #feedback_message(keys)
        
        feedback_message(keys)
        win.flip()
        time.sleep(1)
        
        

        
        

    #goodbye message for last trial
    if b == nblocks-1:
        goodbye = visual.TextStim(win, text = "Goodbye, {0}! \n\nDuw spatie om af te ronden.".format(ppnnaam.split() [0]))
        goodbye.draw()
        win.flip()
        event.waitKeys(keyList = ["space"])














