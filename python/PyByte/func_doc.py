# python/pybyte/
# Filename: func_doc.py

def printMax(x, y):
	''' Prints the maxium of two numbers.
	
	The two values must be integers.'''
	x = int(x) # conver to integers, if possible
	y = int(y)
	
	if x > y:
		print(x, 'is maximum')
	else:
		print(y, 'is maximum')
		
printMax(3, 5)
print(printMax.__doc__)

help(printMax)
