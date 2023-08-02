## import modules
from psychopy import core
from psychopy import parallel 

## set the address of the parallel port
parallel.setPortAddress(0xC020)

## send all the possible trigger numbers
for i in range(256):

    ## start with a baseline of 0
    parallel.setData(0)
    ## send the trigger
    parallel.setData(i) 
    ## wait for 20 milliseconds so the trigger is registered
    core.wait(.02)
    ## end with the baseline again
    parallel.setData(0)

    ## print the number in the output window, just as a check
    print(i)