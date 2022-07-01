# Write the necessary code to display the follow message to the console
#       Time for co-co-co-ding.
# Use an operator and f-string formatting to create this output
print("Time for co-co-co-ding.")


# take the first two characters of a string and reverberate
user_time = input("Time for: ")

# isloate the first two characters
char_two = user_time[0:2]

#reverberate the charaters three times and store in reverb word
reverb_word = ""
for x in range(0,3):
    reverb_word += char_two + "-"

# join the reverb word with the rest of the sentence
complete_word = reverb_word + user_time[2:]

# display message
print("Time for", complete_word)