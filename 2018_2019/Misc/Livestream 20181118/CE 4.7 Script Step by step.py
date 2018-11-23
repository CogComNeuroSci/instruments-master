from psychopy import visual
import numpy as np
import time

#define window
win=visual.Window(size=[600,400], color="black")

#we definieren alle variabelen
bitcoin1= 1
count=0
waardes1= [1]
xstep=0
ystep=0
aantalysteps=0
punten1= []
lijstcolor=[]
colorstep= 0

#ver4dubbeld
bitcoin2= 1
waardes2= [1]
punten2= []

bitcoin3= 1
waardes3= [1]
punten3= []

bitcoin4= 1
waardes4= [1]
punten4= []

#we gebruiken count om te tellen hoeveel keer we door de loop gaan en hoeveel punten er op de grafiek moeten komen

while bitcoin1<=100 and bitcoin2<=100 and bitcoin3<=100 and bitcoin4<=100:
    count+=1
    bitcoin1+= np.random.normal(loc=.1, scale=0.025, size= 1)*bitcoin1
    waardes1.append(bitcoin1[0]) #bitcoin is een array, we willen het element uit deze array: daarom index 0
    bitcoin2+= np.random.normal(loc=.1, scale=0.025, size= 1)*bitcoin2
    waardes2.append(bitcoin2[0]) #bitcoin is een array, we willen het element uit deze array: daarom index 0
    bitcoin3+= np.random.normal(loc=.1, scale=0.025, size= 1)*bitcoin3
    waardes3.append(bitcoin3[0]) #bitcoin is een array, we willen het element uit deze array: daarom index 0
    bitcoin4+= np.random.normal(loc=.1, scale=0.025, size= 1)*bitcoin4
    waardes4.append(bitcoin4[0]) #bitcoin is een array, we willen het element uit deze array: daarom index 0


xstep=1.6/ count
colorstep=2/count
aantalysteps=max(bitcoin1[-1], bitcoin2[-1], bitcoin3[-1], bitcoin4[-1])-1 #we doen -1 omdat onze startwaarde 1 is --> herleiden naar 0 
ystep= 1/aantalysteps

#we maken een lijst met tupples die de coordinaten van de punten bevatten
for waarde in range(count):
    x= xstep* waarde -0.8
    y1=ystep*waardes1[waarde] -0.5
    y2=ystep*waardes2[waarde]-0.5
    y3=ystep*waardes3[waarde]-0.5
    y4=ystep*waardes4[waarde]-0.5
    punten1.append((x,y1))
    punten2.append((x,y2))
    punten3.append((x,y3))
    punten4.append((x,y4))
    col=colorstep*(-waarde) + 1 #wit is 1 dus bij waarde = nul zal col 1 zijn
    lijstcolor.append(col)


#voor iedere waarde: lijnstuk
for punt in range(1, count+1):
    
    for coord in range(1,len(punten1[0:punt+1])):
        lijnstuk1=visual.Line(win, start=punten1[coord-1], end=punten1[coord], lineColor=[lijstcolor[coord-1],1,1])
        lijnstuk1.draw()
        lijnstuk2=visual.Line(win, start=punten2[coord-1], end=punten2[coord], lineColor=[1, lijstcolor[coord-1],1])
        lijnstuk2.draw()
        lijnstuk3=visual.Line(win, start=punten3[coord-1], end=punten3[coord], lineColor=[1, 1, lijstcolor[coord-1]])
        lijnstuk3.draw()
        lijnstuk4=visual.Line(win, start=punten4[coord-1], end=punten4[coord], lineColor=[1, lijstcolor[coord-1], lijstcolor[coord-1]])
        lijnstuk4.draw()
        bitcoinwaarde= visual.TextStim(win, text="{0} euro, {1} euro, \n{2} euro, {3} euro".format(int(waardes1[punt]), int(waardes2[punt]), int(waardes3[punt]), int(waardes4[punt])),pos=(0,0.8))
        bitcoinwaarde.draw()
    win.flip()
time.sleep(5)
win.close()


#plot gaat van -0.8, -0.8, --> breedte 1.6
# hoogte: we hebben waarden van 1 tot 100 --> we gebruiken hoogte van 1
#van elk van de waarden 0,4 aftrekken
#we moeten van bitcoinwaarde naar coordinaat omzetten
#lijst of array hebben met alle waarden
