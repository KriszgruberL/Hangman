import os
import platform
import random
from typing import List


class Hangman:
    def __init__(self):
        """
       Initializes a new instance of the Hangman game with default attributes
       :param possible_words: List[str] A list of possible words that can be chosen for the game.
       :param word_to_find: List[str] The word to be guessed
       :param lives: int Number of lives the player has
       :param correctly_guessed_letters: List[str] List of correctly guessed letters in the word, initially filled with underscores.
       :param wrongly_guessed_letter: List[str] List of incorrectly guessed letters.
       :param turn_count: int Counter for the number of turns played.
       :param error_count: int Counter for the number of errors (wrong guesses) made.
       """
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        # Python Split String in List using unpack(*) method and select the word using radrange
        self.word_to_find: List[str] = [*self.possible_words[random.randrange(len(self.possible_words))].upper()]
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ['_' for _ in range(len(self.word_to_find))]
        self.wrongly_guessed_letter: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def play(self) -> None:
        """
        Play a turn of Hangman and process the player's guess.
        """
        # Prompts the player to guess a letter. Checks if the guessed letter is correct, updates the game state
        # accordingly (correctly guessed letters, lives, errors), and prints the current game status.
        guess: str = ""  # The letter guessed by the player.
        while not guess.isalpha() or len(guess) != 1:
            guess = input("Guess a letter : ").upper().strip()

        if guess not in self.wrongly_guessed_letter and guess not in self.correctly_guessed_letters:
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

            print("\nCorrectly guessed letters : ", self.correctly_guessed_letters)
            print("Incorrectly guessed letters  : ", self.wrongly_guessed_letter)
            print("Lives : ", self.lives)
            print("Error count : ", self.error_count)
            print("Turn : ", self.turn_count)
            print("+----------------------------------------------------------+")

        else:
            print(f"\nYou already proposed the letter {guess}")
            print("+----------------------------------------------------------+")

    def game_over(self, lives: int) -> bool:
        """
        Function that test if the player has less than 1 life
        :param lives = int The number of lives the player has
        :return: An int that is the result of the two params being added to each other.
        """
        if lives < 1:
            print(f"You lose, the word was {"".join(self.word_to_find)}")
            return False
        else:
            return True

    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!.")

    def start_game(self) -> None:
        """
        Starts the game and continues until the player decides to stop.
        """
        choice: str = 'Y'  # Test for the first while loop
        while choice == 'Y':
            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system("clear")

            self.__init__()
            print(self.correctly_guessed_letters)

            while True:
                self.play()
                if self.correctly_guessed_letters == self.word_to_find:
                    self.well_played()
                    break
                if self.lives < 1:
                    self.game_over(self.lives)
                    break

            choice = input("Want to play again ? Y/N : ").upper()

            while choice not in ["Y", "N"]:
                choice = input("Want to play again ? Y/N : ").upper()
