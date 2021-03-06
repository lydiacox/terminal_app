
# Snowman Game Software Development Plan

## Statement of Purpose and Scope
I am creating an application to enable users to play a game of hangman. Not wanting to dipict something as violent as lynching, the hangman will be replaced by a snowman. The snowman will gradually melt with each incorrect guess the player enters. Every correct guess will reveal the letter(s) in the word or phrase. The player will have a total of seven incorrect guesses before the snowman is reduced to a puddle and the game is lost.

The purpose of the game is entertainment and education. The target audience is anyone who is a bit bored and has even a basic knowledge of the English language. The game is often played by children and can help develop their vocabulary and spelling ability, but can be played by anyone.

The game will be able to be played by one or two players. In the single-player version, a random word or phrase will be selected from a list for the player to guess. In the two-player version, Player 1 will type in their own word or phrase for Player 2 to guess.

## Features
* Print a welcome screen with ascii art
* Find out whether it's 1 player or 2
* Get a word or phrase 
    * If only 1 player, select a random word or phrase from a list
    * If 2 player, have Player 1 enter a word or phrase
    * Check entered words are only letters, spaces or hyphens, convert to upper case. If disallowed characters are entered, display an error message instructing Player 1 to enter another word or phrase with only allowed letters
* Using a while loop, while the word or phrase is not correctly guessed, print ascii art snowman and underscores spaces for missing letters
    * Snowman art to be stored in a list, with the list index corresponding to the number of guesses remaining in the game.
* Get letter guesses from Player 2
    * Ensure just one letter per guess, or the guess is equal to the length of the word or phrase
    * Ensure guesses include only letters, otherwise display an error message instructing Player 2 to try again with only allowable letters
    * Keep a list of guesses to prevent guessing same letter twice
    * If a letter is guessed twice, display a message indicating the letter had already been guessed, and to try again. This will not count as an incorrect guess or cause the snowman to melt.
    * Convert guesses to upper case, check if the guessed letter is in the word(s)
* Update word & snowman status
    * After every guess, clear the screen and show an updated screen
    * After every correct guess, print the snowman's status and the word with correct guesses filled in
    * If all letters are guessed correctly, print a "you won" screen
    * After every incorrect guess, print the snowman with one more body part missing or melted and the word with correct guesses filled in
    * After seven incorrect guesses, print a puddle and the completed word

## User interaction and Experience
The player(s) will run the program and be greeted by a welcome screen. It will display ascii art of the name of the game, "Snowman", and ask them to input if there are one or two players. If anything is entered besides the number "1" or "2", the player(s) will be asked to enter a valid response.

If 1 player is selected, the game will go directly to the first snowman scene.

If 2 players is selected, Player 1 will be instructed to make sure that Player 2 cannot see the screen or keyboard, and to input a word or phrase for Player 2 to guess. If any characters other than a - z, hyphen or space is entered, Player 1 will be instructed to enter a valid response. The game will then go to the first snowman scene.

The first snowman scene will show a fully formed snowman, with a head, torso, body, eyes and nose, hat and scarf. The number of letters in the word or phrase will also be depicted. To make it easy to read, every missing letter will be represented by a two underscores, each separated by a single space. Spaces will be indicated by a double space. Hyphens will be shown where they are.

The player/Player 2 will be able it input their guess. They can either guess a single letter or the entire word or phrase. If they guess correctly, the snowman will remain the same and the correctly guessed letter will be revealed in all the spaces it occurs.

If the player guesses a letter that had already been guessed, they will be asked to input another letter. This will not affect the snowman.

If the player guesses incorrectly, a new snowman will be displayed, slightly melted. The displayed word will remain the same.

With each incorrect guess, the snowman will lose his hat, scarf, eyes, nose, head, arms, and torso. After seven incorrect guesses, the game will be lost. A puddle will be displayed, along with the completed word or phrase.

If the player guesses all the letters correctly, or guesses the entire word or phrase, the game will be won. A congratulatory screen will print with snowflake ascii art.

Whether the game was won or lost, players will be asked if they want to play again, and can enter Y or N. N will exit the program, Y will take them back to the welcome screen.

## Control Flow Diagram
![Screen shot of control flow diagram](diagram.png)