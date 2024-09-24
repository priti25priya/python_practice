#1. Int: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x=655
y=8999963726355
z=-987644
print(type(x))
print(type(y))
print(type(z))
#2. Float: Float, or "floating point number" is a number, positive or negative, containing
# one or more decimals.
a=78.9
b=89.0
c=-78.1
print(type(a))
print(type(b))
print(type(c))

#3. Float can also be scientific numbers with an "e" to indicate the power of 10.
x=23e2
y=88E6
z=-98.20e45
print(type(x))
print(type(y))
print(type(z))
#4. Complex: Complex numbers are written with a "j" as the imaginary part:
a=3+8j
b=3j
c=-78j
print(type(a))
print(type(b))
print(type(c))
#5.Type conversion: You can convert from one type to another with the int(), float(), and complex() methods:
a=6
b=9.8
c=1+7j

x=float(a)
y=complex(b)
z=complex(c)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
#Note: We cannot convert complex number into another data type

