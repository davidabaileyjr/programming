# github/pybyte
# lambda.py

def make_repeater(n):
	return lambda s: s * n
	
twice = make_repeater(100)

print(twice('word'))
print(twice(5))