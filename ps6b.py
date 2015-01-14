# Problem Set 6
# Adam Capulong

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"

def load_words():
    # Returns a list of valid words. Words are strings of lowercase letters.
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    if len(word) == n:
        score = 50
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    return score

def get_time_score(score,total_time):
    ## The player's score is penalized for one thousanth of a point for every hundreth of a second.
    return score - float(int(total_time*100))/1000

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    n/3 of the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = {}
    for key in hand:
        newHand[key] =  hand.get(key,0)
    for letter in word:
        newHand[letter] = newHand.get(letter,0) - 1
    return newHand

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    if word in word_list:
        newHand = {}
        for key in hand:
            newHand[key] =  hand.get(key,0)
        newHand = update_hand(hand,word)
        for key in newHand:
            if newHand[key] < 0:
                return False
        return True
    else:
        return False

def is_hand_empty(hand):
    for key in hand:
        if hand[key] > 0:
            return False
        elif hand[key] < 0:
            print "****ERROR: negative letters****"
    return True

def play_hand(hand, word_list, time_limit):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * If the user takes too long to enter a word, the round is over.  

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    
    total_score = 0
    current_input = None
    while True:
        display_hand(hand)
        start_time = time.time()
        current_input = raw_input("Enter a word, or enter a \".\" to end the current round: ")
        end_time = time.time()
        # Calculte time precision hundreths of seconds.
        total_time = float(int((end_time - start_time)*100))/100  
        
        if current_input == ".":
            break
        elif total_time > time_limit:
            print "Your response took too long!"
            print "Total Score:", total_score
            break
        elif is_valid_word (current_input, hand, word_list):
            hand = update_hand(hand, current_input)
            word_score = get_word_score(current_input, HAND_SIZE)
            print "\"",current_input, "\" has earned", word_score, "base points."
            print "It took", total_time, "seconds to think of this word."
            ## The player's score is penalized one thousanth of a point for every hundreth of a second.
            word_score = word_score - total_time/10
            time_limit = time_limit - total_time
            print "Points this round: ", word_score
            print "Time remaining:", time_limit
            total_score = total_score + word_score
            print "Total Score:", total_score
        else:
            print "Word is invalid. Please try again."
        if is_hand_empty(hand):
            break
    return
    

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    
    print "Welcome to WordMaker by Adam Capulong"   

    hand = deal_hand(HAND_SIZE) # random init
    
    while True:
        time_limit = raw_input("Please enter the player's time limit per hand: ")
        try:
            time_limit = int(time_limit)
            break
        except ValueError:
            print "Please enter an interer number of seconds."

            
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list, time_limit)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list, time_limit)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
    return        

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

