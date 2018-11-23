# ClassExcercise 4.7 

# Importing all the modules 
from psychopy import visual 
import time 
import numpy 

# Making a window 
win = visual.Window([600,400], color = "black", units = "norm", monitor = 'testmonitor')

# waarden volgens normale distributie 
bitcoin = 1
end_value = 100
mean = 0.1
sd = 0.025 
## Esther: the two lines of code are not being used, right?
hor_vertices = - 0.9
ver_vertices = - 0.9

# Een plot proberen maken
## Esther: I would initialise the counter right before the loop starts
count = 0
## Esther: why not use end_value as the stopping criterium for the while-loop?
while bitcoin <= 100: 
    
    # update the bitcoin value
    bitcoin += numpy.random.normal(mean, sd, size = None)*bitcoin 
    
    # store the bitcoin value in an array
    array_bitcoin = (numpy.array([bitcoin]))
    
    # determine the position on the y axis
    ## Esther: why are you using a random draw from a normal distribution?
    y_bitcoin = (((numpy.random.normal(array_bitcoin))/100)-0.8)
    
    # determing the position on the x axis
    x_bitcoin = numpy.array([count/50 -0.8])
    
    ## Esther: printing the coordinates helped to find the cause of the plotting error!
    print(count)
    print(y_bitcoin)
    print(x_bitcoin)
    
    # update the step counter
    count += 1
    
    ## Esther: no use to use a separate counter, just keep using count
    ## Esther: or use the length of the array with bitcoin values
    for i in range(count):
        
        print(i)
        
        plot_bitcoin = visual.Line(win, start = (x_bitcoin[i], y_bitcoin[i]), end = (x_bitcoin[i], y_bitcoin[i]), lineColor = 'white')
        plot_bitcoin.draw()
        win.flip()
        time.sleep(1)
   
win.close()
