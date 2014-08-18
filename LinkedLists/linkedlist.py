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