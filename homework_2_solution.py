'''
homework_2_solution.py

Write a program that asks the user for a letter.
The program should then determine if the letter is a vowel or not.
'''

def AskForLetter():

    ask = True
    
    while ask == True:
        input = raw_input('''Please input a single letter:
Type 'quit' to end.\n''')
        if input == 'quit':
            ask = False

        if input != 'quit' and len(input) == 1:
            vowel = IsVowel(input)
            
            if vowel == True:
                PrintIsVowel(input)
                ask = False
            

def IsVowel(letter):

    # determine if it is lowercase vowel
    lowercase = IsLowercaseVowel(letter)
    

    # determine if it is uppercase vowel
    uppercase = IsUppercaseVowel(letter)

    # return True if either of the above functions
    # return True
    if lowercase == True or uppercase == True:
        return True
    else:
        return False

    

def IsLowercaseVowel(letter):

    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    else:
        return False


def IsUppercaseVowel(letter):

    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        return True
    else:
        return False

def PrintIsVowel(letter):

    print "The letter " + letter + " originally input is a vowel."

AskForLetter()

