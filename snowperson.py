import lists_and_defs
import ascii_art

won = False
melts = 0
guessed = []
word = 'confused'

# Find out if there's one player or two
while not won:
    print(ascii_art.game_name)
    print('Welcome to Snowman! Guess the word or your Snowman will melt!')
    players = lists_and_defs.get_players()
    word = lists_and_defs.get_word(players)


# Convert word(s) to underscores
# WHILE LOOP
# Print snowman scene 0
# Print hashed answer
print(lists_and_defs.hide(word))
# Input guess, check it is an allowable character, check if it's in the answer
# Print next snowman scene and hashed answer
# End LOOP
# If guessed correctly, show win scene and the word
# If guesssed incorrectly, show puddle and the word
# Ask if they want to play again
