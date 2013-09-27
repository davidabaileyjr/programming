# github/pythink
# ex64_bool_func.py

'''def is_divisible(x, y):
	if x % y == 0:
		return True
	else:
		return False
		
is_divisible(6, 3)'''

# REFACTORING

def is_divisible(x, y):
	return x % y == 0
	if is_divisible(x, y):
		print 'x is divisible by y'

is_divisible(6, 3)