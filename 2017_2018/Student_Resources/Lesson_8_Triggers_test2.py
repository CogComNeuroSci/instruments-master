from psychopy import core

port=0XBC00
windll.inpout32.Out32(port,0)

for i in range(256):

#    #windll.inpout32.Out32(port,i)
#    #core.wait(.03)
#    #windll.inpout32.Out32(port,0)
    print(str(i))