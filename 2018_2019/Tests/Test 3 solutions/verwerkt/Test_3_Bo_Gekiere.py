from psychopy import visual, event, core, gui
import time, numpy

#dialogue box
info = {"Participant number":0, "Participant name":"Unknown", "Gender":["male", "female","unknown"], "Age":0, "Handedness": ["Left", "Right","Ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Experiment")
if infoDlg.OK:
    print(info)
else:
    print("User Cancelled")

#window creeren 
win = visual.Window([600, 500], units = 'norm')

#the variables
nblocks     = 3
ntrials     = 8
participant = info["Participant number"]
participantname = info["Participant name"]


#values De bedoeling is dat deze value gebruikt word om de ori te draaien met 30 graden en 0 omdat hij verticaal zou staan
GaborStim = numpy.array(["ori = 0"])

### Ik denk dat hier ori niet hoeft te staan en enkel de waarden waarmee ik de ori moet vervangen, enkel vind ik niet waar ik deze kan inplaatsen
GaborOri = numpy.array(["ori = -30","ori = 30"])
### DEze lijst gebruik ik als index om in mijn blokken de tijd aan te geven van de presentatie van de stimulus
BlockTime = numpy.array(["16", "33", "50"])

### Ik vind mijn CorResp niet waardoor het niet werkt en het moeilijker is om andere dingen te testen.
### Ik denk dat ik een van beiden kan gebruiken
#Key_List = ["f","j"]
#CorResp = numpy.array(["f","j"])

#congruency
#CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
#CongruenceBoolean   = numpy.array(GaborStim == GaborOri)
#Congruence          = CongruenceLevels[[CongruenceBoolean*1]]


#store the correct response
#CorResp = numpy.repeat("",len(Congruence))

#store the accuracy
#Accuracy = numpy.repeat(-99,9,len(CorResp))

#add a default response that will be overwritten during the trial loop
#Resp = numpy.repeat(0,len(CorResp))

#add a default RT that will be overwritten during the trial loop
#RT = numpy.repeat(-99,9,len(CorResp))


#add the participant info
#Subject = numpy.repeat(info["Participant number"],len(CorResp))
#Gender  = numpy.repeat("".join(info["Gender"]),len(CorResp))
#Age     = numpy.repeat(info["Age"],len(CorResp))
#Hand    = numpy.repeat(info["Handedness"],len(CorResp))

# combine arrays in trial matrix
#trials = numpy.column_stack([GaborStim, GaborOri, Congruence, CorResp, Accuracy, Resp, RT, BlockTime])

# repeat the trial matrix for the three blocks
#trials = numpy.tile(trials, (nblocks, 1))

###Eerst dacht ik het op deze manier te doen
#def greeting(Participantname):
#    greeting_string = "Welcome" + participantname + "!"
#    return greeting_string

Welcome_string = "Welcome, {0}!".format(participantname)

### dit kon ook een manier zijn om intructies aan te bieden, maar dit lukt mij niet
#message = visual.TextStim(win, pos=(0.0, -0.75), text="Instructions")

Welcome         = visual.TextStim(win, text = Welcome_string + "\n\nPress the space bar to continue.")
Instructions    = visual.TextStim(win, text = "OK", height = 0.05)
Block_start     = visual.TextStim(win, text = "OK")
Feedback        = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)
myItem          = visual.TextStim(win, text="How difficult was this block?", height=.08, units='norm')
myRatingScale   = visual.RatingScale(win, low=1, high=9, marker='slider', tickMarks=[1,5,9], stretch=1.5, tickHeight=1.5, labels=["easy","average","hard"])


#instructions
Instructions.text = ("Als de Gabor naar links gedraaid is dient u op de f-toets te drukken en\n" +
                    "als de Gabor naar rechts gedraaid is dient u op de j-toets te drukken.\n" +
                    "Druk op de spatiebalk om verder te gaan.")

### hier initialiseer ik de klok voor de reactietijd, mijn meting hangt nog steeds af van van het moment wanneer ik mijn klok resetmy_clock = core.Clock()# display the welcome messageWelcome.draw()win.flip()event.waitKeys(keyList = ["space"])# display the instructionsInstructions.draw()win.flip()event.waitKeys(keyList = ["space"])

for b in range(nblocks):
    
    #Start block 
    Block_start.text = "Block " + str(b+1) + " zal starten nadat U op de spatiebalk gedrukt heeft."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])

#BLOCK1
    for i in range(b*ntrials,(b+1)*ntrials):

        #Stimuli
        gabor = visual.GratingStim(win, tex="sin", mask="circle", texRes=256, 
                   size=[1.0, 1.0], sf=[4, 0], ori = GaborOri, name='gabor1')
        gabor.autoDraw = True

        trialClock = core.Clock()

        # repeat drawing for each frame
        while trialClock.getTime() == BlockTime(trials[i,8[0]]): 
            gabor.phase += 0.01
            message.draw()
            # handle key presses each frame
            if event.getKeys(keyList=['escape', 'f', 'j']):
                core.wait()

            win.flip()
            
#            my_clock.reset()
#                
#            keys = event.waitKeys(keyList = ["f","j","escape"])
#                
#            RT = my_clock.getTime()
#                
#            if keys[0] == "escape":
#               break
#                
#            # Store the response information
#            trials[i,4] = keys[0]
#                
#            # determine accuracy
#            trials[i,6] = int(trials[i,3] == trials[i,4])
#                
#            # Store the RT
#            trials[i,5] = RT
#                
#            # determine the feedback message
#            if int(trials[i,5]) == 1:
#                Feedback.text = "Correct!"
#            else:
#                Feedback.text = "Wrong answer!"
#                
#            # display the feedback message
#            Feedback.draw()
#            win.flip()
#            time.sleep(0.25)
            
        # escape from the block loop
        if keys[0] == "escape":
            break
            
### Dan zou ik dit herhalen voor elke blok en telkens mijn blocktime aanpassen



#saygoodbye
#Goodbye.draw()
#message(message_text = "Goodbye!", duration = 1, pos = (0,0.75), height = 0.2)

# close the experiment window
#win.close()
#
#print(trials)