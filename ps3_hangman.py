# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    flag=True
    dictionary={}
    for i in enumerate(lettersGuessed):
        dictionary[i[1]]=i[0]
    
    for i in secretWord:
        if not (i in dictionary):
            flag=False
    return flag

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    dictionary={}
    string=''
    for i in enumerate(lettersGuessed):
        dictionary[i[1]]=i[0]

    for i in secretWord:
        if i in dictionary:
            string=string+i
        else:
            string=string+'_ '
    return string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    strg=''
    dictionary={}
    for i in enumerate(string.ascii_lowercase):
        dictionary[i[1]]=1
    
    for i in lettersGuessed:
        if i in dictionary:
            dictionary[i]=0   
    
    for i in dictionary:
        if dictionary[i]==1:
            strg=strg+i

    list=sorted(strg)
    strg=''
    for i in list:
        strg=strg+i
        
    return strg

def isCorrectGuess(secretWord, lettersGuessed):
    dictionary={}
    for i in lettersGuessed:
        dictionary[i]=1
    secretDict={}
    for i in secretWord:
        secretDict[i]=1
    flag=True
    #print("Dictionary")
   # print(dictionary)
   # print(secretDict)
    for i in dictionary:
        #print(i)
        if not (i in secretWord):
            flag=False
    return flag
            
    

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
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("-----------")
    mistakesMade=0
    lettersGuessed=[]
    correctGuessed=[]
    lettersDict={}
    availableLetters=getAvailableLetters(lettersGuessed)
    #print(getGuessedWord(secretWord,lettersGuessed))
    while (mistakesMade<8):
        print("You have "+str(8-mistakesMade)+" guesses left")
        availableLetters=getAvailableLetters(lettersGuessed)
        print("Available Letters: "+availableLetters)
        user=input("Please guess a letter: ")
        user=user[0].lower()
        if not user in lettersDict:
            lettersDict[user]=1
            correctGuessed.append(user)
            lettersGuessed=list(lettersDict.keys())
            if not isCorrectGuess(secretWord, correctGuessed):
                print("Oops! That letter is not in my word: "+
                     getGuessedWord(secretWord,lettersGuessed))
                mistakesMade+=1
                correctGuessed.pop()
                
                
            else:
                print("Good guess: "+
                      getGuessedWord(secretWord,lettersGuessed))
        else:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            
        print("-----------")

        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you've won!")
            return None
    else:
        print("Sorry, you ran out of guesses. The word was " +
               secretWord +".")
        return None

        
        
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
hangman('sea')
