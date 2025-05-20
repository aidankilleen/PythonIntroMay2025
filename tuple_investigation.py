# tuple_investigation.py
# By: Aidan
# Date: 19/5/2025


# tuple is an immutable list
# create a tuple using round brackets
t = (1, 2, 3, 4, 5, 6)

print (t[0])
print (t[2])

print (t[-1])

print (t[2:4])

for i in t:
    print (i)

print (len(t))

# you can't modify a tuple
# t[0] = 99


# so what?

def process_list(numbers):

    mx = max(numbers)
    mn = min(numbers)

    return (mx, mn)


data = [5,3,6,9,10,32,76,15,1]


m = process_list(data)

print (data)
print (f"Max:{m[0]}")
print (f"Min:{m[1]}")

a = 10
b = 20

print(f"a={a}")
print(f"b={b}")

# swap these variable (traditional)
t = b
b = a
a = t

print(f"a={a}")
print(f"b={b}")

# swap them back using tuples
(a, b) = (b, a)

print(f"a={a}")
print(f"b={b}")


# third example
# initialise multiple values in a single line
# nb: sometimes you don't need the round brackets when creating a tuple
#
x, y, z = 1, 2, 3

print (x, y, z)

(x, y, z) = (4, 5, 6)

print (x, y, z)

t = (27, 30, 45)

# unpack values from a tuple 
(x, y, z) = t

print (x, y, z)





















































