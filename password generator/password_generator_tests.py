from password_generator import *
import unittest

class PasswordGeneratorTests(unittest.TestCase):
	def setUp(self):
		self.generator = PasswordGenerator(True)
		
	def test_generatePassword_throwsValueError(self):
		size = random.randint(0, 9)
		with self.assertRaises(ValueError):
			self.generator.generatePassword(size)

	def test_generatePassword_returnsPassword(self):
		size = random.randint(10, 9999)
		password = self.generator.generatePassword(size)
		self.assertEqual(size, len(password))
		
	# TODO Add tests for passwords with and withous special characters
		
if __name__ == '__main__':
    unittest.main()
