# a class-y script
# to illustrate classes and class inheritance (IEP course Chapter 6)
# Tom Verguts, July 2023

# Import modules
from psychopy import visual, event, core, gui, data
import time

class boxed_stimulus(object):
    """this defines a text object that can be boxed"""
    def __init__(self, win, text, color, draw_box = True):
        self.text  = text
        self.color = color
        self.stim  = visual.TextStim(win, text = self.text, color = self.color)
        self.draw_box = draw_box
        self.n_letter = len(self.text)
        if self.draw_box: # make a box
            width    = self.n_letter*0.07
            height   = 0.10
            self.box = visual.rect.Rect(win, size = (width, height), lineColor = "white", fillColor = None)
    def draw(self):
        self.stim.draw()
        if self.draw_box:
            self.box.draw()
        win.flip()

class boxed_stimulus_extra(boxed_stimulus):
    """a slightly more advanced stimulus class;
    it inherits all the properties from boxed_stimulus,
    but you can choose to draw no, 1, or 2 boxes around it"""    
    def __init__(self, win, text, color, n_box = 0):
        super().__init__(win, text, color) # start with the superclass (boxed_stimulus) initialization
        self.n_box = n_box
        if not self.n_box:
            self.draw_box = False
        if self.n_box > 1: # make a second box
            width    = self.n_letter*0.07 + 0.05
            height   = 0.10 + 0.05
            self.box2 = visual.rect.Rect(win, size = (width, height), lineColor = "white", fillColor = None)
    def draw(self):
        if self.n_box > 1:
            self.box2.draw()
        super().draw() # take the drawing functionality of boxed_stimulus

if __name__ == "__main__": # this is to avoid that the code below is run when the objects are imported in another script
    win = visual.Window(size = (800, 800), units = 'norm', color = 'black')

    s1 = boxed_stimulus(win, text = "hello", color = "green", draw_box = True)
    s2 = boxed_stimulus_extra(win, text = "do you feel boxed?", color = "red", n_box = 2)

    s1.draw()
    time.sleep(1)
    s2.draw()
    time.sleep(1)
    win.close()