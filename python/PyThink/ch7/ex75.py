# github/edu/pythink/ch7
# ex75.py

def test(a, x):
	epsilon = 0.0000000003
	while True:
		print x
		y = (x + a / x) / 2
		if abs(y - x) < epsilon:
			break
		x = y
		
test(4.0, 3.0)