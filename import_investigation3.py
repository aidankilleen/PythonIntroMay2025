# import_investiation1.py

# import the whole library and assign an alias
import random as rnd
import my_module as mm

def choice(l):
    print ("choice isn't what you were expecting")

r = rnd.randint(1, 10)

l = [1,2,3,4,5,6,7,8,9,10]

print (l)

rnd.shuffle(l)

print (l)

val = rnd.choice(l)

print (val)

mm.mod_function()
