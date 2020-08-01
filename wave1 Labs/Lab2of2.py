#1. What is the length of the string variable verse?
#2. What is the index of the first occurrence of the word 'and' in verse?
#3. What is the index of the last occurrence of the word 'you' in verse?
#4. What is the count of occurrences of the word 'you' in the verse?


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
    #length of string variables
verse_lenght = len(verse)
print(verse_lenght)

    #index of first occurence of the word 'and'
ifo_and = verse.find("and")
print(ifo_and)

    #index of last occurence of the word 'you'
ilo_you = verse.rfind("you")
print(ilo_you)

    #count of occurence of the word 'you'
count_of_occurence = verse.count("you")
print(count_of_occurence)

# Bonus: practice using .format() to output your answers in descriptive messages!
print("Guys, the length of the 'verse' varaiable is {} with\n the last occurrence of the 'you' word' at index {} and\n first occurrence of the word 'and' is at index {}. Also\n the total usage of the word 'you' in the variable is {}.".format(verse_lenght, ilo_you, ifo_and, count_of_occurence))