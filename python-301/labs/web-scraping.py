import requests
import json
from pprint import pprint
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")


data = response.json()


with open("names.json", "r") as fin:
    data = json.load(fin)


pprint(data)
