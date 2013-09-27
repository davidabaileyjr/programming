# github/pybyte
# 3.14.1.py

yes = 5

def do_twice(f, r):
	f() + r()
	f() + r()

def print_spam(s):
	print 'love'
	print 'spam'

def print_me():
	print 'hello there'
	print 'how are you'
	
def print_text(x):
	print x
	print x
	
do_twice(print_spam, print_me)
	
print_text('david is awesome')