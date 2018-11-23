#import modules 
from psychopy import visual
from psychopy import visual,event
import timeimport numpyfrom numpy import random

#initialize window
win = visual.Window(size = [600, 600], color = (-1,-1,-1), units = "norm")

#initialize variabeles
start_color_zon     = (1,1,-1)       ## yellow
start_radius_zon    = 0.15     ## 15% van de breedte/hoogte gedeeld door 2, want straal: dus blijft zelfde: *2/2 
radius_planeet      = 0.07      ## 7% van de breedte/hoogte gedeeld door 2, want straal: dus blijft zelfde: *2/2 
radius_maan         = 0.02      ## 2% van de breedte/hoogte geedeeld door 2, want straal: dus blijft zelfde: *2/2 
start_cor_planeet   = (0.705, 0.236)
start_cor_maan      = (0.707, 0.356)
planeet_geraakt = 1
maan_geraakt = 1


#visual stimuli
##zon
zon      = visual.Circle(win, color = start_color_zon, radius = start_radius_zon, pos = (0,0))
##planeet
planeet  = visual.Circle(win, color = (-1,-1,1), radius = radius_planeet, pos = start_cor_planeet)
##maan
maan     = visual.Circle(win, color = (1,1,1), radius = radius_maan, pos = start_cor_maan)

#display startscherm voor 1 seconde
zon.draw()
planeet.draw()
maan.draw()
win.flip()
time.sleep(1)


#groeiende zon
sizes = numpy.array([0.15, 0.1545, 0.1591, 0.1639, 0.1688, 0.1739, 0.1791, 0.1845, 0.19, 0.1957, 0.2016, 0.2076, 0.2139, 0.2479, 0.2554, 0.2630, 0.2709, 0.2791, 0.2874, 0.2960, 0.3049, 0.3141, 0.3239, 0.337, 0.3437, 0.3539, 0.3646, 0.3755, 0.3868,0.3984, 0.41035, 0.4227, 0.4354, 0.4484, 0.4619, 0.4757, 0.49, 0.5047, 0.5198, 0.5354, 0.5515, 0.568, 0.5851, 0.6026, 0.6207,0.6393,0.6585,0.6782,0.6959,0.7196,0.7411,0.7634,0.7863,0.8099,0.8099,0.8342,0.8592])

#adjust color van [1,1,0] naar [1,-1,-1]
#blue = -((numpy.ndarray.round(sizes)/30)-1)
#green = -((numpy.ndarray.round(sizes)/60)-1)
#if blue < -1:
#    blue = -1
#if green < -1:
#    green = -1

for i in sizes:
    groeiende_zon = visual.Circle(win, fillColor = (1, 1 , -1), radius = i, pos = (0,0)) #fillColor = (1, blue, green)
    groeiende_zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.05)

#botsing
if planeet_geraakt==0 and maan_geraakt == 0:
    reactie = "Geen enkele van de hemellichamen heeft de rode reus geraakt!"
elif planeet_geraakt ==1 and maan_geraakt ==1:    reactie = "De planeet en de maan hebben de rode reus allebei geraakt!"elif planeet_geraakt ==1 and maan_geraakt ==0:    reactie = "De planeet heeft de rode reus geraakt!"else:    reactie = "De maan heeft de rode reus!"

#display reactie op botsing
reactie_text = visual.TextStim(win,text=reactie)
reactie_text.draw()win.flip()
time.sleep(1)

#close window
win.close()
