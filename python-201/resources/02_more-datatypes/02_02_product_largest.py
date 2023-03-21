# Take in a few numbers from the user and place them in a randlist.
# If you want, you can instead use the provided randomly generated
# randlist called `randlist` to simulate the user input.
#
# Find the largest number in the randlist and print the result.
# Calculate the product of all of the numbers in the randlist.

#from resources import randlist

#print(randlist)


#establish length of list
#length = len(randlist)
randlist = [1, 5, 6, 2]
length = len(randlist)
print(length)

# pick one item
for x in randlist:
    #set count to 0
    count = 0
    # compare with the rest of the numbers
    for y in randlist:
        # if x is greater than a selected number, award 1
        if x > y:
            count += 1
        
    # if x is greater than all numbers except itself, stop...declare the largest
    if count == (length - 1):
        largest_number = x
        print("largest :", largest_number)
        break
        




