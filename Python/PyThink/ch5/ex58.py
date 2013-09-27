# github/pythink
# ex58.py

def countdown(n):
	if n <= 0:
		print 'BlastOff!'
	else:
		print n
		countdown(n-1)
		
countdown(10)

def print_n(s, n):
	if n <= 0:
		return
	print s
	print_n(s, n-1)
	
print_n('david', 5)

''' Create a function that takes object and number
as arguements and calls the function n times.

def do_n():
	print_n()
	print_n()
	
do_n('''