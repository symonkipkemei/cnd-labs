


import requests
from bs4 import BeautifulSoup
from pprint import pprint




for page_no in range(1,18):
    URL = "https://coreyms.com/"

    CUSTOM_URL = URL + f"page/{page_no}"

    page = requests.get(CUSTOM_URL).text

    soup = BeautifulSoup(page,"lxml")

    #print(soup.prettify())


    for index,article in enumerate(soup.find_all("article"), 1):
        header = article.h2.text
        content = article.div
        description = content.p.text
        link = article.iframe
        print(index, header, end="\n")



    


