import random
import os
import fileinput
import time
f = open("dictionary.txt", "r") 
lines = f.readlines()
wordInt = random.randint(0, 999) #randomly chooses a line at beginning 
word = lines[wordInt] #gets the "word" from the line
word = word.strip('\n')
wordLen = len(word)

mystery = [] #hidden word placeholder
for i in range(wordLen):
    mystery.insert(0,' _ ')
def split(word):
    return list(word)
wordList = split(word)
guessesLeft = 10

guesses = []
while guessesLeft >0:
    correct = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Guess the word: (", guessesLeft ," guesses left)")
    print(mystery)
    guess = input('Guess the letter: ')
    for i in wordList:
        indices = [ez for ez, x in enumerate(wordList) if x == guess]
        if i == guess:
            for ex in indices:
                mystery[ex] = guess #fills the placeholder with the correct letter
                correct = 1
    if correct == 0:
        guessesLeft -= 1
    if mystery == wordList:
        break
if mystery == wordList:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Correct!")
        time.sleep(15)
if guessesLeft == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You lost! The answer is {} .".format(word))
    time.sleep(15)

#TODO
#eliminate one letter words
#compact code
#word input
