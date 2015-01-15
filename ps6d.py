# Problem Set 6
# Adam Capulong

import random
import string
import time
from itertools import combinations

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
HAND_SIZE = 200
TIME_MULTIPLIER = 100
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

def get_words_to_points(word_list):
    """
    Returns a dict that maps every word to its point value.
    """
    points_dict = {}
    for word in word_list:
        points_dict[word] = get_word_score(word,HAND_SIZE)
    return points_dict

def get_word_rearrangements(word_list):
    '''
    Returns a dict that maps every rearragned word to a word in the scrabble dictionary.
    '''
    rearrange_dict = {}
    for word in word_list:
        rearrange_dict[''.join(sorted(word))] = word

    return rearrange_dict

def get_time_limit(points_dict, k):
    """
    Returns the time limit for the computer player as a function of the multiplyer k
    """
    start_time = time.time()
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word,HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time)*k


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

def get_string_hand(hand):
    """
    Returns the alphabetized string version of a hand (dict).
    """
    string_hand = ""

    for letter in hand:
        for x in range(0,hand[letter]):
            string_hand = string_hand + letter
    string_hand = "".join(sorted(string_hand))
    return string_hand


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

def is_valid_word(word, hand):
    """
    Returns True if word is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    newHand = {}
    for key in hand:
        newHand[key] =  hand.get(key,0)
    newHand = update_hand(hand,word)
    for key in newHand:
        if newHand[key] < 0:
            return False
    return True

def is_hand_empty(hand):
    for key in hand:
        if hand[key] > 0:
            return False
        elif hand[key] < 0:
            print "****ERROR: negative letters****"
    return True

def pick_best_word(hand):
    best_score = 0
    best_word = ""
    for word in points_dict:
        if is_valid_word(word,hand):
            if points_dict[word] > best_score:
                best_word = word
                best_score = points_dict[word]
    return best_word   

def pick_best_word_faster(hand):
    """
    given a STRING hand, RETURNS the word with the highest score

    combs is the list of alphabetized combinations of hand
    """
    combs = []
    hand_string = get_string_hand(hand)
    for x in reversed(range(1, len(hand_string)+1)):
        for y in combinations(hand_string, x):
            combs.append("".join(y))
    
    best_score = 0
    best_word = ""
    for comb in combs:
            if pointsdict[rearrange_dict[comb]] > best_score:
                best_score = pointsdict[rearrange_dict[comb]]
                best_word = comb
    return best_word 

def play_hand(hand, word_list, time_limit):
    """
    
    """
    slow_hand = hand
    fast_hand = hand

    slow_time_limit = time_limit
    fast_time_limit = time_limit

    total_score = 0
    current_input = None
    while True:
        display_hand(slow_hand)
        start_time = time.time()
        current_input = pick_best_word(slow_hand)
        end_time = time.time()
        # Calculte time precision hundreths of seconds.
        total_time = float(int((end_time - start_time)*100))/100  
        if current_input == "":
            break
        if total_time > slow_time_limit:
            print "Your *slow* computer's response took too long!"
            print "Total *slow* Score:", total_score
            break
        else:
            slow_hand = update_hand(slow_hand, current_input)
            word_score = get_word_score(current_input, HAND_SIZE)
            print "\"",current_input, "\" has earned", word_score, "base points."
            print "It took", total_time, "seconds to think of this word."
            word_score = word_score - total_time/10
            slow_time_limit = time_limit - total_time
            print "Points this round: ", word_score
            #print "Time remaining:", slow_time_limit
            total_score = total_score + word_score
            print "Total *slow* Score:", total_score

    total_score = 0
    current_input = None
    while True:
        display_hand(fast_hand)
        start_time = time.time()
        current_input = pick_best_word(fast_hand)
        end_time = time.time()
        # Calculte time precision hundreths of seconds.
        total_time = float(int((end_time - start_time)*100))/100  
        if current_input == "":
            break
        if total_time > fast_time_limit:
            print "Your *fast* computer's response took too long!"
            print "Total Score:", total_score
            break
        else:
            fast_hand = update_hand(fast_hand, current_input)
            word_score = get_word_score(current_input, HAND_SIZE)
            print "\"",current_input, "\" has earned", word_score, "base points."
            print "It took", total_time, "seconds to think of this word."
            word_score = word_score - total_time/10
            fast_time_limit = time_limit - total_time
            print "Points this round: ", word_score
            #print "Time remaining:", fast_time_limit
            total_score = total_score + word_score
            print "Total *fast* Score:", total_score        

    return
    

def play_game(word_list, time_limit):
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
    rearrange_dict = get_word_rearrangements(word_list)
    points_dict = get_words_to_points(word_list)
    time_limit = get_time_limit(points_dict, TIME_MULTIPLIER)
    print "get_time_limit returned:", time_limit
    play_game(word_list, time_limit)

