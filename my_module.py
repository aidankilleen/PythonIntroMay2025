# my_module.py

def mod_function():
    print ("mod_function() called")
    print ("this is the function in a module")

# test the function
if __name__ == "__main__":

    print ("running the test code for the module")
    print (f"__name__={__name__}")

    mod_function()

