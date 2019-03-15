# Import modules

from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy
from numpy import random
import os, pandas
import platform

#set the directory
my_directory= os.getcwd()

#initialize fixed elements
## Window
win = visual.Window(size=(1000, 700), units = 'norm') ###Breedte 1000 pixels, hoogte 700 pixels. In een genormaiseerd coördinatenstelsel.

##numerieke waarden
nblok = 12 ##aantal blokken

#initializing variable elements
my_clock = core.Clock()
info = { "Naam": "", "Proefpersoonnummer": 0, "Leeftijd": "", "Gender": ["man", "vrouw", "derde gender"], "Handvoorkeur": ["links", "rechts", "ambidexter"]}  ##verschil met str(0)???
instructietekst = numpy.array(["In dit blok reageert u op de richting van het pijltje. Indien het pijltje naar links wijst, drukt u op het linkse pijltje, indien het pijltje naar rechts wijst, druk u op het rechtse pijltje. Druk op spatie om verder te gaan.", 
                              "In dit blok reageert u op de positie van het pijltje. Indien het pijltje links staat, drukt u op het linkse pijltje, indien het pijltje rechts staat, duwt u op het rechtse pijltje. Indien het pijltje in het midden staat, duwt u op het pijljte dat naar beneden wijst. Druk op spatie om verder te gaan."])
welke_reactie= [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1] ##0 zal gebruikt worden om te verwijzen naar de eerste instructie (richting), 1 om te verwijzen naar de tweede instructie (positie)
##graphical elements
stimulus = visual.TextStim(win, text = "")
instructie = visual.TextStim(win, text = "")
goodbye = visual.TextStim(win, text = "Bedankt voor uw deelname!")
nummering = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
##deze nummeringlijst wordt gebruikt om trialnummer te bepalen

# Esther: waarom niet gewoon numpy.array(range(60)) in plaats van elk van deze getallen te typen?

