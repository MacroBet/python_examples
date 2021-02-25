# INSERT
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# CONCAT LIST
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# CONCAT ITERABLE OBJECTS AS TUPLES
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# REMOVE 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# POP
thislist = ["apple", "banana", "cherry"]
print(thislist.pop(1)) # DEFAULT: last element
print(thislist)

# DEL
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) thislist is not defined!

# CLEAR
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# COPY LIST
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# SORT
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

# CUSTOM SORT FUNCTION
def myfunc(n):
  return abs(n - 50) # numeri più vicini al 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# NOT CASE-SENSITIVE SORT 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) 

