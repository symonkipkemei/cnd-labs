# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 1000000)

gen = (div for div in nums if div % 111 == 0 )

for x in gen:
    print(x)