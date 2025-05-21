# list_comprehension_investigation.py

people = ["aidan", "BOB", "carol", "Dan"]

numbers = [1, 3, 4, 2, 6, 3, 8, 9]


squares = [number*number  for number in numbers]

print (squares)

# uber pythonic
people = [person.capitalize() for person in people]

print (people)

# you could have done it this way - but list comprehensions are more "pythonic"
fixed_people = []
for person in people:
    fixed_people.append(person.capitalize())



# list comprehension with a condition
even_numbers = [n for n in numbers if n % 2 == 0]
print (numbers)
print (even_numbers)


# list comprehension in 2 dimensions
colours = ["red", "green", "blue"]
products = ["pen", "pencil", "crayon"]

product_list = [f"{colour} {product}" for colour in colours for product in products]

print (product_list)

combinations = [(x, y)  for x in range(1, 5) for y in range(1, 5)]

print (combinations)





