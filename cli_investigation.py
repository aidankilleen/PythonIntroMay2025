# cli_investigation.py
import sys
print ("cli investigation")
try:
    filename = sys.argv[1]
    with open(filename, "r") as file:

        count = 0
        line = file.readline()

        while line:
            count+=1
            line = file.readline()

    print (f"#lines:{count}")
except IndexError:
    print (f"Usage:")
    print (f"python cli_investigation.py FILE")

except FileNotFoundError:
    print (f"file {filename} not found")
except:
    print ("something went wrong")


