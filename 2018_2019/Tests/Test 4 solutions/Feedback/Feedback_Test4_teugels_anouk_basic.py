#import modules
from psychopy import data, visual, event, core, gui, os
import numpy

#set the directory
my_directory=os.getcwd()

#dialog box
info = {"Proefpersoonnummer": 0, "Naam": "","Leeftijd":0,"Gender":["man", "vrouw","derde gender"],"Hand voorkeur":["links","rechts","ambidexter"]}

#data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = u"get subject info")
    directory_to_write_to = my_directory + "/data/"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "Test4_subject_" + str(info["Proefpersoonnummer"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Geef een ander proefpersoonnummer in.")
        myDlg2.show()
name=info["Naam"]
info.pop("Naam") ##remove name from data file
thisExp = data.ExperimentHandler(dataFileName = file_name,extraInfo=info)

#initialize window
win = visual.Window(size=[1000,700],units="norm")

#initialize variables
nblocks=12
ntrials=60
RespOptions=["left","down","right"]
my_clock= core.Clock()

#define visual stimuli
stimulus=visual.TextStim(win,text="",pos=(0,0))
MessageOnScreen = visual.TextStim(win,text="")

#a funtion for presenting messages on screen
def message(message_text = "", response_key = "space", duration = 0):
    MessageOnScreen.text=message_text
    MessageOnScreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList=response_key)
    else:
        time.sleep(duration)

#design
Design = [{"Arrow": "<", "Position":(-0.5,0)}, {"Arrow": "<", "Position":(0,0)},{"Arrow": "<", "Position":(0.5,0)},
        {"Arrow": ">", "Position":(-0.5,0)},{"Arrow": ">", "Position":(0,0)},{"Arrow": ">", "Position":(0.5,0)}]

# Esther: goed gedaan, maar je kon hier meteen ook al de congruentie invoegen ;)

#welcome message
message(message_text="Welkom {0}! \n\nDruk op spatie om verder te gaan.".format(name),response_key="space")

#blockloop
for block in range(nblocks):
    
    ## Esther: misschien een goed idee om de text messages op te splitsen over verschillende lijnen zodat je je script beter kan lezen
    
    ## Esther: haha, ok, dat lijkt misschien wat random maar is eigenlijk noch random, noch schaalbaar
    
    #instructions
    if block == 0 or block ==  2 or block == 3 or block == 5 or block == 6 or block== 7 or block== 9 or block== 11:
        message(message_text="Reageer op de richting van het pijltje. Druk op het linkerpijltje op je toetsenbord wanneer het naar links wijst, druk op het rechterpijltje wanneer het naar rechts wijst. Druk op spatie om verder te gaan.",response_key="space")
    else:
        message(message_text="Reageer op de positie van het pijltje. Druk op het linkerpijltje op je toetsenbord wanneer het links staat, druk op het pijltje naar beneden wanneer het in het midden staat en druk op het rechterpijltje wanneer het naar rechts wijst. Druk op spatie om verder te gaan.",response_key="space")
    
    #trials
    trials = data.TrialHandler(trialList = Design, nReps = 10, method = "fullRandom")
    thisExp.addLoop(trials)
    
    # Esther: pas op, deze code hieronder zal het bloknummer enkel wegschrijven op de eerste trial van het blok
    
    trials.addData("BlockNr",block+1)
    
    for trial in trials:
        #present stimulus
        stimulus.text=trial["Arrow"]
        stimulus.pos=trial["Position"]
        stimulus.draw()
        win.flip()
        
        #wait for response
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = RespOptions)
        
        ## Esther: ik zou hier meteen al de RT vastleggen in plaats van eerst nog wat vergelijkingen uit te voeren
        
        #deduce correct answer
        if block == 0 or block ==  2 or block == 3 or block == 5 or block == 6 or block== 7 or block== 9 or block== 11:
            if trial["Arrow"]=="<":
                CorResp="left"
            else:
                CorResp="right"
        else:
            if trial["Position"]==(-0.5,0):
                CorResp="left"
            elif trial["Position"]==(0.5,0):
                CorResp="right"
            else:
                CorResp="down"
        trials.addData("CorResp",CorResp)
        
        #save RT, response,accuracy and trialnumber to data file
        trials.addData("response", keys[0])
        trials.addData("RT", my_clock.getTime())
        accuracy=1*(keys[0]==CorResp)
        trials.addData("Acc", accuracy)
        
        thisExp.nextEntry()


#end message
message(message_text="Dit is het einde van het experiment. Bedankt voor je deelname!",response_key="space")

#close experiment
win.close()
core.quit()