# for_else_investigation.py

for i in range(1, 11):
    # continue terminates this iteration
    if i ==3:
        continue
    print (i)
    #if i == 5:
    #    break
else:
    # only gets run if the main loop doesn't break
    # i.e. if the loop runs to competion
    print ("Else statement activated")

# break will terminate the loop
print ("finished")

names = ["Alice", "Bob", "Carol", "Dan", "David"]

for name in names:
    if name == "David":
        print ("Found David")
        break
else:
    print ("David not found")




