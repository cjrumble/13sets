# SETS LESSON
# Python Set is a programmatic form of sets in mathematics and one of the core data structures in Python.
# It is an unordered and unique collection of immutable objects. But it is in itself mutable by default.

# Sets in Python
# What is a Set? Set is a term that originates from Mathematics.But, in Python, it is a collection type object which
# can store elements of different data types.It doesn’t index the values in a particular order.
# Properties of a Set -  A Python set has the following characteristics.
# The elements don’t have a specific order, and their positions can be inconsistent.
# Each item is unique in a Set and, therefore, can’t have duplicates.
# The elements are immutable and hence, can’t accept changes once added.

# set is itself mutable and allows the addition or deletion of items.
# With Sets, we can execute several mathematical operations such as Union, Intersection, Symmetric Difference,
# and Complement.

# Create or Update Python Set
# Create a Set
# Invoke any of the following two methods to create a Python Set.

# If you have a fixed set of elements, then group them using a comma as the separator and enclose the group inside curly braces.
# Another way is to call the built - in “set()” method, which can also be used to add elements at run - time.
#  Also, remember, the elements can be of any data types such as an integer, float, tuple, or string, etc.
#  The only exception with a set is that it can’t store a mutable item such as List, Set, or Dictionary.

# create a set of numbers
py_set_num = {3, 7, 11, 15}
print(py_set_num)

# create a set of mixed data types
py_set_mix = {11, 1.1, "11", (1, 2)}
print(py_set_mix)
# output
# {3, 11, 7, 15}
# {(1, 2), 1.1, 11, '11'}

# set can't store duplicate elements
py_set_num = {3, 7, 11, 15, 3, 7}
# it'll automatically filter the duplicates
print(py_set_num)

# create a set using the set() method
# creating set with a fixed set of elements
py_set_mix = set([11, 1.1, "11", (1, 2)])
print(py_set_mix)

# creating set with dynamic elements
py_list = [11, 1.1, "11", (1, 2)]
py_list.append(12)
print(py_list)
py_set_mix = set(py_list)
print(py_set_mix)
# output
# {11, 3, 15, 7}
# {(1, 2), 1.1, 11, '11'}
# [11, 1.1, '11', (1, 2), 12]
# {(1, 2), 1.1, 11, '11', 12}

# Let's try to create an empty Python set
py_set_num = {}
print("The value of py_set_num:", py_set_num)
print("The type of py_set_num:", type(py_set_num))
py_set_num = set()
print("The value of py_set_num:", py_set_num)
print("The type of py_set_num:", type(py_set_num))
# The first statement would result in the creation of a dictionary object instead of creating a set.
# You can’t just use curly braces and expect a “Set” in return.
# While in the next non - print statement, we used the set() function but didn’t pass any argument to it.
# It will eventually return us an empty Set object.
# output
# The value of py_set_num: {}
# The type of py_set_num: <class 'dict'>
# The value of py_set_num: set()
# The type of py_set_num: <class 'set'>

# Add Elements to a Set

# Python Set is a mutable object.However, it doesn’t use any indexing, and hence, it doesn’t have any order.
# It also means that you can’t change its elements by accessing through an index or via slicing.
# There is add(), which adds a single element and the update(), which can add more than one item.
# The update() method can even accept tuples, lists, strings, or other sets as an argument.However, duplicate elements
# will automatically get excluded.

# Let's try to change a Python set
py_set_num = {77, 88}
try:
    print(py_set_num[0])
except Exception as ex:
    print("Error in py_set_num[0]:", ex)
print("The value of py_set_num:", py_set_num)
# Let's add an element to the set
py_set_num.add(99)
print("The value of py_set_num:", py_set_num)
# Let's add multiple elements to the set
py_set_num.update([44, 55, 66])
print("The value of py_set_num:", py_set_num)
# Let's add a list and a set as elements
py_set_num.update([4.4, 5.5, 6.6], {2.2, 4.4, 6.6})
print("The value of py_set_num:", py_set_num)
# output
# Error in py_set_num[0]: 'set' object does not support indexing
# The value of py_set_num: {88, 77}
# The value of py_set_num: {88, 99, 77}
# The value of py_set_num: {66, 99, 44, 77, 55, 88}
# The value of py_set_num: {66, 99, 4.4, 5.5, 6.6, 2.2, 44, 77, 55, 88}

