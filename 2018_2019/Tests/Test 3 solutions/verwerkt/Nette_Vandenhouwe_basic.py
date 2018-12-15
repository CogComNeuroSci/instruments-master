# Test 3: Het Gaborexperiment

# importeer de nodige modules
from psychopy import visual, event, core, gui
import time, numpy

# maak een dialog box aan
myDlg = gui.Dlg(title="Gabortaak")
myDlg.addField("Naam:", "Onbekend")
myDlg.addField("Proefpersoonnummer:", 0)
myDlg.addField("Leeftijd:",0)
myDlg.addField("Geslacht:", choices = ["man", "vrouw", "derde gender"])
myDlg.addField("Handvookeur:", choices = ["links", "rechts", "ambidexter"])

# toon de dialog box tot de participant op ok of cancel heeft gedrukt
ParticipantInfo = myDlg.show()
if myDlg.OK:
    print(ParticipantInfo)
    Naam = ParticipantInfo[0]
    PP_Nummer = ParticipantInfo[1]
    Leeftijd = ParticipantInfo[2]
    Geslacht = ParticipantInfo[3]
    Handvoorkeur = ParticipantInfo[4]
else:
    print('user cancelled')

# initialiseer het window
win = visual.Window([600, 500], units = "norm")

# initialiseer de varibiabelen
nBlok = 3
nTrial = 8
InstrTekst = (  "In dit experiment is het de bedoeling dat u de oriëntatie van een gaborstimulus inschat:\n" +
                "   Is deze lichtjes naar links of naar rechts gedraaid?\n\n" +
                "Opgelet de gaborstimulus zal maar heel kort worden aangeboden en zal voorafgegaan en gevolgd worden door een gabor die niet gekanteld is.\n\n" +
                "Als de gabor naar links gekanteld is (de lijnen lopen van linksboven naar rechtsonder), druk dan op de f-toets\n" +
                "Als de gabor naar rechst gekanteld is (de lijnen lopen van rechtsboven naar linksonder), druk dan op de j-toets\n\n" +
                "Als u wil stoppen met het experiment, druk dan op escape.\n\n" +
                "Heeft u nog vragen? Neen? Druk dan op de spatie om verder te gaan.")

#een array om de aanbiedingstijd in te schrijven
AanbiedingsTijd = numpy.repeat(numpy.nan,nTrial)

# 2 arrays met de waarden voor de oriëntatie en de spatiële frequentie
Oriëntatie =            numpy.array([ 30, 30, 30, 30, -30, -30, -30, -30 ])
SpatiëleFrequentie =    numpy.array([ 2, 20, 2, 20, 2, 20, 2, 20 ])

# een array om de correcte response op te slaan
CorResp=[]
CorRespVoorlopig = numpy.copy(Oriëntatie)
for g in range(len(CorRespVoorlopig)):
    g=str(CorRespVoorlopig[g])
    if g == "-30":
        g = "f"
    elif g == "30":
        g = "j"
    CorResp.append(g)

# een array van default responses die overschreven zullen worden
Resp = numpy.repeat(0, nTrial)

# een array om de accuraatheid op te slaan
Accuracy = numpy.repeat(numpy.nan,nTrial)

# een array van default reactietijden die overschreven zullen worden
RT = numpy.repeat(numpy.nan, nTrial)

# voeg de participantinfo toe
ParticipantNaam = numpy.repeat(Naam, nTrial)
ParticipantNummer = numpy.repeat(PP_Nummer, nTrial)
ParticipantLT = numpy.repeat(Leeftijd, nTrial)
ParticipantGesl = numpy.repeat(Geslacht, nTrial)
ParticipantHand = numpy.repeat(Handvoorkeur, nTrial)

#maak een array voor de exacte AanbiedingsTijd
Aanbieding = numpy.repeat(numpy.nan, nTrial)

