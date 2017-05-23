# A simple password generator that will try to generate a password using lower case
# and upper case letters, numbers and special characters. It doesn't however guarantee
# that the password generated will contain all of these components since the algorithm
# implemented here is very simple and quite random

import string
import random

class PasswordGenerator:
	def __init__(self, useSpecialCharacters):
		self.specialCharacters = [ '£', '$', '€', '%', '&', '*', '@', '#' ]
		self.minSize = 10
		self.useSpecialCharacters = useSpecialCharacters
		
	def generatePassword(self, size):
		if size < self.minSize:
			raise ValueError('The minimum size for the password is ' + str(self.minSize) + '. Size specified: ' + str(size))
			
		count = 0
		password = ''
		while count < size:	
			if self.useSpecialCharacters:
				upperLimit = 9
			else:
				upperLimit = 6
		
			number = random.randint(0, upperLimit)
			
			if number <= 3:
				password += random.SystemRandom().choice(string.ascii_letters)
			elif number <= 6:
				password += random.SystemRandom().choice(string.digits)
			else:
				password += random.SystemRandom().choice(self.specialCharacters)
			
			count = count + 1
		
		# Make sure that the password has at least one special character if useSpecialCharacters has been set to true
		if self.useSpecialCharacters and not any((c in self.specialCharacters) for c in password):
			password = password.replace(random.SystemRandom().choice(password), random.SystemRandom().choice(self.specialCharacters))
		
		return password