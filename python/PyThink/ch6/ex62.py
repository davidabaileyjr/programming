# github/pythink
# ex62.py

import math

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	# print 'dx is', dx
	# print 'dy is', dy
	dsquared = dx**2 + dy**2
	# print 'dsquared is: ', dsquared
	result = math.sqrt(dsquared)
	# print result
	
distance(1,2,4,6)

'''Use incremental development to write function
called HYPOTENUSE that returns length of right triangle
given length of two legs as arquement.'''

def hypotenuse(l1, l2):
	h = math.sqrt(l1**2 + l2**2)
	return h

hypotenuse(3,4)