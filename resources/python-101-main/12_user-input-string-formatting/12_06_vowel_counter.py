# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.


#we will continue as from tomorrow.
# learn to prioritise me when you start your day, I deserve better.I am your future. I can actually automate all these task you are struggling to do.


user_input = input("Insert text: ")
count = 0
vowels = ["a", "e", "i", "o", "u"]
for x in user_input:
    if x in vowels:
        count += 1
print(count)
