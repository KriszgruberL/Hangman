import os
import platform
import random
from typing import List

from utils.words import Words
from utils.print_hangman import PrintHangman

class Hangman:
    def __init__(self):
        """
        Initializes a new instance of the Hangman game with default attributes.
        """
        self.possible_words: List[str] = Words().words_list
        self.title = PrintHangman().title_hangman
        self.reset_game()

    def reset_game(self):
        """
        Resets the game state for a new round of Hangman. Clears the console,
        selects a new word, and resets all game attributes.
        """
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        self.word_to_find: List[str] = [*self.possible_words[random.randrange(len(self.possible_words))].upper()]
        self.lives: int = 6
        self.correctly_guessed_letters: List[str] = ['_' for _ in range(len(self.word_to_find))]
        self.wrongly_guessed_letter: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.print_hangman: List[str] = PrintHangman().ascii_hangman

    def get_guess(self, guess) -> str:
        """
        Prompts the player to guess a letter and ensures it is a valid single alphabetic character.
        :return: A single uppercase letter guessed by the player.
        """
        guess: str = guess.upper().strip()

        if not guess.isalpha() or len(guess) != 1:
            raise ValueError("Invalid guess. Please enter a single alphabetic character.")
        return guess

    def update_game_state(self, guess: str) -> None:
        """
        Updates the game state based on the player's guess.
        :param guess: The letter guessed by the player.
        """
        self.turn_count += 1
        in_it: bool = False  # Flag to check if the guessed letter is in the word.
        for i in range(len(self.word_to_find)):
            if guess == self.word_to_find[i]:
                self.correctly_guessed_letters[i] = guess
                in_it = True

        if not in_it:
            self.wrongly_guessed_letter.append(guess)
            self.lives -= 1
            self.error_count += 1

    def play_one_turn(self):
        """
        Conducts a single turn of the game, including getting a guess, updating the game state, 
        and displaying the game status.
        """
        guess = self.get_guess()
        if guess not in self.wrongly_guessed_letter and guess not in self.correctly_guessed_letters:
            self.update_game_state(guess)
            return self.display_game_status(True, guess)
        return self.display_game_status(False, guess)

    def start_game(self) -> None:
        """
        Starts the game and continues until the player decides to stop.
        """
        self.reset_game()
        print(self.correctly_guessed_letters)

        game_continue = True

        while game_continue:
            self.play_one_turn()
            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                game_continue = False
            if self.lives < 1:
                self.game_over(self.lives)
                game_continue = False

    def display_game_status(self, flag: bool, guess: str | None):
        """
        Displays the current status of the game.
        :param flag: Boolean indicating whether the guess was new or a repeat.
        :param guess: The letter guessed by the player.
        """
        status = {
            "message" : "",
            "correctly_guessed_letters": self.correctly_guessed_letters,
            "incorrectly_guessed_letters": self.wrongly_guessed_letter,
            "lives": self.lives,
            "error_count": self.error_count,
            "turn_count": self.turn_count,
            "print_hangman": self.print_hangman[self.error_count]
        }
        if not flag:
            status["message"] = f"\nYou already proposed the letter {guess}"
                
        return status

    def game_over(self) -> bool:
        """
        Checks if the game is over (i.e., the player has run out of lives).
        :param lives: The number of lives the player has.
        :return: Boolean indicating whether the game is over.
        """
        return self.lives < 1

    def well_played(self) -> bool:
        """
        Displays a congratulatory message when the player wins the game.
        """
        return self.correctly_guessed_letters == self.word_to_find

