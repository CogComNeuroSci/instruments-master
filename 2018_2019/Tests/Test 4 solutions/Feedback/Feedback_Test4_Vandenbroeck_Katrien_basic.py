#Test 4; het 'pijltjes' experiment

#import
import os
from psychopy import visual as vis
from psychopy import gui,core,event
import numpy as np
from time import sleep

#Make a clock
core.wait(0.5)
clock = core.Clock()

## Esther: laat geen puntjes liggen door bv. niet de dimensies van het scherm in de voeren

#Make a window
win= vis.Window()

#How many blocks? How many trials?
nb_blocks = 12
nb_trials = 60

#List of core aspects
stimuli     = ['<','>']
pos_stimuli = [-0.5,0,0.5]


#Visual components
error_pffn = vis.TextStim(win,text='Ander pffn aub.')
welkom     = vis.TextStim(win)
instructie          = vis.TextStim(win,text='Je gaat telkens pijltjes op het scherm zien verschijnen. \n '
                                           + 'Soms zal je op de plaats moeten reageren. \n'                                                  ##global instruction presentation
                                           + 'Soms op de richting van de pijl.\n [druk op spatie om verder te gaan]')
instructieA         = vis.TextStim(win,text='Druk op de rechterpijl van jouw toetsenbord als het pijltje naar rechts wijst, \n '
                                           + 'Als het links wijst, druk op de linkerpijl van jouw toetsenbord.\n [druk op spatie om verder te gaan]')                             ## instruction for task A
instructieB         = vis.TextStim(win,text='Druk op de rechterpijl van jouw toetsenbord als het pijltje rechts op het scherm staat, \n '
                                           + 'Als het links op het scherm staat, druk dan op de linkerpijl van jouw toetsenbord.\n [druk op spatie om verder te gaan]')           ## instruction for task B
arrow_vis           = vis.TextStim(win)
Goodbye             = vis.TextStim(win,text='Dankjewel voor jouw deelname! Tot de volgende ;) !')

#Make a dialog box
info={'Naam?':'','Proefpersoonnummer?':0,'Leeftijd?':0,'Gender?':['man','vrouw','derde gender'],'handvoorkeur?':['links','rechts','ambidexter']}

#Assign file name
my_home_directory=os.getcwd()
my_directory = my_home_directory + "/data"
os.chdir(my_directory)

## Esther: hier hadden we liever dat de /data folder automatisch aangemaakt werd

## determine the current working directory
directory_to_write = os.getcwd()