# combineer de arrays in een trialmatrix
trials = numpy.column_stack([AanbiedingsTijd, Oriëntatie, SpatiëleFrequentie, CorResp, Resp, Accuracy, RT, ParticipantNaam, ParticipantNummer, ParticipantLT, ParticipantGesl, ParticipantHand, Aanbieding])

# herhaal de trialmatrix voor de 3 blokken
trials = numpy.tile(trials, (nBlok, 1))

#schrijf in de eerste kolom van trials per blok hoe lang de gabor wordt aangeboden
trials[range(0*nTrial,(0+1)*nTrial),0] = 0.016
trials[range(1*nTrial,(1+1)*nTrial),0] = 0.033
trials[range(2*nTrial,(2+1)*nTrial),0] = 0.050

print(trials)

# initialiseer de grafische elementen
MessageOnSCreen = visual.TextStim(win, text = "OK")
FeedbackMessage = visual.TextStim(win, text = "OK")
Gabor_stim      = visual.GratingStim(win, sf= 4, mask = "circle", ori = 30,color=(1,1,1))
Gabor_Mask      = visual.GratingStim(win, sf= 4, mask = "circle", ori = 0,color=(1,1,1))

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

#een functie om 1 trial uit te voeren
def perform_trial(HuidigeAanbTijd):
    
    # clear de keyboard input
    event.clearEvents(eventType = "keyboard")
    
    # aanbieding van de Maskgabor
    Gabor_Mask.draw()
    win.flip()
    core.wait(1)
    
    # aanbieding van de gedraaide gabor + registreren van de exacte aanbiedingstijd
    Gabor_stim.draw()
    win.flip()
    my_clockAanb.reset()
    core.wait(HuidigeAanbTijd)
    AanbTijd = my_clockAanb.getTime()
    
    #aanbieding van de Maskgabor
    Gabor_Mask.draw()
    win.flip()
    
    # reset de klok
    my_clockRT.reset()
    
    # wacht voor de response
    keys = event.waitKeys(keyList = ["f","j","escape"])
    
    # registreer de reactietijd
    RT = my_clockRT.getTime()
    
    return keys, RT, AanbTijd

#een functie om feedback te geven
def feedback_message(correct = -99):
    if correct == "1":
        message(message_text = "Correct!", duration = 1)
    elif correct == "0":
        message(message_text = "Verkeerd Antwoord", duration = 1)

# Initialiseer een 2 klokken om de RT en de exacte aanbiedingstijd te meten
my_clockRT = core.Clock()
my_clockAanb = core.Clock()

#de welkomsttekst verschijnt op het scherm
message(message_text = "Welkom, " + Naam + "!\nDruk op de spatie om verder te gaan.")

#de instructies verschijnen op het scherm
message(message_text = InstrTekst, height = 0.065)

#3 blokken
for b in range(nBlok):
    
    #kondig de start van een blok aan
    message(message_text = "Blok {0} zal starten als u op de spatie drukt.".format(b+1))
    
    #8 trials
    for i in range(b*nTrial,(b+1)*nTrial):
        #bepaal de waarden voor 1 trial
        HuidigeAanbTijd = float(trials[i,0])
        Gabor_stim.ori = float(trials[i,1])
        Gabor_stim.sf = float(trials[i,2])
        
        #voer 1 trial uit
        keys, RT, AanbTijd = perform_trial(HuidigeAanbTijd)
        
        #sla alle trialinfo op
        trials[i,4] = keys[0]
        trials[i,5] = int(trials[i,3] == trials[i,4])
        trials[i,6] = RT
        trials[i,12] = AanbTijd
        
        #geef feedback
        feedback_message(correct = trials[i,5])
        
        #uit de trialloop ontsnappen
        if keys[0] == "escape":
            break
    #uit de blokloop ontsnappen
    if keys[0] == "escape":
        break

#neem afscheid
message(message_text = "Het experiment is afgelopen.\nHartelijk dank voor uw deelname!\nGelieve de experimentleider te roepen.")

#sluit het experiment window en core
win.close()
core.quit()

print(trials)