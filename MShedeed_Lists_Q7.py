#Mohamed Shedeed
#Exercises - Lists, Strings, and Tuples
# Hi this is kam

import os
import random

#Question 7
os.chdir('/Users/mohamedshedeed/Documents/GIS Algorithms') #for group members: change the working directory to a folder on your computer where you have the .txt file
wordle = open('Exercises/wordle-solutions-08MAY2022.txt', 'r')
wordle = wordle.read()
wordle = wordle.splitlines()
print(wordle)

dictionary = open('Data/large.txt', 'r')
dictionary = dictionary.read()
dictionary = dictionary.splitlines()

dict5 = []
dict5 = [i for i in dictionary if len(i) == 5]
print(len(dict5))

random.seed(10)

def wordle_game():
    wordle1 = word = random.sample(wordle, 1)
    wordle1 = str(wordle1[0])
    guess = str(input('Guess a 5-letter word: '))
    while len(guess) != 5:
        guess = str(input('That word was not 5 letters. Please enter another: '))
    while guess not in dict5:
        guess = str(input('That was not an acceptable word. Please enter another: '))
    tries = 5
    response = []
    while tries > 0:
        guess = list(guess)
        wordle1 = list(wordle1)
        if guess == wordle1:
            print('Congratulations! That is the correct word')
            break
        if guess != wordle1:
            tries -=1
            for i in range(len(guess)):
                if guess[i] == wordle1[i]:
                    response.append(guess[i])
                    print('Letter', i + 1, 'is correct.', sep = " ")
                elif guess[i] in wordle1:
                    response.append('?')
                    print('Letter', i + 1, 'is in the word, but in a different spot.', sep = " ")
                else:
                    response.append('x')
                    print('Letter', i + 1, 'is in not in the word.', sep = " ")
            print(response[0] + response[1] + response[2] + response[3] + response[4])
            guess = input('Guess again: ')
        continue
    if tries == 0:
        print('Sorry! You have run out of tries. The word was', word[0], sep = " ")

wordle_game()
