"""
Docstring for File Handling.With Keyword.Example
"""

# Creating a non-existing file

with open("File Handling/With Keyword/New_file.txt", "w") as f:

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

    print("=="*50)
    print("____FILE CREATED SUCCESSFULLY____")
    print("=="*50)