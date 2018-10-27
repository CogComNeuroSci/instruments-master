class animal(object):
    """a more sophisticated animal class; animals now have a name, species, and children. Name and species are expected on initialization. """
    def __init__(self,name,species):
        self.name = name
        self.species = species
        self.children = list()
        
    def baby(self,name):
        self.children.append(name)


Max = animal("Max", "lion")

# inspect properties
print(Max.species)

# add properties (not optimal way)
Max.children = ["Imal"]

# add property (more optimal way)
Max.baby("Imal")
Max.baby("Happiness")

# inspect properties
print(Max.children)