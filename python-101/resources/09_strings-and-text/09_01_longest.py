# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"


# we can alternatively use python to help us establish which is the largest by use of dictionary
# since thhe comparison is short we wil do it ourselves

print (longest_finnish_word,len(longest_finnish_word) )
print(longest_hungarian_word,len(longest_hungarian_word) )
print (longest_german_word,len(longest_german_word) )
print(strong_password, len(strong_password))


