from psychopy import visual, core, data, event
import numpy, pandas

#variables of the experiment
wait_step = 500/1000
nr_blocks = 3
nr_trials = 16
begin_size = 2/100 * 2

######create the randomization of the trial structure
grow_sizes             = numpy.array([1/100*2,5/100*2])
explosion_points       = numpy.array([1,2,3,4])

# determine the number of levels for the factor
Ngs     = len(grow_sizes) #2
Nep      = len(explosion_points) #4
Nunique    = Ngs * Nep #8

# determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) # 0, ... 7

# make the factorial design
Size = numpy.floor(UniqueTrials / Nep) % Ngs
Point = numpy.floor(UniqueTrials / 1) % Nep

#Realsize = numpy.array(grow_sizes[Size])

# combine arrays in trial matrix
trials = numpy.column_stack([Size, Point]) #Realsize
# we want 16 trials, not 8
nreps = int(nr_trials/Nunique)
trials = numpy.tile(trials, (nreps,1))

#create bigger trial matrix for ALL trials of all blocks
#all_trials = numpy.zeros([nr_trials*nr_blocks, 2])
all_trials = numpy.ones((nr_trials*nr_blocks,3)) * numpy.nan
for b_i in range(nr_blocks):
    numpy.random.shuffle(trials) #per block, we shuffle the trials
    #if two consec trials have the same explosion point, shuffle again! 
    while 0 in numpy.diff(trials[:,1]): #then there is a repeat!
        numpy.random.shuffle(trials)
    #and then we add the randomized trial order to a bigger trial matrix (all_trials)
    all_trials[b_i*nr_trials:(b_i+1)*nr_trials,:2] = trials

all_trials[:,2] = numpy.array(range(nr_trials*nr_blocks))
#transform this now into the needed format! 
#from numpy array to dataframe
dataFrame = pandas.DataFrame.from_records(all_trials)
dataFrame.columns = ["Growth_Size", "Expl_Point", "Trial_index"]
print(dataFrame)
#check with a cross table if every unique trial is equally represented!
print(pandas.crosstab(dataFrame.Growth_Size, dataFrame.Expl_Point))
#transform dataframe to dict
trial_list = pandas.DataFrame.to_dict(dataFrame, orient = "records")
#create trialhandler
trials = data.TrialHandler(trial_list, nReps = 1, method = "sequential")
#add this to experimenthandler
# Define the name of the output file
number = 1
output_file_name = "subject" + str(number)
# Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = output_file_name)
# Couple the TrialHandler to the ExperimentHandler
thisExp.addLoop(trials)


########create elements
#create a window
win = visual.Window((600,400), color = "pink")

#create visual elements
balloon = visual.Circle(win, radius = begin_size, color = "green")
kaboom_text = visual.TextStim(win, text = "KABOOM!!")
breakscreen = visual.TextStim(win, text = "You can take a break")
well_text = visual.TextStim(win,text = "Well done.")

for trial in trials:
    #if we are beginning a new block (not the first one though!), show a break screen!
    if (trial["Trial_index"] % nr_trials == 0) and (trial["Trial_index"] > 0): 
        breakscreen.draw()
        win.flip()
        core.wait(2)
        
    #per trial, we will need to read in the growth size and the explosion point
    gs = grow_sizes[int(trial["Growth_Size"])] #saved in trial["Growth_Size"] is the INDEX of the grow size, so read out the correct value of grow_sizes!
    ep = explosion_points[int(trial["Expl_Point"])] 
    
    ########run a minimal trial
    #first reset the balloon size!
    balloon.radius = begin_size
    balloon.draw()
    win.flip()
    #we check for keypresses!
    keys = event.waitKeys(maxWait = wait_step)
    i = 0
    while keys is None and i < ep:
        #balloon.radius = begin_size + (i+1) * grow_step
        balloon.radius = balloon.radius + gs
        balloon.draw()
        win.flip()
        keys = event.waitKeys(maxWait = wait_step)
        i += 1
    if i == ep: #then the while loop ended without pressing!
        kaboom_text.draw()
        win.flip()
        core.wait(1)
        pressed = 0
        score = 0
    else: #then the while loop ended with pressing!
        #save that something is pressed
        #show a score! balloon.radius --> score
        score = i+1 #to get a score of 1 for pressing immediatly
        well_text.draw()
        win.flip()
        core.wait(1)
        pressed = 1
    
    #save if a key is pressed, what the balloon size was
    trials.addData("Pressed", pressed)
    trials.addData("Score", score)
    
    thisExp.nextEntry()
    
win.close()



#def check_consec_doubles(array):
#    previous_el =array[0]
#    bad = Good
#    for i in range(1, len(array)):
#        el = array[i]
#        if el == previous_el: #we don't want this!
#            bad = True
#            break
#        previous_el = previous
#    return bad
