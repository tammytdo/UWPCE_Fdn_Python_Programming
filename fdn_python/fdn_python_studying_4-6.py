"""

Foundations of Python
UW Continuing Education
Modules 4-6

Study notes

"""

# sets
colors = {"red", "green", "blue", "blue"}
print(colors)

test_string = "what the what?"
print(set(test_string))

test_list = [1, 1, 1, 2]
print(test_list)
print(set(test_list))

print(set(test_string.split(" ")))

# Adding to a set
colors.add("pink")
print(colors)

colors.add("green")
print(colors)

colors.update(["black", "white", "tan"])
print(colors)

# Removing Items from a Set
colors.discard("purple")
print("Discarded purple: ", colors)

# colors.remove("purple")

colors.clear()
print(colors)


a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# union
print(a.union(b))
print(b.union(a))
print(a | b)

# intersection
print(a.intersection(b))
print(b.intersection(a))

# difference
print(a.difference(b))
print(b.difference(a))
print(b - a)

# symmetric difference
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# frozen sets
cities = frozenset(["Frankfurt", "Basel", "Freiburg"])

# Set Membership
print("Frankfurt" in cities)
print("Tuscany" in cities)

# Iterating Through a Set
for city in cities:
    print(city)

# Tuples
# Making a Tuple
my_tuple = (1, "stuff", {"dict_key": "dict_val"}, [1, 2, 3])
print(my_tuple)

# Creating a single element tuple
lonely_tuple = (1,)
print(lonely_tuple)

# Accessing items in a tuple
print(my_tuple[1])
print(my_tuple[2])

# Iterating through a tuple
for i in my_tuple:
    print("-", i)

# Tuple Operations
# Membership
my_tuple = (1, 2, 3)
print(1 in my_tuple)

# Iteration
for letter in my_tuple:
    print(letter)

# Indexing and Slicing
another_tuple = ("ham", "jam", "slam", "wham")
print(another_tuple[0])
print(another_tuple[-1])
print(another_tuple[1:])
print(another_tuple[1:3])

# Dictionaries
# Creating a Dictionary
sample_dict = {"key1": "value1", "key2": "value2"}
pop_dict = {"New York": 8175133, "Los Angeles": 3792621, "Chicago": 2695598}

# Dictionary Operations
# Accessing Items
print(pop_dict["New York"])
pop_dict.update({"Seattle": 668342})
print(pop_dict)
pop_dict["Seattle"] = "too many people, not enough public transit"
print(pop_dict)
del pop_dict["Seattle"]
print(pop_dict)
print("Seattle" in pop_dict)

# Methods Unique to Dictionaries

# get()
pop_dict.get("Fake key value!")
print(pop_dict)

print(pop_dict.keys())
print(pop_dict.values())
print(pop_dict.items())

# Iterating Through Dictionaries
for key, value in pop_dict.items():
    print(key, value)

# Counting in Dictionaries
letter_counts = {}
for x in "Mississippi":
    print(x)
    if x in letter_counts:
        letter_counts[x] = letter_counts[x] + 1
    else:
        letter_counts[x] = 1
print(letter_counts)

# Sorted Dictionaries
print("Sorted: ", sorted(pop_dict.keys()))


# Lists From Dictionaries
cheeses = ["brie", "feta", "butterkasse"]
countries = ["France", "Greece", "Germany"]
cheesy_tuples = zip(countries, cheeses)
print(cheesy_tuples)
# use the zip function, which returns an iterator. Because we can't do much with an iterable object, we need to convert that object to a list of tuples, using the list function:
cheesy_tuples = list(zip(countries, cheeses))
print(cheesy_tuples)
# now convert the list into a dictionary:
cheese_dict = dict(cheesy_tuples)
print(cheese_dict)

# Dictionaries from Lists
cheesy_key_list = list(cheese_dict.keys())
print(cheesy_key_list)

cheesy_value_list = list(cheese_dict.values())
print(cheesy_value_list)

# A regular dictionary is not ordered or sorted. It may appear in the same order sometimes, but it is not guaranteed to appear in any order any time you iterate through it.
print('Regular dictionary')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for key, val in d.items():
    print(key, val)

# Ordered Dictionaries
# import a module to work with dictionaries
from collections import OrderedDict
print('\nOrderedDict:')
od = OrderedDict()
od['a'] = 'A'
od['b'] = 'B'
od['c'] = 'C'
od['d'] = 'D'
od['e'] = 'E'

for key, value in od.items():
    print(key, value)

# Dictionary that maintains keys in sorted order
from sortedcontainers import SortedDict

print ('\nSortedDict:')
d = SortedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for key, value in d.items():
    print(key, value)

# File Handling
# Read from text files
# Opening a file
f = open("./land_time_forgot.txt")
print(f)
type(f)

# Read from text files
f = open("./land_time_forgot.txt")
print(f)

import os
print(os.getcwd())
print(os.listdir)

# Reading CHARACTERS from a File
print(f.read(1))
print(f.read(12))

# Going back to the top of the file
f.seek(0)

# reading LINES from a file
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

print("--------------")

# Reading in all lines from a file into a list
# print(f.readlines())
# print("--------------")

infile = f.readlines()
print("Infile:", infile)

# Garbage Collection of the File Object
print("Anything here?: ", f.read())
print("Garbage-handled. The pointer is gone. Need to re-open the file. ")

