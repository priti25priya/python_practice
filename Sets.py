# Sets: Sets are used to store multiple items in a single variable. A set is a collection which
# is unorderd , unchangeable and unindexed.
# Note: Set items are unchangeable, but we can remove items and add new items.
# Sets are written with curly brackets.
# Create a set
thisset={"Cherry", "ice-cream","ice cubes"}
print(thisset)

# Duplicates are not allowed
myset={"cherry","pie","ice-cream","bubble","cherry"}
print(myset)

# Length of a set
myset={"country","code","food","travel"}
print(len(myset))

# set() constructor
myset=set(("cherry","pie","cake","vanilla"))
print(myset)

# Access items: You cannot access items in a set by referring to an index or a key.
#  But you can loop through the set items using a for loop, or ask if a specified value is
#  present in a set, by using the in keyword.
myset={"apple","orange","pineapple"}
for items in myset:
    print(items)

# Add sets: to add items from another set to the current set , we use update() method.
myset={"plants","start","new","mountain"}
thisset={"roses","race","clever","himalayan"}
myset.update(thisset)
print(myset)

# Remove() method
myset={"plant","flowers","soil","pot"}
myset.remove("pot")
print(myset)

# Join sets:The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
set1={"many","some","while","loop"}
set2={"for","join","statistics","left"}
set3=set1.union(set2)
print(set3)

# Intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
