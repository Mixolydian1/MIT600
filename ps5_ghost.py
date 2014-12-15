# Problem Set 5: Ghost
# Name: Adam Capulong

import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

print "Welcome to Ghost by Adam Capulong"

# boolean to track when game ends
gameOver = False
# player 1 = 1
activePlayer = 1
# track the current word fragment
currentWord = ""

while not gameOver:
    # remind the users of whose turn it is
    if activePlayer == 1:
        cmd = raw_input("Player 1 turn: ")
        print "Player 1 says letter: " + cmd.upper()
    else:
        cmd = raw_input("Player 2 turn: ")
        print "Player 2 says letter: " + cmd.upper()


    # add the lower-case letter to the end of the currentWord
    currentWord = currentWord + cmd.lower()
    print "Current word fragment: " + currentWord.upper()

    fragmentFound = False
    for word in wordlist:
        if currentWord == word[:len(currentWord)]:
            fragmentFound = True
        if len(currentWord) > 3:
            if word == currentWord:
                gameOver = True
                if activePlayer == 1:
                    print "Player 1 formed word", currentWord
                    print "Player 2 wins!"
                else:
                    print "Player 2 formed word", currentWord
                    print "Player 1 wins!"

    if fragmentFound == False:
        gameOver = True
        print currentWord, "does not begin a word."
        if activePlayer == 1:
            print "Player 2 wins!"
        else:
            print "Player 1 wins!"

    activePlayer = activePlayer*-1


