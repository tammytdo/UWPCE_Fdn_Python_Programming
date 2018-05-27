"""

Assignment 04

"""


# Define two lists at the top of your file
names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", 
         "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19] 


# These lists should match up, so Alice’s age is 20, Bob’s age is 21, and so on.
print(len(names) == len(ages))

# Use the zip function to merge these lists into a dictionary
# The names should be the keys, and the age should be the value.
names_ages_list = list(zip(names, ages))
print(names_ages_list)

names_ages_dict = dict(names_ages_list)
print(names_ages_dict)
type(names_ages_dict)

for name, age in names_ages_dict.items():
    print("{} is age: {}".format(name, age))

# Ask the user to input a user name
# Use a while loop to keep asking the user to input a user until they find someone in the dictionary
#give them up to five tries by using a counter outside the while loop
count = 0
input_name = input("Input a name: ")
while count < 5:
    count += 1
    if input_name in names_ages_dict:
        # Return the user's age
        print("{}'s age is {}.".format(input_name, names_ages_dict[input_name]))
        break
    else: 
        print("Name not found")
        input_name = input("Input a name: ")


