# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.

import random
def task1():
    elements = ['rock', 'scissors', 'paper']
    game_over = False
    print('This game emulates the game "rock, scissors, paper"')
    while not game_over:
        player_choice = input("Enter your choice: ")
        computer_choice = elements[random.randint(0, 2)]
        if player_choice == computer_choice:
            print('Draw. Try again.')
            continue
        elif player_choice == 'rock':
            if computer_choice == 'scissors':
                print(f'Computer choice is {computer_choice}. Player win')
                game_over = True
                break
            else:
                print(f'Computer choice is {computer_choice}. Computer win')
                game_over = True
                break

        elif player_choice == 'scissors':
            if computer_choice == 'paper':
                print(f'Computer choice is {computer_choice}. Player win')
                game_over = True
                break
            else:
                print(f'Computer choice is {computer_choice}. Computer win')
                game_over = True
                break

        elif player_choice == 'paper':
            if computer_choice == 'rock':
                print(f'Computer choice is {computer_choice}. Player win')
                game_over = True
                break
            else:
                print(f'Computer choice is {computer_choice}. Computer win')
                game_over = True
                break
        else:
            print('Uknown. Try again.')
            continue


# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!

def task2(kwargs):
    people = kwargs.get('people', None)
    tp = kwargs.get('tp', None)
    if people and tp:
        sheets_have = tp * 500
        sheets_per_day = people * 57
        need_sheets = sheets_per_day * 14
        if need_sheets > sheets_have:
            return 'Oooops. You need to buy more TP!'
        else:
            return 'Wow. You have enough TP!'
    return 'Uknown keys in dict'

print(task2({'people': 3, 'tp': 1}))

# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0b"
# encrypt("karaca") ➞ "0c0r0k"
# encrypt("burak") ➞ "k0r3b"
# encrypt("alpaca") ➞ "0c0pl0"

def task3(word: str):
    letters = {
        'a': '0',
        'e': '1',
        'i': '2',
        'o': '2',
        'u': '3'
    }
    reverse_word = word[::-1]
    for key, value in letters.items():
        reverse_word = reverse_word.replace(key, value)
    print(reverse_word)

task3('banana')
# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"

def task4(args: list):
    # --- one
    if args[0][0] == args[0][1] and args[0][0] == args[0][2]:
        return args[0][0]
    # --- two
    elif args[1][0] == args[1][1] and args[1][0] == args[1][2]:
        return args[1][0]
    # --- three
    elif args[2][0] == args[2][1] and args[2][0] == args[2][2]:
        return args[2][0]
    # | one
    elif args[0][0] == args[1][0] and args[0][0] == args[2][0]:
        return args[0][0]
    # | two
    elif args[0][1] == args[1][1] and args[0][1] == args[2][1]:
        return args[0][1]
    # | three
    elif args[0][2] == args[1][2] and args[0][2] == args[2][2]:
        return args[0][2]
    # \
    elif args[0][0] == args[1][1] and args[0][0] == args[2][2]:
        return args[0][0]
    # /
    elif args[0][2] == args[1][1] and args[0][2] == args[2][0]:
        return args[0][2]
    return 'Draw'

print(task4([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]))
print(task4([
    ["O", "O", "O"],
    ["O", "X", "X"],
    ["E", "X", "X"]
]))
print(task4([
    ["X", "X", "O"],
    ["O", "O", "X"],
    ["X", "X", "O"]
]))

print(task4([
    ["O", "O", "X"],
    ["E", "X", "X"],
    ["O", "E", "X"]
]))