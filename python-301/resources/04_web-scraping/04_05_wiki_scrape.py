# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

URL = "https://en.wikipedia.org/wiki/Web_scraping"

import requests
from bs4 import BeautifulSoup
from pprint import pprint


page = requests.get(URL)

# create a bs object

soup = BeautifulSoup(page.text)

# parse all the paragraphs
paragraph = soup.find_all("a")

