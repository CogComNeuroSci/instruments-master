##waarden die veranderen
##grafische component
##tijdsverloop
## --> 3 grote delen van deze oefening die apart moeten bekeken worden en die samen 1 grote structuur zullen vormen 
##neem loop structuur als laatste, zoek eerst het grafische en de waarden uit

##########################
##WAARDEN DIE VERANDEREN##
##########################
import numpy

from psychopy import visual
import time
win = visual.Window(size = [800,600], units = "norm")


i=1
count = 0
while i < 100:
    # Esther: the author already found a good way to implement the color transition in the rgb code
    bitcoinwaarde = visual.TextStim(win, text = "{0} euro".format(round(i,2)), pos = (0,0.5), color = [1,1-(i*0.02),1-(i*0.02)])
    # Esther: instead of having to limit the color values when the bitcoin value overshoots, the while-loop and position withing the while-loop are used as protection
    # Esther: if the following bitcoin update would lead to a value higher than 100 it doesn't matter because the line is already drawn
    # Esther: it is unclear however whether this approach will remain valid as the rest of the assignment is executed.
    i += i * numpy.random.normal(loc=0.10, scale=0.025, size=None)
    bitcoinwaarde.draw()
    win.flip()
    time.sleep(0.01)
    count += 1
print(count)


#######################
##GRAFISCHE COMPONENT##
#######################

##hierboven gebruiken we count om te tellen hoe vaak we door de loop gaan en dus hoeveel punten we op de grafiek moeten uitzetten aka 
##het aantal knikjes in de grafiek
##grafiek bestaat uit y-waarden die de bitcoin value weergeven, namelijk i, en de x-waarden weerspiegelen het tijdsverloop of de count

##vertices en append commando's 