## Hall of Champions v alpha 1.0
##
##MIT License
##
##Copyright (c) [2016] [Ismail A Ahmed]
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.

##
##Your trial to join the Hall of Champion has begun!
##Kill five Martian's to have your name placed in the Hall of Champion.
##BECOME A LEGEND!


import os
import time
import sys
import random
import textwrap
import os.path

global hp
hp = 225
global ehp
ehp = 100
global count
count = 0
global name


class User:
    def __init__(self, hp, count, name):
        self.userhp = hp
        self.dcount = count
        self.usern = name


userlist = []


def save():
    outfile = open('score.txt', 'a')
    global hp
    global count
    global name
    hp = str(hp)  # strings this because it is a number
    count = str(count)  # strings this because it is a number
    new = User(hp, count, name)  # class object
    file = ("Name:" + new.usern + ' ' + 'HP:' + new.userhp + ' ' + 'Enemy death count:' + new.dcount + ' ')
    userlist.append(file)
    userlist.append(new)
    outfile.write(file + '\n')  # puts the info in a file
    outfile.close()
    hall2()


def hall2():
    os.system('cls')
    print("You are now part of the Hall of Champions!")  # this is the one with the user in it(if he made it)
    infile = open('score.txt', 'r')
    file = infile.read()
    print(file)
    infile.close()
    done = input(
        '\n' + "Click enter once you have finished reading to exit")  # gives them as much time as they need to read(slow readers...)
    if done == '':
        quit()
    else:
        quit()


def killed():
    print("You have been killed. You will NOT be remembered.")
    time.sleep(2)
    quit()


def last():
    global count
    global hp
    global ehp
    hp = int(hp)  # turns this back into int because it was a string
    ehp = int(ehp)  # turns this back into int because it was a string
    count = int(count)  # turns this back into int because it was a string
    if count > 1:  # if you kill more than one person you dont need the Martian background again
        if count >= 5:
            finish = """Congrats! You have defeated 5 Martian's and you are now part of the Hall of Champions!
Your name will be forever remembered in history."""
            list = textwrap.wrap(finish, width=70)
            for element in list:
                print(element)
            time.sleep(7)
            save()
        print("Total amount of enemies killed is,", count)  # prints how many killed as a reminder
        time.sleep(2)
        os.system('cls')
        first()

    print("Total amount of enemies killed is,", count)  # prints how many killed as a reminder
    print("""You have defeated the enemy.
You managed to find a piece of paper on the enemy.
Analayzing paper...""")
    time.sleep(5)
    os.system('cls')
    some = """Several years ago we attacked the humans on their home planet, Earth!
It was the biggest mistake we made. We thought we would be able to crush them and take their planet.
What we didn't expect was that they would be so strong. We hardly killed any of them.
If time would go back, we would never do such a thing.
Within the 1000 years, their power as grown by a lot. They treat us as a game now.
We have no hope and all we can do is wait for them to finish us off slowly...
However, everytime they kill someone, a Martian will get a telepathic signal and teleport there.
We won't die without taking as many with us as possible.
"""
    list = textwrap.wrap(some, width=70)
    for element in list:
        print(element)
    done = input('\n' + "Click enter once you have finished reading!")
    if done == '':
        os.system('cls')
        first()  # takes you to the first Martian
    else:
        os.system('cls')
        first()  # takes you to the first Martian


def retreat():  # what happens when you retreat. No traitors allowed!
    os.system('cls')
    print("""You have chosen to retreat, traitor!
An implant has been activated in your brain. Your head will now go boom...""")
    time.sleep(3)
    os.system('cls')
    print('\t' + '\t' + '\t' + "BOOM! BOOM! BOOOOM!!!!")
    time.sleep(1)
    os.system('cls')
    print('\t' + '\t' + '\t' + "BOOOOOOOOOOOOOOOMMMMMMMMMMMMMMM!!!!!!!!!!!!!!!")
    time.sleep(1)
    os.system('cls')
    killed()


def sword():
    global hp
    print("Enemy attacks with a sword!")
    sword = 7  # enemy damage dealts user
    sword = random.randint(sword, 12)
    wpn = [1, 2, 3, 4]
    atk = random.choice(wpn)  # randomizes if enemy scores a crit, dodge, block, or regular hit
    if atk == 1:
        hp = hp - sword / 2
        print("You blocked and the damage was reduced!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", sword / 2)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a sword and killed!")
            print("Enemy damage dealt:", sword / 2)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 2:
        hp = hp
        print("You dodged and took no damage!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", sword * 0)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a sword and killed!")
            print("Enemy damage dealt:", sword * 0)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 3:
        hp = hp - sword * 2
        print("The enemy scored a crit and the damage was increased!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", sword * 2)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a sword and killed!")
            print("Enemy damage dealt:", sword * 2)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 4:
        hp = hp - sword
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", sword)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a sword and killed!")
            print("Enemy damage dealt:", sword)
            time.sleep(5)
            os.system('cls')
            killed()


