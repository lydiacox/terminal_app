# Production Log
## 12-07-2021

Having completed my Software Development Plan, I have commenced writing code. I am tracking my outstanding tasks in Asana, because it is software I am already comfortable with, and I have enough new programs to learn as it is. All my outstanding tasks, including blocks of code, are tracked in Asana with deadlines, priorities and tags. I have exported these tasks to Excel, but I do not want to be tracking my process on two platforms, so intend to keep Asana up to date with status and notes.

The first code I wrote was the ascii art for the snowmen. Once I'd created the first snowman, it was easy to recreate my melting snowman. I don't think my puddle looks much like a puddle, but it will do.

While I did find this process fun, the bulk of my work writing the code will be the game play, so in the interest of saving time, I copied word art for the welcome screen and snowflakes for the game win screen. I have credited these websites in notes in my code.

I also created a small "dictionary" (actually just a list, not a dictionary in the Python sense) of words to use in the game. I stuck to nouns to keep it simple. No one wants a game where you have to guess "the".

My next step will be to write sudo code to get the overall structure of my code right.

## 14-07-2021

I made really good progress yesterday. I have written more than half of the code I'd planned on. I needed assistance getting my head around while loops, but once I had a better understanding of them, the rest of the code was much easier to write.

Today has not been as productive. There are two features which are giving me a lot of grief. The first is clearing the terminal between turns, which is happening at the wrong moments and making it difficult/impossible to read the messages I'd typed up. The second is having spaces allowed in the words. Checking the entry is a valid a-z is easy, adding space as an allowable character is more complicated.

As these features are not strictly necessary for the game to function, I will take them out for now. If I have time at the end, I'll add them back in.

## 15-07-2021

After great difficulty working out how to reveal only the guessed letters in the word, I have had a breakthrough and my application is now at minimum viable product. The play again feature isn't working as it should, and further testing of all the features is required, but the game works!

The clear screen feature is working, but I will likely only use it at the start of the game, after the secret word has been selected or typed. Turns out that *was* necessary, or player 2 would see the answer before they started.

The code itself could also probably be cleaned up a bit. Some of the functions can't be kept in the list_and_defs.py file, because they append lists kept in snowperson.py, and linking both files to eachother creates an infinite loop, but that doesn't mean I can't make the whole thing easier to read.

I also realised that the ascii art of snowflakes hadn't added '\\' for every '\' to be printed, so I went through and fixed those.