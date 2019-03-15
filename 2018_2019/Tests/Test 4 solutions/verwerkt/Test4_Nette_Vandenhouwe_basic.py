"""TEST 4: de pijltjestaak"""
"""BASIC"""
#ik geraakte er niet aan uit hoe je het moet exporteren naar een extern file gebruik makens van de specifieke naam die je met het participantnummer opstelt

# importeer de nodige modules
from psychopy import visual, event, core, gui
import time, numpy, os, pandas

# bepaal de huidige working directory
directory_to_write = os.getcwd() + "\\data\\"

# maak een dialog box aan
infoDlg = {"Naam":"onbekend","Participantnummer":0, "Geslacht":["man", "vrouw", "derde gender"], "Leeftijd":0, "Handvoorkeur":["rechts", "links", "ambidexter"]}

# blijf vragen voor een nieuw participantnummer totdat we een filenaam kunnen maken die nog niet bestaat
already_exists = True
while already_exists:
    
    # display de gui
    Dlg = gui.DlgFromDict(dictionary=infoDlg, title="Participantinfo")
    number  = infoDlg["Participantnummer"]
    
    # bepaal de file name
    output_file_name = directory_to_write + "Test4_subject_" + str(number)
    print(output_file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(output_file_name + ".csv"):
        already_exists = False

# initialiseer het window
win = visual.Window([1000, 700], units = "norm")

# initialiseer de varibiabelen
nBlok = 2   #12
nBlockTrials = 60

#bepaal alle levels van de factors
RichtingOpties = numpy.array(["links","rechts"])
PositieOpties  = numpy.array(["links","midden", "rechts"])

# bepaal het aantal levels van de factors
NRichting   = len(RichtingOpties)
NPositie    = len(PositieOpties)
##bepaal het aantal unieke trials in 1 blok
NUnique = NRichting * NPositie

# bepaal het aantal unieke trials en maak een array
UniqueTrials = numpy.array(range(NUnique))

# maak het factorieel design voor 1 blok
Richting            = numpy.floor(UniqueTrials / NPositie)
Positie             = numpy.floor(UniqueTrials / 1) % NPositie
InstructionRicht    = numpy.floor(UniqueTrials / NUnique) ##0 = reageren op de Richting
InstructionPos      = numpy.floor((UniqueTrials+1) / (UniqueTrials+1)) ##1 = reageren op de Positie
BlokNummer          = numpy.repeat(int(-9), NUnique)
Congruentie         = numpy.repeat(int(-99), NUnique)
CorResp             = numpy.repeat(int(-999), NUnique)
TrialNummerBlok     = numpy.repeat(int(-9999), NUnique)
TrialNummerExp      = numpy.repeat(int(-99999), NUnique)
RT                  = numpy.repeat(int(-8), NUnique)
Resp                = numpy.repeat(int(-88), NUnique)
Accuracy            = numpy.repeat(int(-888), NUnique)

# combineer de arrays in 2 verschillende trial matrices
blocktrialsRicht    = numpy.column_stack([BlokNummer, Richting, Positie, Congruentie, CorResp, InstructionRicht, RT, Resp, Accuracy, TrialNummerBlok, TrialNummerExp])
blocktrialsPos      = numpy.column_stack([BlokNummer, Richting, Positie, Congruentie, CorResp, InstructionPos, RT, Resp, Accuracy, TrialNummerBlok, TrialNummerExp])

#maak 1 blok van 60 trials: 10 keer de 6 unieke trials
blocktrialsRicht  = numpy.tile(blocktrialsRicht, (int(nBlockTrials/NUnique), 1))
blocktrialsPos    = numpy.tile(blocktrialsPos, (int(nBlockTrials/NUnique), 1))

#make an empty experimentmatrix:
ntrials = nBlok * nBlockTrials
trials = numpy.ones((ntrials,11)) * (-1)

#initialiseer de grafische elementen
MessageOnSCreen = visual.TextStim(win, text = "OK")

HetPijltje = visual.TextStim(win, text = "OK")

InstrAlgemeen = ("In dit experiment zal je moeten regeageren op pijltjes die ofwel naar links ofwel naar rechts wijzen " +
                 "en die links, in het midden of rechts op het scherm kunnen verschijnen.\n" +
                 "Afhankelijk van het blok zal je moeten reageren op richting of de positie van het pijltje.\n" +
                 "Reageer steeds met de pijltjes toetsen op je toestenbord.\n" +
                 "Druk op de spatie op verder te gaan")

InstrRichting = ("In dit blok zal je moeten reageren op de richting van het pijltje.\n" +
                "Wanneer het pijltje naar links wijst, druk dan op de linkerpijltoets op je toetsenbord.\n" +
                "Wanneer het pijltje naar rechts wijst, druk dan op de rechterpijltoets op je toestenbord.\n" +
                "Druk op de spatie om te beginnen")

InstrPositie = ("In dit blok zal je moeten reageren op de positie van het pijltje.\n" +
                "Wanneer het pijltje links staat op het scherm, druk dan op de linkerpijltoets op je toetsenbord.\n" +
                "Wanneer het pijltje in het midden van het scherm staat, druk dan op de naar-benedentoets op je toestenbord.\n" +
                "Wanneer het pijltje rechts staat op het scherm, druk dan op de rechterpijltoets op je toestenbord.\n" +
                "Druk op de spatie om te beginnen")

# make a function to deduce the correct response
def determine_CorRespRicht(target = 0):
    if target == int(0):
        CorResp = int(0)
    elif target == int(1):
        CorResp = int(1)
    
    return CorResp
    
def determine_CorRespPos(target = 0):
    if target == int(0):
        CorResp = int(0)
    elif target == int(1):
        CorResp = int(1)
    elif target == int(2):
        CorResp = int(2)
    
    return CorResp

#een functie om 1 trial uit te voeren
def perform_trial(Richting, Positie):
    
    # clear de keyboard input
    event.clearEvents(eventType = "keyboard")
    
    #bepaal de richting van het pijltje
    if Richting == int(0):
        PijltjeOpScherm = "<-"
    else:
        PijltjeOpScherm = "->"
    
    #bepaal de positie van het pijltje
    if Positie == int(0):
        PosPijltjeOpScherm = (-0.5,0)
    elif Positie == int(1):
        PosPijltjeOpScherm = (0,0)
    else:
        PosPijltjeOpScherm = (0.5,0)
    
    # aanbieding van het pijltje
    HetPijltje.text = PijltjeOpScherm
    HetPijltje.pos = PosPijltjeOpScherm
    HetPijltje.draw()
    win.flip()
    
    # reset de klok
    my_clockRT.reset()
    
    # wacht voor de response
    keys = event.waitKeys(keyList = ["left","down","right"])
    
    # registreer de reactietijd
    RT = my_clockRT.getTime()
    
    return keys, RT

#een functie om een tekst op het scherm te zetten
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

#initialiseer een klok om de RT te meten
my_clockRT = core.Clock()

#de welkomsttekst verschijnt op het scherm
Naam = infoDlg["Naam"]
message(message_text = "Welkom, " + Naam + "!\nDruk op de spatie om verder te gaan.")
message(message_text = InstrAlgemeen)

#12 blokken:
for b in range(nBlok):
    
    #bepaal wat moet gedaan worden in het blok en store de correcte resp en display de instructies voor het specifieke blok
    if (b+1) <= 1:  #8
        blocktrials = blocktrialsRicht
        for i in range(len(blocktrials)):
            blocktrials[i,4] = determine_CorRespRicht(blocktrials[i,1])
        message(message_text = InstrRichting, height = 0.1)

    else:
        blocktrials = blocktrialsPos
        for j in range(len(blocktrials)):
            blocktrials[j,4] = determine_CorRespPos(blocktrials[j,2])
        message(message_text = InstrPositie, height = 0.09)
    
    #schrijf het bloknummer in de trialmatrix
    blocktrials[:,0] = b+1
    
    # volledige random trial volgorde
    numpy.random.shuffle(blocktrials)
    
    #doe de 60 trials
    for h in range(len(blocktrials)):
        keys, RT = perform_trial(Richting = blocktrials[h,1], Positie = blocktrials[h,2])
        
        ##sla alle trialinfo op
        ###de gegeven respons
        if keys[0] == "left":
            blocktrials[h,7] = int(0)
        elif keys[0] == "down":
            blocktrials[h,7] = int(1)
        else:
            blocktrials[h,7] = int(2)
        
        ###de accuraatheid
        blocktrials[h,8] = int(blocktrials[h,4] == blocktrials[h,7])
        
        ###de reactietijd
        blocktrials[h,6] = RT
    
    #schrijf in trials
    trials[b*nBlockTrials:(b+1)*nBlockTrials] = blocktrials

#maak een file aan met de gegevens
dataFrame = pandas.DataFrame.from_records(trials)
dataFrame.columns = ["BlokNummer", "Richting", "Positie", "Congruentie", "CorResp", "Instruction", "RT", "Resp", "Accuracy", "TrialNummerBlok", "TrialNummerExp"]
numpy.savetxt(output_file_name, trials, delimiter = "\t", fmt = "%.0d")

#neem afscheid
message(message_text = "Het experiment is afgelopen.\nHartelijk dank voor uw deelname!\nGelieve de experimentleider te roepen.")

#sluit het experiment window en core
win.close()
core.quit()