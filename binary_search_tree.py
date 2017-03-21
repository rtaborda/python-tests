# A simple Bynary search tree implementation

class Node:
	def __init__(self, value, right, left):
		self.right = right
		self.left = left
		self.value = value
		
class BinarySearchTree:
	def __init__(self):
		self.nodes = []
	
	# Adds the value to the tree, making sure it maintains the tree ordered
	def add(self, value):
		node = Node(value, None, None)
		
		if len(self.nodes) == 0:
			self.nodes.append(node)
			return None
			
		current = self.nodes[0]
		parent = None
		
		# iterate through the tree until we find a leaf
		while current is not None:
			if current.value == value:
				# don't insert if this value already exists in the tree
				return None
			elif current.value > value:
				# if the value from the current node is bigger than the 
				# value we want to insert go left
				parent = current
				current = current.left
			elif current.value < value:
				# otherwise go right
				parent = current
				current = current.right
			
		# add the new node on the left of the current if it's smaller
		# otherwise add it on the right
		if parent.value > value:
			parent.left = node
		else:
			parent.right = node
	
	# Iterates through the tree, using recursion, to find the biggest value that is smaller than the limit passed to the method
	def searchMaxValueSmallerThan(self, limit):
		ret = [None]
		self.__searchMaxValueSmallerThan(limit, self.nodes[0], ret)
		return ret[0]
		
	def __searchMaxValueSmallerThan(self, limit, node, ret):
		# if we reached the end of a branch, or if the current node value is bigger or equal
		# to the limit and doesn't have a node on is left, it means we already found our value 
		# on the previous iterations
		if node is None or (node.value >= limit and node.left is None):
			return None

		# only set the ret value if the current node value is smaller than the limit
		if node.value < limit:
			ret[0] = node.value
		
		if node.value >= limit:
			# if the current node value is bigger or equal to the limit go to the node's left branch
			self.__searchMaxValueSmallerThan(limit, node.left, ret)
		else:
			# otherwise go to the node's right branch
			self.__searchMaxValueSmallerThan(limit, node.right, ret)
			
			

# Testing
# TODO Look into unit testing in Python
tree = BinarySearchTree()
tree.add(11)
tree.add(3)
tree.add(54)
tree.add(6)
tree.add(42)
tree.add(95)
tree.add(2)
tree.add(45)
tree.add(24)
tree.add(23)
tree.add(34)


print("Expected: 3 Result: " + str(tree.searchMaxValueSmallerThan(6)))
print("Expected: 34 Result: " + str(tree.searchMaxValueSmallerThan(35)))
print("Expected: 42 Result: " + str(tree.searchMaxValueSmallerThan(44)))
print("Expected: 45 Result: " + str(tree.searchMaxValueSmallerThan(54)))
print("Expected: 54 Result: " + str(tree.searchMaxValueSmallerThan(55)))
print("Expected: 95 Result: " + str(tree.searchMaxValueSmallerThan(100)))
	
		