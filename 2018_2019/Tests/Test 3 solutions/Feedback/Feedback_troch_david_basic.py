# import modules
from psychopy import visual, event, core, gui
import time, numpy, random

#dialog box aanmaken
### Esther: het is beter om nummers te initializeren als nummers 
### Esther: het is ook beter om de gender en handvoorkeuropties in een lijst te steken zodat het response opties worden in plaats van suggesties
info = {"Participant Number": "0", "Participant Name": "unknown", "age":"0", "Gender": "m, v, derde gender", "Handvoorkeur": "L, R, ambidexter"}
dlg = gui.DlgFromDict(dictionary = info, title = "Test 3 2018")
if dlg.OK:
    print(info)
else:
    print("user cancelled")

#window aanmaken
win = visual.Window([600,500], units = "norm")

#klok maken om RT te meten
my_clock = core.Clock()

#variabelen aanmaken
nBlocks = 3
nTrials = 8
gaborsf = [2, 20]
gabortime = [0.016, 0.033, 0.050]
gaborori = [-30, 30]

#Matrix
Orientation         = numpy.repeat("", nTrials)
Spatial_Frequency   = numpy.repeat("", nTrials)
Correct_Response    = numpy.repeat("", nTrials)
Response_Given      = numpy.repeat("", nTrials)
Reaction_Times      = numpy.repeat("", nTrials)
Accuracy            = numpy.repeat("", nTrials)

Matrix = numpy.column_stack([Orientation, Spatial_Frequency, Correct_Response, Response_Given, Reaction_Times, Accuracy])
Matrix = numpy.tile(Matrix, (nBlocks, 1))

#aanmaken objecten
welkom = visual.TextStim(win, text = "Welkom, {0}. Druk op de spatiebalk om over te gaan naar de instructies.".format(info["Participant Name"]))
instr = visual.TextStim(win, text = "In dit experiment krijg je verschillende gabor stimuli te zien. Bij de trials zal de oriëntatie van de gabor stimulus veranderen. \nAls u denkt dat de stimulus naar links gedraaid werd, duwt u op 'f', als u denkt dat de stimulus naar rechts gedraaid werd, duwt u op 'j'. \nDruk op de spatiebalk om verder te gaan.")
blok = visual.TextStim(win, text = "Blok")
goodbye = visual.TextStim(win, text = "Bedankt voor uw deelname aan dit experiment!")
##feedbackmessages##
fbg = visual.TextStim(win, text = "Correct!")
fbf = visual.TextStim(win, text = "Verkeerd antwoord!")
##gaborstimulus
gabor = visual.GratingStim(win, mask = "circle")

#accuraatheid bepalen
def determine_CorResp():
    if gabor.ori == -30:
        CorResp = 'f'
    elif gabor.ori == 30:
        CorResp = 'j'
    return CorResp


"""Hier start het programmeren van het verloop van het experiment"""

#welkomstboodschap:
welkom.draw()
win.flip()
event.waitKeys(keyList = "spacebar")

#instructies:
instr.draw()
win.flip()
event.waitKeys(keyList = "spacebar")

#trials

for b in range(nBlocks):
    
    ### Esther: 
    for trial in range(b*nTrials, (b+1)*nTrials, (b+2)*nTrials):
        ##first gabor
        gabor.sf = random.choice(gaborsf)
        gabor.draw()
        win.flip()
        core.wait(1)
        
        ##actual stimulus
        gabor.ori = random.choice(gaborori)
        gabor.sf = random.choice(gaborsf)
        
        ### Esther: pas op, hoofdletter typo
        gabor.ori = Matrix[Trial, 0]
        gabor.sf = Matrix[Trial, 1]
        gabor.draw()
        win.flip()
        my_clock.reset
        core.wait(gabortime[b])
        
        ##gabor after stimulus
        gabor.ori = 0
        gabor.sf = random.choice(gaborsf)
        gabor.draw()
        win.flip()
        Response = event.waitKeys(keyList = ["f", "j"])
        RT = my_clock.getTime
        
        ### ESther: op dit moment is de orientatie 
        Matrix[Trial, 2]= determine_CorResp()
        

### Esther: goodbye?











win.close()