# Iterating Through a File
# how does this know to read lines vs reading words?
f = open("./land_time_forgot.txt")
for x in f:
    print(x)

# Closing a File Object
f.close()

# Opening and Closing with with()
with open("./test_file.txt") as file:
    print("Test1: ", file.read(5))
    print("Test2: ", file.readline(5))
    print("Test3: ", file.readlines())

# Access Modes
# Write to text files
with open("./test_file.txt", "w") as f:
    my_string = "stuff"
    f.write(my_string)
    print(my_string)

with open("./test_file.txt", "r") as f:
    print(f.readlines())

out_lines = ["Hello there! This is my first line! \n",
    "This is the second line \n", 
    "This is the last time I'm doing this..."]

with open("./test_file.txt", "a") as f:
    f.writelines(out_lines)

with open("./test_file.txt", "r") as f:
    print(f.readlines())

# Parsing Text Files
with open("./months.txt", "r") as f:
    print(f.readlines())

# Removing New Lines
for line in open("./months.txt"):
    line = line.strip()
    print(line)

f = open("./months.txt")
for month in f.readlines():  # why does this require: .readlines()?
    print("Month =", month.strip())

# Splitting Up Input
name_list = []
year_list = []

for line in open("./rose_winners.txt", "r"):
    line = line.strip()  # strip the new lines
    name, year = line.split(" - ")  #split by the dash
    name_list.append(name)
    year_list.append(year)

rose_winner_list = zip(name_list, year_list)
print(rose_winner_list)

rose_winner_dict = dict(rose_winner_list)
print(rose_winner_dict)

for key, val in rose_winner_dict.items():
    print(key + ", " + val)

# Working with other file types
import csv

fh = open("./City_of_Seattle_Wage_Data.csv")
reader = csv.reader(fh)
for row in reader:
    print(row)

# csv.reader can also read TXT/TSV files by adding the "delimiter" argument to your csv.reader() call:
fr = open("./rose_winners.txt")
reader = csv.reader(fr, delimiter="\t")
for row in reader:
    print(row)

# Writing to CSV/TSV
infile = open("./rose_winners.txt")
reader = csv.reader(infile)
print("Reader: ", reader)
outfile = open("rose_winner.tsv", "w")
writer = csv.writer(outfile, delimiter = "\t")
print("Writer: ", writer)

for row in reader:
    writer.writerow(row)
    print(row)

infile.close()
outfile.close()


# Writing a Dictionary to File
names = []
years = []

for line in open("./rose_winners.txt"):
    line = line.strip()
    name, year = line.split("-")
    names.append(name)
    years.append(year)

name_year = zip(names, years)
rose_dict = dict(name_year)
print(rose_dict)

with open("rose_dict.txt", "w") as outfile:
    for name, year in rose_dict.items():
        outfile.writelines("{}:{}".format(name, year))
        outfile.write("\n")

# Functions
# Abstraction
# Creating Functions
def mad_libs(verb, noun):
    print("Summer Goals: \n \
    1. I will {my_verb} every day \n \
    2. I will go to a {my_noun} with my mom.".format( \
                            my_verb=verb, my_noun=noun))

mad_libs("shimmy", "ski tube")

# Default Parameters
def mad_libs2(verb="gleam the cube", noun="pub crawl"):
    print("Summer Goals: \n \
    1. I will {my_verb} every day \n \
    2. I will go to a {my_noun} with my mom.".format( \
                            my_verb=verb, my_noun=noun))

mad_libs2()

# Encapsulation
ten_pct = 10/100
print(ten_pct)

def percent(input_num):
    return input_num / 100

def integer(input_num):
    return input_num * 100

print(percent(4))
integer(4)

# Names
# Namespaces
# Global vs Local Namespace
print(dir())

def print_string():
    silly_string = "Is this going to erase the global variable?"
    print(silly_string)

silly_string = "This is a global string!"
print_string()
print(silly_string)

def print_string():
    global silly_string
    print(silly_string)
    silly_string = "Is this going to erase the global variable?"
    print(silly_string)

print_string()

# Scope
# Viewing Local and Global Variables
print(globals())
print(locals())

print("my_var" in globals())

# Making a Function
# input_num = 10
def fizzbuzz(input_num):
    if input_num % 3 and input_num % 5 == 0:
        print("fizzbuzz")
    elif input_num % 3 == 0:
        print("fizz")
    elif input_num % 5 == 0:
        print("buzz")
    else:
        print("Not divisible by 3 or 5")

fizzbuzz(50)


names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# lists_to_dict()
def lists_to_dict(names, ages):
    zip_dict = dict(zip(names, ages))
    return zip_dict

# get_age()
def get_age(zip_dict):
    input_age = int(input("Please input an age: "))
    while input_age not in zip_dict.values():
        input_age = int(input("There's nobody in the database with that age, please try again: "))
    return input_age

# age_search()
def age_search(input_dict, input_age):
    name_list = []
    # where does input_dict come from?
    for name in input_dict:
        if input_dict[name] == input_age:
         name_list.append(name)
    if len(name_list):
        print("Found: {}".format(", ".join(name_list)))
    else:
        print("Didn't find anyone")

def run_me(names, ages):
    my_dict = lists_to_dict(names, ages)
    my_age = get_age(my_dict)
    age_search(my_dict, my_age)

run_me(["Betty", "Jim", "Steve", "Sally"], [12,12,34,57])

# Command Line Basics
# terminal
# Basic Commands