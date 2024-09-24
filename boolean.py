#1. When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10>9)
print(100==29)
print(34<12)

#2. Printing a message to know whether a condition is true or false
a=99
b=10

if a>b:
    print("The value of a is greater than the value of b")
else:
    print("The value of a is not greater than the value of b")

#3. Evaluate values and variables: The bool() function allow us to evaluate any values and give the output as
#True or false
print(bool(45))
print(bool("Coding"))

#Evaluate two variables
x="Coding"
y=78
print(bool(x))
print(bool(y))

# Some values return false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(""))

#One more value, or object in this case, evaluates to False, and that is
# if you have an object that is made from a class with a __len__ function that returns 0 or False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

