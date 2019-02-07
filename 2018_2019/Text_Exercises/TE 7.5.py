import numpy

# Make a simple array
x = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Export as a tab separated file
numpy.savetxt('output_tab.txt', x, fmt='%.0d', delimiter = '\t') 

# Export as a comma separated file
numpy.savetxt('output_comma.txt', x, fmt='%.0d', delimiter = ',') 
