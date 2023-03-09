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
import json



def extract_links(URL):
    # create a bs object
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,"lxml")

    data = {}
    for para in soup.find_all("p"):
        try:
            links = para.find_all("a")
            for link in links:
                text = link.text
                page_link = link["href"]
                if page_link[0] == "/":
                    full_link = f"https://en.wikipedia.org{page_link}"
                    data[text] = full_link
        except TypeError as e:
            link = None


    with open("wiki_web_scrap.json", "w") as wws:
        json.dump(data,wws)



def extract_texts():

    with open("wiki_web_scrap.json","r") as r:
        data = json.load(r)

    for key,link in data.items():
        page = requests.get(link)

        soup = BeautifulSoup(page.text, "lxml")

        main_content = soup.find("main")
        divs = main_content.find_all("div", class_="mw-parser-output")
        for div in divs:
            with open(f"resources/04_web-scraping/wiki/{key}.txt","a") as f:
                f.write(div.text)

        print("file created successfully \n")


if __name__ == "__main__":
    extract_texts()
    


   
    
    
    