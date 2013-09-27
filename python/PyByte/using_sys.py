# /python/pybyte/
# Filename: using_sys.py

import sys # we import sys module

print('The command line arguements are:') # show this
for i in sys.argv: # for each arguement we type in the command line
	print(i) # show each arguement we type in command line
	
print('\n\nThe PYTHONPATH is', sys.path, '\n') # print python paths where sys was imported from

# import os
# print(os.getcwd())