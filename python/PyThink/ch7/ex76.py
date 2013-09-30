# github/edu/pythink/ch7
# ex76.py

a = 4.0
x = 3.0

while True:
	print x
	y = (x + a/x) / 2
	if y == x:
		break
	x = y