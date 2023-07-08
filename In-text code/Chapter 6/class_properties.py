# illustration of some object properties
# Tom Verguts, July 2023

from psychopy import visual
from classy import boxed_stimulus # import our boxed_stimulus class

win = visual.Window(size = (800, 800), units = 'norm', color = 'black')
s1 = boxed_stimulus(win, text = "hello", color = "green", draw_box = True)

print(s1.color)
print(type(s1))
print(s1.__doc__)   # print the docstring attached to class boxed_stimulus
print(dir(s1))      # all the attributes of class boxed_stimulus; note that many attributed are inherited