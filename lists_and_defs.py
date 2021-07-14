import random

# Got list from https://onlymyenglish.com/common-noun-list/
dictionary = ["adult", "age", "amount", "area", "back", "bed", "blood", "body", "book", "box", "boy", "bulb", "bunch", "business", "camera", "chicken", "child", "chocolates", "city", "clothes", "colony", "colours", "company", "computer", "continent", "council", "country", "course", "cycle", "dates", "day", "death", "desk", "door", "egg", "face", "fact", "factory", "family", "farm", "farmer", "father", "fish", "floor", "flowers", "flood", "fridge", "food", "future", "game", "garden", "gas", "glass", "group", "health", "hill", "hospital", "idea", "image", "industry", "island", "jewellery", "job", "kitchen", "land", "law", "leaves", "leg", "letter", "life", "magazine", "market", "metal", "mirror", 'mobile', 'money', 'morning', 'mother', 'mountain', 'movie', 'name', 'nest', 'news', 'ocean', 'oil', 'painter', 'park', 'party', 'pen', 'pencil', 'person', 'picture', 'pillow', 'place', 'plant', 'pond','rain', 'rate', 'result', 'ring', 'road', 'rock', 'rocket', 'room', 'rope', 'rule', 'sale', 'school', 'shape', 'ship', 'shop', 'sister', 'site', 'skin', 'snacks', 'son', 'song', 'sort', 'sound', 'soup', 'sports', 'state', 'stone', 'street', 'system', 'taxi', 'tea', 'teacher', 'team', 'toy', 'tractor', 'trade', 'train', 'video', 'view', 'water', 'waterfall', 'week', 'women', 'wood', 'word', 'year', 'yesterday']

def get_players():
    players = False
    while players == False:
        players = input('Are there 1 or 2 players?: ')
        if (players != '1') and (players != '2'):
            print('Please enter "1" or "2"')
            players = False
    return players

def get_word(players):
    word = False
    while word == False:
        if players == '1':
            word = random.choice(dictionary)
        elif players == '2':
            word = input('What word would you like Player 2 to guess? (A thru Z only.) Make sure they can\'t see your screen!:\n')
            if not word.isalpha():
                print('Please only use letters (a thru z)')
                word = False
            elif len(word) < 2:
                print('At least two characters, please.')
                word = False
    return word.upper()

def hide(word):
    hidden = ''
    for letter in word.upper():
        if letter != ' ':
            hidden += '_'
        else:
            hidden += ' '
    return hidden

def get_guess():
    valid_guess = False
    while valid_guess == False:
        valid_guess = input('Guess a letter or word: ')
        if not valid_guess.isalpha():
            print('Only letters (a thru z)')
            valid_guess = False
    return valid_guess.upper()