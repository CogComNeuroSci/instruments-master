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
hor_vertices = - 0.9
ver_vertices = - 0.9
count = 0

# Een plot proberen maken
while bitcoin <= 100: 
    bitcoin += numpy.random.normal(mean, sd, size = None)*bitcoin 
    array_bitcoin = (numpy.array([bitcoin]))
    y_bitcoin = (((numpy.random.normal(array_bitcoin))/100)-0.8)
    x_bitcoin = numpy.array([count/50 -0.8])
    count += 1
    counter = count
    for i in range (counter):
        plot_bitcoin = visual.Line(win, start = (x_bitcoin[i], y_bitcoin[i]), end = (x_bitcoin[i], y_bitcoin[i]), lineColor = 'white')
        plot_bitcoin.draw()
        win.flip()
        time.sleep(1)

win.close()
