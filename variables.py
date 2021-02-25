# CAST
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)
print(type(x))

# UNPACK
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# TEMPLATE STRING
print( 'I like %s' % x)

# FUNCTIONS AND GLOBAL
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

import random
print(random.randrange(1, 10))
