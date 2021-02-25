#########  COOL LOOPS  #########
# 
# newlist = [expression for item in iterable if condition == True]
# 
################################

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

# You can use the range() function to create an iterable:
print(range(10))
newlist = [x for x in range(10) if True]
print(newlist)

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]



#########  OLD STYLES  #########
# FOR I IN RANGE
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# FOR X IN LIST 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# WHILE
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1