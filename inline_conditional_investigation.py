# inline_conditional_investigation.py


from random import randint


active = False

message = f"The user is {'Active' if active == True else 'Inactive'}"

print (message)

r = randint(1, 100)

message = f"The number {r} is {'big' if r > 50 else 'small'}"

print (message)

r = randint(1, 100)

message = f"The number {r} is {'small' if r < 30 else 'medium' if r < 60 else 'large'}"

print(message)
