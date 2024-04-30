# Dice Rolling Simulator
import random

def roll_dice():
    dice_faces = {
    1: '''
 -------
|       |
|   •   |
|       |
 -------''',

    2: '''
 -------
| •     |
|       |
|     • |
 -------''',

    3: '''
 -------
| •     |
|   •   |
|     • |
 -------''',

    4: '''
 -------
| •   • |
|       |
| •   • |
 -------''',

    5: '''
 -------
| •   • |
|   •   |
| •   • |
 -------''',

    6: '''
 -------
| •   • |
| •   • |
| •   • |
 -------'''
}
    roll = input("Roll the dice? (Yes|No): ")
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("".join(dice_faces[dice1]))
        print("".join(dice_faces[dice2]))
        
        roll = input("Roll Again? (Yes|No)?: ")
roll_dice()
