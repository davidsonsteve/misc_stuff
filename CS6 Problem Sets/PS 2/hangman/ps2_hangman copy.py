# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def printletters():
    print ' '.join(letters)
        
def testguess(guess):
    progress = []
    blank = "_"
    blankcount = 0
    for c in ans:
        if guessed.count(c) > 0:
            progress.extend(c)
        else:
            blankcount += 1
            progress.extend(blank)
    print ' '.join(progress)
    if blankcount == 0:
        print("Yay you win!")
        return False
    return True
    
    
        
ans = choose_word(wordlist)
guesses = 8
letters = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessed = []
unsolved = True


print("")
print("")
testguess(ans)
print("")




while guesses > 0 and unsolved:
    print("")
    print("")
    printletters()
    print("Guesses Remaining: "), guesses
    print("")
    
    guess = raw_input("Enter Guess: ")
    guessed.extend(guess)
    print("")
    if guess.lower() in letters:
        letters.remove(guess.lower())
        if guess not in ans:
            guesses -= 1
            print("Bad guess.=(  ")
            
        else:
            print("Great Guess! ")
           

    else:
        print("That's already been guessed or not a valid guess!")

        
        
    #testguess(guess.lower())
    print("")
    print("")
    unsolved = testguess(guess.lower())


if unsolved == False:
    print("Congratulations. Don't get cocky")
else:
    print("You Lose. Try again bitch.")
    print("The solution was "),ans



