# github/edu/pythink/ch7
# ex77.py

# Not figured out (from Exercise 7.3 in 7.9)

def loop(x):
	while x < 9.0:
		x = x + 1
		print x
	else:
		pass

loop(1.0)

def calc(a, x):
	while True:
		y = (x + a/x) / 2
		if y == x:
			print x
			break
		x = y

calc(4.0, 3.0)