#Dialogue box en data-opslag
already_exists = True
while already_exists: ####blijven herhalen tot already_exists = False
    myDlg = gui.DlgFromDict(dictionary = info, title = "Pijlentaak")
    directory_to_write_to = my_directory + "/data"
    if not os.path.isdir(directory_to_write_to):   ##bestaat directory niet:
        os.mkdir(directory_to_write_to)             ##maak directory
    file_name = directory_to_write_to + "/Test4_" + "subject_" + str(info["Proefpersoonnummer"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Ander proefpersoonnummer")
        myDlg2.addText("Beste proefleider, gelieve een ander proefpersoonnummer in te geven.")
        myDlg2.show()

print("Laten we beginnen!")

# Esther: let op, door de naam van de proefpersoon niet te verwijderen uit de dialogue box sla je die mee op in je output file

#Maak de ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

#within-subject design maken
##De variërende eigenschappen van de stimulus krijgen allen een lijst met mogelijke opties
pijlen = ["<", ">"]
locatie = [(-0.5, 0), (0,0), (0.5,0)]
##Het combineren van de lijsten: trials die elke mogelijke combinatie geven, worden aangemaakt
Design = data.createFactorialTrialList({"Pijl": pijlen, "Locaties": locatie})
print(len(Design)) ##Alle mogelijke combinaties samen geven zes trials. Deze dienen dus 10 maal herhaald te worden per blok.



#Gepersonaliseerde welkomsttekst
welkomtekst = visual.TextStim(win, text = "Welkom {}! Druk op spatie om verder te gaan.".format(info["Naam"]))
welkomtekst.draw()
win.flip()
event.waitKeys(keyList = "space")
info.pop("Naam") ##verwijder naam uit datafile

# Esther: die had je dus moeten doen voordat je info toevoegde aan de trialhandler

# Esther: hieronder herhaal je heel veel code, het is eleganter om de problemen lokaal op te lossen in plaats van globaal

#maak de blokken
for blok in range(nblok):
    blok_nr = blok ##Het nummer van het blok bepalen
    if welke_reactie[blok] == 0: ###Aanmaken van blokken en trials voor reactie op de richting van de pijl
        response_mapping = "richting" ##aangeven waarop gereageerd dient te worden. Dit wordt later opgeslagen
        instructie.text = instructietekst[0]
        ##Toon de instructies
        instructie.draw()
        win.flip()
        event.waitKeys(keyList = "space")
        ##maak de trials aan
        
        # fullRandom was hier nog beter dan random
        
        trials = data.TrialHandler(trialList = Design, nReps= 10, method = "random") ##10 maaal doorlopen voor 60 trials, random: item enkel opnieuw nadat volledige rij is afgegaan
        ##add trials to the experiment
        thisExp.addLoop(trials)
        ##start of the trial loop
        trialnr_blok = 1 ##waarde voor trialnummer in het blok bij eerste trial binnen het blok
        for trial in trials: #iterability
            
            ###trialnummer binnen het volledige experiment
            trialnr_exp = (blok* 60) + trialnr_blok ##Bij blok 0 blijft enkel trial over

            ##Display the stimulus
            stimulus.text = trial["Pijl"] 
            stimulus.pos = trial["Locaties"]
            stimulus.draw()
            win.flip()
            
            ##Wait for the response
            event.clearEvents(eventType = "keyboard") ##keyboard inputs uit de buffer verwijderen om overdracht te vermijden
            my_clock.reset() ## vanaf 0 beginnen voor bepalen reactietijd op trial
            keys = event.waitKeys(keyList = ["left", "right"]) 
            
            # Esther: het is nog beter om hier de RT meteen al vast te leggen in plaats van eerst nog een aantal vergelijkingen te gaan uitvoeren
            
            my_clock.getTime()
            ##2 = linkse pijltoets, 3 = rechtse pijltoets geprobeerd, werkte niet
            ##https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples
            ##uiteindelijk opgelost via codeblok 1 onderaan in nieuw script te runnen. Zo nagegaan wat de correcte keys waren
            
            ##determine correct answer
            if trial["Pijl"] == "<":
                CorRes = "left"
            else:
                CorRes = "right"
                
            ##determine accuracy
            if keys[0] == CorRes:
                accuracy = 1
            else:
                accuracy = 0
                
            ##determine concruency
            if trial["Locaties"] == (-0.5,0) and trial["Pijl"] == "<":
                congruence = 1
            elif trial["Locaties"] == (0,0.5) and trial["Pijl"] == ">":
                congruence = 1
            else:
                congruence = 0
            
            # Esther: naast congruentie en incongruentie moest je eigenlijk ook nog de neutrale trials een eigen code geven
            
            ##add the information to the experiment
            trials.addData("response", keys[0])
            trials.addData("RT", my_clock.getTime())
            trials.addData("correct", CorRes)
            trials.addData("accuraatheid", accuracy)
            trials.addData("congruentie", congruence)
            trials.addData("Response mapping", response_mapping)
            trials.addData("bloknummer", blok_nr)
            trials.addData("trialnummer in dit blok", trialnr_blok)
            trials.addData("trialnummer in experiment", trialnr_exp) 
            ##Deze info wordt in het excelfile ingevoegd, voor wat er in extraInfo staat
            
            trialnr_blok += 1 ##Neemt toe met één voor elke trial binnen het blok
            ##go to the next trial
            thisExp.nextEntry()
                
    else:
        response_mapping = "positie"
        instructie.text = instructietekst[1]
        instructie.draw()
        win.flip()
        event.waitKeys(keyList = "space") 
        ##maak de trials aan
        trials = data.TrialHandler(trialList = Design, nReps= 10, method = "random") ##10 maaal doorlopen voor 60 trials, random: item enkel opnieuw nadat volledige rij is afgegaan
        ##add trials to the experiment
        thisExp.addLoop(trials)
        ##start of the trial loop
        for trial in trials: #iterability
            
            ##Display the stimulus
            stimulus.text = trial["Pijl"] 
            stimulus.pos = trial["Locaties"]
            stimulus.draw()
            win.flip()
            
            ##Wait for the response
            event.clearEvents(eventType = "keyboard") ##keyboard inputs uit de buffer verwijderen om overdracht te vermijden
            my_clock.reset() ## vanaf 0 beginnen voor bepalen reactietijd op trial
            keys = event.waitKeys(keyList = ["left", "down", "right"])
            
            ##determine correct answer
            if trial["Locaties"] == (-0.5, 0):
                CorRes = "left"
            if trial["Locaties"] == (0,0):
                CorRes = "down"
            if trial["Locaties"] == (0.5, 0):
                CorRes = "right"
            
            
            
            ##determine accuracy
            if keys[0] == CorRes:
                accuracy = 1
            else:
                accuracy = 0
                
            ##determine concruency
            if trial["Locaties"] == (-0.5,0) and trial["Pijl"] == "<":
                congruence = 1
            elif trial["Locaties"] == (0,0.5) and trial["Pijl"] == ">":
                congruence = 1
            else:
                congruence = 0
            
            ##add the information to the experiment
            trials.addData("response", keys[0])
            trials.addData("RT", my_clock.getTime())
            trials.addData("correct", CorRes)
            trials.addData("accuraatheid", accuracy)
            trials.addData("congruentie", congruence)
            ##Deze info wordt in het excelfile ingevoegd, voor wat er in extraInfo staat
            
            ##go to the next trial
            thisExp.nextEntry()



#print(pandas.crosstab([trials.Locaties, trials.Pijl], trials.blok))
goodbye.draw()
win.flip()


##Codeblok 1

#from psychopy import event, visual

#initialize fixed elements
## Window
#win = visual.Window(size=(1000, 700), units = 'norm') ###Breedte 1000 pixels, hoogte 700 pixels. In een genormaiseerd coördinatenstelsel.

#hoi = visual.TextStim(win, text ='hoi')
#hoi.draw()
#win.flip()
#event.waitKeys(keyList = ["left", "right", "down"])
#hai =visual.TextStim(win, text = 'haaaaaaaaaaaai')
#hai.draw()
#win.flip()
#event.waitKeys(keyList = ["left"])
