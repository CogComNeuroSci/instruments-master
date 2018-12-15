#Test 3

#Achteraf zag ik dat ik ook wat van de advanced oefeningen al had gemaakt maar het was toen al te laat om dit in een apart script te steken 
#dit is dus zowel mijn basic als advanced script

# import modules
from psychopy import visual, event, core, gui
import time, numpy

#gui
info = {"Participant name":"Unknown", "Participant number":0, "Age":0, "Gender":["Male", "Female","Other"],"Hand preference":["Left", "Right", "Ambidextrous"] }
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Task")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")
## gui info opslaan
participant_name = info["Participant name"]
participant_number = info["Participant number"]
participant_age = info["Age"]
participant_gender = info["Gender"]
participant_handpref = info["Hand preference"]


# initialize the window
win = visual.Window([600, 500], units = "norm")
#for key in ['escape']:  #op einde wegdoen !!!!!!!!!!!!!!!!!!!!!!!!
#    event.globalKeys.add(key, func=core.quit)
    
# initialize the variables
nblocks = 3
ntrials = 8 
duration_mask = 1
duration_prime = [0.016, 0.033,0.05]
keys = ['']
my_clock = core.Clock()

#grafische elementen initialiseren
gabor_mask = visual.GratingStim(win,tex="sin", mask='gauss', size=[1.0, 1.0], sf=[4, 0],ori = 0)
gabor_prime = visual.GratingStim(win, tex="sin", mask='gauss', size=[1.0, 1.0], sf=[4, 0], ori = 0)
MessageOnSCreen = visual.TextStim(win, text = "OK")

# arrays voor alles
ori_np = numpy.array([30,30, 30,30,-30,-30,-30,-30])
sf_np = numpy.array([2, 20,2,20,2,20,2,20])
Resp = numpy.repeat(-88.8, len(ori_np))
Accuracy = numpy.repeat(-77.7, len(ori_np))
RT = numpy.repeat(-66.6, len(ori_np))

#correcte response array
#CorResp = numpy.array(["j","j", "j","j","f","f","f","f"]) ##evt later fiksen
#CorResp2=numpy.copy(ori_np)
#CorResp3 = numpy.array2string(CorResp2)
#CorResp3[CorResp3 == 30]     = "j"
#CorResp3[CorResp3 == -30]    = "f"
#print(CorResp3)
#print(type(CorResp3[0]))
CorResp = numpy.repeat(-44.4, len(ori_np))


#info gui
Subject = numpy.repeat(participant_number,len(CorResp))
Gender  = numpy.repeat(participant_gender,len(CorResp))
Age     = numpy.repeat(participant_age,len(CorResp))
Handpref     = numpy.repeat(participant_handpref,len(CorResp))

# alles in 1 grote array
trials = numpy.column_stack([ori_np, sf_np,CorResp,Resp, Accuracy,RT, Subject, Gender, Age, Handpref]) #

# repeat the trial matrix for the three blocks
trials = numpy.tile(trials, (nblocks, 1))

#print(type(trials[0,0]))

#functies
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    MessageOnSCreen.color   = color
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)
        

def feedback_message(correct=-99):
    if correct == 1:
        message(message_text = "Correct!", duration = 1) 
    else:
        message(message_text = "Verkeerd antwoord!", duration = 1)

#welkom
message(message_text = "Welkom " + participant_name + "!\n\nDuw op spacebar om verder te gaan.", response_key = "space")
message(message_text = "In dit experiment zal u enkele cirkels met lijnen te zien krijgen.\n Indien u vindt dat de cirkel naar links gedraaid is, druk dan op de 'f' toets. Indien u vindt dat de stimuli naar rechts gedraaid is, druk dan op de 'j' toets.\n Druk op spatie om het experiment te beginnen ")

#block loop
for block in range(nblocks): 
    message(message_text = "Blok " + str(block+1) + " zal starten wanneer u op de spacebar duwt.", response_key = "space")
    
    # trial loop
    for trial in range(block*ntrials,(block+1)*ntrials):
        gabor_mask.draw()
        win.flip()
        core.wait(duration_mask)
        gabor_prime.ori = int(trials[trial,0])
        gabor_prime.sf=trials[trial,1]
        gabor_prime.draw()
        win.flip()
        core.wait(duration_prime[block])
        gabor_mask.draw()
        event.clearEvents(eventType = "keyboard")
        win.flip()
        my_clock.reset()
        keys = event.waitKeys(keyList = ["f","j", "escape"])
        RT = my_clock.getTime()
        
 
        #feedback en alles opslaan in matrix
        if keys[0] != 0:
            trials[trial,3] = keys[0]
            trials[trial,4] = int(trials[trial,2] == trials[trial,3])
            trials[trial,5] = RT
            feedback_message(correct = int(trials[trial,4]))
            
            
        #correcte repons bepalen
        if trials[trial,0] == '30':
            trials[trial,2] = "j"
        else:
            trials[trial,2]  = "f"
        #ontsnappen aan trial door op spatie te duwen
        if keys[0] == "escape":
            break


#afscheid en sluiten
message(message_text = "Het experiment is nu gedaan, bedankt!", response_key = "space")
win.close()

print(trials)
