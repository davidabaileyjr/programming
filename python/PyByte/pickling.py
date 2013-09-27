# github/pybyte
# pickling.py

import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

print(shoplist, 'test')
del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)