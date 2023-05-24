import random

number_of_sides = int(input("How many sides should the dice have? "))
number_of_dice = int(input("How many dice would you like to roll? "))
dice_roll_count = 0

while dice_roll_count < number_of_dice:
    dice_roll = random.randint(1, number_of_sides)
    print(dice_roll)
    dice_roll_count += 1
