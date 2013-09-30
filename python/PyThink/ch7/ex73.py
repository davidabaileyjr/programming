# github/edu/pythink/ch7
# ex73.py

def countdown(n):
	while n > 0:
		print n
		n = n - 1
	print 'Blastoff!'
	
countdown(10)

def sequence(n):
	while n != 1:
		print n,
		if n % 2 == 0: # n is even
			n = n / 2
		else: # n is odd
			n = n * 3 + 1
			
sequence(53)