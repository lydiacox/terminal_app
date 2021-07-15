import lists_and_defs
import ascii_art

won = False
melts = 0
letters_guessed = []
print(ascii_art.game_name)
print('Welcome to Snowman! Guess the word or your Snowman will melt!')
while won == False and melts <= 8:
    players = lists_and_defs.get_players()
    word = lists_and_defs.get_word(players)
    hidden = lists_and_defs.hide(word)
    lists_and_defs.clear_screen()
    print('Let\'s play Snowman!')
    print(ascii_art.snow_scenes[melts])
    guess = lists_and_defs.valid_guess()
    if len(guess) == 1:
        if guess in letters_guessed:
            print('Choose another letter, you already guessed that one.')
        elif guess not in word:
            print('Nope, try again!')
            letters_guessed.append(guess)
            melts += 1
        else:
            print('Yep, you got one!')
            letters_guessed.append(guess)
            hidden_word = lists_and_defs.guessed_word(guess, hidden)
            if '_' not in hidden_word:
                won = True
    elif len(guess) == len(word):
        if guess == word:
            won = True
        else:
            print('Nope, that\'s not it!')
            melts += 1
    else:
        print('Please enter a single letter or guess the whole word.')
    print(ascii_art.snow_scenes[melts])
    print(lists_and_defs.guessed_word)
if won:
    print(f'YOU GOT IT! {word} was the word!')
else:
    print(f'Your snowman melted! :-( The word was {word}. Better luck next time!')
print(ascii_art.snowflakes)
again = lists_and_defs.play_again()
if again == 'Y':
    won = False
    melts = 0
    letters_guessed = []
else:
    exit()
        

# Print hashed answer
# Input guess, check it is an allowable character, check if it's in the answer
# Print next snowman scene and hashed answer
# End LOOP
# If guessed correctly, show win scene and the word
# If guesssed incorrectly, show puddle and the word
# Ask if they want to play again
