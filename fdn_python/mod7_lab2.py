"""

Module 7 - Lab 2

Practice installing, importing and using external python modules while learning how to scrape (extract data from) web pages. 

"""

"""
import requests
from bs4 import BeautifulSoup

url = "https://wiki.python.org/moin/IntroductoryBooks"
response = requests.get(url)
print(response.headers)
content = response.content


# Parsing Web Pages
soup = BeautifulSoup(content)

print("*" * 20)

print(soup.prettify())
print("Title:", soup.title)
print("Soup title string:", soup.title.string)

all_a = soup.find_all("a")
for x in all_a:
    print(x)

all_a_https = soup.find_all("a", "https")
for x in all_a_https:
    print(x, "\n")

print("Index 0:", all_a_https[0])

for x in all_a_https:
    print(x.attrs['href'], "\n")

data_dict = {}
for a in all_a_https:
    title = a.string.strip()
    data_dict[title] = a.attrs['href']
    print("Data_dict[title]: \n", data_dict[title])

for k, v in data_dict.items():
    print("KEY:", k, "\n VALUE:", v, "\n")

"""

# Now that you've worked through this tutorial, try to parse data from another web site


import requests
from bs4 import BeautifulSoup

url = "https://wiki.python.org/moin/IntroductoryBooks"
response = requests.get(url)
# print("Response.headers:", response.headers)
content = response.content

soup = BeautifulSoup(content)
soup.prettify()
print("Title:", soup.title)
print("Title as string:", soup.title.string)

all_a = soup.find_all("a")
for x in all_a:
    print("This is X:", x)


all_a_https = soup.find_all("a", "https")
for x in all_a_https:
    print("This is X HTTPS:", x)

all_a_https[0]
for x in all_a_https:
    print(x.attrs['href'])