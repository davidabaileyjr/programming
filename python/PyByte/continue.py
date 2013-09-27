# /python/pybyte/
# Filename: continue.py

while True:
	s = input('Enter something : ')
	if s == 'quit':
		break
	# print('Length of the string is', len(s))
	if len(s) < 3:
		print('Too small')
		continue
	print('Input is of sufficient length')
	#Do other kinds of processing here...

print('Done')