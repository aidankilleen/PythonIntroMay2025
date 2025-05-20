# print_investigation.py
# By: Aidan
# Date: 19/05/2025

from time import sleep


print ("Print investigation")

print ("one", "two", "three", sep="-->")

print ("one", end="")
print ("two")

print ("=" * 30)

message = "This is a message "

print (message)

def rotate_text(text = "some placeholder ", direction="rtl", timeout=0.5):
    """
    Rotate the supplied text using the supplied direction with timeout between iterations

    direction: use "ltr" or "rtl"

    timeout: delay (in seconds) between iterations
    """
    # docstring - used for self-documenting out code
    for i in range(len(text)):
        if direction=="ltr":
            text = text[-1] + text[:-1]
        else:
            text = text[1:] + text[0] 

        print (text, end="\r")
        sleep(timeout)

rotate_text(timeout=0.2)

rotate_text(message, timeout=0.1) # "rtl"

rotate_text(direction="ltr", text="This is a different message ", timeout=0.3)






























