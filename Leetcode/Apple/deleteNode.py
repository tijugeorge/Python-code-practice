
class LinkedList(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def deleteNode(self, node):
		node.val = node.val.next
		node.next = node.next.next

	# or
	def deleteNode(self, node):
		while node.next and node.next.next:
			node.val = node.next.val
			node = node.next
		if node.next:
			node.val = node.val.next
			node.next = None
