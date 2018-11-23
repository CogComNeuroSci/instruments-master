# displaying Stroop stimuli

# import modules
import numpy

# we start with adding the values for the words and the colors
ColorWord   = numpy.array([ "red", "red", "red", "red",
                            "blue", "blue", "blue", "blue",
                            "green", "green", "green", "green",
                            "yellow", "yellow", "yellow", "yellow"])
FontColor   = numpy.array([ "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow"])

# deduce the congruence
CongruenceLevels = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean = []
for i in range(len(FontColor)):
    CongruenceBoolean.append(ColorWord[i] == FontColor[i])

print(type(CongruenceLevels))
print(type(CongruenceBoolean))

# do you see what is going wrong here?
# do you understand why?
print(CongruenceBoolean*1)

#Congruence = CongruenceLevels[[CongruenceBoolean*1]]

#  File "C:\Users\esther\Downloads\CE 3.9_FAQ_derived properties_mixing.py", line 27, in <module>
#    Congruence = CongruenceLevels[[CongruenceBoolean*1]]
#IndexError: boolean index did not match indexed array along dimension 0; dimension is 2 but corresponding boolean dimension is 16