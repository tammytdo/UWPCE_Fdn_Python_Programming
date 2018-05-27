"""

Module 4 - Lab 2

create a list of names to group by length, and then count how many names occur in each group.

"""


# Create the following name list and add in at least five female names (with repeats) to support women in tech! 
names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl',
 'luke', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew']
print("Names: ", names, "\n")
names.extend(["emily", "tammy", "susie", "susie", "tammy", "jenna", "sarah"])
print("Names extended: ", names, "\n")

# Create an empty dictionary to store your values
names_dict = {}

# Create a for loop that iterates through the names to add each one to the dictionary along with a count
for name in names:
    if name in names_dict:
        names_dict[name] = names_dict[name] + 1
    else:
        names_dict[name] = 1
print("Name dictionary: " names_dict)
