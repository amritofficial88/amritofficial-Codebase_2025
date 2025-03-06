# A Linked List Node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


# Helper function to print a given linked list
def printList(head):

	ptr = head
	while ptr:
		print(ptr.data, end=' —> ')
		ptr = ptr.next

	print('None')


# Function to insert a given node at its correct sorted position into a given
# list sorted in increasing order
def sortedInsert(head, newNode):

	dummy = Node()
	current = dummy
	dummy.next = head

	while current.next and current.next.data < newNode.data:
		current = current.next

	newNode.next = current.next
	current.next = newNode
	return dummy.next


# Given a list, change it to be in sorted order (using `sortedInsert()`).
def insertSort(head):

	result = None   	# build the answer here
	current = head  	# iterate over the original list

	while current:
		# tricky: note the next reference before we change it
		next = current.next

		result = sortedInsert(result, current)
		current = next

	return result


if __name__ == '__main__':

	# input keys
	keys = [6, 3, 4, 8, 2, 9]

	# points to the head node of the linked list
	head = None

	# construct a linked list
	for i in reversed(range(len(keys))):
		head = Node(keys[i], head)

	head = insertSort(head)

	# print linked list
	printList(head)
