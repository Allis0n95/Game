import random
start = 'scenario.txt'
setting = 'setting.txt'
peer = 'encounter.txt'
inside = 'encounter2.txt'
kitchen = 'kitchen.txt'
bedroom = 'bedroom.txt'
basement = 'basement.txt'
end = 'potion.txt'
you = 'You roll a'
them = 'Nyx rolls a'
youHP = 'Your HP is'
themHP = "Nyx's HP is"

#scenario
infile = open(start, 'r')
readFile = infile.read()
print(readFile)

#setting
print('')
infile = open(setting, 'r')
readFile = infile.read()
print(readFile)

#encounter
print('')
print('You peer into the window')
infile = open(peer, 'r')
readFile = infile.read()
print(readFile)

print('')
print('Type a number for your answer')
idk = False #I've run out of names lmao
while idk == False:
    outside = int(input('What would you like to do? Open the door (1) or Flee (2)?'))
    if outside == 1:
        print('You enter the house')
        idk = True
    elif outside == 2:
        print('You flee')
        print('G A M E  O V E R')
        exit()
        idk = True
    else:
        print('Please type 1 or 2')
        idk = False

print('')
infile = open(inside, 'r')
readFile = infile.read()
print(readFile)

table = 0
kitchenEnter = 0
bedroomEnter = 0
HP = 4
nyxHP = 4
room2 = True
nyxDead = False
tryPotion = False
potion = False
chest = False
while room2 == True:
    if nyxHP == 0:
        print('You stopped Nyx!')
        nyxDead = True
        nyxHP = 4
    else: 
        idk2 = False
        while idk2 == False:
            print('')
            room2 = int(input('What would you like to do? Search the messy table (2), Open the door to the left (3), Open the door to the right (4), Try the attic code (6)'))
            if room2 == 3: #kitchen
                print('')
                print('You open the left door. This room is a kitchen.')
                room2 = False
                infile = open(kitchen, 'r')
                readFile = infile.read()
                print(readFile)
                room3 = True
                while room3 == True:
                    print('')
                    room3 = int(input('What would you like to do? Search (1), Exit (2), Go down the stairs (3)'))
                    if room3 == 1:
                        print('There is nothing else to be found')
                        room3 = True
                    if room3 == 2:
                        print('You leave the kitchen')
                        room3 = False
                        room2 = True
                    if room3 == 3: #kitchen basement
                        if nyxDead == True:
                            print('There is nothing else in the basement')
                        if nyxDead == False:
                            print('You go down the stairs')
                            print('')
                            infile = open(basement, 'r')
                            readFile = infile.read()
                            print(readFile)
                            persuade = False
                            cure = False
                            HP = 4
                            nyxHP = 4
                            while nyxDead == False:
                                print('')
                                choice = int(input('What will you do? Attack (1), Attempt to Persuade (2), Attempt to Cure (3), Flee (4)'))
                                if choice == 1: #attack
                                    print('You attempt to attack')
                                    dice = random.randrange(20)+1
                                    dice2 = random.randrange(20)+1
                                    print(you, dice)
                                    if table == 1:
                                        if dice == 20:
                                            print('Critical Hit!')
                                            nyxHP = 0
                                            print(themHP, nyxHP)
                                            room3 = False
                                            room2 = True
                                            print('Nyx drops a key')
                                            chest = True
                                            nyxDead = True
                                        elif dice+1 >= 12:
                                            print('You hit')
                                            nyxHP -= 2
                                            print(themHP, nyxHP)
                                            if nyxHP == 0:
                                                nyxDead = True
                                                print('Nyx drops a key')
                                                chest = True
                                            else:
                                                print(them, dice2)
                                                print("You are fast so Nyx's hit is -4")
                                                if dice2-4 >=12:
                                                    print('Nyx hits')
                                                    HP -= 2
                                                    print(youHP, HP)
                                                    if HP == 0:
                                                        print('You die')
                                                        print('G A M E  O V E R')
                                                        exit()
                                                if dice2-4 <=11:
                                                    print('Nyx misses')
                                                    print(youHP, HP)
                                        elif dice+1 <= 11:
                                            print('You do not hit')
                                            print(themHP, nyxHP)
                                            print(them, dice2)
                                            print("You are fast so Nyx's hit is -4")
                                            if dice2-4 >=12:
                                                print('Nyx hits')
                                                HP -= 2
                                                print(youHP, HP)
                                                if HP == 0:
                                                    print('You die')
                                                    print('G A M E  O V E R')
                                                    exit()
                                            if dice2-4 <=11:
                                                print('Nyx misses')
                                                print(youHP, HP)
                                            if dice == 1:
                                                print('Critical Fail')
                                                nyxHP += 2
                                                print(themHP, nyxHP)
                                    if table == 0:
                                        if dice == 20:
                                            print('Critical Hit!')
                                            nyxHP = 0
                                            print(themHP, nyxHP)
                                            room3 = False
                                            room2 = True
                                            print('Nyx drops a key')
                                            chest = True
                                            nyxDead = True
                                        elif dice >= 12:
                                            print('You hit')
                                            nyxHP -= 2
                                            print(themHP, nyxHP)
                                            if nyxHP == 0:
                                                nyxDead = True
                                                print('Nyx drops a key')
                                                chest = True
                                            else:
                                                print(them, dice2)
                                                print("You are fast so Nyx's hit is -4")
                                                if dice2-4 >=12:
                                                    print('Nyx hits')
                                                    HP -= 2
                                                    print(youHP, HP)
                                                    if HP == 0:
                                                        print('You die')
                                                        print('G A M E  O V E R')
                                                        exit()
                                                if dice2-4 <=11:
                                                    print('Nyx misses')
                                                    print(youHP, HP)
                                        elif dice <= 11:
                                            print('You do not hit')
                                            print(themHP, nyxHP)
                                            print(them, dice2)
                                            print("You are fast so Nyx's hit is -4")
                                            if dice2-4 >=12:
                                                print('Nyx hits')
                                                HP -= 2
                                                print(youHP, HP)
                                                if HP == 0:
                                                    print('You die')
                                                    print('G A M E  O V E R')
                                                    exit()
                                            if dice2-4 <=11:
                                                print('Nyx misses')
                                                print(youHP, HP)
                                            if dice == 1:
                                                print('Critical Fail')
                                                nyxHP += 2
                                                print(themHP, nyxHP)
                                elif choice == 2: #persuade
                                    if persuade == True:
                                        print('You have already tried this, choose something else')
                                    if persuade == False:
                                        print('You attempt to persuade Nyx that you have no fear')
                                        print('You and Nyx roll a D20')
                                        dice = random.randrange(20)+1
                                        dice2 = random.randrange(20)+1
                                        print(you, dice)
                                        print(them, dice2)
                                        persuade = True
                                        if dice >= dice2+4:
                                            print('You convince Nyx that you are not afraid. Nyx disapears')
                                            nyxHP = 0
                                            room3 = False
                                            room2 = True
                                            print('Nyx drops a key')
                                            chest = True
                                            nyxDead = True
                                            if dice == 20:
                                                print('You are so successful that you and Nyx double disapears somehow')
                                        if dice < dice2+4:
                                            print('You do not convince Nyx')
                                            if dice == 1:
                                                print('You pee your pants from fear')
                                elif choice == 3: #cure
                                    if cure == True:
                                        print('You have already tried this, choose something else')
                                    if cure == False:
                                        print('You believe Nyx is unwell and attempt to use a cure')
                                        if potion == True:
                                            print('You see Nyx is unwell and you remove the curse. Nyx is cured and thanks you for your help')
                                            nyxHP = 0
                                            room3 = False
                                            room2 = True
                                            print('Nyx drops a key')
                                            chest = True
                                            nyxDead = True
                                        if potion == False:
                                            print('You and Nyx roll a D20')
                                            dice = random.randrange(20)+1
                                            dice2 = random.randrange(20)+1
                                            print(you, dice)
                                            print(them, dice2)
                                            cure = True
                                            if dice >= dice2-2:
                                                print('You see Nyx is unwell and you remove the curse. Nyx is cured and thanks you for your help')
                                                nyxHP = 0
                                                room3 = False
                                                room2 = True
                                                print('Nyx drops a key')
                                                chest = True
                                                nyxDead = True
                                                if dice == 20:
                                                    print('You are so successful that you and Nyx become friends')
                                            if dice < dice2-2:
                                                print('You do not notice anything off')
                                                if dice == 1:
                                                    print('Nyx insults you')
                                elif choice == 4:
                                    print('You flee')
                                    print('G A M E  O V E R')
                                    exit()
                                else:
                                    print('Type 1, 2, 3')
            elif room2 == 4: #bedroom
                print('')
                print('You open the right door. This room is a small bedroom.')
                room2 = False
                infile = open(bedroom, 'r')
                readFile = infile.read()
                print(readFile)
                room4 = True
                while room4 == True:
                    print('')
                    room4 = int(input('What would you like to do? Search (1), Exit (2), Attempt to open the chest (3)'))
                    if room4 == 1:
                        print('There is nothing else to be found')
                        room4 = True
                    elif room4 == 2:
                        print('You leave the bedroom')
                        room4 = False
                        room2 = True
                    elif room4 == 3: #chest
                        if chest == False:
                            print('The chest is locked, you do not have the key')
                            room4 = True
                        if chest == True:
                            infile = open(end, 'r')
                            readFile = infile.read()
                            print(readFile)
                            exit()
                    else:
                        print('Type 1, 2, 3')
            elif room2 == 2: #table
                if table == 1:
                    print('You have already found the item')
                    room2 = True
                if table == 0:
                    print('You search the messy table.')
                    print('You have found brass knuckles')
                    table = 1
                    room2 = True
            elif room2 == 6: #attic
                if tryPotion == True:
                    print('You only get one try')
                if tryPotion == False:
                    print('')
                    code = int(input('What do you think the code is? It is 3 numbers long'))
                    if code == 244: #nyx morse code, number of beeps used (why? idk)
                        print('You did it!')
                        potion = True
                        tryPotion = True
                    else:
                        print('Nope')
                        potion = False
                        tryPotion = True
            else:
                print('Type 2, 3, 4, or 6')
                idk2 = False


#https://github.com/Allis0n95/Game/tree/main
