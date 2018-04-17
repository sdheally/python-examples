'''
Steve Heally
07/07/17
Functions and their variables.

1. Repeatedly ask user to input an NFL team name or quit to exit. When an NFL team is
input, determine in which Conference and Division the team is and print it to stdout
e.g. "The 49ers are in the NFC West".
'''
#
# Ask user to type in an NFL team name.  Repeat the question until a valid name is given.
#
def AskForTeam():
    while True:
        user_input = raw_input("\nType the name of an NFL team.\n")
        if user_input == "quit":
            break
                               
        elif user_input != quit:
            result = AFCResult(user_input)
            if result == False:
                NFCResult(user_input)
#
# Determine if the team name entered is in the AFC or not and if so, which division.
#
def AFCResult(result):
    american = IsAFC(result)
    national = IsNFC(result)
    if american == True and IsAFCWest(result) == True:
        print "\nThe",result,"are in the AFC West.\n"
    if american == True and IsAFCNorth(result) == True:
        print "\nThe",result,"are in the AFC North.\n"
    if american == True and IsAFCSouth(result) == True:
        print "\nThe",result,"are in the AFC South.\n"
    if american == True and IsAFCEast(result) == True:
        print "\nThe",result,"are in the AFC East.\n"
    else:
        return False        
#
# If AFCResult(result) returns False, determine which division in the NFC the team is.
#
def NFCResult(result):
    if IsNFC(result) == True and IsNFCWest(result) == True:
        print "\nThe",result,"are in the NFC West.\n"
    if IsNFC(result) == True and IsNFCNorth(result) == True:
        print "\nThe",result,"are in the NFC North.\n"
    if IsNFC(result) == True and IsNFCSouth(result) == True:
        print "\nThe",result,"are in the NFC South.\n"
    if IsNFC(result) == True and IsNFCEast(result) == True:
        print "\nThe",result,"are in the NFC East.\n"   

#
# Determine if the team name given is in the AFC.
#
def IsAFC(division):
    west = IsAFCWest(division)
    north = IsAFCNorth(division)
    south = IsAFCSouth(division)
    east = IsAFCEast(division)

    if west == True or north == True or south == True or east == True:
        return True
    else:
        return False
#
# Determine if the team name given is in the NFC.
#
def IsNFC(division):
    west = IsNFCWest(division)
    north = IsNFCNorth(division)
    south = IsNFCSouth(division)
    east = IsNFCEast(division)

    if west == True or north == True or south == True or east == True:
        return True
    else:
        return False
#
# Define teams and their conference/division.
#
def IsAFCWest(team):
    if team == "Raiders" or team == "Chiefs" or team == "Broncos" or team == "Chargers":
        return True
    else:
        return False
                           
def IsAFCNorth(team):
    if team == "Steelers" or team == "Ravens" or team == "Browns" or team == "Bengals":
        return True
    else:
        return False
                           
def IsAFCSouth(team):
    if team == "Colts" or team == "Texans" or team == "Jaguars" or team == "Titans":
        return True
    else:
        return False
                           
def IsAFCEast(team):
    if team == "Patriots" or team == "Dolphins" or team == "Bills" or team == "Jets":
        return True
    else:
        return False

def IsNFCWest(team):
    if team == "49ers" or team == "Rams" or team == "Cardinals" or team == "Seahawks":
        return True
    else:
        return False
                           
def IsNFCNorth(team):
    if team == "Bears" or team == "Packers" or team == "Lions" or team == "Vikings":
        return True
    else:
        return False
                           
def IsNFCSouth(team):
    if team == "Falcons" or team == "Saints" or team == "Panthers" or team == "Buccaneers":
        return True
    else:
        return False
                           
def IsNFCEast(team):
    if team == "Redskins" or team == "Cowboys" or team == "Giants" or team == "Eagles":
        return True
    else:
        return False

AskForTeam()
