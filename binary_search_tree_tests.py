from binary_search_tree import * 

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