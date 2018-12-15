###############################################################################################################
###                         Test 3 - Instrumenten van de Experimentele Psychologie                          ###
###                                                Mieke Slim                                               ###
###                                                12/12/2018                                               ###
###############################################################################################################

# import modules
from psychopy import gui, visual, core, event
import time, numpy

# display a dialog box
info = {'Naam':'default','Participant number': 0,"Age": 0,'Gender':["female", "male", "other"], "Hand preference":["Righthanded", "Lefthanded", "Ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title='Test3',
    order=['Naam', 'Participant number', 'Age', 'Gender', 'Hand preference']) 
if infoDlg.OK:  
    print(info)
else:
    print('User Cancelled')

# initialise window and graphic components
win = visual.Window(size = [600, 600], color = "grey", units = "norm")
gabor = visual.GratingStim(win, tex="sin", mask="gauss", units = 'norm', size=[1.0, 1.0], sf = [4, 0], ori = 0)

# initialise variables
my_clock = core.Clock()
##number of blocks
nblocks = 3
##number of trials
ntrials = 8
name = info["Naam"] ##name of the participant
## orientiation of the gabor in each trial per block
gaborori = numpy.array([330, 330, 330, 330, 30, 30, 30, 30])
## spatial frequency of the gabor in each trial per block
gaborsf = numpy.array([2, 20,2, 20,2, 20,2, 20, ])
## Correct responses for all trials per block
CorResp = numpy.array(["f","f","f","f","j","j","j","j"]) 
## Duration of which the trial is shown (in miliseconds, as I could not figure out how the frame rates worked again...)
duration = numpy.array([0.016, 0.033, 0.050])
## Response, to be overwritten after each block
Resp = numpy.repeat(0, len (CorResp))
## RT, to be overwritten after each block
RT = numpy.repeat(numpy.nan, len (CorResp))
## Participant number, to be registered in the response matrix
ppnumber = numpy.repeat(info["Participant number"], len (CorResp))

# combine all the arrays in a trial matrix, in which the responses will be registered
trials = numpy.column_stack([ppnumber, gaborori, gaborsf, CorResp, Resp, RT])

# define functions
## This function allows easy programming for text messages on the screen
TextStimulus = visual.TextStim(win, text = "Text") 
def text(messagetext = "", response_key = "space", duration = 0, height = None):
    TextStimulus.text = messagetext
    TextStimulus.height = height
    TextStimulus.draw()
    win.flip()
    if duration == 0:
        keys = event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

# Let the experiment begin!
# display the welcome message
text(messagetext = "Welkom %s!\n\nDruk op de spatiebalk om verder te gaan" % (name), response_key = "space", duration = 0) 

# display instructions
text(messagetext ="In dit experiment krijg je meerdere Gabor stimuli te zien." 
                    + "\nJouw taak is het om aan te geven of elke Gabor naar links of naar rechts is gedraaid.\n" 
                    + "\nAls een Gabor naar rechts is gedraaid lopen de lijnen van linksonder naar rechtsboven.\n"
                    + "\nAls een Gabor naar links is gedraaid lopen de lijnen van linksboven naar rechtsonder.\n"
                    + "\nDruk op de j-toets als de Gabor naar rechts is gedraaid,"
                    + "\nen op de f-toets als de Gabor naar links is gedraaid."
                     + "\n\nDruk op de spatiebalk om verder te gaan", 
                     response_key = "space", duration = 0, height = 0.07) ## The whole text fits on the screen with these height settings

# start the blocks and trials
for block in range(nblocks):
    ## display a text message which says that the block is about to begin
    text(messagetext = "Een nieuw blok begint. \n\nDruk op de spatiebalk om verder te gaan", response_key = "space", duration = 0)
    for trial in range(ntrials):
        ## display a vertical gabor prior to the trial, for which a function is used
        gabor.ori = 0
        gabor.sf = 10 
        gabor.draw()
        win.flip()
        time.sleep(1)
        
        ##display the trial
        gabor.ori = gaborori[trial]
        gabor.sf = gaborsf[trial]
        gabor.draw()
        win.flip()
        core.wait(duration[block])
        
        ## display a vertical gabor that is displayed after the trial, when the participant will respond
        event.clearEvents(eventType = "keyboard")
        gabor.sf = 10
        gabor.ori = 0
        gabor.draw()
        win.flip()
        my_clock.reset()
        keys = event.waitKeys(keyList = ["f","j", "escape"])
        RT = my_clock.getTime()
        
        ## allow for an escape option
        if keys[0] == "escape":
            break
        ## store the key responses and response time in the trials matrix
        else:
            trials[trial, 4] = keys[0]
            trials[trial, 5] = RT
        
        ## Display feedback messages (I know this is meant to be in a separate function, however, I was not able to get such a function working...)
        if gaborori[trial] == 330 and keys[0] == CorResp[trial]:
            text(messagetext = "Goed!", duration = 1)
        elif gaborori[trial] == 30 and keys[0] == CorResp[trial]:
            text(messagetext = "Goed!", duration = 1)
        else:
            text(messagetext = "Fout!", duration = 1)
    
    ## The trial responses are registered per block, therefore, I have added this print-statement in order to easily distinguish the responses between the three blocks in the output
    print("HIER BEGINT HET VOLGENDE BLOK")
    ## Print the registered responses in the output
    print (trials) 

#Display the end message
text(messagetext = "Dit was het einde van het experiment.\n\nBedankt voor je deelname, %s!\n\nDruk op de spatiebalk om af te sluiten" %(name), response_key = "space", duration = 0)

