import random
import lists_and_defs

answer = ''
guesses_remaining = 7
players = ''

while players == False:
    input('How many players are there? 1 or 2?')
    if not players == '1' or players == '2':
        print('Please enter 1 or 2')
    else:
        pass


# for letter in answer:
#     len(answer)