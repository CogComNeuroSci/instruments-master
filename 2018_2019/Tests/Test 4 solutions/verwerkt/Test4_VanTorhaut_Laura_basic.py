# modules importeren
import numpy, os, random, pandas, time
from psychopy import visual, gui, event, core, data

#extra info
n_blokken = 12
n_trials = 60

# factorieel design aanmaken
pijltjes_opties = ["<", ">"]
positie_opties = [-0.5, 0, 0.5] ## enkel de x coördinaat verandert

trial_list = data.createFactorialTrialList ({"pijltjes": pijltjes_opties, "positie": positie_opties})

## lijst van dictionaries veranderen naar een dataframe
dataFrame = pandas.DataFrame.from_dict (trial_list)

## dataframe veranderen naar een numpy array
trial_array = dataFrame.values
print (trial_array)

# herhaal de condities 2 keer
trial_array = numpy.tile (trial_array, (10,1)) 

# volgorde randomiseren
numpy.random.shuffle (trial_array)

print (trial_array)

# huidige directory bepalen
mijn_directory = os.getcwd ()

directory_to_write_to = os.getcwd() + "/data/"

# controleren of de naam al bestaat
info = {"Naam proefpersoon": " ", "Proefpersoonnummer": 0, "Leeftijd": 0, "Gender": [ "man", "vrouw", "derde gender"], "Handvoorkeur": [ "links", "rechts", "ambidexter"]}

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    directory_to_write_to = mijn_directory + "/data"
    
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    nummer = str(info["Proefpersoonnummer"])
    file_name = directory_to_write_to + "/data" + nummer
    
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Geef ander proefpersoonnummer in")
        myDlg2.show()

# correcte response voor richting instructie
## cor_resp = numpy.copy (pijltjes_opties)
##cor_resp [cor_resp == pijltjes_opties [0]] = "left"
##cor_resp [cor_resp == pijltjes_opties [1]] = "right"

# gegeven response en reactietijd; vreemde waarde aan toekennen die later overschreven wordt
##response = numpy.repeat('t',n_trials)
##RT = numpy.repeat(-99.9, n_trials)

# congruentie bepalen
## congruentie_levels = numpy.array ([ "congruent", "incongruent", "neutraal"])
##if pijltjes_opties == "<" and richting_opties == -0.5 or pijltjes_opties == ">" and richting_opties == 0.5 :
    ## congruente trial
##elif richting_opties == 0:
    ## neutrale trial
##else:
    ## incingruente trial


# alle variabelen in een matrix steken
## matrix = numpy.column_stack ([pijltjes_opties, positie_opties, cor_resp, response, RT, congruentie, Leeftijd, Gebder, Handvoorkeur])

# window aanmaken
win = visual.Window (size =(1000, 700), units = 'norm')


# verwelkoming participant
welkom = visual.TextStim (win, text = "Welkom " + info["Naam proefpersoon"] + "!\nDruk op spatie om verder te gaan.")

# instructies
richting_instructietekst = ("In het volgende blok dien je te reageren op de \nrichting van de pijltjes met behulp van de pijltjes \nop het toetsenbord.\n"+
                        "Als het pijltje naar links wijst, druk je op het pijltje naar links.\n Als het pijltje naar rechts wijst, druk je op het pijltje naar rechts.\n"+
                        "Druk op spatie om verder te gaan.")
positie_instructietekst = ("In het volgende blok dien je te reageren op de \npositie van de pijltjes met behulp van de pijltjes \nop het toetsenbord.\n"+
                        "Als het pijltje links staat, druk je op het pijltje naar links.\n Als het pijltje rechts staat, druk je op het pijltje naar rechts\n"+
                        "en als het pijljte in het midden staat, druk je op het pijltje naar onderen.\nDruk op spatie om verder te gaan.")

richting_instructie = visual.TextStim (win, text = richting_instructietekst, height = 0.05)
positie_instructie = visual.TextStim (win, text = richting_instructietekst, height = 0.05)

# welkom proefpersonen
welkom.draw ()
win.flip ()
event.waitKeys(keyList = "space")

# klok aanmaken
mijn_klok = core.Clock()

#for i in range (n_blokken):
#    if n_blokken%3 == 0: ## instructies laten afwisselen
#        positie_instructie.draw ()
#        win.flip ()
#        event.waitKeys(keyList = ["space"])
#        numpy.random.shuffle (trial_array)
#    else:
#        richting_instructie.draw ()
#        win.flip ()
#        event.waitKeys(keyList = ["space"])
#        numpy.random.shuffle (trial_array)

# trialloop maken
for i in range (n_trials):
    stimuli = visual.TextStim (win, text = trial_array[i, 0], pos = (trial_array[i,1], 0))
    stimuli.draw ()
    win.flip ()
    event.clearEvents (eventType="keyboard")
    mijn_klok.reset()
    response = event.waitKeys (keyList = ["left", "right", "down"])
    RT = mijn_klok.getTime()
    print (response)
    print (RT)

# print (matrix)
# exporteren matrix naar een bestand
##matrix.to_csv(path_or_buf = file_name, index = False)

# einde
einde = visual.TextStim (win, text = "Bedankt voor je deelname!")
einde.draw ()
win.flip ()
event.waitKeys(keyList = "space")


# window sluiten
win.close ()