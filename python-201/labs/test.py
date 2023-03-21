names  = {"kip":3,"sam":5, "lel":6,"nana": 9}


#sorts the key
print(sorted(names))


#sorted by key
print(sorted(names.items()))

#sorted by value
print(sorted(names.items(),key=lambda v:v[1]))

#conert to dict

names = {bundle[0]:bundle[1] for bundle in sorted(names.items(),key=lambda v:v[1],reverse=True) }
large = next(iter(names))
print(large)

#print first item in the bundle

for k,v in names.items():
    print(k,v)