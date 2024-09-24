# Tuple: Tuples are used to store items in a single variable. It is ordered and unchangeable(immutable).
# It is represented by square brackets.
thistuple=("apple","kiwi","tomato")
print(thistuple)

# Allow duplicates
thistuple=("apple","kiwi","emily","orange","orange")
print(thistuple)

# Tuple length
mytuple=("apple","salad","fruits","veggies","soup")
print(len(mytuple))

# Create tuple with one item: To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple1 = ("apple")
print(type(thistuple1))

# Tuple() constructor: It is also possible to use the tuple() constructor to make a tuple.
thistuple=tuple(("grapes","pie","cherry","watermelon"))
print(thistuple)

# Access tuple item: You can access tuple items by referring to the index number, inside square brackets.
thistuple=("apple","mango","fruits","orange")
print(thistuple[2])

# Negative indexing
thistuple=("apple","cherry","pie","watermelon")
print(thistuple[-1])

# Range of indexes
thistuple=("apple","pie","pineapple","orange","fruit")
print(thistuple[2:5])

# Range of negative index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1.

# Check if item exists
tuple1=("apple","mango","chia seeds","rosemary")
if "chia seeds" in tuple1:
    print("Yes! it is present in the tuple")
# Change tuple values: Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Remove items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Unpacking a tuple: When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Packing a tuple:
tuple1=("orange","fruits","subjects","exams")
print(tuple1)

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples
tuple1=("mango","grapes","pineapple","coconut")
mytuple=tuple1*2
print(mytuple)
