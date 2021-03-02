import random

dice_number = [1,2,3,4,5,6]

def roll_dice(num_rolls):
    i = 0
    while i < num_rolls:
        print("Roll #", (i+1), " = ", random.choice(dice_number))
        i += 1

print("How many times would you like to roll this dice?")
number_of_rolls = int(input())

roll_dice(number_of_rolls)