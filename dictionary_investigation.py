# dictionary_investigation.py
# By: Aidan
# Date: 19/05/2025

# no need for a list to heterogenous (items are all the same type)
list = [1, 4, 2, 3, "one", "two", 1.234, [1, 1, 1]]

# dictionary can also contain different types
dict = {
    "name": "Aidan", 
    "company": "Professional Training", 
    "phone": "021 4632010", 
    "id": 12345, 
    "average": 5.67,
    "languages": ["c", "c++", "python", "perl"]
}

print (dict)

print(dict["name"])
print(dict["company"])
print(dict["phone"])

print(dict.keys())

for key in dict.keys():
    print (f"{key}: {dict[key]}")

print (dict.values())

# dictionaries are mutable
dict["name"] = "Changed Name"
print (dict)

dict["Country"] = "Ireland"
print (dict)

text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[33]
Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[34][35]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language, and he first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[37]
Python consistently ranks as one of the most popular programming languages, and it has gained widespread use in the machine learning community.
"""

words = text.split(" ")

word_counts = {}

for word in words:

    if word in word_counts:
        word_counts[word] += 1
    else: 
        word_counts[word] = 1

print (word_counts)
































