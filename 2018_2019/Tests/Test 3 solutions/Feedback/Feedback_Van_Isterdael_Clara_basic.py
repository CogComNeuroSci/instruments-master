"""This is my basic version of Test 3 (12/12/2018).
Participants have to guess the orientation of a Gabor stimulus that is only shortly shown and masked by a different Gabor stimulus.
Display time and frequence of the stimulus is manipulated."""

#did not have enough time


# import modules
from psychopy import visual, event, core, gui
import time, numpy

# create a dialog box
info = {"Naam Proefpersoon":"Onbekend", "Proefpersoonnummer":0, "Leeftijd": 0, "Gender":["", "Man", "Vrouw", "Derde gender"], "Handvoorkeur": ["", "Links", "Rechts", "Ambidexter"]}
# for the forced choice options (Gender & Handvoorkeur), i use "" so it is obvious in the trial matrix if the participant has not responded to the question (instead of reading the default value (e.g. "Links"), you read an empty string)
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Experiment", order = ["Naam Proefpersoon", "Proefpersoonnummer", "Leeftijd", "Gender", "Handvoorkeur"])
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# instead of a list of strings of seperate letters, Gender & Handvoorkeur should be one string
info["Gender"]= "".join(info["Gender"])
info["Handvoorkeur"]="".join(info["Handvoorkeur"])

# initialize the window
win = visual.Window(size = [600,500], units = "norm")

#initialize variables
blocks = [0.016,0.033,0.050]
ntrials = 8

# determine text of Instructions
Instructions_text = ("In dit experiment krijg je Gabor stimuli te zien.\n\n"+
                        "Eerst zie je telkens een cirkel met zwat-witte strepen met een loodrecht verticale oriëntatie. "+
                        "Daarna krijg je kort een cirkel te zien waar de strepen wat gedraaid zijn: ofwel zijn ze meer naar links gedraaid, ofwel meer naar rechts. "+
                        "Na een korte aanbieding van de gedraaide Gabor-cirkel, verschijnt er weer een cirkel met loodrechte verticale oriëntatie.\n"
                        "De bedoeling is dat je de oriëntatie van 2de gedraaide cirkel probeert te zien en te registeren. Dit doe je door ofwel de f-toets in te drukken, ofwel de j-toets.\n\n"+
                        "Druk 'f' wanneer de Gabor-cirkel naar links gedraaid is. Dit wil zeggen dat de lijnen van linksboven naar rechtsonder lopen.\n"+
                        "Druk 'j' wanneer de Gabor-cirkel naar rechts gedraaid is. Dit wil zeggen dat de lijnen van rechtsboven naar linksonder lopen.\n\n"+
                        "Het experiment bestaat uit 3 blokken van telkens 8 trials. "
                        "Als je om een bepaalde reden met het experiment wil stoppen, druk 'escape'.\n\n"
                        "Alles duidelijk?\n\n\n\n"+
                        "<Druk op de spatiebalk om verder te gaan>")


#add the values for display time & spatial frequency
GaborOri = numpy.array([30,30,30,30,-30,-30,-30,-30])
SpatialFrequency = numpy.array([2,2,20,20,2,2,20,20])

#define the correct response
## i tried like this but it didn't work, so for now i just created the array myself
##CorResp = numpy.copy(GaborOri)
##CorResp[CorResp == 30]   = "j"
##CorResp[CorResp == -30]  = "f"
CorResp = numpy.array(["j","j","j","j","f","f","f","f"])

# allow to store response & accuracy (for later on)
Response = numpy.repeat("", len(CorResp))
Accuracy = numpy.repeat(-99.9, len(CorResp))
RT = numpy.repeat(-99.9, len(CorResp))


#create trial matrix
trials = numpy.column_stack([GaborOri, SpatialFrequency, CorResp, Response, Accuracy, RT])

#repeat the trial matrix for each block


# initialize graphical elements
MessageOnSCreen = visual.TextStim(win, text = "OK")
Gabor_stim     = visual.GratingStim(win, tex = "sin", mask = "circle", size = (1,1))


#create a function for displaying a message
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    #change message characteristics
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    MessageOnSCreen.color   = color
    
    #draw your text
    MessageOnSCreen.draw()
    win.flip()
    
    # You either have to wait a certain period or wait for the participant to press a key. When the the period is over or the participant presses the asked key, the experiment continues
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        core.wait(duration)

# Create a function to display a Gabor stimulus
def Gabor_draw(ori = 99.9, sf = -99.9, name = "", displayTime = 0, response_key = ["space"]):
    #change stimulus characteristics
    Gabor_stim.ori = ori
    Gabor_stim.sf = sf
    Gabor_stim.name = name
    
    #draw your stim
    Gabor_stim.draw()
    
    #clear keyboard input
    event.clearEvents(eventType = "keyboard")
    
    win.flip()
    
    ### Esther: dit zou het goede moment geweest zijn 
    TrialClock.reset()
    # You either have to wait a certain period or wait for the participant to press a key. When the the period is over or the participant presses the asked key, the experiment continues
    if displayTime == 0:
        #by using this function, we place the answer into the global namespace, making it accessable in the main script 
        global answer
        
        answer = event.waitKeys(keyList = response_key)
    else:
        core.wait(displayTime)
    global RT
    RT = TrialClock.getTime()
    


# create a function to perform a Trial
def perform_trial(TargetOri, SpatFreq, displayTime):
    
    ### Esther: elk van de Gabor stimuli had eigenlijk een andere aanpak nodig, dus deze aanpak van functies was hier niet echt gepast.
    
    Gabor_draw(ori = 0, sf = SpatFreq, name = "preMask", displayTime = 1)
    
    Gabor_draw(ori = TargetOri, sf = SpatFreq, name = "TargetStim", displayTime = displayTime)
    
    Gabor_draw(ori = 0, sf = SpatFreq, name = "postMask", response_key = ["f","j","escape"])

def feedback_message():
    if answer[0] == CorResp[i]:
        trials[i,4] =1
    else:
        trials[i,4]=0
        
    if int(int(trials[i,4])) ==1:
        message(message_text = "Correct!", duration = 1)
    else:
        message(message_text = "Verkeerd antwoord", duration = 1)

# initialize a clock to measure reaction times
TrialClock = core.Clock()

# display a Welcome message
message(message_text = "Welkom, " + info["Naam Proefpersoon"] + "! \n\n\n\n<Druk op de spatiebalk om verder te gaan>")


#display instructions
message(message_text = Instructions_text, height = 0.055)


for b in blocks:
    
    ### Esther: str(blocks.index(b)+1) is misschien wat ingewikkeld in vergelijking met str(b+1)
    message(message_text = "Block " + str(blocks.index(b)+1) + " zal nu beginnen.  \n\n\n\n<Druk op de spatiebalk om verder te gaan>")
    for i in range(ntrials):
        #display the 3 Gabor stimuli
        perform_trial(TargetOri = GaborOri[i], SpatFreq = trials[i,1], displayTime = b)
        
        
        
        #escape from trial loop
        if answer == ["escape"]:
            break
        
        feedback_message()

    
    
    #escape from block loop if the participant presses escape
    if answer == ["escape"]:
        break
    
    
#Display Goodbye
message(message_text = "Het experiment is ten einde, bedankt voor je deelname en tot ziens!\n\n\n\n<Druk op de spatiebalk om te eindigen>")
# close the experiment window
win.close()

trials = numpy.column_stack([GaborOri, SpatialFrequency, CorResp, Response, Accuracy])

print(trials)

# Cancel the core function
core.quit()