# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
# Create Dictionary
mydict={"name":"John",
        "id":"1877",
        "designation":"manager"
        }

print(mydict)

# Dictionary items
mydict={"name":"john",
        "id":1988,
        "designation":"engineer"
}
print(mydict["id"])

# Dictionary length
mydict={"name":"john",
        "id":1988,
        "designation":"Jr.Data Analyst "
}
print(len(mydict))

# Dict() constructor
thisdict=dict(name="John",marks=100,country="Egypt")
print(thisdict)

# Get keys
thisdict = {
  "name": "Fam",
  "occupation": "student",
  "cgpa": 9.8
}
x = thisdict.keys()
print(x)

# Get values
thisdict = {
  "name": "Fam",
  "occupation": "student",
  "cgpa": 9.8,
    "id":19880
}
x = thisdict.values()
print(x)

# Get Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)

# Check if keys exists
thisdict = {
  "flower": "roses",
  "color": "red",
  "brand": "nike"
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("doesn't contain")

# Update dictionary
thisdict = {
  "name": "Fam",
  "occupation": "student",
  "cgpa": 9.8,
    "id":19880
}
thisdict.update({"name":"Edward"})
print(thisdict)

# Remove dictionary items
thisdict = {
  "name": "Fam",
  "occupation": "student",
  "cgpa": 9.8,
    "id":19880
}
thisdict.pop("id")
print(thisdict)

# Copy a dictionary
thisdict = {
  "name": "Fam",
  "occupation": "student",
  "cgpa": 9.8,
    "id":19880,
    "course":"Computer Science"
}
x = thisdict.copy()
print(x)

# Nested Dictionary
mycollege = {
  "student1" : {
    "name" : "Emil",
    "course" :"Computer Science"
  },
  "student2" : {
    "name" : "Tobias",
    "course" : "Artificial Intelligence"
  },
  "student3" : {
    "name" : "Linus",
    "course" : "Data Science"
  }
}

print(mycollege)

