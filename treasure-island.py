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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

option1 = input("You arrive to the island and on the right there is a clear path aiming straight to the other side of the island and the left path with full of leaves and trees. Which path do you choose?(Left or Right): ")

while noplay == 'yes' or noplay == 'Yes' or noplay == 'y':
    
    if option1 == 'left' or option1 == 'Left':
        input("You encounter a snake while going throught the trees and leaves you have to optiones run or take out a matchete(type run or matchete): ")
    elif option == 'right' or option1 == 'right':
        print("You end up at the other side of island and encounter some pirates pointing a gun at you.")
     print("They take you hostage into their ship leaving the island and never to been seen again.")
        print('''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⠻⣿⣿⣿⣿⣿⣿⣷⡀⢸⣿⣷⠀⠀⣾⣿⡇⢀⣾⣿⣿⣿⣿⣿⣿⠟⣿⣿
    ⣿⣿⡆⠙⣿⣿⣿⣿⣿⣿⣄⠈⠛⠋⡰⢆⠙⠛⠁⣠⣿⣿⣿⣿⣿⣿⠋⢰⣿⣿
    ⣿⣿⣿⡀⠈⠻⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⠟⠁⢀⣿⣿⣿
    ⣿⣿⣿⣷⡀⠀⠘⢿⣿⣿⣿⡇⠘⢿⣿⣿⡿⠃⢸⣿⣿⣿⡿⠃⠀⢀⣾⣿⣿⣿
    ⣿⣿⣿⣿⣷⣄⠀⠀⠙⠿⣿⣿⣦⣀⠈⠁⣀⣴⣿⣿⠿⠋⠀⠀⣠⣾⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠈⠻⢿⣿⣿⣿⣿⡿⠟⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⣀⣭⡿⠟⠉⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣏⡉⢻⣿⠟⠋⠁⠀⠀⢀⣠⣴⣿⡟⢉⣹⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠿⣿⠿⠛⢷⡄⠹⣇⣀⣠⣴⣾⣟⣉⣸⠏⢠⡾⠛⠿⣿⠿⣿⣿⣿⣿
    ⣿⣿⣿⡇⠀⢸⣧⣤⣾⣿⣄⣹⣿⣿⣿⣿⣿⣿⣏⣠⣿⣷⣤⣼⡇⠀⢸⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')
    else:
        input("You have to pick the options provided to you. Do you want to play again?(types yes if not type no): ")