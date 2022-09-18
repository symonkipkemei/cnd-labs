# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.
gen = (y for y in range(0,900))
print(gen)

for y in gen:
    print(y)