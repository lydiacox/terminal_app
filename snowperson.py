import lists_and_defs
import ascii_art

won_lost = False
melts = 0
letters_guessed = []
print(ascii_art.game_name)
print('Welcome to Snowman! Guess the word or your Snowman will melt!')
while won_lost == False:
    players = lists_and_defs.get_players()
    word = lists_and_defs.get_word(players)
    lists_and_defs.clear_screen()
    message = 'Let\'s play Snowman!'
    hidden = lists_and_defs.hide(word)
    while melts < 7:
        print(ascii_art.snow_scenes[melts])
        print(message)
        print(hidden)
        guess = lists_and_defs.valid_guess()
        if len(guess) == 1:
            if guess in letters_guessed:
                message = 'Choose another letter, you already guessed that one.'
            elif not guess in word:
                message = 'Nope, try again!'
                melts += 1
                letters_guessed.append(guess)
            else:
                message = 'Yep, you got one!'
                letters_guessed.append(guess)
                hidden = lists_and_defs.currently_revealed(guess, word, hidden)
                if hidden == word:
                    won_lost = 'Won'
                    melts = 9
        elif len(guess) == len(word):
            if guess == word:
                won_lost = 'Won'
                melts = 9
            else:
                message = 'Nope, that\'s not it!'
                melts += 1
        else:
            print('Please enter a single letter or guess the whole word.')
    if melts == 8:
        print(ascii_art.snow_scenes[8])
        print(f'Your snowman melted! :-( The word was {word}. Better luck next time!')
        won_lost = 'Lost'
print(ascii_art.snowflakes)
print(f'YOU GOT IT! {word} was the word!')
again = lists_and_defs.play_again()
if again == 'Y':
    won = False
    melts = 0
    letters_guessed = []
else:
    exit()