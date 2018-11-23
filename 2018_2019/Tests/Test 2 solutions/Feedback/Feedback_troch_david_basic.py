#importeren

from psychopy import visual
import time


#scherm aanmaken

win = visual.Window(size = [600,600], color ="black", units = "norm")

#STATIONAIR ZONNESTELSEL

#hemellichamen initialiseren
straalzon = 0.15
zon = visual.Circle(win, radius = straalzon, fillColor = "yellow", lineColor = "yellow")
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
planeet = visual.Circle(win, radius = 0.07, fillColor = "blue", lineColor = "blue", pos = (0.705,0.236))
maan = visual.Circle(win, radius = 0.02, fillColor = "white", lineColor = "white", pos = (0.707, 0.356))

#hemellichamen tekenen en tonen
zon.draw()
planeet.draw()
maan.draw()

win.flip()
time.sleep(1)


#VAN GELE ZON TOT RODE REUS

#straal zon doen toenemen


sizes = [0.15,0.1545,0.159135,0.16390905,0.16882632150000002,0.17389111114500003,0.17910784447935002,0.18448107981373052,0.19001551220814245,0.19571597757438672,0.20158745690161833,0.2076350806086669,0.21386413302692692,0.22028005701773473,0.22688845872826677,0.23369511249011476,0.2407059658648182,0.24792714484076275,0.2553649591859856,0.2630259079615652,0.2709166852004122,0.27904418575642453,0.2874155113291173,0.29603797666899084,0.3049191159690606,0.3140666894481324,0.32348869013157633,0.33319335083552365,0.34318915136058936,0.35348482590140706,0.36408937067844926,0.37501205179880276,0.38626241335276684,0.39785028575334985,0.40978579432595036,0.4220793681557289,0.43474174920040076,0.4477840016764128,0.4612175217267052,0.47505404737850637,0.4893056687998616,0.5039848388638575,0.5191043840297732,0.5346775155506664,0.5507178410171865,0.567239376247702,0.5842565575351332,0.6017842542611872,0.6198377818890228,0.6384329153456936,0.6575859028060644,0.6773134798902464,0.6976328842869538,0.7185618708155624]
for i in sizes:
    zon = visual.Circle(win, radius = i, fillColor = "yellow", lineColor = "yellow")
    zon.draw()
    win.flip()
    planeet.draw()
    maan.draw()
time.sleep(5)



#kleur zon doen veranderen

#botsing detecteren




win.close()