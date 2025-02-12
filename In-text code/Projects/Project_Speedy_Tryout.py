# Magnitude comparison task #

# Import modules
from psychopy import visual, event, core, gui, data
import os, random, time

# provide a short test while programming (if set to 1)
earlyExit = 0

# provide a speeded version of the experiment for debugging (if set to 1)
speedy = 1

# Set directory
my_directory = os.getcwd()

## construct the name of the folder that will hold the data
directory_to_write_to = my_directory + "/data"
    
## if the folder doesn't exist yet, make it
if not os.path.isdir(directory_to_write_to):
    os.mkdir(directory_to_write_to)

# Create and save datafile
dlginfo = {"Participant name":"Incognito", "Participant number": 0, "Gender": ["Female","Male"], "Handedness": ["Right","Left"], "Age": 0}
exists = True
while exists:
    
    mydlg       = gui.DlgFromDict(dictionary = dlginfo, title = "Magnitude comparison task")
    filename    = directory_to_write_to + "/Magnitude comparison task_p" + str(dlginfo["Participant number"])
    
    if not os.path.isfile(filename + ".csv"):
        exists  = False
    else:
        mydlg2  = gui.Dlg(title = "Error")
        mydlg2.addText("Participant number already exists. Please enter another one.")
        mydlg2.show

## extract the name of the participant from the dialog box information
subject_name = dlginfo["Participant name"]

## remove the name of the participant from the dialog box information (anonimity!)
dlginfo.pop("Participant name")

# Initilialize the experiment handler
magnexp = data.ExperimentHandler(dataFileName = filename, extraInfo = dlginfo)

# Set stimulus parameters
keyList             = ["f","j","escape"]
colorbackground     = (1,1,1)
colorstim           = (0,0,0)
number              = [1,2,3,4,6,7,8,9]
random.shuffle(number)
magntrials          = len(number) 
magntotalcorrect    = 0 
my_clock            = core.Clock()

# Initialize window
win = visual.Window(fullscr = True, color = colorbackground)

# Prepare graphical elements
stim                = visual.TextStim(  win, text = "", color = colorstim)

welcome             = visual.TextStim(  win,text=(  "Hi {},\n"+
                                                    "Welkom op dit experiment!\n\n"+
                                                    "Druk op spatie voor de instructies.").format(subject_name), color = colorstim)
    
instructions        = visual.TextStim(  win,text=(  "Je krijgt zo meteen een reeks getallen te zien tussen 1 en 9 \n"+
                                                    "met de uitzondering van 5. Het is de bedoeling dat je aangeeft \n"+
                                                    "of het getal kleiner of groter is dan 5.\n\n"+
                                                    "Druk op ‘f’ als het getal kleiner is dan 5.\n"+
                                                    "Druk op ‘j’ als het getal groter is dan 5.\n\n"+
                                                    "Druk op spatie om te starten."), color = colorstim)

goodbye             = visual.TextStim(win,text=(    "Dit is het einde van het experiment.\n\n"+
                                                    "Laat de proefleider weten dat je klaar bent.\n\n"+
                                                    "Bedankt voor je deelname!"), color = colorstim)

# Make Mouse Invisible
win.mouseVisible = False

welcome.draw()
win.flip()
keys = event.waitKeys(keyList = "space")

instructions.draw()
win.flip()
keys = event.waitKeys(keyList = "space")

# Start of magnitude comparison task
for trialnr in range(magntrials):
    
    # quick fixation cross
    stim.text = "+"
    stim.draw()
    win.flip()
    if speedy != 1:
        time.sleep(0.2)
    
    # display the stimuli on the screen
    stim.text = number[trialnr]
    stim.draw()
    win.flip()
    
    # wait for the response
    my_clock.reset()
    if speedy != 1:
        keys = event.waitKeys(keyList = keyList)
    else:
        keys = "f"
    
    # register response info
    magnexp.addData("Answer",       keys[0])
    magnexp.addData("MagnitudeRT",  my_clock.getTime())
    
    # add an escape option
    if keys[0] == ["escape"]:
        break
    
    # determine accuracy
    magncorrect = 0
    if number[trialnr] < 5 and keys[0] == "f":
        magncorrect = 1
    elif number[trialnr] > 5 and keys[0] == "j":
        magncorrect = 1
    magntotalcorrect += magncorrect
    
    # store the trial info
    magnexp.addData("Magnitudenumber",  number[trialnr])
    magnexp.addData("Magncorrect",      magncorrect)
    magnexp.addData("Magntotcorrect",   magntotalcorrect)
    magnexp.addData("Trial",            trialnr)
    
    # proceed to next line of the output file
    magnexp.nextEntry()
    
    # exit after a few trials in the demo version
    if earlyExit == 1 and trialnr == 2:
        break

## say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

win.close()
