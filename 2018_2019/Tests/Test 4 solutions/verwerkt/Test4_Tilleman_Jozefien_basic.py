import numpy as np
import time,os
from psychopy import visual,gui,data,core,event


# create a dialog box for name

name = {"naam?": ""}
infoDlg = gui.DlgFromDict(dictionary=name, title="name")

info = {"participantennummer?":"0","leeftijd?":0,"gender?":["man","vrouw","derde gender"],"handvoorkeur?":["links","rechts","ambidex"]}
 
# determine the current working directory
directory_to_write = os.getcwd()

data_directory = directory_to_write+"/data"
print(data_directory)

if not os.path.isdir(data_directory):
    data=os.mkdir(data_directory)

os.chdir(data_directory)
 
# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="info")
    pp=info["participantennummer?"]
    
    
    # determine the file name
    file_name = data_directory + "/test4_subject_" + pp
    print(file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False
        print("doesn't exist")

#window maken
win=visual.Window(size=[1000,7000])

#welkom

welkom=visual.TextStim(win,text="welkom{0}".format(name["naam?"]))

welkom.draw()
win.flip()
time.sleep(3)

#taakuitleg
uitleg=visual.TextStim(win,text="yolo")

#stimuli maken
arrow = visual.TextStim(win,text="--",pos=[0,0])
L="<--"
R="-->"

links=[-0.5,0]
rechts=[0.5,0]
midden=[0,0]

richt="reageer op de richting"
pos="reageer op de positie"

#variabelenopties

#trials
richting_op=np.array([L,R])
positie_op=np.array([links,rechts,midden])

#blok
opdracht_resp=np.array([richt,pos,richt,pos,richt,pos,richt,pos,richt,richt,richt,richt])


#creating factorial design
trial_list = data.createFactorialTrialList({"richting":richting_op,"positie":positie_op})

#creating trialhandler
trials=data.TrialHandler(trial_list,nReps=10,method="random")

#creating experimenthandler
thisExp=data.ExperimentHandler(dataFileName=file_name,extraInfo=info)

#add trials to experiment
thisExp.addLoop(trials)

#creating clock
clock=core.Clock

#blokdesign
for j in opdracht_resp:
    uitleg.text=j
    uitleg.draw()
    win.flip()
    time.sleep(5)
    #loop design
    for i in trials:
        trials.addData("opdracht",j)
        arrow.pos= i["positie"]
        arrow.text= i["richting"]
        arrow.draw()
        event.clearEvents(eventType="keybord")
        win.waitBlanking
        win.flip()
        clock.reset
        Keys=event.waitKeys(keyList=("<",">"))
        RT=clock.getTime
        
        #add reactions to trials
        trials.addData("reactietijd",RT)
        trials.addData("respons",Keys[-1])
        
        #correcte respons bepalen
        if j == richt:
            trials.addData("corr_resp",["richting"])
        else:
            trials.addData("corr_rexp",["positie"])
        
    thisExp.nextEntry


win.close()
