# import modules
from psychopy import visual, event, core, gui
import time, numpy


# initialize the window
win = visual.Window(size = [600,500], units = "norm")


# GUI dialog box: register participant info
info = {"Name": "Unknown","Participant Number": 0, "Age": 0, "gender":["Male", "Female", "X"], "Hand preference":["Left", "Right", "Ambidexter"]}

## Van info GUI maken
infoDlg = gui.DlgFromDict(dictionary=info, title='GaborExperiment')

if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
        print("user Cancelled")


#escape the experiment using esc
for key in ['escape']:
            event.globalKeys.add(key, func=core.quit)


# initialize the variables
Name                     = info["Name"]
nblocks                  = 3
ntrials                  = 3 ##moet 8 zijn, kijken hoe tijd aanpassen
timer                    = core.Clock()


# initialize graphical elements
## welcome text
Welcome                 = visual.TextStim( win, text = "Welcome to this experiment {0}.".format(Name) + "\nPress the spacebar to continue")

## instruction text
Instructions            = visual.TextStim(win, text = "The instructions of the experiment are the following: on each trial you will see a gabor stimulus, this is a figure with black en white stripes." + 
                                            "\n\nWhat you have to do is decide if the strips are turned to the left, this means the stripes start in the left upper corner and end in the right lower corner." +
                                            "\n\nOr if they are turned to the right, this means the stripes start at the right upper corner and end at the left lower corner." + 
                                            "\n\nif you think the figure is turned left, you have to press the F-key, if you think the figure is turned right, you have to press the J-key." +
                                            "\n\nif everything is clear press the spacebar to continue.", height = 0.05)

## goodbye text
Goodbye                 = visual.TextStim(win, text = "Goodbye {0}, I hope you enjoyed the experiment!".format(Name))

## block text
Block_start             = visual.TextStim(win, text = "OK")

## gabor stimulus
Gabor                   = visual.GratingStim(win, mask = "circle", ori = 0, sf = [4,0])

Gabor_left              = visual.GratingStim(win, mask = "circle", ori = 30, sf = [4,0] )

Gabor_right             = visual.GratingStim(win, mask = "circle", ori = 330, sf = [4,0] )

## feedback text
Feedback                = visual.TextStim(win, text = "OK")

###Make a function of the Feedback : werkt niet
#def Feedback():
#    ## feedback text
#    Feedback                = visual.TextStim(win, text = "OK")
#    if Key == "j":
#        Feedback.text = "Wrong Answer!"
#    
#    else:
#        Feedback.text = "Correct!"
#    
### Esther: hier staat de .text te veel
#    Feedback.text.draw()


#display the Gabor stimulus are you ready for various number of seconds
### Esther: pas op deze aanbiedingstijden zijn 10 keer te 
Gabor_time              = numpy.array([0.16, 0.33, 0.50])


#Register info
##Register the participant respons on the trial (F or J)
###Respons                = numpy.repeat(-99.9, len(Gabor_time))

###RT                     = numpy.repeat(-99.9, len(Gabor_time))

#Output tabel
###trials                 = numpy.column_stack([Respons, RT])


#display elements on the screen
##Welcome text
Welcome.draw()
win.flip()
### Esther: "space" hoeft niet in een list te worden opgenomen
event.waitKeys(keyList = ["space"])

##instructions text
Instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#loops
for b in range(nblocks):
    
    ## announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start now." + "\nPress the space bar to go to the next block."
    Block_start.draw()
    win.flip()
    
    ## escape out of the experiment by pressing the space bar
    event.waitKeys(keyList = ["space"])
    
    for i in range(ntrials):
        
        
        ##display the standar gabor stimulus for 1 second
        Gabor.draw()
        win.flip()
        time.sleep(1)
        
        ##display the turned gabor stimulus for the asked time
        Gabor_left.draw()
        
        ### Esther: dit is het moment om het keyboard te clearen
        
        win.flip()
        
        ### Esther: dit is het moment om de clock te resetten
        
        core.wait(Gabor_time[i])
        ### Esther: hier had je de index van de blokloop moeten gebruiken ;)
        
        ##clear the previous Respons
        event.clearEvents(eventType = "keyboard")
        
        ##display the standard gabor stimulus while waiting for the respons
        Gabor.draw()
        win.flip()
        
        ## reset the timer to measure the RT 
        timer.reset()
        
        ## Only F and J are allowed, show in the output what key is pressed
        Key = event.waitKeys(keyList = ["f", "j"])
        print(Key)
        
        ##measure the RT and show it in the output
        RT = timer.getTime()
        print(RT)
        
        ##give feedback
        if Key == "j":
            Feedback.text = "Wrong Answer!"
            ### Esther: dit is niet het moment om te breaken
            break
        else:
            Feedback.text = "Correct!"
        
        Feedback.draw()
        win.flip()
        time.sleep(1)
        



#Display elements on the screen
##Goodbye text
Goodbye.draw()
win.flip()
time.sleep(2)


##print(trials)


#close window
win.close()