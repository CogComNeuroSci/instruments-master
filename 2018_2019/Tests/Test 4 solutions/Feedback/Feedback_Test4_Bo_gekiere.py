from psychopy import visual, event, core, gui, data
import time, numpy
import os

my_directory = os.getcwd()

win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

nblocks     = 12
ntrials     = 60
# Esther: deze posities zijn onmogelijk want ze staan ver buiten de coordinaten van het norm coordinatenstelsel
leftKeys    = (0,-250)
Centrekeys  = (0,0)
Rightkeys   = (0,250)
#RespOptions = ['leftKeys'=['left'], 'RightKeys'=['right'], 'CentreKeys'=['down']]
info        = {"Participant name":"Unknown", "Participant number":0, "Age":0,"Gender":["male", "female","unknown"], "Handedness": ["Left", "Right","Ambidexter"]}

# Esther: deze moeten hier inderdaad aangemaakt worden
blockdirection  
blockposition 

# Esther: nBlockTrials bestaat nog niet
nReps = int(nBlockTrials/(2*3))

CorResp

Trials   = numpy.array([ "<", ">"])
Position = numpy.array(["Left","Centre","Right"])

CongruenceLevels    = numpy.array(["Incongruent", "Neutral", "Congruent"])
CongruenceBoolean   = numpy.array(Trials == Position)
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]

already_exists = True
while already_exists:
    
    # Esther: let er op om de puntjes op de i te zetten: we vragen een folder met de naam data en een file met die start met Test4
    
    myDlg = gui.DlgFromDict(dictionary = info, title = "Arrow_Experiment")
    directory_to_write_to = my_directory + "/data_Arrow_Experiment"

    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)

    file_name = directory_to_write_to + "/Test_subject_" + str(info["Participant number"])
    
    if not os.path.isfile(file_name + ".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

subject_name = info["Name"]

info.pop("Name")

thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

trials = numpy.column_stack([blockdirection, blockposition, Congruence, CorResp, RT])

trials = numpy.tile(trials, (nblocks, 1))

Welcome         = visual.TextStim(win, text = "Welcome! {0}!\n" + "press spacebar to continue".format(subject_name))
Instructions    = visual.TextStim(win, text = "")

# Esther: hier staat er een syntax fout door het missen van een dubbele punt
if position == 0
    Instructions.Text = (                       "In this experiment you will see arrows < or > \n" +
                                                "presented in a random order and on a random position left, centre or on the right of the window.\n\n" +
                                                "You have to respond to the direction of the arrows or to the position\n" +
                                                "You can use the following four response buttons (left, down and right arrows\n" +"If the arrow is presented at the left part of the window, press “Leftarrow”.\n" +
                                                "If the arrow is presented at the centre part of the window, press “Downarrow”.\n" +
                                                "If the arrow is presented at the right part of the window, press “Rightarrow”.\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                                "Any questions?", height = 0.05)
                                                "Press spacebar to continue"
# Esther: idem hier
else
    Instruction.Text = (                        "In this experiment you will see arrows < or > \n" +
                                                "presented in a random order and on a random position left, centre or on the right of the window.\n\n" +
                                                "You have to respond to the direction of the arrows or to the position\n" +
                                                "You can use the following four response buttons (left, down and right arrows\n" +"If this arrow < is presented, press “Leftarrow”.\n" +
                                                "If this arrow > is presented, press “Rightarrow”.\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                                "Any questions?", height = 0.05)
                                                "Press spacebar to continue"

Block_start     = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)

# Esther: in de code hierboven gebruik je dan wel coordinaten die passen in dit coordinatenstelsel

my_clock = core.Clock()

Welcome.draw()
win.flip()
time.sleep(1)
event.waitKeys(keyList = "space")

Instructions.draw()
win.flip()
time.sleep(1)
event.waitKeys(keyList = "space")

for b in range(nblocks):
    
    Block_start.text = "Block " + str(b+1) + " will start now"
    Block_start.draw()
    win.flip()
    time.sleep(1)

    for i in range(b*ntrials,(b+1)*ntrials):
        
        blockdirection.text    = trials[i,0]
        blockposition.pos      = trials[i,1]
        
        # Esther: mocht die eerste win.flip() en time.sleep() er niet hebben gestaan was de code voor de response registratie hieronder perfect
        
        blockdirection.draw()
        win.flip()
        time.sleep(duration)

        event.clearEvents(eventType = "keyboard")
        win.flip()
        my_clock.reset()
        keys = event.waitKeys(keyList = ["left","down","right"])
        RT = my_clock.getTime()
        print(RT)

Goodbye.draw()
win.flip()
time.sleep(1)

win.close()

print(trials)