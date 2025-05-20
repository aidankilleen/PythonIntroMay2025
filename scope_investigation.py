# scope_investigation.py


first_name = "Aidan"


def greet(name):
    global first_name
    message = f"Welcome {name}"

    print (message)
    print (first_name)
    first_name = "CHANGED" 

def another_function():
    first_name = "changed"

print (first_name)
# print (message) message is not available outside the function
if True:
    last_name = "Killeen"


    print (last_name)



print (first_name)
print (last_name) # different to Java etc.

greet("Aidan")



