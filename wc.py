# stdin_investigation.py
# linux like utility 
# perform word count operation on 
# file or stdin
import sys

file = sys.stdin
if len(sys.argv) == 2:
    # a file was provided
    file = open(sys.argv[1], "r")

line_count = 0
character_count = 0
word_count = 0
for line in file:
    line_count += 1
    character_count += len(line)
    word_count += len(line.split(" "))

print (f"Lines:{line_count} {word_count} {character_count} ")

    