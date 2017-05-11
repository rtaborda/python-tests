# Client app for Password Generator

from password_generator import * 

print('Welcome to the Password Generator console app!')
useSpecialChars = input('Do you want to use special characters in the generated password? (y/n): ')
passwordGenerator = PasswordGenerator(useSpecialChars == 'y')
print('Type "exit" at anytime to close the app')
print('--------------------------------------------')

while True:
	size = input('Specify the size of the password: ')
	
	if size.lower() == 'exit':
		break
	
	try:
		parsedSize = int(size)
	except ValueError:
		print('You must specify a numeric value or "exit" if you want to close the app')
		print('--------------------------------------------')
		continue
	
	try:
		print('Your generated password: ' + passwordGenerator.generatePassword(parsedSize))
	except ValueError as ex:
		print(ex)
		print('--------------------------------------------')
		continue
	
	print('--------------------------------------------')
