# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!


import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://codingnomads.co/"
page= requests.get(url)
soup = BeautifulSoup(page.text)
body = soup.find("div",class_="fusion-text fusion-text-3")
print(body.text)