# My first program
# Created on 09/15/2025
# Purpose: to learn python
# Editor: Aaron Huang
start = 1
while True:
    dice = int(input("what did you roll?: "))
    if start + dice == 100:
        print("You have reached then End!")
        print("You Win!")
        break
    elif start + dice < 100:
        new_position = start + dice
        game_dict = {
            9 : 34,
            54 : 19,
            40 : 64,
            90 : 48,
            67 : 86,
            99 : 77
        }
        if new_position in game_dict:
            start = game_dict[new_position]
        else:
            start += dice
