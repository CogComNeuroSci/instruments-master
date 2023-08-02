"""
This demo code demonstrates how you can register bimanual responses.
For instance, here a participant would be pressing button 1 and 4 simultaneously 
(left and right middle finger), or buttons 2 and 3 simultaneously (left and right index).
"""

# import the Cedrus response box module
import pyxid2 as pyxid
import numpy

# detect the occupied port numbers and display them
devices = pyxid.get_xid_devices()
print(devices)

# detect the Cedrus COM port and reset the timers
dev = devices[0]
if dev.is_response_device():
    dev.reset_base_timer()
    dev.reset_rt_timer()

# initialise the array where we will store the two keys that have been pressed
ncycles = 2
nkeys = 2
nevents = nkeys * 2     ## because there is a press and release for each response
returnedKey     = numpy.empty([1,ncycles])
pressPattern    = numpy.concatenate((numpy.repeat(1.,nkeys),numpy.repeat(0.,nkeys)))    ## two presses followed by two releases

# collect some double key presses on the Cedrus response box
## set the counter to 0
cycles = 0
## keep on collecting responses as long as there have been less than 5 responses
while cycles < ncycles:
    
    ## announce the start of this trial
    print("start trial " + str(cycles+1) + " of " + str(ncycles))
    
    ## give instructions
    print("Please press the (1 and 4) or the (2 and 3) button simultaneously")
    
    ## keep on looping untill a correct response is given
    while True:
        
        ## keep track of the number of responses
        nresp = 0
        
        ## keep track of the content of the responses
        tempKey     = numpy.empty([1,nevents])
        tempPress   = numpy.empty([1,nevents])
        
        ## as long as there have not been two responses, we keep on sampling
        while nresp < nevents:
            
            ## collect a response
            dev.poll_for_response()
            
            ## check whether a response has been detected
            if dev.response_queue_size() > 0:
                
                ## register the received response
                response = dev.get_next_response()
                
                ## exit the while-loop when key number 6 has been pushed (escape key)
                if response.get("pressed") == True and response.get("key") == 6:
                    break
                
                ## store the port number and the pressed key, increase the number of key presses already detected
                tempKey[0,nresp] = response.get("key")
                tempPress[0,nresp] = response.get("pressed")
                nresp = nresp + 1
        
        ## check whether the two presses preceed the two releases
        if (tempPress == pressPattern).all():
            
            ## check whether only two buttons were involved
            if len(numpy.unique(tempKey)) == nkeys:
                
                ## check whether a correct combination of buttons was pressed
                if numpy.isin(numpy.unique(tempKey), [1.,4.]).all():
                    returnedKey[0,cycles] = 14     # code for outer buttons
                    break
                elif numpy.isin(numpy.unique(tempKey), [2.,3.]).all():
                    returnedKey[0,cycles] = 23     # code for inner buttons
                    break
                else:
                    print("Please press either (1 and 4) or (2 and 3)")
            else:
                print("Please press only two unique keys!")
        else:
            print("Please press the two buttons simultaneously, not consecutively!")
        
    ## update the cycle number
    cycles += 1

# print the output in the output window
print("These are the button combinations that you pressed simultaneously")
print(returnedKey[0,])

#########
## END ##
#########