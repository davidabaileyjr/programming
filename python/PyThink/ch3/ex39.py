import math

def printTwice(bruce):
	print bruce, bruce

printTwice('spam')
printTwice(5)
printTwice(3.14159)

printTwice('Spam'*4)
printTwice(math.cos(math.pi))

printTwice("'Spam'*4")

michael = 'Eric, the half a bee.'
printTwice(michael)

def catTwice(part1, part2):
	cat = part1 + part2
	printTwice(cat)

chant1 = "Pie Jesu Domine."
chant2 = "Dona eis requiem."

catTwice(chant1, chant2)