##keep asking for new participant number if file already exist
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info)
    pffn = info['Proefpersoonnummer?']
    
    # determine the file name
    file_name = directory_to_write + "/Test4_subject_" + str(pffn) + ".csv"
    print(file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False
    #If the file already exists, ask for new pffn
    else:
        error_pffn.draw()
        win.flip()
        sleep(2)
        
    ## Esther: ik ben er niet zo'n fan von om hier gui's en windows door elkaar te gebruiken

Age    = info['Leeftijd?']
Gender = info['Gender?']
Hand   = info['handvoorkeur?']

#Arrays
##Pffn, Age, Gender, hand, Block number,trial number
pffn_array             = np.repeat (pffn,nb_trials*nb_blocks)
age_array              = np.repeat (Age, nb_trials*nb_blocks)
gender_array           = np.repeat (Gender,nb_trials*nb_blocks)
hand_array             = np.repeat (Hand, nb_trials*nb_blocks)
block_array            = np.repeat (nb_blocks, nb_trials*nb_blocks)
trial_array            = np.repeat (nb_trials, nb_trials*nb_blocks)

##arrow and pos
uni_arrows      = np.repeat(stimuli,(nb_trials/len(stimuli)))          ##Array containing arrows trial of number times
uni_pos         = np.repeat(pos_stimuli,(nb_trials/len(pos_stimuli)))  ##Array containing positions trial of number times

##empty matrices to fill in with arrows and pos in a random order
arrows  = np.repeat('r',nb_blocks*nb_trials)
pos     = np.repeat(0.,nb_blocks*nb_trials)

for b in range (nb_blocks): ## to randomize the trials in each block
    current_trials = np.array(range(nb_trials))+b*nb_trials
    np.random.shuffle(uni_arrows)
    np.random.shuffle(uni_pos)
    arrows[current_trials] =uni_arrows
    pos[current_trials]    =uni_pos

# Esther: pas op, er is geen enkele garantie dat deze manier van randomiseren resulteert in een gebalanceerd design op blokniveau

##congruency
cong = np.copy(arrows)
cong[cong=='<']='-0.5'
cong[cong=='>']=' 0.5'
for i in range(nb_blocks*nb_trials):      ##change values of congruency depending on position and arrow: if same, cong; if pos=0, neutral, else : incong
    a = pos[i]
    print(str(a))          ##it doesn't convert into a string, why????
    if cong[i]==str(a):
        cong[i]='cong'
    elif pos[i]==0:
        cong[i]='neutral'
    else:
        cong[i]='incong'

print(cong)
##CorResp
##CorResp depends on block number; 8 first blocks, react to arrow ; 4 last blocks, react to position on screen
first_trials = nb_trials*8
CorResp_8        = np.copy(arrows[0:first_trials])
CorResp_8[CorResp_8=='<']= -1
CorResp_8[CorResp_8=='>']= 1
##change 4 last trials
#CorResp_4last  = np.copy(str(pos[first_trials:]))  ## Ik wilde die cijfers in strings vertalen maar dat lukte maar niet!
#print(CorResp_4last)
#CorResp_4last[CorResp_4last==-0.5] = 'left'
#CorResp_4last[CorResp_4last==0]    = 'down'
#CorResp_4last[CorResp_4last==0.5]    = 'right'
##stack both
#print(CorResp_8,CorResp_4last)
#CorResp = CorResp_8+CorResp_4last



#Empty Arrays to fill in
##Resp
Resp= np.repeat('tttt',nb_blocks*nb_trials)
##RT
RT  = np.repeat(-99,nb_blocks*nb_trials)
##ACC
ACC = np.repeat(-99,nb_blocks*nb_trials)

#Start experiment
welkom.text= 'Welkom {0}'.format(info['Naam?'])
welkom.draw()
win.flip()
sleep(2)
instructie.draw()
win.flip()
event.waitKeys(keyList=['space'])

#first 8 blocks
instructieA.draw()
win.flip()
event.waitKeys(keyList=['space'])

for block in range (int(nb_blocks*(2/3))):
    for trial in range (nb_trials):
        i = trial + block*nb_trials
        arrow_vis.text=arrows[i]
        arrow_vis.pos = (pos[i],0)
        arrow_vis.draw()
        win.flip()
        clock.reset()
        k = event.waitKeys(keyList=['left','down','right'],timeStamped=clock)
        print(k)
        Resp[i]=k[0][0]
        RT[i]  =k[0][1]

#last 4 blocks
instructieB.draw()
win.flip()
event.waitKeys(keyList=['space'])

for block in range (int(nb_blocks*(1/3))):
    for trial in range (nb_trials):
        i = trial + (block+8)*nb_trials
        arrow_vis.text=arrows[i]
        arrow_vis.pos = (pos[i],0)
        arrow_vis.draw()
        win.flip()
        clock.reset()
        k = event.waitKeys(keyList=['left','down','right'],timeStamped=clock)
        Resp[i]=k[0][0]
        RT[i]  =k[0][1]

Test_4= np.column_stack((pffn_array,age_array,gender_array,hand_array,block_array,trial_array,arrows,pos,cong,RT,ACC))  ##en de CorResp is dan nog niet gelukt

#Save file text
np.savetxt(file_name,Test_4,fmt='%s',delimiter=',')

#Goodbye!
Goodbye.draw()
win.flip()
sleep(5)