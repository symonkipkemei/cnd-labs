# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1


user_numbers = [1,2,3,4,5,6,7,8,9,10]


# separate even from odd and sort in ascending order
user_numbers_even = [num for num in user_numbers if num % 2 == 0]
user_numbers_even.sort(reverse= False)
print(user_numbers_even)

# separate odd from even and sort in descending order
user_numbers_odd = [num for num in user_numbers if num % 2 != 0]
user_numbers_odd.sort(reverse= True)

print(user_numbers_odd)

# merge into one list
combined = user_numbers_even + user_numbers_odd
print(combined)