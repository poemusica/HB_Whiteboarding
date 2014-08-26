import math

# Practice Problems from Cynthia

# ==================================
# QUESTION 1: Write a function takes the width of a square grid 
#and returns the coordinates that trace a spiral path through the grid
# starting from the top left corner and moving inward (clockwise).

def spiral_recursive(n):
	# base cases
	if n == 1 :
		return [(0, 0)]
	if n == 2:
		return [(0, 0), (1, 0), (1, 1), (0, 1)]

	# rest
	if n > 2:
		outer = []
		for i in range(n):
			outer.append((i, 0))
		for i in range(1, n):
			outer.append((n-1, i))
		for i in range(n-2, -1, -1):
			outer.append((i, n-1))
		for i in range(n-2, 0, -1):
			outer.append((0, i))
		inner = spiral_recursive(n-2)
		
		inner = [(x+1, y+1) for (x, y) in inner]
		outer = outer + inner
		return outer

def print_list(l):
	for item in l:
		print item

# print_list(spiral_recursive(1))
# print_list(spiral_recursive(2))
# print_list(spiral_recursive(4))

def spiral(n):
	# inputs less than one don't make sense.
	if n < 1:
		return None

	# set inital velocity. start out going east.
	vel_x = 1
	vel_y = 0

	# start at top-left corner.
	pos_x = 0
	pos_y = 0

	# set initial boundaries.
	max_x = n-1 # eastern boundary
	min_x = 0 # western boundary
	max_y = n-1 # northern boundary
	min_y = 0 # southern boundary

	print "upper:\t", (max_x, max_y), "lower:\t", (min_x, min_y), "vel:\t", (vel_x, vel_y), "pos:\t", (pos_x, pos_y)

	while True:
		# if you've got nowhere left to go, stop.
		if max_x == min_x and max_y == max_y:
			break
		
		# update position.
		pos_x += vel_x
		pos_y += vel_y

		# if you've gone too far east, go north instead.
		if pos_x > max_x:
			# change velocity to go north.
			vel_x = 0
			vel_y = 1
			# update position.
			pos_x = pos_x - 1 # correct for going too far east. 
			pos_y += vel_y
			# you'll never need to go this far south again. shrink the southern boundary.
			min_y += 1

		# if you've gone too far north, go west instead.
		if pos_y > max_y:
			# change velocity to go west.
			vel_x = -1
			vel_y = 0
			# update position.
			pos_x += vel_x
			pos_y = pos_y - 1 # correct for going too far north.
			 # you'll never need to go this far east again. shrink the eastern boundary.
			max_x -= 1

		# if you've gone too far west, go south instead.
		if pos_x < min_x:
			# change velocity to south.
			vel_x = 0
			vel_y = -1
			# update position.
			pos_x = pos_x + 1  # correct for going too far west.
			pos_y += vel_y
			 # you'll never need to go this far north again. shrink the northern boundary.
			max_y -= 1

		# if you've gone too far south, go east instead.
		if pos_y < min_y:
			# change velocity to go east.
			vel_x = 1
			vel_y = 0
			# update position.
			pos_x += vel_x
			pos_y = pos_y + 1  # correct for going too far south.
			# you'll never need to go this far west again. shrink the western boundary.
			min_x += 1

		print "upper:\t", (max_x, max_y), "lower:\t", (min_x, min_y), "vel:\t", (vel_x, vel_y), "pos:\t", (pos_x, pos_y)

# SOME TEST CASES
#Letters indicate the order that the coords should be printed.
# spiral(0)
# spiral(1)
# spiral(2)
# A(0, 0)	B(1, 0)
# D(0, 1)	C(1, 1)
# spiral(3)
# A(0, 0)	B(1, 0)	C(2,0)
# H(0, 1)	I(1, 1)	D(2, 1)
# G(0, 2)	F(1, 2)	E(2, 2)
# spiral(4)
# A(0, 0)	B(1, 0)	C(2,0)	D(3, 0)
# L(0, 1)	M(1, 1)	N(2, 1)	E(3, 1)
# K(0, 2)	P(1, 2)	O(2, 2)	F(3, 2)
# J(0, 3)	I(1, 3)	H(2, 3)	G(3, 3)

# ==================================
# QUESTION 2: Write a Linked List method that finds the k-th element from the end of a singly linked list.
# Do it in one pass through the linked list.
class LinkedList():
	head = None
	tail = None

	# ...other methods go here (See crackingcoding.py)

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

# ==================================
# QUESTION 3: The "100 chairs" problem

# You are in a room with a circle of 100 chairs. The chairs are 
# numbered sequentially from 1 to 100.

# At some point in time, the person in chair #1 will be asked to 
# leave. The person in chair #2 will be skipped, and the person in 
# chair #3 will be asked to leave. This pattern of skipping one 
# person and asking the next to leave will keep going around the 
# circle until there is one person left...the survivor.
# Write a program to determine which chair the survivor is sitting 
# in.

# Hints:
# 1) This can be solved with a circular linked list.
# 2) It's also possible to solve it without a linked list.
# Try both.

# Cheater solution
def survivor(n):
	if n == 0:
		return None
	if n == 1:
		return n

	exp = math.log(n, 2)
	exp = int(math.ceil(exp))

	next_pow_two = 2 ** exp

	steps = next_pow_two - n
	total = steps * 2
	return next_pow_two - total

# Test survivor function
for i in range(101):
	print "list of length: ", i, "\tsurvivor is: ", survivor(i)

# circularly linked list solution
class Node():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class CircularLinkedList():
	def __init__(self):
		self.head = None

	def __str__(self):
		if self.head == None:
			print None
		else:
			node = self.head
			while node.next != self.head:
				print node.data
				node = node.next
			print node.data

	def add(self, data):
		if self.head == None:
			self.head = Node(data)
			self.head.next = self.head
		else:
			node = self.head
			while node.next != self.head:
				node = node.next
			node.next = Node(data)
			node.next.next = self.head

	def link_to_head(self):
		if self.head == None:
			return None
		node = self.head
		while node.next != self.head:
			node = node.next
		return node

	def remove(self, target):
		if self.head == None:
			return
		if self.head.data == target and self.head.next == self.head:
			self.head = None
			return
		if self.head.data == target:
			node = self.link_to_head()
			node.next = self.head.next
			self.head = self.head.next
			return

		node = self.head
		while True:
			if node.next.data == target:
				node.next = node.next.next
				break
			else:
				node = node.next

	def remove_every_other(self):
		if self.head == None:
			return None
		if self.head.next == self.head:
			return self.head
		node = self.head
		while node.next != node:
			next = node.next
			self.remove(node.data)
			node = next.next
		return node

# TEST CASES

# Create Circular Linked List
# l = CircularLinkedList()
# for i in range(1, 7):
# 	l.add(i)
# l.__str__()

# Test remove method
# l.remove(1)
# print "removed 1"
# l.__str__()

# Test remove every other method
# n = l.remove_every_other()
# print "finding survivor"
# l.__str__()

# Test link to head method
# print "link to head is:"
# print l.link_to_head().data


# for i in range(1, 101):
# 	l = CircularLinkedList()
# 	for j in range(1, i):
# 		l.add(j)
# 	last = l.link_to_head()
# 	if last:
# 		print "list of length: ", last.data, 
# 	n = l.remove_every_other()
# 	if n:
# 		print "\tsurvivor is: ", n.data

# ==================================
# QUESTION 4: 
