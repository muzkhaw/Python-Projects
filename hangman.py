import random
from words import words

def get_valid_word(words):
    word = random.choice(words) # chose word
    while '' in word or '' in word:
        word = random.choice(words)

    return word.title()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)v# letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guesseed

    while len(word_letters) > 0:
       
       
    user_letter = input("Type something: ").upper()
    if user_letter in alphabet - used_letters:
     used_letters.add(user_letter)
    if user_letter in word_letters:
        word_letters.remove(user_letter)
    elif user_letter in used_letters:
       print("You already have used that character")
    else:
       print("You already have used that letter")