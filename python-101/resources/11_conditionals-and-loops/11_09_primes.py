# Print out every prime number between 1 and 1000.

for x in range(2, 1000):
    count = 0
    for y in range (2,x):
        if x % y == 0:
            count += 1
            
            
    if count == 0:
        print(f"Prime number : {x}")
