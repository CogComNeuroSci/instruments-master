"""
This demo code allows you to see what Cedrus button corresponds to what button code.
The 7 Cedrus buttons are coded 0 to 6 from left to right.
"""

# import the Cedrus response box module
import pyxid2 as pyxid

# detect the devices and display them
devices = pyxid.get_xid_devices()
print(devices)

# detect the Cedrus device and reset the timers
dev = devices[0]
if dev.is_response_device():
    dev.reset_base_timer()
    dev.reset_rt_timer()

# initialise the lists where we will store the COM port and the key that is pressed
returnedPort = []
returnedKey = []

# give instructions
print("Please press 5 keys or exit by pushing the far right key")

# collect 5 key presses from the Cedrus response box
## set the counter to 0
cycles = 0
## keep on collecting responses as long as there have been less than 5 responses
while cycles < 5:
    
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
        if response.get("pressed") == True:
            print(response)
            port = response.get("port")
            key = response.get("key")
            returnedPort.append(port)
            returnedKey.append(key)
            cycles += 1

# print the output in the output window
print(returnedPort)
print(returnedKey)

#########
## END ##
#########