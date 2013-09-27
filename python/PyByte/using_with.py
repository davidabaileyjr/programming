# github/pybyte
# using_with.py

#import time

with open("poem.txt") as f:
	for line in f:
		print(line)
		#time.sleep(2)