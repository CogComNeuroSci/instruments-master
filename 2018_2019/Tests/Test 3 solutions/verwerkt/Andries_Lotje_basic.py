#test 3 2018 Lotje Andries

#import modules
from psychopy import visual, event, core, gui
import time, numpy

# initialize the window
win = visual.Window([600,500], units = "norm")

# initialize the variables
n_blocks=3
n_trials = 3
Gabor_duration = [0.16,0.33,0.50]
orientations= (n_blocks*[30.0,330.0,30.0,330.0,30.0,330.0,30.0,330.0])
KeyResp = ['']
keyList = ["j","f"]
myClock= core.Clock()

#diaglog box
info = {"Participant name":" ","Participant number":0, "Age": 0, "Gender":["male", "female","/"], "Handness" : ["right", "left", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Eperiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# initialize graphical elements
Welcome = visual.TextStim(win, text = "Welkom"+ info["Participant name"] + "!\nDruk op de spatiebalk om verder te gaan.")
Instructions = visual.TextStim(win, text = "Wanneer de gabor stimulus naar links gedraaid is (lijnen lopen van linksboven tot rechtsonder) druk op de (f) toets, \nwanneer de gabor stimulus naar rechts gedraaid (lijnen lopen van  rechtsboven to linksonder is druk op de (j) toets."+ "\nDruk op de spatiebalk om verder te gaan.", height = 0.05)
Block_start = visual.TextStim(win, text = "OK")
Feedback = visual.TextStim(win, text = "OK")
Goodbye = visual.TextStim(win, text = "Het expiriment is afgelopen, bedankt voor je deelname! \nRoep de proefleider\n" + "Druk op de spatiebalk om af te sluiten", pos = (0,0.75), height = 0.2)

# display the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = ["space"])

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#RT
RT= numpy.repeat(-99.9,(n_blocks*n_trials))

#response
Resp = numpy.repeat(-99.9,(n_blocks*n_trials))

#correct response
CorResp = numpy.repeat(-99.9,(n_blocks*n_trials))

#graton
grating = visual.GratingStim(win=win, units="pix",size=[150, 150])
#hier zou ik iets moeten aanpassen dat die Hz 2 of 20 is maar ik vind niet hoe dus vond dit mooiste om te laten staan
grating.sf = 5.0 / 150.0
grating.mask = "gauss"

#Feedback
def Feedback_message():
    if CorResp:
        Feedback.text= "Correct!"
    else:
        Feedback.text= "Verkeerde antwoord!"
    Feedback.draw()
    win.flip
    time.sleep(1)


#two blocks
for b in range (n_blocks):
    Block_start.text = "Block " + str(b+1) + " start nu\n"+ "Duw op de spatieknop om verder te gaan"
    Block_start.draw()
    win.flip()
    gratingTime= (Gabor_duration[b])
    event.waitKeys(keyList = ["space"])
    for i in range(b*n_trials,(b+1)*n_trials):
        #graton met verticale oriëntatie
        grating.draw()
        win.flip()
        time.sleep(1)
        event.clearEvents(eventType= "keyboard")
        #gedraaide graton
        grating.ori= orientations[i]
        grating.draw()
        win.flip()
        time.sleep(gratingTime)
        
        # graton verticale oriëntatie
        grating.ori = 0
        grating.draw()
        win.flip()
        #reset clock
        myClock.reset()
        #clear keyboard
        event.waitKeys(keyList = ["j", "f", "espace"])
        GratingResp= event.waitKeys(keyList = ["j", "f", "espace"])
#        #measure RT
#        RT[i] = myClock.getTime()
#        #store response
#        Resp[i]= GratingResp[0]
#       #correct response
#        if grating.ori == 45.0:
#           CorResp= "j"
#        if grating.ori == 135.0:
#           CorReso="f"
#
#        print feedback
#        Feedback_message()
    if KeyResp[0] == "escape":
        break

#print(RT)
#
#meantime = numpy.mean(RT)
#print(meantime)
#
print(Resp)

#display goodbye message
Goodbye.draw()
win.flip
event.waitKeys(keyList = ["space"])


#ik heb wat gesukkeld met die oriëntatie van mijn graton en de duration in de blocks waardoor mijn loop niet echt werkt
#zoals je ziet heb ik toch nog dingen toegevoegd (feedback, RT, CorResp) ondanks mijn experiment niet werkt

