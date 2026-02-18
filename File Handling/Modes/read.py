"""
Docstring for File Handling.Modes.read

Reading a file
"""

# open
f = open("File Handling/Modes/demo.txt", "r")

# read
data = f.read()
print(data)
# close
f.close()