# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

list_names = [len(longest_german_word), len(longest_hungarian_word), len(longest_finnish_word), len(strong_password)]
print(list_names)
list_names.sort(reverse= True)

print(list_names)
print("The largest is",list_names[0])


