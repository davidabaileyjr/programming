# github/pythink
# mypolygon.py

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

fd(bob, 100)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)

for i in range(4):
	print 'Hello!'
	
for i in range(4):
	fd(bob, 100)
	lt(bob)
	
wait_for_user()