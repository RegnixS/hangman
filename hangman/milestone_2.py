# %%
import random

word_list = ['banana', 'mango', 'kiwi', 'plum', 'pear']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Please enter a letter ')
print(guess)

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')  
else:
    print('Oops! That is not a valid input.') 
# %%   