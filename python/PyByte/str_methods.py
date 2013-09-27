# github/pybyte
# str_methods.py

name = 'Swaroop' # This is the string object

if name.startswith('Swa'):
	print('Yes, the string starts with "Swa"')
	
if 'a' in name:
	print('Yes, it contains the string "a"')
	
if name.find('kar') != -1:
	print('Yes, it contains the string "kar"')
	
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))