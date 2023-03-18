# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?


num =9
num = float(num)
print(num)

num =9.6
num = int(num)
print(num)
print(type(num))

ans = 9.0/3
print(ans)

ans1 = ans * num
print(ans1)