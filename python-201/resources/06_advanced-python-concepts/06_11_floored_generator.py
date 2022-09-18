# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?


nums = range(1, 1000000)

gen = (div for div in nums if div // 111 == 1111 )

for x in gen:
    print(x)