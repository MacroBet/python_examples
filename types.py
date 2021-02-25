# INSTANCE
x = 200
print(isinstance(x, int))

# BITWHISE OPERATIONS
"""
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

# TYPES 
x = "Hello World"	#str
x = 20	#int
x = 20.5	#float
x = 35e3
y = 12E4
z = -87.7e100
x = 1j+1	#complex
print("complex")
print(x)
x = ["apple", "banana", "cherry"]	#list
x = ("apple", "banana", "cherry")	#tuple
x = range(6)	#range
print("range")
print(x)
x = {"name" : "John", "age" : 36}	#dict
print("dict")
print(x)
x = {"apple", "banana", "cherry"}	#set
x = frozenset({"apple", "banana", "cherry"})	#frozenset
print("frozenset")
print(x)
x = True	#bool
x = b"Hello"	#bytes
print("bytes")
print(x)
x = bytearray(5)	#bytearray
print("bytearray")
print(x)
x = memoryview(bytes(5))	#memoryview
print("memoryview")
print(x)
