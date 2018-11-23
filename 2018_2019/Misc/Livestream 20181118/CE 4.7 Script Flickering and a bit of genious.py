#begin bitcoin(14/11/18)

#Import modules

from psychopy import visual, monitors, core, event
import time, numpy


#Screen

mon = monitors.Monitor("my laptop screen")
mon.setDistance(40)
mon.setWidth (38)
mon.setSizePix((1536,864))

win = visual.Window(fullscr = True , color = 'black', units = 'norm', monitor = mon)

for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)


#Duration

duration = 0.2


#Teller
teller = visual.TextStim(win, text='', color = 'white', pos = (-0.5,0.6))
counter = 1
rotaties = 0

#Graph
start1= -0.9
start2 =-0.9
startP= (start1, start2)
end1 = -0.8
end2 = -0.9
endP= (end1, end2)

graf = visual.Line(win, start= (startP), end= (endP))
graf.setColor((1,0,0) ,'rgb')


#Teller2
teller2 = visual.TextStim(win, text='', color = 'white', pos = (0.5,0.6))
counter2 = 1
rotaties2 = 0

#Graph2
start12= -0.9
start22 =-0.9
startP2= (start12, start22)
end12 = -0.8
end22 = -0.9
endP2= (end12, end22)

graf2 = visual.Line(win, start= (startP2), end= (endP2))

graf2.setColor((0,1,0) ,'rgb')


#Teller3
teller3 = visual.TextStim(win, text='', color = 'white', pos = (-0.5,0.4))
counter3 = 1
rotaties3 = 0

#Graph3
start13= -0.9
start23 =-0.9
startP3= (start13, start23)
end13 = -0.8
end23 = -0.9
endP3= (end13, end23)

graf3 = visual.Line(win, start= (startP3), end= (endP3))

graf3.setColor((0,1,0) ,'rgb')


#Teller4
teller4 = visual.TextStim(win, text='', color = 'white', pos = (0.5,0.4))
counter4 = 1
rotaties4 = 0


#Graph4
start14= -0.9
start24 =-0.9
startP4= (start14, start24)
end14 = -0.8
end24 = -0.9
endP4= (end14, end24)

graf4 = visual.Line(win, start= (startP4), end= (endP4))

graf4.setColor((0,1,1) ,'rgb')



#Display
uitleg = visual.TextStim(win, text = 'Current bitcoin value:', pos = (0,0.75))
uitleg.autoDraw = True

while counter < 100:
    counter+= (counter*numpy.random.normal(loc = 0.1, scale = 0.025, size=None))     ##van Helena
    counter2+= (counter2*numpy.random.normal(loc = 0.1, scale = 0.025, size=None))
    counter3+= (counter3*numpy.random.normal(loc = 0.1, scale = 0.025, size=None))
    counter4+= (counter4*numpy.random.normal(loc = 0.1, scale = 0.025, size=None))
    teller.text= ('{:.2f} euro'.format(counter))     ##.2f voor 2 getallen na komma want kleiner gaan centen niet
    teller2.text= ('{:.2f} euro'.format(counter2))
    teller3.text= ('{:.2f} euro'.format(counter3))
    teller4.text= ('{:.2f} euro'.format(counter4))
    teller.draw()
    teller2.draw()
    teller3.draw()
    teller4.draw()
    graf = visual.Line(win, start= (start1,start2), end= (end1,end2))
    graf2 = visual.Line(win, start= (start12,start22), end= (end12,end22))
    graf3 = visual.Line(win, start= (start13,start23), end= (end13,end23))
    graf4 = visual.Line(win, start= (start14,start24), end= (end14,end24))
    graf.setColor((1,0,0) ,'rgb')
    graf2.setColor((0,1,0) ,'rgb')
    graf3.setColor((0,0,1) ,'rgb')
    graf4.setColor((0,1,1) ,'rgb')
    graf.color = [1,1-(counter*0.02),1-(counter*0.02)]   ##van Hélène
    graf2.color = [1-(counter2*0.02),1,1-(counter2*0.02)]
    graf3.color = [1-(counter3*0.02),1-(counter3*0.02),1]
    graf4.color = [1-(counter4*0.02),1,1]
    graf.autoDraw = True
    graf2.autoDraw = True
    graf3.autoDraw = True
    graf4.autoDraw = True
    start2 = end2
    start1 = end1
    end2+= counter*0.001
    end1+= rotaties*0.001
    start22 = end22
    start12 = end12
    end22+= counter2*0.001
    end12+= rotaties2*0.001
    start23 = end23
    start13 = end13
    end23+= counter3*0.001
    end13+= rotaties3*0.001
    start24 = end24
    start14 = end14
    end24+= counter4*0.001
    end14+= rotaties4*0.001
    win.flip()
    time.sleep(duration)
    rotaties2 += 1
    win.flip()
    time.sleep(duration)
    rotaties += 1

print(rotaties)


#End

    ##als al de rest niet zichtbaar is maar het einde wel, weet ik dat het tot hier werkte maar onzichtbaar
einde = visual.TextStim(win, text = "Dag en bedankt", pos = (0,0.75), height = 0.2)
uitleg.autoDraw = False
graf.autoDraw = False
graf2.autoDraw = False
graf3.autoDraw = False
graf4.autoDraw = False

einde.draw()
win.flip()
time.sleep(1)


#Stilletjes afsluiten

win.close()
