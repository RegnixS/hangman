# %%
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    print(self.word_guessed)
                    self.word_guessed[idx] = guess 
                    print(self.word_guessed)
            self.num_letters = self.num_letters - 1
        else:
            print(f'Sorry, {guess} is not in the word.')
            self.num_lives = self.num_lives - 1
            print (f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Please enter a letter ')

            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.') 
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ['banana', 'mango', 'kiwi', 'plum', 'pear']
game = Hangman(word_list)
print(game.word)
game.ask_for_input()

# %%
