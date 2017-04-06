from binary_search_tree import * 
import unittest

class BinarySearchTreeTests(unittest.TestCase):
	def setUp(self):
		self.tree = BinarySearchTree()
		self.tree.add(11)
		self.tree.add(3)
		self.tree.add(54)
		self.tree.add(6)
		self.tree.add(42)
		self.tree.add(95)
		self.tree.add(2)
		self.tree.add(45)
		self.tree.add(24)
		self.tree.add(23)
		self.tree.add(34)
		
	def test_searchMaxValueSmallerThan(self):
		self.assertEqual(None, self.tree.searchMaxValueSmallerThan(2))
		self.assertEqual(3, self.tree.searchMaxValueSmallerThan(6))
		self.assertEqual(34, self.tree.searchMaxValueSmallerThan(35))
		self.assertEqual(42, self.tree.searchMaxValueSmallerThan(44))
		self.assertEqual(45, self.tree.searchMaxValueSmallerThan(54))
		self.assertEqual(54, self.tree.searchMaxValueSmallerThan(55))
		self.assertEqual(95, self.tree.searchMaxValueSmallerThan(100))
		
if __name__ == '__main__':
    unittest.main()
