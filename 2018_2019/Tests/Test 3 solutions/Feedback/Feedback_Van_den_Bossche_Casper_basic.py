
# import modules
from psychopy import visual, event, core, gui
import time, numpy

### Esther: waarom was dit uitgecomment? Het ziet er nochtans goed uit
# create a dialog box
### Esther: het is nog beter om numerische eigenschappen ook te initializeren als nummers
info = {'Naam proefpersoon':'', 'Leeftijd':'', 'Gender':['man', 'vrouw', 'andere'], 'Handvoorkeur':['links', 'rechts', 'ambidexter']}
info_dialog = gui.DlgFromDict(dictionary = info, title = 'Experiment')
if info_dialog.OK:
    print(info)
else:
    print("User Cancelled")

# create the window
win = visual.Window(size = (600, 500), units = 'norm')

# clock
my_clock = core.Clock()

# define message
MessageOnSCreen = visual.TextStim(win, text = '')

def message(message_text = '', response_key = 'space', duration = 0):
    
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)
    
    return message

Gabor_stimuli = visual.GratingStim(win, tex="sin", mask="gauss", sf = 0, ori = 0)

def Gabor_trial(sf= 0, ori = 0):
    
    Gabor_stimuli.ori = ori
    Gabor_stimuli.sf = sf
    
    Gabor_stimuli.draw()
    win.flip()

Orientatie = numpy.array([30, -30, 30, -30, 30, -30, 30, -30])
SF = numpy.array([2, 20])

### Esther: waarom staat dit uitgecomment? Het ziet er ook goed uit
# Welkom message
message(message_text = 'Welkom ' + info['Naam proefpersoon'].capitalize() + '\nDruk op spatiebalk om verder te gaan')

# Instructies
message(message_text = 'Druk op de f toets wanneer de cirkel stimuli naar links gedraaid is - de lijnen lopen van linksboven naar rechtsonder\n'
 + 'Druk op de j toets wanneer de cirkel stimuli naar rechts gedraaid is - de lijnen lopen van rechtsboven naar linksonder\n\n'
 + 'Druk op spatiebalk om verder te gaan')



for i in range(8):
    
    ### Esther: eerst moet er een maskerende stimulus komen
    
    Gabor_trial(sf=2)
    core.wait(1)
    Gabor_trial(sf=2, ori = -30)
    Gabor_trial(sf=2)
    my_clock.reset()
    keys = event.waitKeys(keyList = ('f', 'j', 'escape'))
    print(my_clock.getTime())
    print(keys)
    
    if keys[0] == 'escape':
            break


# Afscheid message
message(message_text = 'Dit het einde van het experiment!\nBedankt voor uw aandacht')

win.close()






