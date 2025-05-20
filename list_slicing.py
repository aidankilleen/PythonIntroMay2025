# list_slicing.py


list = [2, 5, 3, 4, 10, 8, 6]


print (list)

print (list[0])

print (list[len(list)-1])

# cool feature - negative index
print (list[-1])
print (list[-2])


# cool feature - slicing

print(list[1:4])

#print ="no longer a function"

#print ("is this broken?")

print (list[:4])
print (list[4:])

names = ["Alice", "Bob", "Carol", "Dan", "Eve"]

print (names[:2])
print (names[2:])

print (names)

names_copy = names

names[0] = "CHANGED"
print (names)
print (names_copy)


print (id(names))
print (id(names_copy))

# to make a copy you can use the slice operator

names_copy_2 = names[:]

print (id(names_copy_2))

names[1] = "ALSO CHANGED"

print (names)
print (names_copy)
print (names_copy_2)


# a string is just a list of characters

message = "This is a message"

print (message[0])
print (message[-1])

print (message[5:7])
print (message[:5])
print (message[5:])

for letter in message:
    print (letter)


print (message[-7:])

print (len(message))

# NB - strings are immutable
# message[0] = "X"


message = "m1"
print (f"{id(message)}:{message}")
message = "m2"
print (f"{id(message)}:{message}")














































