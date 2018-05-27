"""

Module 6 - Lab 1

Update a script to use functions


"""
# Update the code to have a function that reads in the file and returns contents as a list
def read_and_parse_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines


# Update the code to have a function that converts the list of book lines into a list of the words
def split_lines_to_words(lines):
    word_list = []
    for line in lines:
        word_list.extend(line.split(" "))
    return word_list


# Update the code to have a function that calculates the word count by taking in the word list and return the dictionary
def calc_word_freq(word_list):
    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1
    return word_freq

# def max_word(word_freq):
#     max_word = max(word_freq, key=word_freq.get)

#     print("Most frequent word is '{}' with frequency {}".format(
#         max_word, word_freq[max_word]))

# Update the code to have a function that calculates the minum word frequency and gets the list of words from the word frequency dictionary
def calc_min_words(word_freq):
    min_word_freq = min(word_freq.values())
    min_words = []
    for word, fr in word_freq.items():
        if fr == min_word_freq:
            min_words.append(word)
    return min_word_freq, min_words
    print("The lowest word_frequency is {} and there are {} words in the book with that word_frequency".format(min_word_freq, len(min_words)))

# Create a main section at the bottom of the code
if __name__ == "__main__":
    # Update the main section to call the function that reads the file and the function that converts the book lines into a list.  Remember to pass the appropriate variable into the function and return the value you want and store it in a variable
    my_lines = read_and_parse_file("./land_time_forgot.txt")
    my_words = split_lines_to_words(my_lines)
    # Update the main section to create a word set and print the sentence about unique words
    word_set = set(my_words)
    print("There are {} words in the book and {} of them are unique".format(len(my_words), len(word_set)))
    # Update the main section to call the function that calculates the word count and find the word with the maximum count (hint: use max)
    my_freq = calc_word_freq(my_words)
    max_word = max(my_freq, key=my_freq.get)
    print("Most frequent word is '{}' with frequency {}".format(max_word, my_freq[max_word]))
    # Update the main section to call the minimum word function and print the results
    min_word = calc_min_words(my_freq)
    mw_freq, min_word_list = calc_min_words(my_freq)    
    print("The lowest word_frequency is {} and there are {} words in the book with that word_frequency".format(mw_freq, len(min_word_list)))
