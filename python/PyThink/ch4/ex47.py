# github/pythink
# ex47.py

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	
	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle)

# REFACTORING ==============		

def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)
		
def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length /n
	setp_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)
	
def circle(t, r):
	arc(t, r, 360)