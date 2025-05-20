# oo_investigation.py


# Object
# data (member variables, properties)
# functions (methods)

name = "Aidan"

class Car:
    # constructor
    # self refers to the current object (same as "this" in other oo languages)
    # self is implicitly passed to every function 
    def __init__(self):
        self.make = "Nissan"
        self.model = "Micra"
        self.colour = "Blue"

    def show(self):
        print ("Car:")
        print (f"{self.make}")
        print (f"{self.model}")
        print (f"{self.colour}")


class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.driver = "some driver"
    pass


sc = SportsCar()
sc.show()
print (sc.driver)






# create an instance of Car
c = Car()

c.show()

print(c.make)


# oo programming language

# Abstration - the ability to create an object (a construct that has data and method)
# Encapsulation - the ability to protect the data from outside changes
# Inheritance - the ability to build one object on top of another
# Polymorphism - the ability for two objects to behave as if they are the same






