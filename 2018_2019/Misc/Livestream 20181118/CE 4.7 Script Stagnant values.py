#ClassExcercise 4.7 

#Importing all the modules 
##This is always the first step 

from psychopy import visual 
import time 
import numpy 

# Making a window 

#win = visual.Window([600,400], color = "black", units = "norm", monitor = 'testmonitor')

# waarden volgens normale distributie 


bitcoin = 1
end_value = 100
mean = 0.1
sd = 0.025 
hor_vertices = - 0.9
ver_vertices = - 0.9
count = 0

# Initialize the graphical elements
#stim    = visual.TextStim(win, text = "test", pos = (0.0,0.5))
#curve   = visual.Line(win, start = (0,0), end = (0,0))
#curve.lineWidth = 2

numpy.random.normal(mean, sd, size = None)



#Tekst bovenaan
#Plot hierbij samen voegen


while bitcoin <= 100:     ##Zodat het gaat van 0 tot honderd
    
    bitcoin += numpy.random.normal(mean, sd, size = None) * bitcoin ## Uw bitcoin van de vorige + uw gemiddelde van de vorige maal uw bitcoin om de random waarden te geneneren
    array_bitcoin = (numpy.array(bitcoin))
    
    red_making = -((numpy.array(bitcoin)/50)-1)
    if red_making < -1:
        red_making = -1
    
#    stim.text = "Current value: {0} euro".format(round(bitcoin))
#    stim.color = (1, red_making, red_making)
    
    count += 1
    counter = count
    
    # /100 en /50 zodat het tussen 0 en 1 is en dan - 0.8 zodat het tussen -0.8 en 0.8 is 
    y_bitcoin = (((numpy.random.normal(array_bitcoin))/100)-0.8)
    x_bitcoin = numpy.array([count/50 -0.8])
    
    #zodat je uw coördinaten hebt
    x_y = numpy.vstack([x_bitcoin, y_bitcoin])
    print(count)
    print(x_y)
    
    #plot tekenen
    #for i in range(counter): 
#        curve.start = (x_y[i,0], x_y[i,1]) 
#        curve.end = (x_y[i,0], x_y[i,1])
#        curve.draw() 
        
    # plot en tekst samen 
#    stim.draw()
#    win.flip()
#    time.sleep(0.1)


##We gebruiken count om te zien hoeveel keer we door de loop gaan 
##Dit gebruiken we om dan te zien hoeveel punten er in onze plot moeten zijn ( x as) 

# waarden die we berekent hebben als punten voor plot

## van - 0.8 tot 0.8 en die afstand is 1.6 daartussen zijn stappen van tijd dat we moeten gebruiken 
## Uw y coordinaten zijn uw waarden van uw bitcoin, je moet uw bitcoin waarden zorgen dat ze van -1 tot 1 gaan in plaats van 0 tot 100
## Je wilt ze delen door 100 want je wilt dat van 0 tot 1 gaat en van al uw waarden - 0.8 zodat uw grafiek meer naar beneden is 
##Een array maken van uw bitcoin om deze waarden dan te kunnen gebruiken in uw plot

###Je maakt een array van uw numpy random normal bitcoin en dat /100 en - 0.8, dit is uw Y 
### Uw x is uw time en dit moet je doen met count en dit berekenen zodat dit past in de afstand van 1.6 dus ik denk /50 en dan nog - 0.8 dat het beide begint bij 



#while bitcoin <= 100:     ##Zodat het gaat van 0 tot honderd
#    bitcoin += numpy.random.normal(mean, sd, size = None)*bitcoin 
#    array_bitcoin = (numpy.array([bitcoin]))
#    
#    #voor uw for loop te definiëren
#    count += 1
#    counter = count
#    
#    
#    # /100 en /50 zodat het tussen 0 en 1 is en dan - 0.8 zodat het tussen -0.8 en 0.8 is 
#    y_bitcoin = (((numpy.random.normal(array_bitcoin))/100)-0.8)
#    x_bitcoin = numpy.array([count/50 -0.8])
#    
#    #zodat je uw coördinaten hebt
#    x_y = numpy.vstack([x_bitcoin, y_bitcoin])
#    print(x_y)
#
#    for i in range (counter):
#        plot_bitcoin = visual.ShapeStim(win, vertices = x_y[i,i], lineColorSpace = (1, red_making, red_making), autoDraw = True)
#        plot_bitcoin.draw()
#        win.flip()
#        time.sleep(1)
#
#win.close()








