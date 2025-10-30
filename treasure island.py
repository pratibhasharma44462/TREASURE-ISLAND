print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at the middle of the road.Where do you want to go")
choose = input("      Type 'left' OR 'right'     \n")
if choose == "right":
    print("YOU GOT TRAP IN SNAP TRAP. \nGAME OVER!!!!")
else:
    print("THERE IS A ISLAND RIGHT IN FRONT OF YOU AT CENTRE OF LAKE. HOW YOU WANT TO CROSS THE LAKE?")

    choice = input("TYPE 'wait' if you wanna wait for the boat or 'swim' if you wanna swim on your own\n")
    if choice == 'wait':
        print("YOU ARRIVED AT THE ISLAND")
    else:
        print("YOU ARE EATEN BY HUNGRY CROCODILE. GAME OVER!!!!")
        exit()
    print("Now there are three doors infront of you.")
    print("RED,BLUE,PURPLE")    
    DOORS = input("which door you choose?: ").lower()
    if DOORS == "RED":
        print("YOU ARE BURNED BY FIRE. GAME OVER!!!!")
    elif DOORS == "BLUE":
        print("YOU ARE DROWN IN WATER. GAME OVER!!!")
    else:
        print("YOU WIN!!. YOU CHOOSE THE RIGHT DOOR.")
        print("ALL TREASURE IS YOURS.!!!")


