# github/pythink
# ex63_composition.py

radius = distance(xc, yc, xp, yp)
result = area(radius)

# ENCAPSULATE - put the code into a function

def circle_area(xc, yc, xp, yp):
	radius = distance(xc, yc, xp, yp)
	result = area(radius)
	return result
	
# CONDENSE THE CODE - same code as above 

def circle_area(xc, yc, xp, yp):
	return area(distance(xc, yc, xp, yp))
	