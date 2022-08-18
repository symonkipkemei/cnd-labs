# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist


# Write your code below here

# list
new_list = []
sub_list = []


#sort list
randlist.sort()



# after soring list, check if the length is odd or even
length_of_randlist = len(randlist)
# if odd apend 0 to make it even.
if length_of_randlist % 2 != 0:
    randlist.append(0)
    for num in randlist:
        # add num to sub list
        sub_list.append(num)
    
        sub_length = len(sub_list)
    
        # check to ensure the length does not exceed 2
        if sub_length == 2:
            sub_tuple = tuple(sub_list)
            new_list.append(sub_tuple)
    
            # reset sub list to 0
            sub_list = []
     
    print(new_list)

# if even continue
else:
    for num in randlist:
        # add num to sub list
        sub_list.append(num)

        sub_length = len(sub_list)
    
        # check to ensure the length does not exceed 2
        if sub_length == 2:
            sub_tuple = tuple(sub_list)
            new_list.append(sub_tuple)
    
            # reset sub list to 0
            sub_list = []
     
    print(new_list)