# basic_fileio.py

# traditional mecanism
file = open("file.txt", "r")
contents = file.read()
print (contents)
file.close()

# preferred mechanism 

with open("file.txt", "r") as file:
    contents = file.read()
    print (contents)

# nb - no need to close 
# the file will be automatically closed when the 
# with block exits.

# context management
with open("newfile.txt", "a") as file:
    file.write("Is this working")



