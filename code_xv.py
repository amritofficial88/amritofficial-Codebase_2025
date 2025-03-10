import sys


# A class to store a BST node
class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Recursive function to insert a key into a BST
def insert(root, key):

	# if the root is None, create a new node and return it
	if root is None:
		return Node(key)

	# if the given key is less than the root node, recur for the left subtree
	if key < root.data:
		root.left = insert(root.left, key)

	# if the given key is more than the root node, recur for the right subtree
	else:
		root.right = insert(root.right, key)

	return root


# Function to find the k'th largest node in a BST.
# Here, `i` denotes the total number of nodes processed so far
def kthLargest(root, i, k):

	# base case
	if root is None:
		return None, i

	# search in the right subtree
	left, i = kthLargest(root.right, i, k)

	# if k'th largest is found in the left subtree, return it
	if left:
		return left, i

	i = i + 1

	# if the current node is k'th largest, return its value
	if i == k:
		return root, i

	# otherwise, search in the left subtree
	return kthLargest(root.left, i, k)


# Function to find the k'th largest node in a BST
def findKthLargest(root, k):

	# maintain index to count the total number of nodes processed so far
	i = 0

	# traverse the tree in an inorder fashion and return k'th node
	return kthLargest(root, i, k)[0]


if __name__ == '__main__':

	keys = [15, 10, 20, 8, 12, 16, 25]

	root = None
	for key in keys:
		root = insert(root, key)

	k = 2
	result = findKthLargest(root, k)

	if result != sys.maxsize:
		print(result)
	else:
		print("Invalid Input")
