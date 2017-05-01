# Hangman game

import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print( str(len(wordlist)) + " words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
print('------------')

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    summa = 0
    buf = []
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] not in buf:
            summa += secretWord.count(lettersGuessed[i])
            buf.append(lettersGuessed[i])
    if summa == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    buf = ''
    for i in range(len(secretWord )):
        if secretWord[i] in lettersGuessed:
            buf +=secretWord[i]
        else:
            buf+='_'
    return buf



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    buf1 = string.ascii_lowercase
    buf2 = ''
    for i in range(len(buf1)):
        if buf1[i] not in lettersGuessed:
            buf2+=buf1[i]
    return buf2
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('------------')
    lettersGuessed = []
    life = 8
    while life != 0:
        print('You have ' + str(life) + ' guesses left')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        if guessInLowerCase in  lettersGuessed:
            lettersGuessed += guessInLowerCase
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('------------')
        elif  guessInLowerCase in secretWord:
            lettersGuessed += guessInLowerCase
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            print('------------')
        elif guessInLowerCase not in secretWord:
            lettersGuessed += guessInLowerCase
            print('Oops! That letter is not in my word: '+ getGuessedWord(secretWord, lettersGuessed))
            life-=1
            print('------------')
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            break
    if life == 0:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)
        return None
    


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
