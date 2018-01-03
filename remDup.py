#Remove Duplicates from Unsorted List

class ListNode(object):
	def __init__(self, val, next = None):
		self.val = val
		self.next = next


	def deleteDuplicates(self, head):
		if head is None:
			return None
		curr = head
		while curr is not None:
			inner = curr
			while inner.next is not None:
				inner = curr
				if inner.next.val == curr.val:
					inner.next = inner.next.next
				else:
					inner = inner.next
			curr = curr.next
		return head
