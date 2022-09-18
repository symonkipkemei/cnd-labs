import random

mylist = [x**2 for x in range(0,5)]
print(mylist)


set1 = {y*2 for y in range(0,10)}
print(set1)

dictcomp = { k: v**2 for k, v in {"a": 1,"b": 2, "c":3, "d":4}.items()}
print(dictcomp)