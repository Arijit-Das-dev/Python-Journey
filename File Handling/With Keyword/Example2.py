"""
Docstring for File Handling.With Keyword.Example2
"""

with open("File Handling/With Keyword/New_File.txt", "r") as f:

    data = f.read()
    print(data)

    print("=="*50)
    print("____FILE READ SUCCESSFULLY____")
    print("=="*50)