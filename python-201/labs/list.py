

fruits= ["mango", "watermelon", "banana", "oranges", "carrots", "pears", "palms", "grapes"]



print(fruits[::-1])


print(fruits[5:])


print(fruits[-1])




bucket_list = ["rootop love", "sun bath", "go to Namibia desert", "Kill a gazelle", "impact the world", "influence people"]

bucket_list[0] += " making with my partner"

print(bucket_list)

a = [1, 2, 3 ,4 ]
b = [1 ,2 ,3 ,4 ]
    
print(a== b)
print(a is b)


b = a

print(a== b)
print(a is b)

b[0] = 4

print(a)

bucket_list.append("Travel to kapkelelwa")
print(bucket_list)

bucket_list.insert(0, "Travel to bahamas")
print(bucket_list)

bucket_list.pop()
print(bucket_list)

bucket_list.remove("sun bath")
print(bucket_list)

names = [1, 2, 3, 4, 2]

# remove two from the list

names.remove(2)
print(names)


# specify the index
names = [1, 2, 3, 4, 2]
names.remove(names[4])
print(names)

names = [1, 2, 3, 4, 2]
del names[4]
print(names)

item_index = names.index(2)
print(item_index)

names = [1, 2, 3, 4, 2]
names.pop()
print(names)


names = [1, 2, 3, 4, 2]
name = names.pop(0)
print(name)

#list comprehension
names = ["Kipchunba", "Sammy", "Lavenda","Otieno" ] 
lower_case = [x.lower() for x in names]

print(lower_case)