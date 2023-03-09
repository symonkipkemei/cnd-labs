# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.


import json
from pprint import pprint
from bs4 import BeautifulSoup
import requests


URL = "https://www.archidatum.com/projects/"

def article_content(articles):
    for article in articles:
        project_description = article.a.text.split("/")
        project_name = project_description[0]
        try:
            project_architect = project_description[1]
        except IndexError:
            project_architect = None
            print(f"architect locked in {project_description}")

        
        link = article.a["href"]

        print(f"project architect: {project_architect}")
        print(f"project name: {project_name}")
        print(f"project link: {link}\n")


for page_no in range(1,13):
    print(f"page no {page_no}")
    URL = f"{URL}?page ={page_no}"

    page = requests.get(URL).text

    soup = BeautifulSoup(page,"lxml")

    articles_white = soup.find_all("div",class_="background_white")
    articles_grey = soup.find_all("div",class_="entry_content_background content_font")

    article_content(articles_grey)
    article_content(articles_white)


 
