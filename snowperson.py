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
    lists_and_defs.get_players()

# If two player, get a word or words from the player
        # elif players == '2':
        #     word = input('Enter a word or phrase (a-z or spaces only). Make sure the other player can\'t see the screen or keyboard!')

# Check the word only has the allowable characters
# If one player, select random word from dictionary
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
