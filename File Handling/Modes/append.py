"""
Docstring for File Handling.Modes.append

appending some text into a existing file

Used Mode : "a"

**Note : All the text will be append at the end of all text of that file
"""

f = open("File Handling/Modes/New_text_file.txt", "a")

text = """
==============================
        FILE HANDLING DEMO
==============================

Name: Arijit Das
Course: BCA
Subject: Python Programming

This is a demo text file created using Python.

Concepts Covered:
1. File Creation
2. Write Mode ("w")
3. Append Mode ("a")
4. With Statement
5. Automatic File Closing

Advantages of using 'with':
- Automatically closes the file
- Prevents memory leaks
- Cleaner and safer code

End of demo file.

"""

f.write(text)
f.close()