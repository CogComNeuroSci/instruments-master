############
## import ##
############

from psychopy import core, visual, event

# The content found in this script is adopted from the file 'gabor.py', which can be found under Demos > Stimuli
## While the main setup of this script is very similar to that file, we added some extra explanation, and some adaptations to the original script

## In the code below, we will draw a gabor patch
## Gabor patches are stimuli that drive early visual activity in a controlled fashion
    ## Because of this characteristic, they are a solid presence in any vision lab
        ## For a very elaborate overview of the importance of Gabor patches, we refer to:
        # http://neuroanatody.com/2016/05/whats-in-a-gabor-patch/
    ## Alternatively, we refer to a paper which uses Gabor patches to research the effect of perceptual experience on brain development:
        ## Blakemore, C., & Cooper, G. F. (1970). Development of the brain depends on the visual environment. Nature, 228(5270), 477-478.
        ## The pdf version of this paper can be downloaded by using the link below (activate your VPN connection, just to be sure that it downloads without issues)
        # https://www.researchgate.net/profile/Colin_Blakemore/publication/51273162_Development_of_the_Brain_Depends_on_the_Visual_Environment/links/5612970608ae400c16af1164/Development-of-the-Brain-Depends-on-the-Visual-Environment.pdf

## As usual, we first create a window to draw in

win = visual.Window([400,400])

## Below, we start by declaring the name of our Gabor patch, namely 'gabor'
## To draw arbitrary bitmaps (a term which refers to the storage of digital images), we can use the specific function called 'GratingStim()'
    ## We can draw multiple types of bitmaps: circles, crosses, gabor patches... based on the defined arguments in GratingStim()
        ## This also suggests that the Gabor patch is indeed widely used, as there is a special argument in GratingStim() to draw one

