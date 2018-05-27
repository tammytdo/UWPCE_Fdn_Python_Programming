"""

Assignment 07

Module 7 - Lab 2

Practice installing, importing and using external python modules while learning how to scrape (extract data from) web pages. 

# IN PROGRESS

"""

import requests
from bs4 import BeautifulSoup


# Create a function that allows you to pull out a tag (passed as an argument to your function) from any URL (also passed as an argument to your function)
# Create a function to format the output in a meaningful way (ex: If you are parsing anchor tags, then get the link, the alt text, and the text that was inside the link).
# Create a function to write the formatted results to a txt file
# Create a main function that allows the script to be run on its own from the command line

# Get user input for a URL and type of tag to parse from the URL.
def get_url_and_tag():
    url = input("Enter a url: ")
    tag = input("Enter a tag type: ")
    response = requests.get(url)
    print(response.headers)
    content = response.content
    return tag, response, content

# Parsing Web Pages
def parse_webpage(tag, response, content):
    soup = BeautifulSoup(content)
    soup.prettify()
    title = soup.title.string
    return soup
    return title

    find_tag = soup.find_all(tag)
    for x in find_tag:
        print("Found", tag, ":", x)

    data_dict = {}
    for a in find_tag:
        title = a.string.strip()
        data_dict[title] = a.attrs['tag']
        print("Data_dict[title]: \n", data_dict[title])

    for k, v in data_dict.items():
        print("KEY:", k, "\n VALUE:", v, "\n")

if __name__ == "__main__":
    a, b, c = get_url_and_tag()
    meaningful_output = parse_webpage(a, b, c)


# url = "https://wiki.python.org/moin/IntroductoryBooks"
# tag = "a"