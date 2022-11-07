# Importing modules
import numpy

# Initialize variables
start_value     = 1
end_value       = 100
value           = start_value
mean            = 0.10
sd              = 0.025

# Initialize array to track the four values over time
value_array = numpy.array([value, value, value, value])

# first pass through the while loop
## adjust all four values
## we sample from the normal distribution with mean 0.10 and sd 0.025
adjustment = numpy.random.normal(loc = mean, scale = sd, size = 4)

## update the current value
value = value + adjustment*value

## append the current value to the list
value_array = numpy.vstack([value_array, value])

# set the f and i value
f = 0
i = 1

# first print the most nested part
print(value_array[i,f])

# then grow the code from the inside to the outside
print(                  value_array[i,f]                        )
print(          round(  value_array[i,f]    )                   )
print(          round(  value_array[i,f]    )   /50             )
print(      (   round(  value_array[i,f]    )   /50     )-1     )
print(  -(  (   round(  value_array[i,f]    )   /50     )-1)    )

# check if this is the same as in one go
adjusted_color = -((round(value_array[i,f])/50)-1)
print(adjusted_color)