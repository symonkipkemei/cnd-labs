# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

from curses.ascii import isdigit


secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""
for x in secret:
    if x.isdigit():
        pass
    else:
        solution += x

print(solution)