# Remove Elements from a Set
# You can use the following Set methods to delete elements from it.
# Discard() method
# Remove() method
# There is a small difference in the way these two methods operate.
# The discard() method doesn’t throw any error if the target item is not the part of the set.
# The remove() method will throw the “KeyError” error in such a case.
# Let's try to use a Python set
py_set_num = {22, 33, 55, 77, 99}
# discard an element from the set
py_set_num.discard(99)
print("py_set_num.discard(99):", py_set_num)
# remove an element from the set
py_set_num.remove(77)
print("py_set_num.remove(77):", py_set_num)
# discard an element not present in the set
py_set_num.discard(44)
print("py_set_num.discard(44):", py_set_num)
# remove an element not present in the set
try:
    py_set_num.remove(44)
except Exception as ex:
    print("py_set_num.remove(44) => KeyError:", ex)
# output
# py_set_num.discard(99): {33, 77, 22, 55}
# py_set_num.remove(77): {33, 22, 55}
# py_set_num.discard(44): {33, 22, 55}
# py_set_num.remove(44) = > KeyError: 44
# There is the pop() method to remove an element.
# Also, since the Set doesn’t use indexing, so you can’t be sure which of the item would get popped.
# It’ll randomly pick one element and remove it.
# There is also a method called clear(), which flushes everything from the set.
# Let's use the following Python set
py_set_num = {22, 33, 55, 77, 99}
print("py_set_num:", py_set_num)
# pop an element from the set
py_set_num.pop()
print("py_set_num.pop():", py_set_num)
# pop one more element from the set
py_set_num.pop()
print("py_set_num.pop():", py_set_num)
# clear all elements from the set
py_set_num.clear()
print("py_set_num.clear():", py_set_num)
# output
# py_set_num: {33, 99, 77, 22, 55}
# py_set_num.pop(): {99, 77, 22, 55}
# py_set_num.pop(): {77, 22, 55}
# py_set_num.clear(): set()

# Python Set Operations
# We'll use the setA and setB for our illustration
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}

# Union Operation
# Union of setA and setB is a new set combining all the elements from both the Sets.
# Python Set - Union
# The “ | ” operator is the one to perform the union operation on the sets.
# We'll use the setA and setB for our illustration
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
print("Initial setA:", setA, "size:", len(setA))
print("Initial setB:", setB, "size:", len(setB))
print("(setA | setB):", setA | setB, "size:", len(setA | setB))
# We’ve used the Len() method to calculate the length of the set.
# output
# Initial setA: {'u', 'i', 'g', 'o', 'e', 'h', 'a'}
# size: 7
# Initial setB: {'u', 'z', 'b', 'o', 'e', 'a', 't'}
# size: 7
# (setA | setB): {'h', 'u', 'z', 'b', 't', 'g', 'o', 'e', 'i', 'a'}
# size: 10
# Can achieve Similar results using the union() method.
# Python set example using the union() method
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
print("setA.union(setB):", setA.union(setB), "size:", len(setA.union(setB)))
print("setB.union(setA):", setB.union(setA), "size:", len(setB.union(setA)))
# You can apply the union() method on any of the set(i.e., set A or B); the output will remain the same.
# output
# setA.union(setB): {'a', 'o', 'e', 'b', 'u', 't', 'i', 'g', 'z', 'h'}
# size: 10
# setB.union(setA): {'a', 'o', 'e', 'b', 'u', 't', 'i', 'g', 'z', 'h'}
# size: 10

# Intersection Operation
# The intersection of setA and setB will produce a set comprising common elements in both the Sets.

# Python Set - Intersection
# You can use Python’s “ & ” operator to perform this operation.
# Python intersection example using the & operator
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
print("Initial setA:", setA, "size:", len(setA))
print("Initial setB:", setB, "size:", len(setB))
print("(setA & setB):", setA & setB, "size:", len(setA & setB))
# output
# Initial setA: {'e', 'o', 'h', 'a', 'g', 'u', 'i'}
# size: 7
# Initial setB: {'b', 'e', 't', 'o', 'z', 'a', 'u'}
# size: 7
# (setA & setB): {'o', 'a', 'u', 'e'}
# size: 4
# Alternatively, you can call the intersection() method to perform this operation.
# Python set example using the intersection() method
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
intersectAB = setA.intersection(setB)
print("setA.intersection(setB):", intersectAB, "size:", len(intersectAB))
intersectBA = setB.intersection(setA)
print("setB.intersection(setA):", intersectBA, "size:", len(intersectBA))
# output
# setA.intersection(setB): {'a', 'u', 'e', 'o'}
# size: 4
# setB.intersection(setA): {'a', 'u', 'e', 'o'}
# size: 4

