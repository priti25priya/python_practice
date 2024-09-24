#1.
x=12
y=13
z= x+y
print(z)

#2.
y=int(5)
x="Priti"
print(x)
print(y)

#3.
a=int(3)
b=str(3)
c=float(3)
print(a)
print(b)
print(c)

#4.
a=5
b="4"
c="Priti"
d=6.9
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#5.
my_var="Code in Python"
print(my_var)
#6.Many values to multiple variables
x,y,z="Code", "Python","Programming"
print(x)
print(y)
print(z)
#7.Unpack a collection:If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables.
# This is called unpacking.
fruits=["Cherry","Apple","Orange"]
x,y,z=fruits
print(x)
print(y)
print(z)
#8.Output variables
x="Python"
y="is"
z="awesome"
print(x,y,z)
print(x+" "+y+" "+z)

#9. Global variable:Variables that are created outside of a function  are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.
x="awesome"

def myfunc():
    print("Python is "+ x)
myfunc()
#If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

x="awesome"

def myfunc():
    x="fantastc"
    print("Python is "+x)
myfunc()

print("Python is " + x)



