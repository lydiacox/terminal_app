# Testing

## Test 1 - 15-07-2021

### Feature to be tested: print guessed word status
One of the more complicated features of the application is that which hides the word to be guessed and reveals the guessed letters. I have been testing this as I wrote my code, but I have not yet tested it on a word with letters that repeat, such as "letters".

### Outline
I will run the game in 2 player mode, so that I can enter a word of my choosing. When gameplay commences, I will enter letters I know to be repeated, and observe the outcome.

### Case test A: "Letters"
Letters appeared as expected.

### Case test B: "AAABBBAAACCCC"
Letters appeared as expected.

### Outcome
This particular feature of the application ran as expected, with each instance of the letter appearing when guessed. I did encounter other bugs, however. These included the play again feature, which does not work as expected, and the placement of the "you won" message. Because this appears above the snowflakes ascii art, which is quite large, it moves too easily out of view.

## Test 2 - 16-07-2021

### Feature to be tested: play again

### Outline
This feature allows players to start the game again after finishing play. I knew it to be broken during my previous test. I have amended two elements of the code. The first was adding parentheses after .upper, which had been missing. I have also put the main game in a function, so that I can execute the function if the user types "Y" or "y". 

To test, I will finish the game, either winning or losing, and when prompted about playing again, I will test y, Y, n, N, and invalid responses.

### Case test A: "y", "Y"
Game restarts, but the previous game is still visible.

### Case test B: "n", "N"
Program terminates.

### Case test C: "Maybe"
Player instructed to type "Y" or "N". Player remains in the loop until they enter a correct response.

### Outcome
The function now operates as intended. I will, however, add the clear screen function to the start of the main game, so that previous games are not visible.