
# Hangman Game
![Hangman (Image)](./asset/output-onlinegiftools.gif)

## Description
This Hangman game is a text-based implementation where players guess letters to uncover a hidden word. The game provides a set of possible words from which one is randomly selected for each game session. Players have a limited number of lives to guess the word correctly, and incorrect guesses lead to the drawing of a hangman. The game continues until the player either guesses the word correctly or runs out of lives.

## Features
- Randomly selects a word from a predefined list for each game.
- Allows players to guess letters until they either win or lose.
- Visual representation of the hangman as incorrect guesses accumulate.
- Tracks number of turns, errors, and displays current game state after each turn.
- Supports replayability with an option to start a new game after finishing.

## Requirements
- Python 3.12
- `utils/print_hangman.py` for ASCII art of hangman stages.
- `utils/game.py` for game logic.

## How to Run
1. Clone the repository to your local machine.
2. Ensure Python 3.12 is installed.
3. Run the following command to start the game:
   ```bash
   python game.py
   ```
4. Follow the prompts to guess letters and play the game.

## Game Controls
- Guess a letter: Enter a single alphabetical character to guess.
- Repeat guesses are not penalized, but incorrect guesses decrease remaining lives.
- Choose 'Y' or 'N' to play again or quit after each game session.

## Notes
- Developed using object-oriented principles.
- Clear screen functionality for Windows and Unix-based systems implemented using `os` module.

---