def spear():
    global hp
    print("Enemy attacks with a spear!")
    spear = 8  # enemy damage dealts user
    spear = random.randint(spear, 13)
    wpn = [1, 2, 3, 4]
    atk = random.choice(wpn)  # randomizes if enemy scores a crit, dodge, block, or regular hit
    if atk == 1:
        hp = hp - spear / 2
        print("You blocked and the damage was reduced!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", spear / 2)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a spear and killed!")
            print("Enemy damage dealt:", spear / 2)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 2:
        hp = hp
        print("You dodged and took no damage!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", spear * 0)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a spear and killed!")
            print("Enemy damage dealt:", spear * 0)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 3:
        hp = hp - spear * 2
        print("The enemy scored a crit and the damage was increased!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", spear * 2)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a spear and killed!")
            print("Enemy damage dealt:", spear * 2)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 4:
        hp = hp - spear
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", spear)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a spear and killed!")
            print("Enemy damage dealt:", spear)
            time.sleep(5)
            os.system('cls')
            killed()


def dagger():
    global hp
    print("Enemy attacks with a dagger!")
    dagger = 6  # enemy damage dealts user
    dagger = random.randint(dagger, 11)
    wpn = [1, 2, 3, 4]
    atk = random.choice(wpn)  # randomizes if enemy scores a crit, dodge, block, or regular hit
    if atk == 1:
        hp = hp - dagger / 2
        print("You blocked and the damage was reduced!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", dagger / 2)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a dagger and killed!")
            print("Enemy damage dealt:", dagger / 2)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 2:
        hp = hp
        print("You dodged and took no damage!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", dagger * 0)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a dagger and killed!")
            print("Enemy damage dealt:", dagger * 0)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 3:
        hp = hp - dagger * 2
        print("The enemy scored a crit and the damage was increased!")
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", dagger * 2)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a dagger and killed!")
            print("Enemy damage dealt:", dagger * 2)
            time.sleep(5)
            os.system('cls')
            killed()
    elif atk == 4:
        hp = hp - dagger
        if hp > 0:
            print("HP remaning: ", hp)
            print("Enemy damage dealt:", dagger)
            time.sleep(4)
            print("")
            begin()
        elif hp <= 0:
            print("You were attacked by a dagger and killed!")
            print("Enemy damage dealt:", dagger)
            time.sleep(5)
            os.system('cls')
            killed()


def sword2():
    global ehp
    global hp
    global count
    sword = 10  # amount of damage you deal to enemy
    sword = random.randint(sword, 15)
    wpn = [1, 2, 3, 4]
    atk = random.choice(wpn)  # randomizes if you get crit, block, dodge, or regular attack
    if atk == 1:
        print("The enemy blocked and the damage was reduced!")
        ehp = ehp - sword / 2
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", sword / 2)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a sword")
            print("Your damage dealt:", sword / 2)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 2:
        print("The enemy dodged and took no damage!")
        ehp = ehp
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", sword * 0)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a sword")
            print("Your damage dealt:", sword * 0)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 3:
        print("You scored a crit and the damage was increased!")
        ehp = ehp - sword * 2
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", sword * 2)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a sword")
            print("Your damage dealt:", sword * 2)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 4:
        ehp = ehp - sword
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", sword)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a sword")
            print("Your damage dealt:", sword)
            time.sleep(4)
            os.system('cls')
            last()


def dagger2():
    global ehp
    global hp
    global count
    dagger = 7  # amount of damage you deal to enemy
    dagger = random.randint(dagger, 12)
    wpn = [1, 2, 3, 4]
    atk = random.choice(wpn)  # randomizes if you get crit, block, dodge, or regular attack
    if atk == 1:
        print("The enemy blocked and the damage was reduced!")
        ehp = ehp - dagger / 2
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", dagger / 2)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a dagger")
            print("Your damage dealt:", dagger / 2)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 2:
        print("The enemy dodged and took no damage!")
        ehp = ehp
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", dagger * 0)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a dagger")
            print("Your damage dealt:", dagger * 0)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 3:
        print("You scored a crit and the damage was increased!")
        ehp = ehp - dagger * 2
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", dagger * 2)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a dagger")
            print("Your damage dealt:", dagger * 2)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 4:
        ehp = ehp - dagger
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", dagger)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1  # counts how many Martian you killed
            print("You killed the enemy with a dagger")
            print("Your damage dealt:", dagger)
            time.sleep(4)
            os.system('cls')
            last()


