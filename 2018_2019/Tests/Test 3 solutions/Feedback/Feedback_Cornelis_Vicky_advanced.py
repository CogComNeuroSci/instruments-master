#import modules
##############################
from psychopy import visual, gui, event, core
import time, numpy



#initialize constant
#####################

##Initialize window
win = visual.Window([600,500], units = 'norm')


##Lijst met blokken
bloks = [1,2,3]


###Oriëntatie in een array => kunnen we in een trialmatrix zetten door een trials = (array, array, array) structuur te maken
orie = numpy.array([30,30,30,30,350,350,350,350,
                     30,30,30,30,350,350,350,350,
                     30,30,30,30,350,350,350,350])
##spatiele frequentie in een array
spat_freq = numpy.array([2,2,20,20,2,2,20,20,
                         2,2,20,20,2,2,20,20,
                         2,2,20,20,2,2,20,20])
##aanbiedingstijden in een array
duur = numpy.array([0.016, 0.016, 0.016, 0.016, 0.016, 0.016, 0.016, 0.016,
                     0.033, 0.033, 0.033, 0.033, 0.033, 0.033, 0.033, 0.033,
                    0.050, 0.050, 0.050, 0.050, 0.050, 0.050, 0.050, 0.050])
##array met correct antwoorden aanmaken
CorRes= numpy.array(['j', 'j', 'j', 'j', 'f', 'f', 'f', 'f',
                    'j', 'j', 'j', 'j', 'f', 'f', 'f', 'f'
                    'j', 'j', 'j', 'j', 'f', 'f', 'f', 'f'
                    'j', 'j', 'j', 'j', 'f', 'f', 'f', 'f'])
## lege array voor antwoorden 
respons = numpy.array([])
## lege array voor reactietijden: is array
RT_lijst =numpy.array([])
##array met feedback maken voor in trialmatrix
feedback_array = numpy.array([])

#functie aanmaken voor bepalen feedback
def feedback_message():
        ##accuraatheid antwoord bepalen
    if keys [0] == CorRes[tr]:
        feedback = visual.TextStim(win, text = 'ok')
        feedback.text = 'Correct!'
    else:
        feedback = visual.TextStim(win, text = 'ok')
        feedback.text = 'Verkeerd antwoord!'
    feedback.draw()
    ##array met feedback aanvullen
    numpy.append(feedback_array, feedback.text)
    win.flip()
    core.wait(1)

#De verwijzingsmethoden moeten aangepast worden! Bij basic versie gebruikte ik lijsten, nu moet er telkens naar elementen uit een array verwezen worden waar nodig
#initialize non-constants
#############################

bloktekst = visual.TextStim(win, text = 'ok')
goodbye = visual.TextStim(win, text = 'Bedankt voor uw deelname!')

