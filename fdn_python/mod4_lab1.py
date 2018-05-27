"""

Module 4 - Lab 1

Using sets to analyze text

"""

import string

# Given the following two sentences
s1 = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man — for precisely the same reasons."
s2 = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was this: So long and thanks for all the fish."
print("\n")

# Determine how to remove all the punctuation from the sentences before turning them into a set?
for punc in string.punctuation:
    s1 = s1.replace(punc, "")


# Determine the number of unique words in each sentence
s1_unique = set(s1.split(" "))
print("Num of unique words:", len(s1_unique))
print("s1 Unique:", s1_unique)
print("\n")

s2_unique = set(s2.split(" "))
print("Num of unique words:", len(s2_unique))
print("s2 Unique:", s2_unique)
print("\n")


# Determine the number of words that appear in both sentences
print("Num of words in both sentence:", (len(s1_unique) + len(s2_unique)))
print("Words in both sentences:", set(s1_unique.intersection(s2_unique)))
print("\n")

# Determine the number of words that are contained in either one sentence or the other, but not in both
print("Num of words in one sentence or the other but not both:", len(set(s1_unique.symmetric_difference(s2_unique))))
print("Words in one or the other but not both:", set(s1_unique.symmetric_difference(s2_unique)))
