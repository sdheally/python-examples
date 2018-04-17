'''
Python for Beginners 20776.059
Steve Heally
07/13/17
Homework #3

Write a program that takes a 3 word phrase and then converts the words
to Pig Latin.
'''
#
# Define a global variable for vowels.
#
VOWELS = ["a","e","i","o","u","A","E","I","O","U"]
#
# Ask user for input and if input is 'quit', then exit. Otherwise, call
# PrintThreeWordPhrase().
#
def AskForSentence():
    while True:
        user_input = \
        raw_input("\nType 3 words separated by spaces or 'quit' to quit:\n")
        if user_input == "quit":
            break
        
        length = len(SplitSentenceIntoList(user_input))
    
        if length > 3 or length < 3:    
            print "\nI will only convert phrases of 3 words..try again.\n"
        else:
            PrintThreeWordPhrase(user_input)
#
# Convert user input string phrase to lower case.
#
def LowercaseSentence(string):
    lowercase = string.lower()
    return lowercase
#
# Convert user input string phrase to a list.
#
def SplitSentenceIntoList(list1):
    split_list = LowercaseSentence(list1).split()
    return split_list
#
# 1. Determine if there are 3 words exactly in user's input. If yes, continue
# if not, then repeat asking for 3 words.
# 2. Take each word, determine if it begins with a vowel. Convert word to
# igPay atinLay based on rules.
# 3. Create new phrase by creating list of new words and joining them with spaces.
#
def ConvertWordToPigLatin(word):
    
    word_1 = SplitSentenceIntoList(word)[0]
    word_2 = SplitSentenceIntoList(word)[1]
    word_3 = SplitSentenceIntoList(word)[2]
    
    if word_1[0] in VOWELS:
        new_word_1 = word_1 + "hay"
    else:
        new_word_1a = word_1[1:]
        new_word_1 = new_word_1a + word_1[0] + "ay"
        
    if word_2[0] in VOWELS:
        new_word_2 = word_2 + "hay"
    else:
        new_word_2a = word_2[1:]
        new_word_2 = new_word_2a + word_2[0] + "ay"
        
    if word_3[0] in VOWELS:
        new_word_3 = word_3 + "hay"
    else:
        new_word_3a = word_3[1:]
        new_word_3 = new_word_3a + word_3[0] + "ay"
        
    new_phrase_1 = new_word_1,new_word_2,new_word_3
    new_phrase = " ".join(new_phrase_1)
    return new_phrase
#
# Print the new phrase to stdout.
#
def PrintThreeWordPhrase(phrase):
        new_phrase = ConvertWordToPigLatin(phrase)
        print "\nBelow is your phrase in Pig Latin:",new_phrase
 
AskForSentence()
