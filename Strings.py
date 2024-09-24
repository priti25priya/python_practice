#Creating variables
a=34
b="John"
print(a)
print(b)

#1. You can assign a multiline string to a variable by using three quotes:
a="""Assigning a string to a variable is done with the variable
name followed by an equal sign and the string"""

print(a)

#2. Slicing: You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
a="Hello coders!"
print(a[1:6])

#3. Slice from the start: By leaving out the start index, the range will start at the first character:
a="Hello programmers"
print(a[:7])

#4. Slice to the end: By leaving out the end index, the range will go to the end:
a="Hello programmers"
print(a[0:])

#5. Negative Indexing: Use negative indexes to start the slice from the end of the string:
a="Welcome python programmers"
print(a[-10:-1])

#6. Upper Case: The upper() method returns the string in upper case
a="Antivirus software"
print(a.upper())

#7. Lower Case: The lower() method returns the string in lower case
a="Antivirus software"
print(a.lower())

#8. Remove whitespace: Whitespace is the space before and/or after the actual text, and
# very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
my_var=a.strip()
print(my_var)

#23. Replace string: The replace() method replaces a string with another string.
a="Hello students"
var=a.replace("H","F")
print(var)

#24. Split string: The split() method returns a list where the text between the specified separator becomes the list items.
var="Cherry Pie"
myvar=var.split()
print(myvar)

#25. Concatenation: It is used to combine two strings.
a="Himalayan"
b="River"
print(a+" "+b)

#26. Format Strings:As we learned in the Python Variables, we cannot combine strings and numbers as these are of different
#data types but, we can combine strings and numbers using f-string or format() method.
marks=89
txt=f"My name is John, I got {marks} in mathematics"
print(txt)

#27. Placeholders and modifiers: A placeholder can contain variables, operations, functions, and
# modifiers to format the value.
price=10
txt=f"the price is {price} euro"
print(txt)

#28. A modifier is included by adding a colon : followed by a legal formatting type, like .2f which
# means fixed point number with 2 decimals
price=34
txt=f"The cost of perfume is {price:.2f} dollars"
print(txt)

#29. Escape characters: We will get an error if you use double quotes inside a string that is
# surrounded by double quotes, to fix this error we use escape characters(\")
txt="Can we have \"icecream\" ?, its really hot outside"
print(txt)
