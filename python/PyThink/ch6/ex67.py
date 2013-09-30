# github/pythink
# ex67.py

def is_power(a, b):
	if a == 1 or (a/b == 1):
		result = True
	elif a % b == 0 and a != 0:
		result is_power( (a/b), b)
	else:
		result = False
	return result
	
print is_power(64,2)

# not working yet