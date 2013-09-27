# github/pythink
# ex514.py

# x = raw_input()
# y = raw_input()
# z = raw_input()
# n = raw_input()

def fermat(a, b, c, n):
	if a**n + b**n == c**n:
		print 'Holy Smokes! Fermat was wrong!'
	else:
		print "No that doesn't work"

fermat(2, 3, 4, 5)

'''Prompt user to input values for a, b, c, and n...
convert them to integers and use fermat()'''	