## First, we will define the arguments that are used here; further on, we define some possible extra arguments
    ## win signifies the window we are drawing the Gabor patch in, of course the name 'win' is arbitrary
    ## tex defines the structure to use as a grating on the stimulus
        ## We have a lot of choice when it comes to defining the grating used
            ## sin
            ## sqr
            ## saw
            ## tri
            ## None
                ## None actually shows the 'bare foundation' of the Gabor patch we draw: a white circle that gradualy blends in with the grey background
            ## If we define 'tex' as one of the others, we will see a grating instead of the white circle
                ## The grating here actually greatly resembles the dictionary definition of grating:
                    ## a fixed frame of bars or the like covering an opening to exclude persons, animals, coarse material, 
                    ## or objects while admitting light, air, or fine material
                ## So, the bars in front of prison windows are also gratings
                ## A similar pattern can also be seen in our Gabor patch
            # We recommend to play a bit with the different arguments of 'tex', and to spot the difference
            ## Note that we can also use our own Numpy array to define tex (you'll get to know Numpy arrays in Lesson 11 and 12), or even an imported image!
                ## It is logical that we can use an array to define the grating if we understand what a bitmap actually is
                ## Because this is beyond the scope of this course, we will let this slide, but for the interested reader, we refer to:
                    ## https://en.wikipedia.org/wiki/Bitmap
                ## which provides enough information on bitmaps to understand why we can use arrays to define the grating on our stimulus
    ## mask is used to define the shape of our stimulus
        ## circle
        ## gauss
        ## raisedCos
        ## cross
            ## If we use cross for example, we will see a large cross, with a black and white grating in it (assuming that tex is not set on 'None')
        # Again, play around with the different values to see for yourself!
    ## texRes sets the resolution of both tex and mask
        ## Keep in mind that the resolution always has to be square (number x number), and that number has to be power-of-two dimensions (e.g. 256, which equals 2**8)
            ## So, a valid resolution would be 256
        ## Also, when an array or an external picture is provided, the dimensions of these are used, so the defined texRes will be ignored in that case
        ## As a final note, we mention that the resolution will be upscaled until a required dimension is reached
            ## e.g. if the dimension was 233 x 233, then it will be upscaled to 256 x 256
    ## size obviously defines the size of the displayed stimulus
        ## The arguments define the width (x, horizontal axis) and height (y, vertical axis), with the first argument being the width
        ## Alternatively, both arguments can be negative (flipped across the x-axis or y-axis)
        ## As a side note, we can make the stimulus larger than the window
    ## sf stands for spatial frequency of the grating texture
        ## Can be pair (representing x and y), or float/integer
        ## Depending on the units of your window, the definition of sf may have other implications:
            ## if units are 'deg' or 'cm'
                ## sf represents the cycles per deg/cm
            ## if units equals 'norm', then
                ## sf represents cycles per stimulus
            ## The texture can also be an external loaded image, then
                ## 1 cycle of the image will default to 1/(size of the stimulus)
    ## ori represents the orientation of the stimulus in degrees 
        ## Usually, this is defined as a scalar (float or integer)
            ## 0 means that no rotation is done
            ## Positive values represent clockwise rotation
            ## Rotating 370 degrees is of course the same thing as rotating 10 degrees
    ## Why would we define a name if we already have a variable name ('gabor')?
        ## name is the name that is used when writing data about the drawing of this stimulus
            ## So, if we log information about 'gabor', we will see that the name of this drawing is 'gabor1' in our external text file
            ## When we have multiple patches in our experiment, this helps us to remember what kind of stimulus the participants saw
                ## It is always a good idea to have more descriptive names, such as 'gabor_phase1', 'gabor_testphase' etc.
                    ## 'gabor1' does not tell us that much really
                    # try to be descriptive when defining variables
            ## Name can also be set to 'None', meaning that this stimulus will be logged as 'unnamed TextStim'
        ## Obviously, name has to be a string
    ## autoDraw determines whether a stimulus is drawn with every frame flip or not (you'll get to understand this in Lesson 8)
        ## True means that this will happen
    ## phase represents the phase of the stimulus in each dimension of the texture
        ## This is defined by a scalar (float/integer), and not in degrees or radians (in which phase shifts are usually defined)
        ## To understand phase shifts, we refer to
            ## http://jwilson.coe.uga.edu/EMAT6680/Dunbar/Assignment1/sine_curves_KD.html
        ## which provides a thorough introductory explanation on waves and transformations of waves 
        ## For basic concepts on waves, we also refer to
            ## http://engineers4world.blogspot.be/2009/10/properties-and-characteristics-of-wave.html
        ## For a visualisation of a phase shift of a sine wave, we refer to
            ## https://www.mathsisfun.com/algebra/images/sine-cosine-graph.gif
                ## In this animation, we see a sine wave
                   ## Shifting this sine wave will result in a sine with the same amplitude and period
                   ## The phase (the position of a point in time) will of course be different
                ## Shifting the sine with pi/2 to the left will result in a cosine wave
                    ## This wave is obtained by phase shifting with pi/2 to the left
                        ## In radians, 2pi equals 360 degrees, so, shifting with pi/2 would be a shift by 90 degrees
                ## That the sine is shifted can be noticed by looking at the extremities of the sine
                    ## In the original sine, the peaks of the sine are situated at n*(1/2pi)
                        ## Sine at its highest at pi/2, at its lowest at 3pi/2...
                    ## When the sine is shifted pi/2 to the left, all the extremities are situated at n*(pi)
                        ## Sine at its highest at 0 (pi*0), at its lowest at pi (pi*1)
                        ## The shifted sine has the exact same properties as a cosine wave
    ## We recommend to understand the concept of phase shifting, as this is also (implicitly) important for other procedures (such as analysis of neuroimaging data (EEG))
    # While this explanation is all mathematics, the main message is that the stimulus is moved in time by defining phase
        # how much the stimulus is moved depends on the integer associated with phase (which is + 0.01 every cycle in this case)
        # If we would neglect phase, the stimulus would remain stationary of course

gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')
gabor.autoDraw = True
message = visual.TextStim(win, pos=(0.0, -0.9), text='Hit < escape > to quit')
trialClock = core.Clock()

## repeat drawing for each frame
while trialClock.getTime() < 20: 
    gabor.phase += 0.01
    message.draw()
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()

    win.flip()

win.close()
core.quit()

## We gave an extensive overview of the arguments used in this particular demo, however, other arguments are still available
    ## color (speaks for itself)
    ## clearTextures(stimulusname)
        ## Clears all textures associated with a certain stimulus
    ## opacity
        ## Determines how transparant a certain stimulus is (visibility in contrast to the background)
    ## And many other arguments are still available!
# We refer to 
    # http://www.psychopy.org/api/visual/gratingstim.html
# For a complete overview of all the arguments avaible for visual.GratingStim

# We HEAVILY recommend to play with the different arguments for yourself, you learn by doing!

#########
## END ##
#########
