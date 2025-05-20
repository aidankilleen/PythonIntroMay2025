# hello_world.py
# comments are human-readable
# By: aidan
# Date: 19/05/2025


# building block #2 - ability to create a variable


multi_line_string = """
this
is a 
multi line
string
"""



"""
you can use this for multi-line comments
"""

print (multi_line_string)


from random import randint


name = "Aidan"
a = 10
b = 20
f = 1.23456

x = 99
print (x)
x = "ninety nine" # python is not strongly typed - no error if I change the type of a variable
print (x)

first_name = "Aidan" # snake case - this is recommended

firstName = "Aidan" # camel case - don't use this in python


# building block #3 - expressions

a = 10
b = 20

answer = (b / (a * 100)) + (1000 / a)     # pemdas

print ("*" * 25)

# building block #4 - conditions
if a > b:
    print ("a > b")
elif a == b:
    print ("equal")
else:
    print ("a > b")

# building block #5 - loop(s)

x = 0

while x <= 10:
    print ("x=", x)
    x = x + 1

for i in range(1, 10, 2):
    print (i)

print ("=" * 30)
# building block #6 - array / list

list = [1, 5, 3, 2, 7, 9, 11]

print(list[1]) # list index starts at 0
print(list[0])
print (list[6])


for n in range(len(list)):
    print (list[n])


for n in list:
    print (n)

x = "1223"
#print (list[100]) # out of bounds

# in python 
# lists[]
# tuple - list that you can't change
# set - list that only contains unique items
# dictionary


# building block #7 - functions

# built in functions - https://docs.python.org/3/library/functions.html
print("print is a function")
r = range(10)# range is a function


# functions from standard library
r = randint(1, 10)
print ("r=", r)


# functions from 3rd party libraries


# user defined functions
def greet(name):
    print ("Welcome " + name)


greet("Aidan")
greet("Bob")
greet("Carol")
greet("Danielle")


print ("s1" + "s2")

answer = 42

print ("The answer is" + str(answer))


# Building Block #8 - Objects
# python is full object oriented programming language




































































