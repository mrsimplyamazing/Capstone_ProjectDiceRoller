import random

#range of the values of a dice
min_val = 1
max_val = 6

# ASCII representations of dice
dice = {
    1: "[     ]\n[  0  ]\n[     ]",
    2: "[0    ]\n[     ]\n[    0]",
    3: "[0    ]\n[  0  ]\n[    0]",
    4: "[0   0]\n[     ]\n[0   0]",
    5: "[0   0]\n[  0  ]\n[0   0]",
    6: "[0   0]\n[0   0]\n[0   0]"
}

#to loop the rolling through user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    #generating and printing 1st random integer from 1 to 6
    roll1 = random.randint(min_val, max_val)
    print(f"Dice 1: {roll1}\n{dice[roll1]}")
    
    #generating and printing 2nd random integer from 1 to 6
    roll2 = random.randint(min_val, max_val)
    print(f"Dice 2: {roll2}\n{dice[roll2]}")
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again?")

