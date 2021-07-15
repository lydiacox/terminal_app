import lists_and_defs
import ascii_art

won = False
melts = 0
letters_guessed = []
print(ascii_art.game_name)
print('Welcome to Snowman! Guess the word or your Snowman will melt!')
while not won:
    players = lists_and_defs.get_players()
    word = lists_and_defs.get_word(players)
    lists_and_defs.clear_screen()
    print('Let\'s play Snowman!')
    # generate currently revealed word
    hidden = lists_and_defs.hide(word)
    while melts <= 8:
        print(ascii_art.snow_scenes[melts])
        guess = lists_and_defs.valid_guess()
        if len(guess) == 1:
            if guess in letters_guessed:
                print('Choose another letter, you already guessed that one.')
            elif not guess in word:
                print('Nope, try again!')
                melts += 1
                letters_guessed.append(guess)
            else:
                print('Yep, you got one!')
                letters_guessed.append(guess)
                hidden = lists_and_defs.currently_revealed(guess, word, hidden)
                print(len(hidden), len(word))
                if hidden == word:
                    won = True
                    melts = 9
        elif len(guess) == len(word):
            if guess == word:
                won = True
                melts = 9
            else:
                print('Nope, that\'s not it!')
                melts += 1
        else:
            print('Please enter a single letter or guess the whole word.')
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