# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

sum = 0
count = 0

for x in range(1, 1001):
    count += 1
    if count == 5:
        print(x)
        count = 0