def spear2():
    global ehp
    global hp
    global count
    spear = 15  # amount of damage you deal to enemy
    spear = random.randint(spear, 20)
    wpn = [1, 2, 3, 4]
    atk = random.choice(wpn)  # randomizes if you get crit, block, dodge, or regular attack
    if atk == 1:
        print("The enemy blocked and the damage was reduced!")
        ehp = ehp - spear / 2
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", spear / 2)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1
            print("You killed the enemy with a spear")
            print("Your damage dealt:", spear / 2)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 2:
        print("The enemy dodged and took no damage!")
        ehp = ehp
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", spear * 0)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1
            print("You killed the enemy with a spear")
            print("Your damage dealt:", spear * 0)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 3:
        print("You scored a crit and the damage was increased!")
        ehp = ehp - spear * 2
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", spear * 2)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1
            print("You killed the enemy with a spear")
            print("Your damage dealt:", spear * 2)
            time.sleep(4)
            os.system('cls')
            last()
    elif atk == 4:
        ehp = ehp - spear
        if ehp > 0:
            print("Enemy HP remaning: ", ehp)
            print("Your damage dealt:", spear)
            time.sleep(4)
            print("")
            begin()
        elif ehp <= 0:
            ehp = 100  # this is the new Martian's health points
            count += 1
            print("You killed the enemy with a spear")
            print("Your damage dealt:", spear)
            time.sleep(4)
            os.system('cls')
            last()


def first():
    print("A Martian appears. What will you do?")
    begin()


def defend():
    print("The Martian attacks!")
    time.sleep(2)
    wpn = [1, 2, 3]
    atk = random.choice(wpn)  # randomizes what the enemy attacks with
    if atk == 1:
        sword()  # enemy attacks with sword
    elif atk == 2:
        dagger()  # enemy attacks with dagger
    elif atk == 3:
        spear()  # enemy attacks with spear


def attack():
    wpnchoice = int(input("""What would you like to attack with?
1.Sword
2.Dagger
3.Spear
"""))
    if wpnchoice == 1:
        sword2()  # when user chooses this he gets taken to a function where he attcks with a sword
    elif wpnchoice == 2:
        dagger2()  # when user chooses this he gets taken to a function where he attcks with a dagger
    elif wpnchoice == 3:
        spear2()  # when user chooses this he gets taken to a function where he attcks with a spear
    else:
        attack()


def begin():
    enemy = int(input("1.Attack" + '\n' + "2.Defend" + '\n' + "3.Retreat" + '\n' + "4.Quit" + '\n'))
    if enemy == 1:
        attack()  # takes user to a function where they make a weapon choice and game save

    elif enemy == 2:
        defend()  # takes user to a function where enemy attacks user

    elif enemy == 3:
        retreat()  # goes to function where user dies for retreating
    elif enemy == 4:
        print("Your choice: Quit")
        time.sleep(1)
        quit()
    else:
        print("Please choose on of the following choices!")
        begin()


def start():
    print("""WELCOME TO MARS!
Congrats, you have successfully landed on Mars!
Your mission: Join the Hall of Champions!""")
    time.sleep(3)
    os.system('cls')
    abc = """1000 years ago, the Martian's attacked your home planet, Earth!
They thought they could defeat us. They were fooled.
Our planet united and we beat them back.
As we were going to finish them off, the leader of Earth came up with an idea.
He said every 100 years a person will be sent to their planet to kill as many as possible.
If they had killed five Martian's they would be able to join the Hall of Champions!
To join the Hall of Champions that person will be recognized as the one of the strongest warrior in history.
Throughout the 1000 years, only five have become part of the Hall of Champions.
It is now your time to join the Hall of Champions!
Once you have defeated five of them, your name will be placed within the Hall of Champions and you will be taken back to Earth.
Good luck!
Oh and remember, NEVER RETREAT!!!!"""
    list = textwrap.wrap(abc, width=70)
    for element in list:
        print(element)
    done = input(
        '\n' + "Click enter once you have finished reading!")  # gives them as much time as they need to read(slow readers...)
    if done == '':
        os.system('cls')
        hall()  # shows them the members of the hall
    else:
        os.system('cls')
        hall()  # shows them the members of the hall


def hall():
    print("Hall of Champion members:")  # hall of champion members
    infile = open('score.txt', 'r')
    file = infile.read()
    print(file)
    infile.close()
    done = input(
        '\n' + "Click enter once you have finished reading!")  # gives them as much time as they need to read(slow readers...)
    if done == '':
        os.system('cls')
        first()  # takes you to the first Martian
    else:
        os.system('cls')
        first()  # takes you to the first Martian


def name():
    global name
    name = input("Your name: ")
    print("Hello", name)
    time.sleep(1)
    start()


name()