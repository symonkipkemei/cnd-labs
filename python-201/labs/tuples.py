empty = ()
print(type(empty))


tupl = 1, 4, "symon"
print(tupl)
print(type(tupl))

tuple1 = (1, 4, "symon")
tuple2 = tuple1[:3]
print(tuple2)


great = tuple1 + tuple2

name = "gueufbbnfkwehlhewfh"
name= tuple(name)
print(len(name))

for element in great:
    print(element)


friends = ("winny", "kipchumba","langat", "mercy", "beverly", "materte", "agnes")

friend = friends[1]
print(friend[1])


for friend in friends:
    print(friend[-1])



print("Break\n")

numbers = [1, 2, 3]
numbers.extend([8,9])
print(numbers)