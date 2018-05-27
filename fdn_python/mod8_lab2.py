"""

Mod 8 - Lab 2

Opening a nonexistant file

"""
import sys

# When you try to open a file that doesn't exist on your file system the open function raises a nice error called FileNotFoundError

# write some pseudo code that opens a non-existant file location

try:
    with open("text_file.txt") as f:
        for line in f:
            print(line)

#use try/except to handle the FileNotFoundError and output a nicer message for the user about what happened
except FileNotFoundError:
    print("Error: File was not found.")
    raise FileNotFoundError

except Exception:
    print("An unexpected error occurred")

# Let's say some other type of error happens but we don't know the specifc name of it. How can our try/except handle this?
finally:
    try:
        file.close()
    except Exception:
        sys.exit()
