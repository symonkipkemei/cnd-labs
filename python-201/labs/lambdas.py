counties = ["Naironi, Baringo", "Laikipia", "Kirinyaga", "Embu", 'Siaya',"Makueni"]

def last_char(x):
    return x[-1]

counties.sort(key=last_char, reverse=True)
print(counties)



capital = list(map(lambda x:str.upper(x), counties))
print(capital)

counties = [str.upper(x) for x in counties]
print(counties)

dict = {n: n*2 for n in range(5)}

print(dict)