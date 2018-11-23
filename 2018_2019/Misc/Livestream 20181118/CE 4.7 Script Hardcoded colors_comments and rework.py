from psychopy import visual
import time
import numpy

#window maken
win= visual.Window([600,400], color= (-1,-1,-1))

#beginwaarde van Bircoin vastleggen
Bitcoin=1

#de animatie moet tot 100 lopen dus while loop
while Bitcoin<100:
    # een getal uit een normaaldistributie nemen met gemiddelde 100 en standaarddeviatie 2.5
    add=numpy.random.normal(loc= 0.1,scale= 0.025, size= None)*Bitcoin
    # de bitcoinwaarde laten toenemen met het getal uit de normaalditstributie
    Bitcoin = Bitcoin + add
    
    #de kleur roder laten worden 
    c=-((Bitcoin/50)-1)
    #Bitcoin laten toenemen in output venster
    print(Bitcoin)
    #als de Bitcoin de waarde 100 heeft dan stopt het
    ## Esther: dit is een goede manier om edge cases te vermijden!
    if Bitcoin>100:
        break
    #de tekst in window laten verschijnen, {0:.3} om 3 cijfer te laten verschijnen
    tekst= visual.TextStim(win, text= "Current bitcoin value: \n {0:.3}".format(Bitcoin),pos=(0,0.8), color= (1,c,c))
    tekst.draw()
    
    ## Esther: hier wordt het dus moeilijk omdat je de kleurcode hebt gehardcode in plaats van via een berekening abstract te bepalen.
    ## Esther: je zal waarschijnlijk in de opgeloste oefeningen al gezien hebben hoe het eleganter kan.
    #grafiek maken
    if Bitcoin >=0:
        linea = [(-0.5, -0.5), (-0.4,-0.5)]
        a= visual.ShapeStim(win, vertices=linea, closeShape=False, lineWidth=2, pos=(-1, -1.2), ori=180,lineColor= (1,1,1))
        a.draw()
    if Bitcoin >=3:
        lineb = [(-0.5, -0.5), (-0.4,-0.49)]
        b= visual.ShapeStim(win, vertices=lineb, closeShape=False, lineWidth=2, pos=(-0.9, -1.19), ori=180,lineColor= (1,-0.05,-0.05))
        b.draw()
    if Bitcoin >= 6:
        linec = [(-.5, -0.50), (-0.4,-0.49)]
        c= visual.ShapeStim(win, vertices=linec, closeShape=False, lineWidth=2, pos=(-0.8, -1.18), ori=180,lineColor= (1,-0.2,-0.2))
        c.draw()
    if Bitcoin >=10:
        lined = [(-0.5, -0.5), (-0.4,-0.495)]
        d= visual.ShapeStim(win, vertices=lined, closeShape=False, lineWidth=2, pos=(-0.7, -1.175), ori=180,lineColor= (1,-0.3,-0.3))
        d.draw()
    if Bitcoin >=15:
        linee = [(-0.5, -0.5), (-0.4,-0.49)]
        e= visual.ShapeStim(win, vertices=linee, closeShape=False, lineWidth=2, pos=(-0.6, -1.165), ori=180,lineColor= (1,-0.4,-0.4))
        e.draw()
    if Bitcoin >=20:
        linef = [(-0.5, -0.5), (-0.4,-0.45)]
        f= visual.ShapeStim(win, vertices=linef, closeShape=False, lineWidth=2, pos=(-0.5, -1.115), ori=180,lineColor= (1,-0.5,-0.5))
        f.draw()
    if Bitcoin >= 30:
        lineg = [(-0.5, -0.5), (-0.4,-0.45)]
        g= visual.ShapeStim(win, vertices=lineg, closeShape=False, lineWidth=2, pos=(-0.4, -1.065), ori=180,lineColor= (1,-0.6,-.6))
        g.draw()
    if Bitcoin >=50:
        lineh = [(-0.5, -0.5), (-0.4,-0.40)]
        h= visual.ShapeStim(win, vertices=lineh, closeShape=False, lineWidth=2, pos=(-0.3, -0.965), ori=180,lineColor= (1,-0.7,-0.7))
        h.draw()
    if Bitcoin >=70:
        linei = [(-0.5, -0.5), (-0.3,-0.35)]
        i= visual.ShapeStim(win, vertices=linei, closeShape=False, lineWidth=2, pos=(-0.1, -0.815), ori=180,lineColor= (1,-0.8, -0.8))
        i.draw()
    if Bitcoin >=80:
        linej = [(-0.5, -0.5), (-0.4,-0.35)]
        j= visual.ShapeStim(win, vertices=linej, closeShape=False, lineWidth=2, pos=(0.0025, -0.664), ori=180,lineColor= (1,-0.9,-0.9))
        j.draw()
    if Bitcoin >=90:
        linek = [(-0.5, -0.5), (-0.4,-0.30)]
        k= visual.ShapeStim(win, vertices=linek, closeShape=False, lineWidth=2, pos=(0.10, -0.47), ori=180,lineColor= (1,-1,-1))
        k.draw()
    win.flip()
    time.sleep(0.1)

win.close()