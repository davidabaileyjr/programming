# github/pythink
# ex68.py

def gcd(a, b):
	if b == 0:
		return a
	else:
		r = a % b
	print b, "," , r
	return gcd(b, r)
	
print "gcd(1989, 867 =", gcd(1989,867)

# don't quite get the math yet...
# need to study more Euclid! ;)