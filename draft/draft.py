# from typing import List


# def get_word() -> str:
#     """
#     Prompt the user for a word and return it
#     :return: str : The word that the player entered
#     """
#     return (lambda x: x if len(x) > 1 else get_word())(input("Enter your word please"))


# def get_lives() -> int:
#     """
#     Prompt the user for the number of lives and return it
#     :return: int : the number of lives
#     """
#     return (lambda x: x if x.isdigit() else get_lives())(input("How many lives? "))


# def get_guess(suggested_letters) -> List:
#     """
#     Getter for suggested_letters
#     :param suggested_letters: A list of the letters suggested by the guesser player
#     :return: The list of suggested_letters
#     """
#     return suggested_letters


# def get_guess(*args) -> str:
#     # letter = input("Enter a letter")
#     # while len(letter.trim()) != 1 or letter in args :
#     #     letter = input("Enter a letter")
#     # return letter
#     return ((lambda letter: letter if len(letter.strip()) == 1 and letter in args else get_guess(*args))
#             (input("Enter a letter: ")))


# def asses_guess(secret_word, guessed_letter, lives_left) -> int:
#     """
#     Outputs if the guess is correct or not
#     :param secret_word: the word to be guessed
#     :param guessed_letter: the last letter suggested from guesser player
#     :param lives_left: lives left
#     :return: int : returns the current lives of the player
#     """
#     if guessed_letter not in secret_word:
#         lives_left -= 1
#     return lives_left


# def display_word(secret_word, suggested_letter):
#     """
#     Displays the secret word with letter found or "_".
#     :param secret_word: The secret word in list format
#     :param suggested_letter: The list of guessed letters
#     :return: returns True if the correct word has been found
#     """
#     return True if [letter if letter in suggested_letter else '_' for letter in secret_word] == secret_word else False
