# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\\(<bCGHv^FfM}.;)khpkSYTfMA@>N"
print(len(strong_password))


list_longest_word = [longest_german_word, longest_hungarian_word, longest_finnish_word,strong_password]
len_longest_word = 0
for word in list_longest_word:
    if len(word) > len_longest_word:
        len_longest_word = len(word)
        longest_word = word
print(longest_word , len_longest_word)

