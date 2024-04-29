from psychopy import visual, gui
from psychopy.hardware import keyboard
import time, numpy

#hardcoded experiment variables
textColor = 'black'
nr_trials = 12
nr_blocks = 2

nr_cells = 3
size_field = 50/100 * 2
start_field = -1
end_field = -1 + size_field
middle_field = (start_field - end_field)/2
size_cell = size_field/nr_cells
middle_cells = [start_field + size_cell/2 + i*size_cell for i in range(nr_cells)]
height_per_cell = [0 for i in range(nr_cells)]
size_square = size_field/nr_cells

#GUI dialogue box
info = {'Participant number':0,  'Full name': 'Fien Goetmaeckers', 'Gender': '', 'Age': 0, 'Handedness': ['right', 'left', 'both']}
infoDlg = gui.DlgFromDict(dictionary = info, title="My experiment")
if infoDlg.OK: 
    print(info)
else:
    print("User cancelled")
    
#create window
win = visual.Window([800, 800], units = "norm", color = "Gainsboro")
#create keyboard
kb = keyboard.Keyboard() 
#create all stimuli
Welcome             = visual.TextStim(win, text = "Welcome %s!" % (info["Full name"].split()[0]), color = textColor)
Instructions        = visual.TextStim(win, text = "Collect points by creating full lines. Drop the objects at a good position, to clear the line and score points!", color = textColor)
BasicText           = visual.TextStim(win, text = "", color = textColor) #can be used to change text messages (block per block for example)
Goodbye             = visual.TextStim(win, text = "This is the end of the experiment. Thanks for participating, %s!" % (info["Full name"].split()[0]), color = textColor)
Proceed             = visual.TextStim(win, text = "Press space to continue", color = textColor, pos = (0, -0.8))

Field               = visual.rect.Rect(win, width = size_field, height = 2, fillColor = "white", pos = (middle_field, 0))
Square              = visual.rect.Rect(win, width = size_square, height = size_square, fillColor = "green", pos = (middle_field, 0.8)) #square starts on the middle two cells
Score               = visual.TextStim(win, text = "", color = textColor, pos = (0.5, 0), wrapWidth = 1)

#welcome message
Welcome.draw()
Proceed.draw()
win.flip()
kb.waitKeys(keyList = ["space"])

#Instructions
Instructions.draw()
Proceed.draw()
win.flip()
kb.waitKeys(keyList = ["space"])

for b in range(nr_blocks):
    BasicText.text = "Block %s out of %s" % (b+1, nr_blocks)
    BasicText.draw()
    Proceed.draw()
    win.flip()
    kb.waitKeys(keyList = ["space"])
    points = 0
    ground = [-1, -1, -1] #at the beginning of a round, the ground is back to the lowest level
    
    #show already the playing field for a first time
    Field.draw()
    Score.text = "You currently have %s points" %points
    Score.draw()
    win.flip()
    time.sleep(3)
    
    for t in range(nr_trials):
        Field.draw() #you first have to draw the field, otherwise this will be on the front
        Square.draw()
        
        lowest_position = 0.8 - size_square/2
        x_pos = 1 #which x cell (from 0-2) is filled with this object?
        
        Score.text = "You currently have %s points" %points
        Score.draw()
        win.flip()
        
        #the trial only ends if the object hits the ground. To know this, we need to save where the ground is
        while lowest_position > ground[x_pos]:
            print(lowest_position)
            print(ground[x_pos])
            Field.draw()
            print(Square.pos)
            #Square.draw()
            Score.draw()
            win.flip()
            #keep on listening to clicks
            keys = kb.waitKeys(keyList = ["f", "j", "space"])
            if keys[0] == "f":
                #we move the object one to the left (if possible)
                if x_pos > 0:
                    #We can move the square to the left
                    x_pos -= 1
                    Square.pos[0] -= size_square
            elif keys[0] == "j":
                #we move the object one to the right (if possible)
                if x_pos < 2:
                    #We can move the square to the right
                    x_pos += 1
                    Square.pos[0] += size_square
            elif keys[0] == "space":
                #we lower the object
                lowest_position -= size_square
                Square.pos[1] -= size_square
            
    BasicText.text = "You scored %s points during this block" % (points)
    BasicText.draw()
    Proceed.draw()
    win.flip()
    kb.waitKeys(keyList = ["space"])
    
#Goodbye
Goodbye.draw()
Proceed.draw()
win.flip()
kb.waitKeys(keyList = ["space"])

win.close()