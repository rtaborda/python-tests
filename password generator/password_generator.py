# A simple password generator that will try to generate a password using lower case
# and upper case letters, numbers and special characters. It doesn't however guarantee
# that the password generated will contain all of these components since the algorithm
# implemented here is very simple and quite random

import string
import random

class PasswordGenerator:
	def __init__(self):
		self.specialCharacters = [ '£', '$', '€', '%', '&', '*', '@', '#' ]
		self.minSize = 10
		
	def generatePassword(self, size):
		if size < self.minSize:
			raise ValueError('The minimum size for the password is ' + str(self.minSize) + '. Size specified: ' + str(size))
			
		count = 0
		password = ''
		while count < size:	
			number = int(random.SystemRandom().choice(string.digits))
			
			if number <= 3:
				password += random.SystemRandom().choice(string.ascii_letters)
			elif number <= 6:
				password += random.SystemRandom().choice(string.digits)
			else:
				password += random.SystemRandom().choice(self.specialCharacters)
			
			count = count + 1
		
		return password
