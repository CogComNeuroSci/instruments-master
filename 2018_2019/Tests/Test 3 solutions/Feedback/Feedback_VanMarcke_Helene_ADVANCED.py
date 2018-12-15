from psychopy import visual, event, core, gui
import numpy, time

win = visual.Window(size = [600,500], units = "norm")


##dialog box_________________________________________________________________________________________________________________________________

info = {"deelnamenummer": 1 ,
        "naam" : "voornaam",
        "leeftijd" : 20,
        "geslacht": "man, vrouw of derde gender",
        "handvoorkeur" : "rechts, links of ambidexter"}
        
infoDlg = gui.DlgFromDict(dictionary = info, 
                          title ='GaborExperiment') 

if infoDlg.OK:          ##geef me de info weer die de pp ingeeft
    print(info)         
else:
    print('User Cancelled')         ##geef me ook iets weer als de pp op cancel geduwd heeft

participantnumber = info["deelnamenummer"]


##welcome_____________________________________________________________________________________________________________________________________

welcome           = visual.TextStim(win,text="Welkom {0}! Druk op de spatie om verder te gaan.".format(info["naam"]))
instructies       = visual.TextStim(win,text = "In dit experiment krijg je telkens een Gabor stimulus aangeboden, en dit gedurende 3 blokken.\n\n" +
                                                "Een Gabor stimulus is een witte cirkel met een patroon van parallelle zwarte lijnen.\n\n" + 
                                                "Jouw taak bestaat eruit om de oriëntatie van de stimulus in te schatten.\n\n" + 
                                                "De stimulus zal telkens verticaal beginnen, maar zich dan draaien.\n\n" + 
                                                "Wordt ze naar LINKS gedraaid, druk dan op F. \n\n" + 
                                                "Wordt ze naar RECHTS gedraaid, druk dan op J.\n\n" +
                                                "Klaar? Druk dan op de spatie om verder te gaan",
                                                height = 0.08)

welcome.draw()
win.flip()
k = event.waitKeys(keyList = "space")
instructies.draw()
win.flip()
k = event.waitKeys(keyList = "space")


##stimuli_____________________________________________________________________________________________________________________________________

spatfreq   = [ 20,  20,   2,   2, 20, 20,  2,  2]
orientatie = [-30, -30, -30, -30, 30, 30, 30, 30]
corResp    = ["f", "f", "f", "f", "j","j","j","j"]

aanbiedtijd = [0.016, 0.033, 0.05]

gaborMask = visual.GratingStim(win, tex="sin", mask="gauss", size=[1.0, 1.0], sf=[4, 0], ori = 0)
correct   = visual.TextStim(win, text = "Correct!")
wrong     = visual.TextStim(win, text = "Verkeerd!")


measureRT = core.Clock()
measureAT = core.Clock()  ##AT van AanbiedingsTijd of ActualTime


##functies_____________________________________________________________________________________________________________________________________

def BLOCKNUMMER(): 
    blocknummer = visual.TextStim(win, text = "Blok {0} begint zo dadelijk. Druk op spatie om te starten.".format(block+1))  ##pers begroeting
    blocknummer.draw()
    win.flip()
    k = event.waitKeys(keyList = "space")

eigenlijketijd  = ["default"]*24
accuraatheid    = ["default"]*24

def FEEDBACK_MESSAGE():
    if k[0] == [corResp[trial]]: 
        correct.draw()
        accuraatheid[trial*(block+1)] = "juist"
        win.flip()
        time.sleep(1)
    else:
        wrong.draw()
        accuraatheid[trial*(block+1)] = "fout"
        win.flip()
        time.sleep(1)

#trial matrix_________________________________________________________________________________________________________________________________

deelnamenummerL = numpy.repeat(info["deelnamenummer"],24)               ##matrix bestaat uit 3 blokken met 8 trials == 24 rijen in totaal
leeftijdL       = numpy.repeat(info["leeftijd"],24)
geslachtL       = numpy.repeat("".join(info["geslacht"]),24)
handvoorkeurL   = numpy.repeat("".join(info["handvoorkeur"]),24)

RTlist         = ["default"]*24
geplandetijd   = numpy.repeat(aanbiedtijd,8)
orientatieL    = numpy.tile(orientatie,3)      ##gebruik tile ipv repeat om de lijst in volgorde 3x na elkaar te printen en niet elk element apart 3 keer
spatfreqL      = numpy.tile(spatfreq,3)
corRespL       = numpy.tile(corResp,3)

matrix = numpy.column_stack(( deelnamenummerL,
                              leeftijdL,
                              geslachtL,
                              handvoorkeurL,
                              orientatieL,
                              spatfreqL,
                              corRespL,
                              RTlist,
                              accuraatheid,
                              geplandetijd,
                              eigenlijketijd))

### Esther: het is eenvoudiger om de matrix drie keer te tilen in plaats van elke array op voorhand te herhalen

##loop_________________________________________________________________________________________________________________________________________

for block in range(3):
    
    BLOCKNUMMER()
    
     
    for trial in range(8):
        
        #gaborMask.draw()
        #win.flip()
        #time.sleep(1)
        
        gabor = visual.GratingStim(win, tex="sin", mask="gauss", size=[1.0, 1.0], sf=spatfreq[trial], ori = orientatie[trial])  ##neem voor elke iteratie het volgende element uit de lijst van sf en ori
        gabor.draw()
        win.flip()
        core.wait(aanbiedtijd[block])           ##de aanbiedtijd verandert in functie van de blokken
        
        measureAT.reset()   
        AT = round(measureAT.getTime()*1000,4)  ##meet eigenlijke aanbiedtijd
        eigenlijketijd[trial*(block+1)] = AT                        ##overwrite default waarden naar eigenlijke aanbiedingstijd
        
        measureRT.reset()                       ##refresh dus ook hier pas de RT 
        
        gaborMask.draw()                        ##bied opnieuw de maskerende S aan 
        win.flip()                              
        
        ##pas nu wordt een respons (R) mogelijk, want (1) R < 50 ms zijn toch onmogelijk, en (2) zo voorkom je dat R worden overgedragen van de ene naar de andere trial
        
        k[0] = event.waitKeys(keyList = ["f","j"])       ##er is geen maxwait, gabormask blijft staan tot er antwoord wordt gegeven
        print(k[0])
        
        RT = round(measureRT.getTime()*1000,4)
        RTlist[trial*(block+1)] = RT
        
        FEEDBACK_MESSAGE()
        
        if "esc" in event.getKeys():            ##zorg ervoor dat je uit exp kan ontsnappen gedurende de trials
            break


##afsluit_____________________________________________________________________________________________________________________________________

afsluit = visual.TextStim(win, text = "Het experiment is gedaan! Bedankt voor uw deelname.\n\n" + 
                                      "Gelieve de proefleider bij u te roepen.")
afsluit.draw()
win.flip()
k = event.waitKeys(keyList = "space")
win.close()

##matrix_____________________________________________________________________________________________________________________________________
print(matrix)