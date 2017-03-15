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
	def Add(self, value):
		node = Node(value, null, null)
		
		if self.nodes.count == 0:
			self.nodes.add(node)
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
		if parent.Value > value:
			parent.left = newNode
		else:
			parent.right = newNode
	
	# Iterates through the tree, using recursion, to find the biggest value that is smaller than the limit passed to the method
	def SearchMaxValueSmallerThan(self, limit):
		ret = null
		SearchMaxValueSmallerThan(limit, self.nodes[0], ret)
		return ret
		
	def SearchMaxValueSmallerThan(limit, node, ret):
		# if we reached the end of a branch, or if the current node value is bigger or equal
		# to the limit and doesn't have a node on is left, it means we already found our value 
		# on the previous iterations
		if node is None or (node.value >= limit and node.left is None):
			return None

		# only set the ret value if the current node value is smaller than the limit
		if node.value < limit:
			ret = node.value
		
		if node.value >= limit:
			# if the current node value is bigger or equal to the limit go to the node's left branch
			SearchMaxValueSmallerThan(limit, node.left, ret)
		else:
			# otherwise go to the node's right branch
			SearchMaxValueSmallerThan(limit, node.right, ret)
			
			

# Testing
#tree = BinarySearchTree()
#tree.Add(11)
#tree.Add(3)
#tree.Add(54)
#tree.Add(6)
#tree.Add(42)
#tree.Add(95)
#tree.Add(2)
#tree.Add(45)
#tree.Add(24)
#tree.Add(23)
#tree.Add(34)
	
		