"""
    Maths Calculation Game
"""
import os
import sys
#from getpass import getpass
import time
from random import randint,choice

WIDTH = os.get_terminal_size().columns

if sys.platform == 'win32' or sys.platform == 'win64':
    os.system('cls')# windows
else:
    os.system('clear') # linux, macos

print("_"*WIDTH)
print('\n')
print(time.ctime())
print("Welcome to Maths Calculation Game".center(WIDTH))
print()
print("Rules: ")
print("1. If your answer is in decimal than write only the value which is before decimal point.")
print("2. Giving 5 Correct ans before 5 Incorrect ans will win you the Game and vice-versa")
print('\n')
print("_"*WIDTH)
print('\n\n')

ch = input("Do you want to play this Game yes/no :").strip().lower()
if ch in ('yes', 'y', 'yo', 'true'):
    print()
    name = input("Enter Player Name: ").strip().upper()
    correct = 5
    incorrect = 0
    while correct > 0:
        if incorrect == 5:
            print("\n\n")
            print(f"Shame on you {name}!!! You Lost the Game".center(WIDTH))
            print("\n\n")
            print("_"*WIDTH)
            print('\n\n')
            break
        a,b,c,d = (randint(1,9) for _ in range(4))
        x,y,z = (choice(['+','-','*','/']) for _ in range(3))
        expr = f"{a}{x}{b}{y}{c}{z}{d}"
        print("\n")
        ans = int(eval(expr))
        uans = int(input(expr + " = "))
        if uans == ans:
            print(".........................Processing...............", end='', flush=True)
            for _ in range(randint(3, 10)):
                print('.', end='', flush=True) # lazy execution / evaluation
                time.sleep(1)
            print()
            print("!!CORRECT!!")
            print("_"*WIDTH)
        else:
            incorrect += 1
            print(".........................Processing...............", end='', flush=True)
            for _ in range(randint(3, 10)):
                print('.', end='', flush=True) # lazy execution / evaluation
                time.sleep(1)
            print()
            print("!!INCORRECT!!")
            print("_"*WIDTH)
            continue
        correct -= 1
    else:
        print("\n\n")
        print(f"Congratualations {name}!! You such a Master".center(WIDTH))
        print("\n\n")
        sys.exit(0)
else:
    print("Thank You")
    sys.exit(1)

print("\n\n")

