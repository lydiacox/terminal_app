import lists_and_defs
import ascii_art
import os

won = False
guessed_letters = []
melts = 0
print(ascii_art.game_name)
print('Welcome to Snowman! Guess the word or your Snowman will melt!')
while not won:
    players = lists_and_defs.get_players()
    words = lists_and_defs.get_word(players)
    hidden_word = lists_and_defs.hide(words)
    print('Let\'s play Snowman!')
    while melts < 8:
        print(ascii_art.snow_scenes[melts])
        print(hidden_word)
        guess = lists_and_defs.get_guess()
        if len(guess) == 1:
            if guess in guessed_letters:
                print('Choose another letter, you already guessed that one.')
            elif guess not in words:
                print('Nope, try again!')
                guessed_letters.append(guess)
                melts += 1
            else:
                print('Yep, you got one!')
                guessed_letters.append(guess)
        elif len(guess) == len(words):
            if guess == words:
                print('YOU GOT IT!!')
                won = True
        else:
            print('Please enter a single letter or guess the whole thing.')
print(ascii_art.snowflakes)
        

# Print hashed answer
# Input guess, check it is an allowable character, check if it's in the answer
# Print next snowman scene and hashed answer
# End LOOP
# If guessed correctly, show win scene and the word
# If guesssed incorrectly, show puddle and the word
# Ask if they want to play again
