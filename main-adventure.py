from sys import exit
import random

prompt = ">>> "

for i in range(1):
    key = random.randint(1, 1000)
    randy = key

def start():
    print("Welcome...")
    print("Try to end the game without dying and gaining some loot.")
    print("You come to the entrance of a building and see two doors.")
    print("Take door 1 or door 2?")

    choice = input(prompt)
    if choice == "1":
        print("You find a plate of pancakes...")
        pancake_room()
    elif choice == "2":
        print("You find a dark staircase.")
        staircase()
    else:
        dead("I didn't understand that.")


def dead(reason):
    print(reason, "\nPlay again!")
    exit(0)


def pancake_room():
    print("""You look around the room and you only see a plate of pancakes
    and a perculiar painting hanging on the east wall.""")
    print("Do you...")
    print("1. Eat the pancakes.")
    print("2. Inspect the painting.")

    choice = input(prompt)
    if choice == "1":
        print("You eat the pancakes and suddenly shrink to 3in tall.")
        dead("A beast enters the room and squashes you to death underfoot.")
    elif choice == "2":
        print("The painting reveals a secret room!")
        print("Maybe it's a trap...")
        gold_maybe()
    else:
        dead("I didn't understand that.")

def gold_maybe():
    print("Enter the room? (y/n)")
    choice = input(prompt)
    if choice == 'y':
        gold_room()
    else:
        print("Better to be safe. You win with 0 loot.")
        exit(0)


def gold_room():
    print("You enter into a room full of gold and loot.")
    print("How much do you take?")
    choice = input(prompt)

    if "0" in choice or "1" in choice:
        amount = int(choice)
    else:
        print("You gotta type a real number!")

    if amount < 50:
        print(f"Congrats! You win with {amount} loot!")
        exit(0)
    else:
        print("You were being watched by Davy Jones and you were greedy.")
        dead("You were killed by Davy Jones inside his locker.")


def staircase():
    print("""As you descend the staircase, you hear heavy breathing coming from the bottom of the steps. \n
    Do you...""")
    print("1. Flip on the light switch to see what's breathing.")
    print("2. Keep the lights off and avoid the breathing at all costs.")

    choice = input(prompt)
    if choice == "1":
        dead("You wake a sleeping dragon that immediately kills you with fire.")
    elif choice == "2":
        print("You brush up against a large scaley creature and realize that you made a good choice.")
        levers_maybe()
    else:
        print("You have to choose 1 or 2.")
        exit(0)

def levers_maybe():
    print("""You walk through a small door in the back of the room.\n After entering, you come to two large doors. The door on the left says: EXIT\n And the door on the right says: LEVERS
    Which door do you take?""")

    choice = input(prompt)
    if choice == "left":
        print("Better to be safe. You win with 0 loot.")
        exit(0)
    elif choice == "right":
        levers()
    else:
        print("You must choose: right or left.")
        exit(0)


def levers():
    print("""You enter a room full of flashing lights. On the wall before you is three large levers\n
    The instructions say that you can only choose one lever\n
    One will give you a random amount of gold and the other two will kill you.\n
    Do you choose lever 1, 2, or 3?""")

    choice = input(prompt)
    if choice == "1":
        dead("A massive spike juts out from the floor and impales you.")
    elif choice == "2":
        print(f"You escape alive with {randy} gold!")
        if randy < 50:
            print("You could do better!")
        else:
            print("Best possible outcome!")
        exit(0)
    elif choice == "3":
        dead("A two headed lion enters the room through a secret door and eats you alive.")
    else:
        print("You have to choose 1, 2, or 3!")
        exit(0)


start()
