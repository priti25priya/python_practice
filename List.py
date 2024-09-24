# Lists are used to store multiple values in a single variable.
# Lists are created using square brackets.
# Create a list
var1=["Apple", "Cherry","Pie"]
print(var1)

# Allow duplicates: Lists can have the same values.
var1=["name", "id","23",45,45,"Role"]
print(var1)

# List length: Determines the length of the list.
var1=["Name", "Id","Designation",23]
print(len(var1))

# Type()
mylist=["Name","Id","Designation"]
print(type(mylist))

# The list() constructor: It is possible to use the list() constructor when creating a new list.
thislist=list(("apple","cherry","pie"))
print(thislist)

# Access list
mylist=["apple","orange","pie","cherry"]
print(mylist[3])

# Negative indexing
mylist=["apple","name","fruit","vegetable","designation"]
print(mylist[-1])

# Range of indexes
mylist=["apple","name","fruit","vegetable","designation"]
print(mylist[2:5])

# Check if items exists
thislist=["mango", "name","designation","fruit"]
if "name" in thislist:
    print("yes! the item exists")

# Change/replace item value
mylist=["orange","strawberry","roses"]
mylist[2]="mango"
print(mylist)

# Change the range of item values
mylist=["name","id","designation","lunch"]
mylist[1:2]=["fruit", "salad"]
print(mylist)

# Insert item value
thislist=["watermelon","fruit","jackfruit","pineapple"]
thislist.insert(3,"apple")
print(thislist)

# Append items
myvar1=["Snacks","Coke","Game"]
myvar1.append("Cricket")
print(myvar1)

# Extend
myvar1=["employee","employer","evaluation"]
myvar2=["work","designation","name"]
myvar1.extend(myvar2)
print(myvar1)

# Remove specified item:
thisvar=["apple","milkshake","cherrypie"]
thisvar.remove("milkshake")
print(thisvar)

# Remove specified index: For removing specific index, we use pop() method.
thislist=["Parabola","mathematics","geometry","syllabus"]
thislist.pop(3)
print(thislist)

# Clear the list
mylist=["Apple","fruits","salad","desserts"]
mylist.clear()
print(mylist)

# Sort the list
mylist=["Apple","Kiwi","Grapes","Cherry"]
mylist.sort()
print(mylist)

# Sort descending
mylist=["orange","kiwi","mango","zebra","giraffe"]
mylist.sort(reverse=True)
print(mylist)

# Reverse order: What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
mylist=["orange","kiwi","mango","zebra","giraffe"]
mylist.reverse()
print(mylist)

# Python copy list
mylist=["kiwi","mango","orange","apple"]
myvar=mylist.copy()
print(myvar)

# Use the list() method to copy
mylist=["apple","fruits","guava","pineapple"]
myvar=list(mylist)
print(myvar)

# Use the slice operator
mylist=["watermelon","network","veggies","apple"]
thislist=mylist[:]
print(thislist)

# Join two list
list1=["abc","xyz","mango"]
list2=["veggies","salad","fruits"]
list3=list1+list2
print(list3)


