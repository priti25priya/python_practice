#Python arithmetic operators: Arithmetic operators are used with numeric values to perform common mathematical operations.
#1. Addition
x=599
y=600
print(x+y)
#2. Subtraction
x=566
y=120
print(x-y)
#3. Multiplication
x=56
y=75
print(x*y)
#4. Division
x=67
y=4
print(x/y)
#5. Modulus
x=56
y=6
print(x%y)
#6. Exponentiation
x=23
y=2
print(x**y)
#7. Floor division
x=45
y=2
print(x//y)

# Python assignment operators: Assignment operators are used to assign the values to the variables.
x=5
x += 4
print(x)

#Python comparison operators: Comparison operators are used to compare two values.
#Equal
x=3
y=5
print(x==y)
#!=
x=56
y=90
print(x!=y)
#>
x=45
y=56
print(x>y)
#<
x=67
y=77
print(x<y)
#>=
x=67
y=67
print(x>=y)
#<=
var1=78
var2=88
print(var1<=var2)

#Python logical operator
#AND
var1=66
print(var1>56 and var1<89)

#OR
var1=89
print(var1>100 or var1>67)

#NOT
var1=89
print(not(var1>23 and var1>34))

#Python Identity operator
#is
x=["apple", "cherry","pie"]
y=["apple", "cherry","pie"]
var1=x
print(x is var1) # returns True because z is the same object as x
print(x is y) #returns False because x is not the same object as y, even if they have the same content
print(x==y) # to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y

#is not
x=["apple", "cherry","pie"]
y=["apple", "cherry","pie"]
var1=x
print(x is not var1) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x!=y) # to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y


#Python membership operator
#in
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

#not in

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

#Python bitwise operator
#& AND
print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

#| OR
print(12 | 3)
print(6 | 3)



"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#^XOR
print(6 ^ 3)



"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
