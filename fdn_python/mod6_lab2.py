"""

Module 6 - Lab 2

Practicing with Unix

"""

# Create a new directory called testing
# Change into the new directory
# Create a new file called test.txt
# List the contents of the directory to make sure that your file was created
# Add a line to the file that says "line1"
# Add a line to the file that says "line2"
# Add another a total of ten lines, as above (line3,line4,etc.)
# View the first three lines of the file
# View the last five lines of the file
# Stretch Goal: can you figure out how to count the number of lines in the file using the "wc" command?

# Tammys-MBP:~ tammydo$ mkdir testing
# mkdir: testing: File exists
# Tammys-MBP:~ tammydo$ cd testing
# Tammys-MBP:testing tammydo$ touch test.txt
# Tammys-MBP:testing tammydo$ ls
# test.txt    text.txt
# Tammys-MBP:testing tammydo$ echo "line1" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line2" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line3" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line4" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line5" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line6" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line7" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line8" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line9" >> test.txt
# Tammys-MBP:testing tammydo$ echo "line10" >> test.txt
# Tammys-MBP:testing tammydo$ head -3 test.txt
# line1
# line2
# line1
# Tammys-MBP:testing tammydo$ tail -5 test.txt
# line6
# line7
# line8
# line9
# line10
# Tammys-MBP:testing tammydo$ wc -l test.txt
#       12 test.txt
# Tammys-MBP:testing tammydo$ 
