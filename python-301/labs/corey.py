


import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

data = {}
post_id = 0
for page_no in range(1,18):
    URL = "https://coreyms.com/"

    CUSTOM_URL = URL + f"page/{page_no}"

    page = requests.get(CUSTOM_URL).text

    soup = BeautifulSoup(page,"lxml")

    #print(soup.prettify())


    for index,article in enumerate(soup.find_all("article"), 1):
        header = article.h2.text
        description = article.find("div", class_="entry-content").p.text
        post_id = post_id + 1

        try:
            link = article.find("iframe",class_="youtube-player")["src"]
            vid_id = link.split("/")[4]
            vid_id = vid_id.split("?")[0]
            video_link = f"https://www.youtube.com/watch?v={vid_id}"
            print(video_link)
        except TypeError:
            video_link = None

        data[post_id]=[header,description,video_link]

with open("coreyschafer.json", "w") as cs:
    json.dump(data,cs)


        
        



    


