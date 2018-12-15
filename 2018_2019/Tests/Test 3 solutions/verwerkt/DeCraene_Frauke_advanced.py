from psychopy import visual, event,core,gui
import time, numpy

#create window
win= visual.Window([600,500])

#create variables
duration= numpy.array([0.016,0.033,0.05])
orientation=numpy.array([-0.3,0.3,0.3,-0.3,0.3,-0.3,-0.3,0.3])
sf=numpy.array([2,2,20,20,20,2,20,2])

nblocks=3
ntrials=8

timer= core.Clock() 

#create arrays to store generated values
matrixinfo=numpy.repeat("xxx",nblocks*ntrials)
matrixplannedpresentation=numpy.repeat("xxx",nblocks*ntrials)
matrixactualpresentation =numpy.repeat("xxx",nblocks*ntrials)
matrixorientation =numpy.repeat("xxx",nblocks*ntrials)
matrixsf  =numpy.repeat("xxx",nblocks*ntrials)
matrixRT =numpy.repeat("xxx",nblocks*ntrials)
matrixresponse =numpy.repeat("xxx",nblocks*ntrials)
matrixaccuracy=numpy.repeat("xxx",nblocks*ntrials)
matrixcorresp=numpy.repeat("xxx",nblocks*ntrials)

#create trialmatrix:
Trialmatrix= numpy.column_stack([matrixinfo, matrixorientation,matrixsf,matrixcorresp, matrixRT, matrixresponse, matrixaccuracy,matrixactualpresentation,matrixplannedpresentation])

#create textstim:
Welcome = visual.TextStim(win,text='text will be determined later')
Instructions = visual.TextStim(win,text='In dit experiment zal je de orientatie van een Gabor stimuli moeten inschatten. '
                                    +'\nDeze zal steeds voor een korte tijd op het scherm komen. '
                                    +'\nAls je denk dat de stimulus naar links gedraaid is (de lijnen lopen van linksboven naar rechtsonder) dan druk je op de linkertoets (F).'
                                    +'\nAls je echter denkt dat de stimulus naar rechts gedraaid is (de lijnen lopen van rechtsboven naar linksonder) dan druk je op de rechtertoets (J).'
                                    +'\nHet experiment bestaat uit 3 blokken, als je klaar bent om te beginnen met het eerste blok druk dan op spatie.', height = 0.06)
BlockText= visual.TextStim(win,text='text will be determined later')
Bye= visual.TextStim(win,text='Dit was het einde van het experiment! \nBedankt voor je deelname. \nJe kan op de spatiebalk duwen om af te sluiten')
FBText=visual.TextStim(win,text='text will be determined later')

#create basic gabor
basicgabor=visual.GratingStim(win, ori =0.0, mask='gauss', units='height')
testgabor= visual.GratingStim(win, ori =0.0, mask='gauss',units='height')

#create function to wait for spacebar press
def space():
    win.flip()
    event.waitKeys(keyList=['space'],clearEvents=True)

#create function to generate feedback
def feedback_message(matrixaccuracy,trial,block):
    if (orientation[trial]==-0.3 and response == ['f']) or (orientation[trial]==0.3 and response == ['j']):
        FBText.text = 'Correct!'
        Trialmatrix[(block*ntrials)+trial,6] = 1
    else:
        FBText.text='Verkeerd antwoord!'
        Trialmatrix[(block*ntrials)+trial,6] = 0
    FBText.draw()
    win.flip()
    core.wait(1)
    return matrixaccuracy

#create GUI
info = {'Naam van de proefpersoon':'schrijf hier je naam','leeftijd':0, 'geslacht':['man', 'vrouw', 'derde gender'],'handvoorkeur':['links','rechts','ambidetexter']}
infoDlg = gui.DlgFromDict(dictionary=info, title='TestExperiment')
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    Trialmatrix[0,0] = info['leeftijd']
    Trialmatrix[1,0] = info['geslacht']
    Trialmatrix[2,0] = info['handvoorkeur']
else:
    Trialmatrix[0] = 'User Cancelled'


#personalise welcometext
Welcome.text = "Welkom bij het experiment, {0}. \nDurk op de spatiebalk om verder te gaan.".format(info['Naam van de proefpersoon'])

Welcome.draw()
space()

Instructions.draw()
space()

#Blockloop
for block in range (nblocks):
    BlockText.text = 'Blok {0} begint nu. \nDruk op de spatiebalk om verder te gaan'.format(block+1)
    BlockText.draw()
    space()
    
    #trialloop
    for trial in range(ntrials):
        #change en generate all values before starting presentation to reduce delay on presentationtime
        
        basicgabor.sf=sf[trial]
        testgabor.ori=orientation[trial]
        testgabor.sf=sf[trial]
        
        basicgabor.draw()
        win.flip()
        core.wait(1)
        
        
        testgabor.draw()
        win.flip()
        timer.reset()
        core.wait(duration[block])
        
        basicgabor.draw()
        win.flip()
        actualpresentation = timer.getTime()
        response = event.waitKeys(keyList=['f','j', 'escape','esc'],clearEvents=True)
        RT=timer.getTime()
        
        if response==['escape'] or response==['esc']:
            break
        
        matrixaccuracy =feedback_message(matrixaccuracy,trial,block)
        
        #store values
        Trialmatrix[(block*ntrials)+trial,1] = orientation[trial]
        Trialmatrix[(block*ntrials)+trial,2]= sf[trial]
        if orientation[trial] == -0.3:
            Trialmatrix[(block*ntrials)+trial,3]= 'f'
        if orientation[trial] == 0.3:
            Trialmatrix[(block*ntrials)+trial,3]= 'j'
        Trialmatrix[(block*ntrials)+trial,4]= RT
        Trialmatrix[(block*ntrials)+trial,5]= response[0]
        Trialmatrix[(block*ntrials)+trial,7]= duration[block]
        Trialmatrix[(block*ntrials)+trial,8]= actualpresentation
        
    
    if response==['escape'] or response==['esc']:
        print('participant pressed escape')
        break

Bye.draw()
space()

print(Trialmatrix)
win.close()