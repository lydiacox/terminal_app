import random
# Got list from https://onlymyenglish.com/common-noun-list/
dictionary = ["adult", "age", "amount", "area", "back", "bed", "blood", "body", "book", "box", "boy", "bulb", "bunch", "business", "camera", "chicken", "child", "chocolates", "city", "clothes", "colony", "colours", "company", "computer", "continent", "council", "country", "course", "cycle", "dates", "day", "death", "desk", "door", "egg", "face", "fact", "factory", "family", "farm", "farmer", "father", "fish", "floor", "flowers", "flood", "fridge", "food", "future", "game", "garden", "gas", "glass", "group", "health", "hill", "hospital", "idea", "image", "industry", "island", "jewellery", "job", "kitchen", "land", "law", "leaves", "leg", "letter", "life", "magazine", "market", "metal", "mirror", 'mobile', 'money', 'morning', 'mother', 'mountain', 'movie', 'name', 'nest', 'news', 'ocean', 'oil', 'painter', 'park', 'party', 'pen', 'pencil', 'person', 'picture', 'pillow', 'place', 'plant', 'pond','rain', 'rate', 'result', 'ring', 'road', 'rock', 'rocket', 'room', 'rope', 'rule', 'sale', 'school', 'shape', 'ship', 'shop', 'sister', 'site', 'skin', 'snacks', 'son', 'song', 'sort', 'sound', 'soup', 'sports', 'state', 'stone', 'street', 'system', 'taxi', 'tea', 'teacher', 'team', 'toy', 'tractor', 'trade', 'train', 'video', 'view', 'water', 'waterfall', 'week', 'women', 'wood', 'word', 'year', 'yesterday']

allowable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-', ' ']

def computer_word():
    word = random.choice(dictionary)
    return word.upper()

def hide_word(answer):
    for letter in answer:
        if letter == "-":
            pass
        elif letter == " ":
            letter.replace("  ")
        