# Python interprets / on integers as long division (e.g., 7/2 = 3).
# If you don't like it, you can import a different definition of division as follows:
from __future__ import division
print(7/2) # becomes standard division
print(7//2.0) # remains long division