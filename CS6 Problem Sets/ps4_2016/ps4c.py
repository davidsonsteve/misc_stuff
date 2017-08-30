# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
     is_word(word_list, 'bat') returns
    True
     is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
wordlist = load_words(WORDLIST_FILENAME)
# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        vwords = []
        splittext = text.split()
        #print splittext
        for word in splittext:
            if is_word(wordlist, word):
                vwords.append(word)
                
        self.valid_words = vwords
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        mapped = {'A': vowels_permutation[0].upper(), 'E': vowels_permutation[1].upper(),
                  'I': vowels_permutation[2].upper(), 'O': vowels_permutation[3].upper(),
                  'U': vowels_permutation[4].upper(), 'a': vowels_permutation[0],
                  'e': vowels_permutation[1], 'i': vowels_permutation[2],
                  'o': vowels_permutation[3], 'u': vowels_permutation[4],
                  'b': "b", 'c':"c", 'd':"d", 'f':"f", 'g':"g", 'h':"h", 'j':"j", 'k':"k",
                  'l':"l", 'm':"m", 'n':"n", 'p':"p", 'q':"q", 'r':"r", 's':"s", 't':"t",
                  'v':"v", 'w':"w", 'x':"x", 'y':"y", 'z':"z", 'B':"B",'C':"C",'D':"D",
                  'F': "F",'G':"G",'H':"H",'J':"J",'K':"K",'L':"L",'M':"M",'N':"N",'P':"P",
                  'Q': "Q",'R':"R",'S':"S",'T':"T",'V':"V",'W':"W",'X':"X",'Y':"Y",'Z':"Z"}

        return mapped
        
       
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        string = self.message_text
        # encryption_dict = self.build_transpose_dict(transpose_dict)
        encoded = []
        for char in string:
            if char.isalpha():
                encoded.append(transpose_dict[char])
            else:
                encoded.append(char)
        return ''.join(encoded)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):


        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        permsoftext = get_permutations(permutation)
        mostmatches = 0
        bestfit = 0
        bestmessage = ""
        for i in permsoftext:
            test = str(i)
            tempdict = self.build_transpose_dict(test)
            teststring = self.apply_transpose(tempdict)
            testlist = teststring.split()
            temp_matches = 0
            for j in testlist:
                if is_word(wordlist,j):
                    temp_matches += 1
            if temp_matches > mostmatches:
                mostmatches = temp_matches
                bestfit = i
                bestmessage = teststring
        #print mostmatches, bestfit, bestmessage
        return bestmessage



    




if __name__ == '__main__':
    load_words("words.txt")





    print "######## TEST CASE 2 ######"
    message = SubMessage("Hello World!")
    message.get_valid_words()
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:   ", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:  ", enc_message.decrypt_message())


    print "######## TEST CASE 2 ######"
    message2 = SubMessage("Today was a very good day for many different people in the world!")
    #message2.get_valid_words()
    permutation2 = "oieua"
    enc_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:   ", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "Tudoy wos o viry guud doy fur mony deffirint piupli en thi wurld!")
    print("Actual encryption:  ", message2.apply_transpose(enc_dict2))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:  ", enc_message2.decrypt_message())

    print "######## TEST CASE 3 ######"
    message3 = SubMessage("Don't forget to bring me some food before you come home. I'm fat and need nourishment.")
    # message3.get_valid_words()
    permutation3 = "iuaeo"
    enc_dict3 = message3.build_transpose_dict(permutation3)
    print("Original message:   ", message3.get_message_text(), "Permutation:", permutation3)
    print("Expected encryption:", "Den't fergut te brang mu semu feed buferu yeo cemu hemu. A'm fit ind nuud neorashmunt.")
    print("Actual encryption:  ", message3.apply_transpose(enc_dict3))
    enc_message3 = EncryptedSubMessage(message3.apply_transpose(enc_dict3))
    print("Decrypted message:  ", enc_message3.decrypt_message())


    # encrypted = EncryptedSubMessage("Hawdy nueghbar. E'm yair freundly nueghbar Mr. Bittfocu.")
    # print encrypted.get_valid_words()
    # print encrypted.decrypt_message()

    #TODO: WRITE YOUR TEST CASES HERE

