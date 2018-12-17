### Esther: hier ben je vergeten om de library van de gui in te laden
from psychopy import visual, event, core
import time 

### ESther: hier heb je meteen al een syntax error
info = {"Participant name":"Unknown", "Participant number":0, "Age":0, "Gender":["male", "female", "", "Handpreference":["left", "right", "ambidexter"]}

### Esther: het is nog beter om numerische eigenschappen ook te initializeren als nummers
info = {"Naam":"Unknown", "Proefpersoonnummer": "Unknown", "Leeftijd": "Unknown", "Gender": ["man", "vrouw", "derde gender"], "Handvoorkeur": ["links", "rechts", "ambidexter"]}

### Esther: If you want to give participants with an ever versus odd number different instructions, that will only work when the participant number is an actual number

### Esther: het is nog beter om numerische eigenschappen ook te initializeren als nummers
### Esther: het is beter om de response opties voor gender en handvoorkeur ook echt te presenteren als respons opties in plaats van enkel een suggestie
expInfo = {'voornaam': '', 'achternaam': '', 'proefpersoonnummer': '','leeftijd': '', 'gender': 'man, vrouw, derde gender', 'handvoorkeur': 'links, rechts of ambidexter'}
dlg = gui.DlgFromDict(dictionary=expInfo, title="")

### Esther: kies misschien een niet-gebruikt proefpersoon nummer als de default
info = {"Participant number":20, "Participant name":"Unknown", "Gender":["male", "female","third gender"], "Age":0, 'hand preference':['left','right','ambiodextrous']}

### Esther: waarom dit in een functie plaatsen? Op die manier weet je enkel de info over de naam van de participant maar niets anders
def dialoguebox():
    ### Esther: kies misschien een niet-gebruikt proefpersoon nummer als de default
    info = {"Participant number":20, "Participant name":"Unknown", "Gender":["male", "female","third gender"], "Age":0, 'hand preference':['left','right','ambiodextrous']}
    infoDlg = gui.DlgFromDict(dictionary=info, title="Stroop Experiment")
    if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
        print(info)
    else:
        print("User Cancelled")
        exit()
    participant = info ["Participant name"]
    return participant

# create a window to draw in
win = visual.Window(units = 'norm', size = [600, 500], allowGUI=False)

#some variables for the text
duration = 0
participant = dialoguebox()

### Esther: het is nog beter om age te initialiseren als een nummer in plaats van een string
# maken dialoogvenster
def check_input_device():
    info = {"name":"", "Participant number":0,"age":"","gender":["man","vrouw","neutraal"], "handvoorkeur":["links","rechts","ambidexter"]}
    gui.DlgFromDict(dictionary = info)
    return info
participant_info = check_input_device()