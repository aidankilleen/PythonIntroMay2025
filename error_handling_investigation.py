# error_handling_investigation.py


from random import randint


print("error handling investigation")

n = 10
i = 0
l = [1,2,3]
answer = 0

r = randint(1, 5)

try:
    if r == 1:
        answer = int("ninety nine")
    elif r == 2:
        open("doesntexist.txt")
    elif r == 3:
        answer = l[3]
    elif r == 4:
        answer = n / i
    else:
        answer = 42
       
except IndexError:
    print ("can't access item outside bounds of list")
    answer = l[0]
except ValueError:
    print ("Can't convert value")
    answer = 99
except ZeroDivisionError:
    print ("Divide by zero")
    answer = 0
except Exception as e:
    print("something went wrong")
    print(type(e))
    print(e)     

finally:
    # this code gets run regardless of wheter or not there was an exception
    print (f"The answer is {answer}")




print ("finished")


# n = input ("enter a number:")

# try:
#     n = int(n)
# except:
#     # generates an error - forcing the calling code to provide an exception handler
#     raise ValueError("invalid value")




























# exception handling
# alot more optimistic - glass is half full
# doesn't necessarily mean less code
# try:
#     DoSomething(n)
#     DoSomethingElse()
# except NetworkException:
#     print ("network error")
# except FileNotFoundError:
#     print ("File error")
# except ValueError:
#     print ("some value wrong")
# except:
#     print ("something went wrong")




# traditional error handling
# c programming
# glass is half empty - always expecting the worst
# n = 0
# if n != 0:
#     r = DoSomething(n)

# if r == -1:
#     print ("network error")
# elif r == -2:
#     print ("file error")
# elif r == -3:
#     print ("some other error")
# else:
#     print ("everything is ok")

# r = DoSomethingElse(0)

# if r == -1:
#     print ("network error")
# elif r == -2:
#     print ("file error")
# elif r == -3:
#     print ("some other error")
# else:
#     print ("everything is ok")








