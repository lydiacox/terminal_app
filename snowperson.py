import lists_and_defs
import ascii_art

won = False
melts = 0
guessed_letters =[]

# Find out if there's one player or two
print(ascii_art.game_name)
print('Welcome to Snowman! Guess the word or your Snowman will melt!')
while not won and melts < 8:
    players = lists_and_defs.get_players()
    words = lists_and_defs.get_word(players)
    hidden_word = lists_and_defs.hide(words)
    print('Let\'s play Snowman!')
#  Because in the following lines of code, the guesses are appended to lists stored in THIS file, I did not define these blocks of code in the lists_and_defs.py file, only to have them added back in this file.
    guess = False
    while guess == False:
        print(ascii_art.snow_scenes[melts])
        print(hidden_word)
        guess = input('Guess a letter or the answer: ').upper
        guess_nospace = guess.replace(' ','')
        if not guess_nospace.isalpha():
            print('Only letters (a thru z) and spaces')
            guess = False
        elif len(guess) == 1:
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
                guess = True
                won = True
        else:
            print('Please enter a single letter or guess the whole thing.')

# Print hashed answer
# Input guess, check it is an allowable character, check if it's in the answer
# Print next snowman scene and hashed answer
# End LOOP
# If guessed correctly, show win scene and the word
# If guesssed incorrectly, show puddle and the word
# Ask if they want to play again
