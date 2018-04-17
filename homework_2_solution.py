'''
homework_2_solution.py

'''
#  General requirements with point values:
#  Points:                                                        pts. off if corrected       pts. off if not corrected
#  1.  Violation of style guide                                    0                            5
#  2.  Very Confusing Code                                         0                            5
#  3.  Function AskForLetter() is present                          1                            2
#  4.  Repeatedly ask user for letter until vowel or 'quit'          1                            3
#  5.  Use of len()                                                1                            3
#  6.  AskForLetter() calls IsVowel()                               1                            2
#  7.  AskForLetter() calls PrintIsVowel(letter)                   1                            2
#  8.  Function IsVowel() is present                                1                            2
#  9.  IsVowel() takes letter as input                               1                            3
#  10.  IsVowel() returns Boolean                                    1                            2
#  11.  IsVowel() calls IsLowercaseVowel() and IsUppercaseVowel()    1                            3
#  12.  IsLowercasseVowel() is present                               1                            2
#  13.  IsLowercaseVowel() determines if single letter is lowercase   2                            4
#  14.  IsLowercaseVowel() returns Boolean if lowercase               1                            2
#  15.  IsUppercasseVowel() is present                               1                            2
#  16.  IsUppercaseVowel() determines if single letter is uppercase   2                            4
#  17.  IsUppercaseVowel() returns Boolean if uppercase               1                            2
#  18.  Function PrintIsVowel(letter) is present                      1                            2


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
