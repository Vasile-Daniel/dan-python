# Author Vasile Daniel Dan, original data: september 2020, data modified: 11.03.2021, Edinburgh, UK 
######################################################################################################
import random
from random import choice
###########################################################################################################
words = ["python", "apple","hello", "google", "orange"] # a word list is generated
secret_word = random.choice(words) # choose, at random, a word from the generated list
dashes = "-" * len(secret_word) # it will generates as many dashes as the letter has the word
guesses_left = 10 # the number of attempts to guess the correct letter

###########################################################################################################
def get_guess():
    while True:
        guessed_character = input("Enter a character: ")
        if not guessed_character.islower():
            print("enter lower case letter only!!")
            continue
        elif len(guessed_character) != 1:
            print("enter one lower case letter only!!")
            continue
        else:
            return guessed_character

#########################################################################################################
def update_dashes(secret_word, dashes, guessed_char):
    found = 0
    
    for i in range(len(secret_word)):
        if secret_word[i] == guessed_char and dashes[i] == "-":
            dashes = dashes[:i] + guessed_char + dashes[i+1:]
            found = 1
      
    if found == 1:        
        return dashes
    else:
        return 0
#####################################################################################################   
while secret_word != dashes and guesses_left > 0: 
    print( guesses_left, "incorrect guesses left")
    print(dashes)

    guessed_char = get_guess()
    result = update_dashes(secret_word, dashes, guessed_char)
    
    if result == 0:
        guesses_left -= 1 
    else:
       dashes = result
 
######################################################################################################            
if secret_word == dashes:
    print("Congrats. You win! The word was: ", secret_word)
else:
    print("You lose! The word was: ", secret_word)

######################################################################################################