# Difference Operation
# When you perform the difference operation on two Sets, i.e., < setA – setB >, the resultant will be a set of
# elements that exist in the left but not in the right object.

# Python Set – Difference
# Likewise, the operation < setB – setA > will return those elements of setB which don’t exist in the setA.
# You can use the minus(-) operator to carry out this operation.
# Python set's difference operation
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
diffAB = setA - setB
print("diffAB:", diffAB, "size:", len(diffAB))
diffBA = setB - setA
print("diffBA:", diffBA, "size:", len(diffBA))
# output
# diffAB: {'i', 'g', 'h'}
# size: 3
# diffBA: {'z', 'b', 't'}
# size: 3
# Can achieve the same set of operations using the difference() method.
# Python set's difference operation using the difference() method
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
diffAB = setA.difference(setB)
print("diffAB:", diffAB, "size:", len(diffAB))
diffBA = setB.difference(setA)
print("diffBA:", diffBA, "size:", len(diffBA))
# output
# diffAB: {'i', 'g', 'h'}
# size: 3
# diffBA: {'b', 't', 'z'}
# size: 3

# Symmetric Difference
# The symmetric difference of two sets will generate a set of elements that exist in < setA > and < setB > but not in both.
# Python Set – Symmetric Difference
# You can execute this operation with the help of the caret operator ( ^ ) in Python.
# Python set example using the caret ^ operator
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
symdiffAB = setA ^ setB
print("symdiffAB:", symdiffAB, "size:", len(symdiffAB))
symdiffBA = setB ^ setA
print("symdiffBA:", symdiffBA, "size:", len(symdiffBA))
# The output is as follows.
# symdiffAB: {'z', 't', 'h', 'g', 'b', 'i'}
# size: 6
# symdiffBA: {'z', 'h', 'g', 't', 'b', 'i'}
# size: 6
# You can also get the operation done with the method symmetric_difference().
# Python set example using the symmetric_difference() method
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
symdiffAB = setA.symmetric_difference(setB)
print("symdiffAB:", symdiffAB, "size:", len(symdiffAB))
symdiffBA = setB.symmetric_difference(setA)
print("symdiffBA:", symdiffBA, "size:", len(symdiffBA))
# result
# symdiffAB: {'z', 'h', 'i', 'g', 't', 'b'}
# size: 6
# symdiffBA: {'z', 'i', 'g', 'b', 't', 'h'}
# size: 6

# Miscellaneous Set Operations

# Access Set Elements
# It’s not possible to accessan element directly in a set.But you can fetch all of them together.
# You need a loop to retrieve a list of particular items over the Set.
# Python set example to access elements from a set
basket = set(["apple", "mango", "banana", "grapes", "orange"])
for fruit in basket:
    print(fruit)
# output
# apple
# banana
# mango
# orange
# grapes

# Set Membership Test
# You can surely check if a set contains a particular element or not.
# You can make use of the “ in ” keyword for this purpose.
# Python set example to test elements in a set
basket = set(["apple", "mango", "banana", "grapes", "orange"])
# confirm if 'apple' is in the basket
print("Is 'apple' in the basket?", 'apple' in basket)
# confirm if 'grapes' is in the basket
print("Is 'watermelon' in the basket?", 'watermelon' in basket)
# output
# Is 'apple' in the basket? True
# Is 'watermelon' in the basket? False

# Frozen Sets in Python
# It is a unique type of set which is immutable and doesn’t allow changing its elements after assignment.
# It supports all methods and operators as a set does, but those that don’t alter its content.
# The sets are mutable and thus become unhashable. So, we can’t use them as keys for a Python dictionary.
# On the contrary, the Frozen Set is by default hashable and can work as keys to a dictionary.

# You can create a Frozen set with the help of the following function.
frozenset()
# The following Python methods can work with the Frozen set.
# copy()
# difference()
# intersection()
# isdisjoint()
# issubset()
# issuperset()
# symmetric_difference()
# union()
# The methods which perform add or remove operations aren’t applicable for Frozen sets as they are immutable.
# The differences between a standard vs. the frozen set.
# Python Sample - Standard vs. Frozen Set
# A standard set
std_set = set(["apple", "mango", "orange"])
# Adding an element to normal set is fine
std_set.add("banana")
print("Standard Set:", std_set)
# A frozen set
frozen_set = frozenset(["apple", "mango", "orange"])
print("Frozen Set:", frozen_set)
# Below code will raise an error as we are modifying a frozen set
try:
    frozen_set.add("banana")
except Exception as ex:
    print("Error:", ex)