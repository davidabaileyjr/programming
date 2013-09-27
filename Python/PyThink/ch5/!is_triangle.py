# github/pythink
# is_triangle.py

def is_triangle(a, b, c):
	if a + b >= c:
		if b + c >= a:
			if a + c >= b:
				print 'yes'
	else:
		print 'no'
	
is_triangle(2, 3, 8)

'''Receive input from users, convert to integers...
and check whether yes or no.'''