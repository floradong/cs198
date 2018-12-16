"""MORSE CODE TRANSLATOR

An algorithm that translates morse code into English"""

morse_code_dictionary = {
	'1':'.----', 
    '2':'..---', 
    '3':'...--', 
    '4':'....-', 
    '5':'.....', 
    '6':'-....', 
    '7':'--...', 
    '8':'---..', 
    '9':'----.', 
    '0':'-----', 
    ', ':'--..--', 
    '.':'.-.-.-', 
    '?':'..--..', 
    '/':'-..-.', 
    '-':'-....-', 
    '(':'-.--.', 
    ')':'-.--.-',
    'A': '.-', 
    'B':'-...', 
    'C':'-.-.', 
    'D':'-..', 
    'E':'.', 
    'F':'..-.', 
    'G':'--.', 
    'H':'....', 
    'I':'..', 
    'J':'.---', 
    'K':'-.-', 
    'L':'.-..', 
    'M':'--', 
    'N':'-.', 
    'O':'---', 
    'P':'.--.', 
    'Q':'--.-', 
    'R':'.-.', 
    'S':'...', 
    'T':'-', 
    'U':'..-', 
    'V':'...-', 
    'W':'.--', 
    'X':'-..-', 
    'Y':'-.--', 
    'Z':'--..'
	}

# Decode from morse code to English text

def morse_to_english(morse):
	morse += " "
	letter = ""
	word = ""
	space = 0
	for code in morse:
		# If there is no space, then it means that it is still the same 
		# character and you keep adding to the same character -- in this case,
		# the character is stored in the variable called 'letter' 
		if code != " ":
			# You add letter to code to keep track of the current character
			# and if it is a new character or not
			letter += code
			# Space keeps track of how many spaces there are. If space is 0, 
			# then that means that it is continuing the character. If the 'code'
			# is not a space, then that means that the next 'code' is still part
			# of the same character. 
			space = 0
		else:
			# You add a space to indicate the start of a new character
			space += 1
			# When space is 2, that means that there is a space before and 
			# after, signaling that is a new word
			if space == 2: 
				# Adding a space between words in English
				word += " " 
			else:
				word += list(morse_code_dictionary.keys())[list(morse_code_dictionary 
                .values()).index(word)] 
                letter = ""
	return word

def english_to_morse(english):
	morse = " "
	for letter in english:
		if letter != " ":
			#Add the corresponding letter from the dictionary to the word
			morse += morse_code_dictionary[letter] + " " 
		else: 
			#If it is a space, add a space in the morse code worse 
			morse += " "
	return morse
