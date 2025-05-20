# data structures

#list []
values = [1,2,3]

#tuple ()
tvalues = (1, 2, 3)

#dictionary {}
dvalues = {
    1: "one", 
    2: "two", 
    3: "three"
}

# set - UNIQUE list
# DISTINCT list
# 
s = {1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6}
print (s)

l = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6]

s = set(l)

print (s)

s1 = {"red", "green", "blue", "violet"}
s2 = {"green", "indigo", "violet"}

combined_set = s1.union(s2)

print (combined_set)

combined_list = list(combined_set)

print (combined_list)

text = "this this this this this is some test text where some of the the text is repeated"

word_list = set(text.split(" "))

print (word_list)


print (s1.intersection(s2))














