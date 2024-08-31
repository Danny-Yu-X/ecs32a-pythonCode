# translate.py
# Danny Yu
#This program prompts the user to enter a word and translate the word to Pig Latin
# If the first letter is a vowel, the translation would be the word and "way"
# If the first letter is a consonant, the translation would be moving the first consonant to the end of the word and "ay"

#prompts the user to enter a word
word = input("Enter a word:")
#makes the word all lower case
lower_word = word.lower()
# the vowels 
vowel = "aeiou"
# the consonants
consonant = "qwrtypsdfghjklzxcvbnm"
#checks to see the first character is a vowel
if lower_word[0] in vowel:
    print(lower_word, "in Pig latin is", lower_word + "way")
#checks to see if the first character is a consonant
elif lower_word[0] in consonant:
    print(lower_word, "in Pig latin is", lower_word[1:] + lower_word[0] + "ay")
