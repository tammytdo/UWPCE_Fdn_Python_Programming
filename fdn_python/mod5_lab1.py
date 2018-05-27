"""

Module 5 - Lab 1

Text analysis of Project Gutenberg's The Land That Time Forgot, by Edgar Rice Burroughs.

https://ia800301.us.archive.org/13/items/thelandthattimef00551gut/551.txt

"""


# Read the file into a list
with open("./land_time_forgot.txt", "r") as f:
    infile = f.readlines()

# Calculate the total number of lines in the file
total_lines = len(infile)  # 3,973 total lines

# Calculate the lines that are in 1/3rd of the file
total_lines_third = int(total_lines//3)  # 1,324 lines per third

# Store the middle third of the book's lines in a list (hint: use list accessor methods)
first_third = infile[:total_lines_third] #total_lines_third represents the 1,324th line 
mid_third = infile[total_lines_third+1: total_lines_third * 2]
last_third = infile[(total_lines_third * 2) + 1: ]
#print(mid_third)  # uncomment to print the list

# Print the number of lines in the file
print("Total lines in file:", total_lines)

# Print the number of lines in the middle third of the book
print("Total lines mid third of file:", len(mid_third))

# Print the line that is 1/3rd of the way through the book 
one_third_line = mid_third[0]
print("The line that is 1/3 of the way through the file:\n", one_third_line)

# Print the line that is 2/3 of the way through the book
second_third_line = last_third[0]
print("The line that is 2/3 of the way through the file:\n", second_third_line)

# Write the lines you printed above to a file
with open("./new_file", "w") as file:
    one_third_line
    second_third_line

with open("./new_file", "r") as file:
    file.readlines()















