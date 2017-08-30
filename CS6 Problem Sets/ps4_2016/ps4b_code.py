# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string



### HELPER CODE ###
def load_words(file_name):

	print("Loading word list from file...")
	# inFile: file
	inFile = open(file_name, 'r')
	# wordlist: list of strings
	wordlist = []
	for line in inFile:
		wordlist.extend([word.lower() for word in line.split(' ')])
	print(len(wordlist), "words loaded.")
	return wordlist


def is_word(word_list, word):

	word = word.lower()
	word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
	return word in word_list


def get_story_string():

	f = open("story.txt", "r")
	story = str(f.read())
	f.close()
	return story


### END HELPER CODE ###


class Message(object):
	def __init__(self, text):

		self.message_text = text
		self.msglist = self.message_text.split(' ')
		vwords = []
		for word in self.msglist:
			if is_word(wordlist, word):
				vwords.append(word)
		self.valid_words = vwords

	def get_message_text(self):

		return str(self.message_text)

	def get_valid_words(self):

		return list(self.valid_words)

	def build_shift_dict(self, shift):

		alphabet = string.ascii_lowercase
		shifted = alphabet[shift:] + alphabet[:shift]
		upperalpha = alphabet.upper()
		shiftedupper = shifted.upper()
		alphabet_and_shifted = zip(alphabet, shifted)
		upper_and_shifted = zip(upperalpha, shiftedupper)
		shift_dict = dict(alphabet_and_shifted + upper_and_shifted)

		return shift_dict

	def apply_shift(self, shift):

		string = self.message_text
		encryption_dict = self.build_shift_dict(shift)
		encoded = []
		for char in string:
			if char.isalpha():
				encoded.append(encryption_dict[char])
			else:
				encoded.append(char)
		return ''.join(encoded)


class PlaintextMessage(Message):
	def __init__(self, text, shift):
		Message.__init__(self, text)
		self.shift = shift
		self.encryption_dict = self.build_shift_dict(shift)
		self.message_text_encrypted = self.apply_shift(shift)


	def get_shift(self):

		return self.shift

	def get_encryption_dict(self):

		copydict = self.encryption_dict
		return copydict

	def get_message_text_encrypted(self):

		return self.message_text_encrypted

	def change_shift(self, shift):

		self.shift = shift
		self.encryption_dict = self.build_shift_dict(shift)
		self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
	def __init__(self, text):

		Message.__init__(self, text)

	def decrypt_message(self):

		shiftamt = 0
		matches = 0
		finalshift = 0
		finaltext = ""
		msglen = 0
		while shiftamt < 27:
			test = PlaintextMessage(self.message_text, shiftamt)
			temp = Message(test.get_message_text_encrypted())
			if matches < len(temp.get_valid_words()):
				matches = len(temp.get_valid_words())
				finalshift = test.get_shift()
				finaltext = test.get_message_text_encrypted()
				msglen = len(temp.msglist)
			else:
				shiftamt += 1
		if finalshift < 26:
			answer = (26 - finalshift, finaltext)
		else:
			answer = (finalshift - 26, finaltext)
		print matches, " words match of ", msglen
		return answer





if __name__ == '__main__':
	####load word list
	wordlist = load_words('words.txt')

	###### Test of Message (enter message), PlainText Message (encrypts message), and Cipher Message (decrypts message)
	# Takes the message entered below, encrypts it, then decrypts it, figuring out the shift value. Prints certain data as it runs.
	messageclass = Message("This is a message that was encrypted")

	print "Original Message:\n", messageclass.get_message_text(), "\n", "valid words in message:\n", messageclass.get_valid_words()

	plaintextmessage = PlaintextMessage(messageclass.get_message_text(), 13)
	print "entire message string encrypted:\n", plaintextmessage.get_message_text_encrypted()

	ciphermessage = CiphertextMessage(plaintextmessage.get_message_text_encrypted())
	print "message shift, message decrypted:\n", ciphermessage.decrypt_message()

	# Test of decrypting story (takes ~5 seconds):
	#encryptedstory = get_story_string()
	#poop = CiphertextMessage(encryptedstory)
	#print poop.decrypt_message()
