


names ={0: 'symon', 1: 'kip', 2: 'lel', 3: 'sap', 4: 'reter', 5: 'tyio', 6: 'uio', 7: 'uopw'}
count = 0

for x in names:
    print(x, names[x])
print(names)

for a, x in names.items():
    print(a, x)


names[1] = "Kiplelgo"

print(names)


print('dictionariesA\n')
my_dict = {(1, "hi")}
print(type(my_dict))

print('dictionariesB\n')
my_dict = {}
my_dict[1] = "hi"

print(type(my_dict))