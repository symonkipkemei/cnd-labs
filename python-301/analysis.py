import json
from pprint import pprint

with open("coreyschafer.json") as cs:
    data= json.load(cs)


topics = [ [value[0], value[2]] for value in data.values()]
pprint(topics)
