# Python for Beginners 20776.059
# Steve Heally
# 06/29/17
#
# Homework #1
#
# 
# 1. Ask user for their dream job title.
#
job_input = raw_input ("What is your dream job title?\n")
job = str(job_input)
print "\n",job,"is a nice choice!\n"
#
# 2. Ask user for the hourly wage they want to earn reflected in dollars and cents.
#
while True:
    try:
        wage_desired = float(raw_input("What is the hourly wage in dollars and cents you want to earn?\n"))
    except ValueError:
        print "\nInput is not a valid dollar and cents entry, please try again.\n"
        continue
    else:
        print "\n",wage_desired, "is a nice figure!\n"
        break
#
# 3. Calculate the annual wage based on hourly wage for 48 weeks paid over 52 weeks.
#
annual_wage = wage_desired*40*52*.65
print "Annual net wage after taxes is",annual_wage,"\n"
#
# 4. Ask user how much money they feel they will need at retirement.
#
while True:
    retire_amount = raw_input("How much money do you think you will need at the time you retire?\n")
    try:
        retire = int(retire_amount)
    except ValueError:
        print "\nThe number you input is not a valid integer, please try again.\n"
        continue
    if retire <= annual_wage*2:
        print "\nThat's not enough money!\n"
        continue
    else:
        print "\nWow, that's a lot of dough!\n"
        break
#    
# 5. Determine number of years to reach retirement dollar value.
#
years = int(retire/annual_wage)
print "You will reach retirement dollar value in",years,"years.\n"
#
# 6. Determine if the number of years is needed to save is odd or even.
#
state = years%2
#
# 7. Tell user if the number of years is odd or even. 
#
if state == 0:
    print "The number of years to reach retirement is an even number.\n"
else:
    print "The number of years to reach retirement is an odd number.\n"
