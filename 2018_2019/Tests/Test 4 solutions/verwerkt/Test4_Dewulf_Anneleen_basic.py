
# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import os,platform,numpy,pandas

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing

RespOptions=["left","down","right"]
clock    = core.Clock()
info        = { "Name": "","Participant number": str(0), "leeftijd":0,"gender":["man","vrouw","derde gender"],"handvoorkeur":["links","rechts","ambidexter"]}
nblocks=12
nblocktrials=60
correct=[]

# Data file
already_exists = True 
while already_exists: 
    
    myDlg = gui.DlgFromDict(dictionary = info, title = "Data") 
    
    directory_to_write_to = my_directory + "/Data"
    
    if not os.path.isdir(directory_to_write_to): 
        os.mkdir(directory_to_write_to)
        
    file_name = directory_to_write_to + "/Test4" + "_subject_"+str(info["Participant number"])+"_data"
    if not os.path.isfile(file_name+".csv"): 
        already_exists = False 
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

print("OK, let's get started!")
subject_name = info["Name"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


# Within-subjects design 
Designlinks = [{"pijltje":"<","pos":(-0.75,0),"congruentie":"congruent"}, {"pijltje":"<","pos":(0,0),"congruentie":"neutraal"}, {"pijltje":"<","pos":(0.75,0),"congruentie":"incongruent"}]
Designrechts= [{"pijltje":">","pos":(-0.75,0),"congruentie":"incongruent"}, {"pijltje":">","pos":(0,0),"congruentie":"neutraal"}, {"pijltje":">","pos":(0.75,0),"congruentie":"congruent"}]

Design=Designlinks+Designrechts



# graphical elements
stimulus        = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to task!\n"+
                                                "Push the space bar to proceed.").format(subject_name))
                                                
instruct        = visual.TextStim(win,text="")
                                                
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Push the space bar to proceed"))
#defining
def instructions(blocknr):
    if block <8:
        instruct.text=("Push left when the arrow is directed left or\n"+
                      "Push right when the arrow is directed right\n\n"+
                      "Push the space bar to start the experiment.")
        
    else:
        instruct.text=("Push left when the arrow is positioned left or\n"+
                      "Push right when the arrow is postioned right\n\n"+
                      "Push down when the arrow is at the center\n\n\n"+
                      "Push the space bar to start the experiment.")
    instruct.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
def correct_response(pijltje=0,pos=0):
    if (block <9) and (pijltje=="<"):
        CorResp = "left"
    
    if (block <9) and (pijltje==">"):
        CorResp = "right"
        
    if (block>9) and (pos==(-0.75,0)):
        CorResp = "left"
        
    if (block>9) and (pos==(0.75,0)):
        CorResp = "right"
        
    if (block>9) and (pos==(0,0)):
        CorResp:"down"
    return CorResp

# welcome
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

for block in range(nblocks+1):
    trials = data.TrialHandler(trialList = Design, nReps = 1, method = "random")  
    thisExp.addLoop(trials) ##om experimenthandler te verbinden aan trialhandler #ceze connectie moet gemaakt worden VOOR je loopt over trials
   
    ##instructies -->2/3 v blokken kijken naar richting, rest is kijken naar positie
    instructions(block)

    for trial in trials:
        ##stimulus presenteren
        stimulus.text=trial["pijltje"]
        stimulus.pos=trial["pos"]
        stimulus.draw()
        win.flip()
        
        event.clearEvents(eventType="keyboard")
        clock.reset()
        keys = event.waitKeys(keyList = ["left","right","down"])
        RT=clock.getTime()
        
        ##alles opslaan
        trials.addData("response", keys[0])
        trials.addData("RT", RT)
        trials.addData("Congruentie",trial["congruentie"])
        
        CorResp=correct_response(pijltje=trial["pijltje"],pos=trial["pos"])
        Accuracy=1*(keys[0]==CorResp)

        trials.addData("CorResp",CorResp)
        trials.addData("Accuracy",Accuracy)
        trials.addData("Blocknr",(block+1))
        thisExp.nextEntry()


# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()
