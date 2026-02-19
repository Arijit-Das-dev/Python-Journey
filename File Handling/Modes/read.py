"""
Docstring for File Handling.Modes.read

Reading a file

Used Mode => "r"

**Note : File have to be exist which is going to be read
"""

# open
f = open("File Handling/Modes/demo.txt", "r")

# read
data = f.read()
print(data)
# close
f.close()