"""
This demo code demonstrates how you can clear the Cedrus buffer 
to get rid of previous response info before starting response registration.
Failing to do so will result in erroneous responses. For instance,
the release of the previous trial will be carried over to the current trial.

See what would happen if you comment out clearBuffer(dev)!
"""

# import the generic experiment modules
from psychopy import visual, event, core

# import the Cedrus response box module
import pyxid2 as pyxid

# detect the Cedrus device and reset the timers
devices = pyxid.get_xid_devices()
dev = devices[0]
if dev.is_response_device():
    dev.reset_base_timer()
    dev.reset_rt_timer()

# open the experiment window
win = visual.Window(size = [500,500], color = 'black', fullscr = False)
event.Mouse(visible = False)

# Prepare graphical elements
Message = visual.TextStim(win)

# make the function to clear the Cedrus buffer
def clearBuffer(CedrusID):
    while True:
        CedrusID.poll_for_response()
        if CedrusID.response_queue_size() == 0: break
        if CedrusID.response_queue_size() > 0: CedrusID.clear_response_queue()

# initialise the lists where we will store the key that is pressed
returnedKey = []

# collect some key presses from the Cedrus response box
## set the counter to 0
cycles = 0
ncycles = 5
## keep on collecting responses as long as there have been less than 5 responses
while cycles < ncycles:
    
    ## give instructions
    Message.text = "trial " + str(cycles+1) + " of " + str(ncycles) + "\n" + "start the waiting time for a spurious key press: feel free to press!"
    Message.draw()
    win.flip()
    core.wait(2)
    
    ## collect and clear all the responses that were given
    clearBuffer(dev)
    
    ## give instructions
    Message.text = "Now give your actual response"
    Message.draw()
    win.flip()
    
    ## wait until a respons is given
    while True:
    
        ## collect a response
        dev.poll_for_response()
        
        ## check whether a response has been detected
        if dev.response_queue_size() > 0:
            
            ## register the received response
            response = dev.get_next_response()
            
            ## exit the while-loop when key number 6 has been pushed (escape key)
            if response.get("pressed") == True and response.get("key") == 6:
                break
            
            ## store the pressed key, increase the number of key presses already detected
            if response.get("pressed") == True:
                print(response)
                key = response.get("key")
                returnedKey.append(key)
                cycles += 1
                break

# print the output in the output window
print(returnedKey)

# close the experiment Window
win.close()

#########
## END ##
#########