class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return "<Node: %s | %s >" % (str(self.data), str(self.next))

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def contents(self):
		node = self.head
		while node:
			print node,
			node = node.next

	def append(self, data):
		node = Node(data)

		if self.head == None:
			self.head = node
			self.tail = node

		self.tail.next = node
		self.tail = node

	def delete(self, data):
		if self.head == None:
			return
		if self.head.data == data:
			self.head = self.head.next
			return

		node = self.head.next
		while node.data:
			if node.data == data:
				return
			else:
				node = node.next

	def kth_from_end(self, k):
		if not self.head:
			return None
		if k < 0:
			return None

		count = 0
		current_tail = self.head
		current_k = self.head

		while current_tail:
			count += 1

			if count > k:
				current_k = current_k.next

			current_tail = current_tail.next
		
		if count < k:
			return None

		return current_k

	def center_node(self):
		if not self.head:
			return None

		current_center = self.head
		current_tail = self.head.next

		while current_tail and current_tail.next:
			current_center = current_center.next
			current_tail = current_tail.next.next

		return current_center