# create a dialog box
##·Twee nullen bij proefpersoonnummer en leeftijd, anders zijn er problemen met waarden hoger dan 10
info = {"Naam proefpersoon":"Onbekend", "Proefpersoonnummer":00, "Leeftijd":00, "Gender":["man", "vrouw", "derde gender"], "Handvoorkeur": ["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Demografische info")
if infoDlg.OK:
    print(info)
else:
    print("User Cancelled")
##Zorgen dat gender en handvoorkeur als aaneensluitende strings worden opgeslagen
info["Gender"]="".join(info["Gender"])
info["Handvoorkeur"] = "".join(info["Handvoorkeur"])

print(info)

#persoonlijke verwelkoming
verwelkoming=visual.TextStim(win, text =  "ok")
verwelkoming.text = "Welkom {0}! Druk op spatie om verder te gaan.".format(info["Naam proefpersoon"])
verwelkoming.draw()
win.flip()
##Druk op spatie om verder te gaan
spatie_verder = event.waitKeys(keyList = ["space"])
if spatie_verder[0] == 'space':
    #Instructies
    Instructies = visual.TextStim(win, text = "Je krijgt zo dadelijk een aantal Gabor-stimuli te zien. Dit zijn gestreepte cirkels. '\n'"
"Indien de oriëntatie van de strepen naar links gedraaid is, drukt u op 'f'. (De strepen lopen van van linksboven naar rechtsonder). '\n'"
"Indien de oriëntatie van de strepen naar rechts gedraaid is, drukt op 'j'. '\n' (De strepen lopen van rechtsboven naar linksonder). '\n'"
"Druk op de spatiebalk om verder te gaan.")
    Instructies.draw()
    win.flip()
    spatie_verder = event.waitKeys(keyList = ["space"])
    if spatie_verder[0] == 'space':
        #trial blok: Verificicatie presentatieduur: blok 3 heeft de langste presentatie van de trialstimulus, gevolgd door blok 2. Blok 1 heeft de kortste presentatie.
        for b in range(3):
        ##start blok aankondigen
            bloktekst.text = "Blok {0} begint zo meteen. Druk op de spatiebalk om te starten.".format(bloks[b])
            bloktekst.draw()
            win.flip()
            spatie_verder = event.waitKeys(keyList = ["space"])
            if spatie_verder[0] == 'space':



    # aanbieding verticale afleidingsstimuli, trialstimuli en stimuli voor geven antwoord
                for tr in range(8):
                    ##aanbieding verticale afleidingsstimulus
                    gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=300, 
                        size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')
                    gabor.draw()
                    win.flip()
                ##Maak een timer voor de verticale gabor stimulus
                    trialClock = core.Clock()
    
    ## blijven tekenen gedurende 1 seconde
                    while trialClock.getTime() < 1: 
                        gabor.phase += 0.01
                        if trialClock.getTime ==1:
                            continue
    
                    ##aanbieding trialstimuli: trials zelf
                    gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=300, 
                            size=[1.0, 1.0], sf= spat_freq[tr], ori = orie[tr], name='gabor2')
                    gabor.draw()
                    win.flip()
                ##Maak een timer voor de gabor stimulus: hiermee de tijd meten vanaf dat de stimulus op het scherm verschijnt
                    trialClock = core.Clock()
    
    ## blijven tekenen gedurende pass seconde
    ##duur b verwijst terug naar de tijdsduur voor de stimulus uit elks blok b
                    while trialClock.getTime() < duur[b]: 
                        gabor.phase += 0.01
                        if trialClock.getTime == duur[b]:
                            continue
            
            ## aanbieding stimuli voor geven antwoord
                        gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=300, 
                        size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')
                    gabor.draw()
                    win.flip()
            ##toetsen waar op gedrukt mag worden bij antwoorden
                    keys = event.waitKeys(keyList = ["f", "j", "escape"])
            ##Maak een timer voor de verticale gabor stimulus
    
            ##de reactietijd voor het duwen op de toets vinden
                    RT = trialClock.getTime()
                    
            ##de RT en de responsen opslaan in de lijsten

                    numpy.append(RT_lijst, RT)
                    numpy.append(respons, keys[0])
            
            ##nagaan of de juiste RT's en responsen toegevoegd worden.
                    print(RT_lijst)
                    print(keys[0])
                    print(respons)
            
            ##verder gaan als antwoord gegeven
                    if keys [0] == 'f' or keys[0] == 'j':
                        feedback_message()
                        continue
            ##we gebruiken else voor de escape, want dat is de enige toets waar buiten 'j' en 'f' op gedrukt kan worden
                    else:
                        break

#Trialmatrix maken: de arrays samenvoegen: de effectieve presentatietijd ontbreekt nog, kan ik thuis nog verder uitwerken via het instellen van een tweede timer via core.Clock(). 
#Deze begint te timen bij de win.flip voor de trialstimulus en stopt met timen als deze verdwijnt, dus als de tweede afleidingsstimulus (de verticale) verschijnt.
#Deze tijden kunnen dan worden opgeslagen in een array die eerst als lege array aangemaakt wordt en dan wordt deze in de trialmatrix geplaatst.
#trials = numpy.vstack(info["Proefpersoonnummer"], info["Leeftijd"], info["Gender"], info["Handvoorkeur"], orie, spat_freq, CorRes, RT_lijst, respons, feedback_array, duur)
#print(trials)
#of dit kan juist zijn. Thuis verder uitwerken
trials2 = (info["Proefpersoonnummer"], info["Leeftijd"], info["Gender"], info["Handvoorkeur"], orie, spat_freq, CorRes, RT_lijst, respons, feedback_array, duur)
print(trials2)

### Esther: dit diende te gebeuren voor de blok- en trialloop