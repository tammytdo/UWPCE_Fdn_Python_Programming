"""

Mod 7 - Lab 1

Try out the code in this tutorial as you read through it. Post answers to the questions asked below to the discussion board.

"""

# Mutable Objects
list1 = [ [1,2,3], ['a','b'] ]

list2 = list1

# Q1. What does list1 and list2 contain? 
## list1 and list2 contain the excact same things. Both equal: [ [1,2,3], ['a','b'] ]

# Q2. What space in memory have list1 and list2 been assigned to? Are they the same? 
## list1 and list2 point to the exact same memory space
print(id(list1))
print(id(list2))
#4367664328
#4367664328

# What happens when we update a mutable element? 
list1[0] = [5,6,7]

# Q3. Now what do list1 and list2 contain? What happened? 
## list1 and list2 now both contain [ [5,6,7], ['a','b'] ]
print(list1)
# [[5, 6, 7], ['a', 'b']]
print(list2)
# [[5, 6, 7], ['a', 'b']]

# Let's properly copy the list, using slicing syntax: 
list2 = list1[:]
print("Slicing copy: ", list1)
print("Slicing copy: ", list2)
print("Slicing copy: ", id(list1))
print("Slicing copy: ", id(list2))
# Slicing copy:  [[5, 6, 7], ['a', 'b']]
# Slicing copy:  [[5, 6, 7], ['a', 'b']]
# Slicing copy:  4366550920
# Slicing copy:  4331668040

# Q4. What does [:] in the above statement mean? 
## [:] took a slice of list1 from beginning to end. Slicing creates a deepcopy and the copy is in a different memory space

# Now we'll update a mutable element of list1: 
list1[0] = [2,4,6]

# Q5. What do list1 and list2 contain now? Why? (Hint, check the memory space each item has been assigned to).
# list1 and list2 are now in separate memory spaces

print("Updated slicing copy: ", list1)
print("Updated slicing copy: ", list2)
print("Updated slicing copy: ", id(list1))
print("Updated slicing copy: ", id(list2))
# Updated slicing copy:  [[2, 4, 6], ['a', 'b']]
# Updated slicing copy:  [[5, 6, 7], ['a', 'b']]
# Updated slicing copy:  4364439176
# Updated slicing copy:  4362411016

# But what happens if we update the list itself? 
list1[1].append('c')
print(list1)
print(list2)
print("Updated slicing copy: ", id(list1))
print("Updated slicing copy: ", id(list2))
# [[2, 4, 6], ['a', 'b', 'c']]
# [[5, 6, 7], ['a', 'b', 'c']]
# Updated slicing copy:  4364401480
# Updated slicing copy:  4367321928

# Q6. What do list1 and list2 contain now? Why? 
## Each list had 'c' appened to it, using [:] gives each list its own location in memory but the lists contained within it are still "shallow copies"


# Make list2 a deep copy of list1
from copy import deepcopy
list2 = deepcopy(list1)

# Append the letter "x" to list1
list1.append("x")

# Report what list1 and list2 now contain
## "x" only appended to list1. the lists are in different memory spaces

print(list1)
print(list2)
print("Deepcopy: ", id(list1))
print("Deepcopy: ", id(list2))
# [[2, 4, 6], ['a', 'b', 'c'], 'x']
# [[2, 4, 6], ['a', 'b', 'c']]
# Deepcopy:  4334783752
# Deepcopy:  4364442696