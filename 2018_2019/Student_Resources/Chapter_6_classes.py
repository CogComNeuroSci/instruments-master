# animal class; code to illustrate the core concepts of class and object in Python

class animal(object):
    """an elementary animal class; animals have a name, species, and children. Name and species are expected on initialization. """
    def __init__(self,name,species):    # what happens on constructing a new animal object
        self.name = name
        self.species = species
        self.children = list()
    def baby(self,name):                # a function to grow the family
        self.children.append(name)
    def __str__(self):                  # a function to give nice output when you do print(object)
        return self.name

# now try it out
Max = animal("Max","lion")
print(Max.species)
Max.baby("Imal")
Max.baby("Happiness")
print(Max)                              # here the function __str__ is used
print(Max.children)
print(type(Max.children))               # this is of course a list of children
print(animal.__doc__)                   # print the docstring attached to class animal
print(dir(animal))                      # all the attributes of class animal; note that many attributed are inherited; only attributed baby is brand new