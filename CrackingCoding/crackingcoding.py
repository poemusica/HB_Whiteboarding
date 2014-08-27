# QUESTION 1
# Test if all chars in a string are unique.

# SOLUTION 1
def unique_dict(s):
	d = {}
	for char in s:
		if d.get(char):
			return False
		d[char] = True
	return True

# in this case, run-time is n^2
def unique(l):
	for i in range(len(l)):
		if l[i] in l[:i] or l[i] in l[i+1:]:
			return False
	return return True

# TESTS 1
# s1 = "Jessica"
# s2 = "Devin"
# print unique(s1)
# print unique(s2)

# QUESTION 2
# Remove duplicates from an unsorted linked list.

# SOLUTION 2
class Node():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, node):
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def find(self, target):
		node = self.head
		if node.data == target:
			return node
		while node.next:
			if node.data == target:
				return node
			else:
				node = node.next

	def remove(self, target):
		if self.head == None:
			return
		if self.head.data == target and not self.head.next:
			self.head = None
			self.tail = None
			return
		if self.head.data == target:
			self.head = self.head.next

		node = self.head
		while node.next:
			if node.next.data == target and node.next.next:
				node.next = node.next.next
				return
			elif node.next.data == target:
				node.next = None
				self.tail = node
			else:
				node = node.next

	def remove_duplicates(self):
		d = {}
		node = self.head
		while node:
			d[node.data] = d.get(node.data, 0) + 1
			node = node.next
		for k in d:
			while d[k] > 1:
				self.remove(k)
				d[k] = d[k] - 1

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




# TESTS 2
l = LinkedList()
for i in range(1, 7):
	l.add(Node(i))
# l.add(Node(3))
# l.add(Node(3))
# l.add(Node(5))
# l.remove_duplicates()
node = l.head
while node:
	print node.data
	node = node.next

n = l.kth_from_end(4)
if n:
	print n.data
else:
	print n