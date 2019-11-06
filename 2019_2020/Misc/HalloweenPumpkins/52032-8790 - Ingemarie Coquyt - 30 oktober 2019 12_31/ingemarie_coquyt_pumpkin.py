#importing modules
from psychopy import visual
import time

#make window
win = visual.Window(fullscr=True, units="norm", color="#29220A")



x=0.2
#make pumpkin
pum1=visual.Circle(win,radius=0.5,pos=(-x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum1.draw()

pum3=visual.Circle(win,radius=0.5,pos=(x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum3.draw()

pum2=visual.Circle(win,radius=0.5,pos=(0,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum2.draw()

#pumpkin stem
vertStem=[(-0.05,0.6),(-0.05,0.7),(0,0.8),(0.1,0.9),(0.2,0.8),(0.12,0.82),(0.1,0.8),(0.03,0.7),(.05,0.6)]
stem=visual.ShapeStim(win,vertices=vertStem, fillColor="#0B3B0B",lineColor="#264d00")
stem.draw()

#eyes
vertEye1=[(-0.3,0.4),(-0.2,0.2),(-0.05,0.3)]
eye1=visual.ShapeStim(win, vertices=vertEye1, fillColor= "#ff9630",lineColor="#b34700")
eye1.draw()

vertEye2=[(0.3,0.4),(0.2,0.2),(0.05,0.3)]
eye2=visual.ShapeStim(win, vertices=vertEye2,fillColor= "#ff9630",lineColor="#b34700")
eye2.draw()

#mouth
vertMouth=[(-0.4,0.1),(-0.25,-0.1),(-0.2,-0.05),(-0.1,-0.15),(0,-0.05),(0.1,-0.15),(0.2,-0.05),(0.25,-0.1),(0.4,0.1),(0.25,-0.02),(0.2,0.05),(0.1,-0.02),(0,0.05),(-0.1,-0.02),(-0.2,0.05),(-0.25,-0.02)]
mouth=visual.ShapeStim(win,vertices=vertMouth,fillColor="#ff9630",lineColor="#b34700")
mouth.draw()

#text
halloween=visual.TextStim(win,text="Happy Halloween!",font="Chiller",pos=(0,-0.6),height=0.2,color="#00ff00")
halloween.draw()


win.flip()
time.sleep(1)




#flash after 1 second, no text
x=0.2
#make pumpkin
pum1=visual.Circle(win,radius=0.5,pos=(-x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum1.draw()

pum3=visual.Circle(win,radius=0.5,pos=(x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum3.draw()

pum2=visual.Circle(win,radius=0.5,pos=(0,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum2.draw()

#pumpkin stem
vertStem=[(-0.05,0.6),(-0.05,0.7),(0,0.8),(0.1,0.9),(0.2,0.8),(0.12,0.82),(0.1,0.8),(0.03,0.7),(.05,0.6)]
stem=visual.ShapeStim(win,vertices=vertStem, fillColor="#0B3B0B",lineColor="#264d00")
stem.draw()

#eyes
vertEye1=[(-0.3,0.4),(-0.2,0.2),(-0.05,0.3)]
eye1=visual.ShapeStim(win, vertices=vertEye1, fillColor= "#ff9630",lineColor="#b34700")
eye1.draw()

vertEye2=[(0.3,0.4),(0.2,0.2),(0.05,0.3)]
eye2=visual.ShapeStim(win, vertices=vertEye2,fillColor= "#ff9630",lineColor="#b34700")
eye2.draw()

#mouth
vertMouth=[(-0.4,0.1),(-0.25,-0.1),(-0.2,-0.05),(-0.1,-0.15),(0,-0.05),(0.1,-0.15),(0.2,-0.05),(0.25,-0.1),(0.4,0.1),(0.25,-0.02),(0.2,0.05),(0.1,-0.02),(0,0.05),(-0.1,-0.02),(-0.2,0.05),(-0.25,-0.02)]
mouth=visual.ShapeStim(win,vertices=vertMouth,fillColor="#ff9630",lineColor="#b34700")
mouth.draw()

win.flip()
time.sleep(0.5)



#flash after 0.5 seconds, text
x=0.2
#make pumpkin
pum1=visual.Circle(win,radius=0.5,pos=(-x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum1.draw()

pum3=visual.Circle(win,radius=0.5,pos=(x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum3.draw()

pum2=visual.Circle(win,radius=0.5,pos=(0,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum2.draw()

#pumpkin stem
vertStem=[(-0.05,0.6),(-0.05,0.7),(0,0.8),(0.1,0.9),(0.2,0.8),(0.12,0.82),(0.1,0.8),(0.03,0.7),(.05,0.6)]
stem=visual.ShapeStim(win,vertices=vertStem, fillColor="#0B3B0B",lineColor="#264d00")
stem.draw()

#eyes
vertEye1=[(-0.3,0.4),(-0.2,0.2),(-0.05,0.3)]
eye1=visual.ShapeStim(win, vertices=vertEye1, fillColor= "#ff9630",lineColor="#b34700")
eye1.draw()

vertEye2=[(0.3,0.4),(0.2,0.2),(0.05,0.3)]
eye2=visual.ShapeStim(win, vertices=vertEye2,fillColor= "#ff9630",lineColor="#b34700")
eye2.draw()

#mouth
vertMouth=[(-0.4,0.1),(-0.25,-0.1),(-0.2,-0.05),(-0.1,-0.15),(0,-0.05),(0.1,-0.15),(0.2,-0.05),(0.25,-0.1),(0.4,0.1),(0.25,-0.02),(0.2,0.05),(0.1,-0.02),(0,0.05),(-0.1,-0.02),(-0.2,0.05),(-0.25,-0.02)]
mouth=visual.ShapeStim(win,vertices=vertMouth,fillColor="#ff9630",lineColor="#b34700")
mouth.draw()

#text
halloween=visual.TextStim(win,text="Happy Halloween!",font="Chiller",pos=(0,-0.6),height=0.2,color="#00ff00")
halloween.draw()

win.flip()
time.sleep(0.5)


#flash after 0.5 seconds, no text
x=0.2
#make pumpkin
pum1=visual.Circle(win,radius=0.5,pos=(-x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum1.draw()

pum3=visual.Circle(win,radius=0.5,pos=(x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum3.draw()

pum2=visual.Circle(win,radius=0.5,pos=(0,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum2.draw()

#pumpkin stem
vertStem=[(-0.05,0.6),(-0.05,0.7),(0,0.8),(0.1,0.9),(0.2,0.8),(0.12,0.82),(0.1,0.8),(0.03,0.7),(.05,0.6)]
stem=visual.ShapeStim(win,vertices=vertStem, fillColor="#0B3B0B",lineColor="#264d00")
stem.draw()

#eyes
vertEye1=[(-0.3,0.4),(-0.2,0.2),(-0.05,0.3)]
eye1=visual.ShapeStim(win, vertices=vertEye1, fillColor= "#ff9630",lineColor="#b34700")
eye1.draw()

vertEye2=[(0.3,0.4),(0.2,0.2),(0.05,0.3)]
eye2=visual.ShapeStim(win, vertices=vertEye2,fillColor= "#ff9630",lineColor="#b34700")
eye2.draw()

#mouth
vertMouth=[(-0.4,0.1),(-0.25,-0.1),(-0.2,-0.05),(-0.1,-0.15),(0,-0.05),(0.1,-0.15),(0.2,-0.05),(0.25,-0.1),(0.4,0.1),(0.25,-0.02),(0.2,0.05),(0.1,-0.02),(0,0.05),(-0.1,-0.02),(-0.2,0.05),(-0.25,-0.02)]
mouth=visual.ShapeStim(win,vertices=vertMouth,fillColor="#ff9630",lineColor="#b34700")
mouth.draw()

win.flip()
time.sleep(0.5)


#flash after 0.5 seconds, text
x=0.2
#make pumpkin
pum1=visual.Circle(win,radius=0.5,pos=(-x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum1.draw()

pum3=visual.Circle(win,radius=0.5,pos=(x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum3.draw()

pum2=visual.Circle(win,radius=0.5,pos=(0,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum2.draw()

#pumpkin stem
vertStem=[(-0.05,0.6),(-0.05,0.7),(0,0.8),(0.1,0.9),(0.2,0.8),(0.12,0.82),(0.1,0.8),(0.03,0.7),(.05,0.6)]
stem=visual.ShapeStim(win,vertices=vertStem, fillColor="#0B3B0B",lineColor="#264d00")
stem.draw()

#eyes
vertEye1=[(-0.3,0.4),(-0.2,0.2),(-0.05,0.3)]
eye1=visual.ShapeStim(win, vertices=vertEye1, fillColor= "#ff9630",lineColor="#b34700")
eye1.draw()

vertEye2=[(0.3,0.4),(0.2,0.2),(0.05,0.3)]
eye2=visual.ShapeStim(win, vertices=vertEye2,fillColor= "#ff9630",lineColor="#b34700")
eye2.draw()

#mouth
vertMouth=[(-0.4,0.1),(-0.25,-0.1),(-0.2,-0.05),(-0.1,-0.15),(0,-0.05),(0.1,-0.15),(0.2,-0.05),(0.25,-0.1),(0.4,0.1),(0.25,-0.02),(0.2,0.05),(0.1,-0.02),(0,0.05),(-0.1,-0.02),(-0.2,0.05),(-0.25,-0.02)]
mouth=visual.ShapeStim(win,vertices=vertMouth,fillColor="#ff9630",lineColor="#b34700")
mouth.draw()

#text
halloween=visual.TextStim(win,text="Happy Halloween!",font="Chiller",pos=(0,-0.6),height=0.2,color="#00ff00")
halloween.draw()

win.flip()
time.sleep(0.5)


#flash after 0.5 seconds, no text
x=0.2
#make pumpkin
pum1=visual.Circle(win,radius=0.5,pos=(-x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum1.draw()

pum3=visual.Circle(win,radius=0.5,pos=(x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum3.draw()

pum2=visual.Circle(win,radius=0.5,pos=(0,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum2.draw()

#pumpkin stem
vertStem=[(-0.05,0.6),(-0.05,0.7),(0,0.8),(0.1,0.9),(0.2,0.8),(0.12,0.82),(0.1,0.8),(0.03,0.7),(.05,0.6)]
stem=visual.ShapeStim(win,vertices=vertStem, fillColor="#0B3B0B",lineColor="#264d00")
stem.draw()

#eyes
vertEye1=[(-0.3,0.4),(-0.2,0.2),(-0.05,0.3)]
eye1=visual.ShapeStim(win, vertices=vertEye1, fillColor= "#ff9630",lineColor="#b34700")
eye1.draw()

vertEye2=[(0.3,0.4),(0.2,0.2),(0.05,0.3)]
eye2=visual.ShapeStim(win, vertices=vertEye2,fillColor= "#ff9630",lineColor="#b34700")
eye2.draw()

#mouth
vertMouth=[(-0.4,0.1),(-0.25,-0.1),(-0.2,-0.05),(-0.1,-0.15),(0,-0.05),(0.1,-0.15),(0.2,-0.05),(0.25,-0.1),(0.4,0.1),(0.25,-0.02),(0.2,0.05),(0.1,-0.02),(0,0.05),(-0.1,-0.02),(-0.2,0.05),(-0.25,-0.02)]
mouth=visual.ShapeStim(win,vertices=vertMouth,fillColor="#ff9630",lineColor="#b34700")
mouth.draw()

win.flip()
time.sleep(0.5)


#flash after 0.5 seconds, textx=0.2
#make pumpkin
pum1=visual.Circle(win,radius=0.5,pos=(-x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum1.draw()

pum3=visual.Circle(win,radius=0.5,pos=(x,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum3.draw()

pum2=visual.Circle(win,radius=0.5,pos=(0,0.1), edges=99,fillColor="#ff6600",lineColor="#e65c00",size=(0.7,1))
pum2.draw()

#pumpkin stem
vertStem=[(-0.05,0.6),(-0.05,0.7),(0,0.8),(0.1,0.9),(0.2,0.8),(0.12,0.82),(0.1,0.8),(0.03,0.7),(.05,0.6)]
stem=visual.ShapeStim(win,vertices=vertStem, fillColor="#0B3B0B",lineColor="#264d00")
stem.draw()

#eyes
vertEye1=[(-0.3,0.4),(-0.2,0.2),(-0.05,0.3)]
eye1=visual.ShapeStim(win, vertices=vertEye1, fillColor= "#ff9630",lineColor="#b34700")
eye1.draw()

vertEye2=[(0.3,0.4),(0.2,0.2),(0.05,0.3)]
eye2=visual.ShapeStim(win, vertices=vertEye2,fillColor= "#ff9630",lineColor="#b34700")
eye2.draw()

#mouth
vertMouth=[(-0.4,0.1),(-0.25,-0.1),(-0.2,-0.05),(-0.1,-0.15),(0,-0.05),(0.1,-0.15),(0.2,-0.05),(0.25,-0.1),(0.4,0.1),(0.25,-0.02),(0.2,0.05),(0.1,-0.02),(0,0.05),(-0.1,-0.02),(-0.2,0.05),(-0.25,-0.02)]
mouth=visual.ShapeStim(win,vertices=vertMouth,fillColor="#ff9630",lineColor="#b34700")
mouth.draw()

#text
halloween=visual.TextStim(win,text="Happy Halloween!",font="Chiller",pos=(0,-0.6),height=0.2,color="#00ff00")
halloween.draw()

win.flip()
time.sleep(10)


#close window
win.close()

