# github/pybyte
# seq.py

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation
# print('If blank we get', shoplist[:])
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# Slicing on a string with negatives
print('characters 1 to 3 is', name[-6:-4])
print('characters 2 to end is', name[-5:])
print('characters 1 to -1 is', name[-6:-1])
print('characters start to end is', name[:])

# Slicing with negative steps
print('characters 1 to 3 is', name[::-1])
print('characters 2 to end is', name[::-2])
print('characters 1 to -1 is', name[::-3])
print('characters start to end is', name[::-4])

# Slicing with steps
print('characters 1 to 3 is', name[::1])
print('characters 2 to end is', name[::2])
print('characters 1 to -1 is', name[::3])
print('characters start to end is', name[::4])