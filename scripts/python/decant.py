# The purpose of this program is to calculate the number of
# 4 dose potions I can make out of 3 dose potions in RuneScape
# I generally use this to compute whether or not I'll make
# money off of doing herblore.


import sys
import math

def main():

    print("Convert potion (3)'s into potion (4)'s")
    
    
    help_string = """ 
    usage: python main.py <POTION_NUMBER>
    """

    name = ""
    amount = 0

    try:
        name , amount = sys.argv
        amount = int(amount)
    except Exception as e:
        print(help_string)


    full_potion_number = (amount * 3) / (4)
    
    # determine wether or not there will be leftover potions
    leftover = False
    if float(math.floor(full_potion_number)) == full_potion_number:
        leftover = True
               
    print("number of potion (4)s " + str(full_potion_number))

    if leftover:
        print("There will be no leftover potions")
    else:
        print("There will be leftover potions")
        
        

    
main()
