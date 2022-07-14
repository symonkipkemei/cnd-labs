# Your cat just had kittens! Now you want to put up an ad to give them
# to your friends. You'll need to save all names of the kittens,
# confirm that they each of them is cute, and show a message that
# that kitten is ready for adoption.
#
# Break this task up into a couple of steps of pseudocode
# and write the pseudocode below in code comments.
# You don't need to write any functional code, just map out the steps.

import random

# naming the kittens
kittens = ["sarah", "cynthia", "brian", "lawi", "kipchumba", "lewar"]

# descriptive description about them

description = ["charming", "cute", "handsome", "colorful", "playful"]

# displaying the message to friends
print("I have the following kittens for sale, they are: ")
for  kitten in kittens:
    print(kitten, "is", random.choice(description))