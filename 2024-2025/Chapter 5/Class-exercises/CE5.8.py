#basic code for test 3
#differences from test 3:
#left, middle or right mouse clicks as answers
#always show a history stimuli underneath each tree

from psychopy import visual, gui, event
import time, numpy
from psychopy.hardware import keyboard
#experiment details
nr_blocks = 4
nr_trials = 8
#before starting the experiment; call for a GUI

#use the GUI dialogue to collect information about the
#participant's number, full name, age, gender and handedness
dlg = gui.Dlg(title="My experiment", pos=(200, 400))
dlg.addText('Subject Info', color='Blue')
dlg.addField('Participant number:', initial = 0)
dlg.addField('Full name:')
dlg.addField('Age:')
dlg.addField('Gender:', choices = ('woman', 'man', 'non-binary', 'other', 'prefer not to say'))
dlg.addField('Handedness:', choices = ('right', 'left', 'both'))
thisInfo = dlg.show()
if dlg.OK: 
    print(thisInfo)

win = visual.Window([800, 800], units = 'norm', color = [0.68, 0.85, 0.9])

#Display a welcome message
Welcome             = visual.TextStim(win, text = "Welcome {}!".format(thisInfo[1].split()[0]), color = 'black')
Instructions        = visual.TextStim(win, height = 0.05, text = 
                                "In this experiment, you will have to pick apples from trees.\n" +
                                "During {} rounds, you'll visit {} fruit orchard,\n".format(nr_blocks, nr_blocks) +
                                "in which all of them you'll have three trees to pick apples from.\n" +
                                "By selecting a tree, you pick an apple from that tree.\n" +
                                "The apple you pick will have a specific weight (expressed in grams),\n" +
                                "with some trees yielding heavier apples than the others.\n" +
                                "It is your task to collect as many grams of apples as possible,\n" +
                                "by learning, per fruit orchard, which tree yields the heavier apples.", color = 'black')
BeginBlock          = visual.TextStim(win, text = "Block 1 out of {}".format(nr_blocks), color = 'black')
EndBlock            = visual.TextStim(win, text = "In this fruit orchard, you have collected 0 grams of apples", color = 'black')
EndExperiment       = visual.TextStim(win, text = "Thank you for your participation, {}.".format(thisInfo[1].split()[0]), color = 'black')
SkipInstructions    = visual.TextStim(win, text = "To continue, press space", height = 0.05, pos = (0,-0.8), color = 'black')

kb = keyboard.Keyboard() 

#stimuli for trial
TreeRed             = visual.Circle(win, radius = 0.15, pos = (-0.5, 0.5), fillColor = 'FireBrick')
TreeGreen           = visual.Circle(win, radius = 0.15, pos = (0, 0.5), fillColor = 'ForestGreen')
TreeYellow          = visual.Circle(win, radius = 0.15, pos = (0.5, 0.5), fillColor = 'Gold')
WeightRed           = visual.TextStim(win, text = "History:\n", pos = (-0.5, 0), height = 0.08, color = 'black')
WeightGreen         = visual.TextStim(win, text = "History:\n", pos = (0, 0), height = 0.08, color = 'black')
WeightYellow        = visual.TextStim(win, text = "History:\n", pos = (0.5, 0), height = 0.08, color = 'black')
InstructionsKb      = visual.TextStim(win, text = "Press 'g' to pick an apple from the red three,\n" +
                                                   "'h' for the green tree and 'j' for the yellow tree.",
                                                   pos = (0, -0.8), height = 0.05, color = 'black')

#responses matrix
# store the colour of the tree
Colour = numpy.repeat("white", nr_blocks * nr_trials)
#allow to store weight of the sampled apple
Weight = numpy.repeat(0, nr_blocks * nr_trials)
RT = numpy.repeat(0.0, nr_blocks * nr_trials)
# combine arrays in trial matrix
trials = numpy.column_stack([Colour, Weight, RT])

#the mean weights per tree, which differ per round
mean_weights_total = [[300, 200, 100],
                      [200, 100, 300],
                      [100, 300, 200],
                      [300, 100, 200]]

#run the experiment
Welcome.draw()
SkipInstructions.draw()
win.flip()
keys = kb.waitKeys(keyList = ['space'])

Instructions.draw()
SkipInstructions.draw()
win.flip()
keys = kb.waitKeys(keyList = ['space'])

#the trials
for block_nr in range(nr_blocks):
    #show the block announcement
    BeginBlock.text = "Block {} out of {}".format(block_nr+1, nr_blocks)
    BeginBlock.draw()
    SkipInstructions.draw()
    win.flip()
    keys = kb.waitKeys(keyList = ['space'])
    
    #set up
    mean_weights = mean_weights_total[block_nr]
    total_weight_round = 0
    
    #reset the history of each tree:
    WeightRed.text = "History:\n"
    WeightGreen.text = "History:\n"
    WeightYellow.text = "History:\n"
    
    for trial_nr in range(nr_trials):
        
        #show the stimuli
        TreeRed.draw()
        TreeGreen.draw()
        TreeYellow.draw()
        #show also the history
        WeightRed.draw()
        WeightGreen.draw()
        WeightYellow.draw()
        
        #show the instructions for the tree selection:
        InstructionsKb.draw()
        win.flip()
        
        #reset the clock immediately after showing the stimili
        kb.clock.reset()
        keys = kb.waitKeys(keyList = ["g", "h", "j"])
        #a trial only ends when one of the keys is pressed
        
        if (keys[-1].name == 'g'): # then Red has been selected
            response = "Red"
            #sample a weight
            weight = numpy.random.normal(mean_weights[0], 30)
            #update the history of the red tree
            WeightRed.text += "{} g\n".format(round(weight))
            #to ensure that this press gets only recorded once
            time.sleep(0.2) 
                
        elif (keys[-1].name == 'h'): #green tree
            response = "Green"
            weight = numpy.random.normal(mean_weights[1], 30)
            WeightGreen.text += "{} g\n".format(round(weight))
            #to ensure that this click gets only recorded once
            time.sleep(0.2)
                
        elif (keys[-1].name == 'j'): #yellow tree
            response = "Yellow"
            weight = numpy.random.normal(mean_weights[2], 30)
            WeightYellow.text += "{} g\n".format(round(weight))
            #to ensure that this click gets only recorded once
            time.sleep(0.2)
            
        #save the relevant data of this trial
        total_weight_round += weight
        trials[block_nr * nr_trials + trial_nr, 0] = str(response)
        trials[block_nr * nr_trials + trial_nr, 1] = round(weight)
        trials[block_nr * nr_trials + trial_nr, 2] = keys[-1].rt
    
    #after all nr_trials clicks, we still want the participant to see the feedback of their last click:
    #show the stimuli
    TreeRed.draw()
    TreeGreen.draw()
    TreeYellow.draw()
    #show also the history
    WeightRed.draw()
    WeightGreen.draw()
    WeightYellow.draw()
    
    win.flip()
    time.sleep(2)
    
    EndBlock.text = "In this fruit orchard, you have collected {} grams of apples".format(round(total_weight_round))
    EndBlock.draw()
    SkipInstructions.draw()
    win.flip()
    keys = kb.waitKeys(keyList = ['space'])
    
print(trials)


EndExperiment.draw()
SkipInstructions.draw()
win.flip()
keys = kb.waitKeys(keyList = ['space'])


win.close()

