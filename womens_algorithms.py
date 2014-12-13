import random

# Coding interview questions from
# http://meetupresources.herokuapp.com/whiteboard.html
 
# ==================================
# QUESTION 1: Write a method that converts an integer to its Roman numeral equivalent, i.e., 476 => 'CDLXXVI'.

arabic_to_roman = (
	(1000, 'M'),
	(900, 'CM'),
	(500, 'D'),
	(400, 'CD'),
	(100, 'C'),
	(90, 'XC'),
	(50, 'L'),
	(40, 'XL'),
	(10, 'X'),
	(9, 'IX'), 
	(5, 'V'),
	(4, 'IV'), 
	(1, 'I')
)

def number_to_numeral(n):
	numeral = []
	if n == 0:
		return None

	for item in arabic_to_roman:
		m = item[0]
		rom = item[1]
		result = n/m
		n = n - result * m
		numeral.append(rom * result)

	return "".join(numeral)

# TESTS
# for i in range(1,1001):
# 	print number_to_numeral(i)

 
# ==================================
# QUESTION 2: Pig Latin
# Write a method the takes in a string and returns the pig latin equivalent.
# Pig Latin takes the first consonant, moves it to the end of the word and places "ay" at the end.
# If the string starts with a vowel do nothing. "pig" = "igpay", "banana" = "ananabay"

def is_vowel(c):
	vowels = ('a', 'e', 'i', 'o', 'u')
	for vowel in vowels:
		if c == vowel:
			return True
	return False

def eng_to_pig_latin(w):
	if not w:
		return None
	first = w[0]
	if is_vowel(first):
		return w
	result = w[1:] + w[0] + 'ay'
	return result

# # TESTS
# print eng_to_pig_latin('maple')
# print eng_to_pig_latin('almond')

# ==================================
# QUESTION 3: Shuffle
# Without using a shuffle or sort write your own shuffle method for an array.
# The method will take an array and returns a new array with all of the elements in a random order.
# One important property of a good shuffle method is that every permutation is equally likely.

def shuffle(l):
	result = l[:]
	for i in range(len(result)):
		rand_i = random.randint(i, len(result)-1)
		temp = result[i]
		result[i] = result[rand_i]
		result[rand_i] = temp
	return result
# TEST
# l = range(10)
# print l
# print shuffle(l)

# ==================================
# QUESTION 4: Anagrams
# An anagram is a word formed by rearranging the letters of another word, e.g., iceman is an anagram of cinema.
# We're going to write a method called anagrams_for that takes as its input a word and an array of words,
# representing a dictionary, and returns an array consisting of all the anagrams of the input word. 
# anagrams_for should return an empty array ([]) if no anagrams are found in the dictionary.
# You don't have to worry about the order of the returned Array.

def find_anagrams(word, word_list):
	results = []
	sword = sorted(word)

	for w in word_list:
		if sorted(w) == sword:
			result.append(w)

	return results

# ==================================
# QUESTION 5: Factorial
# Write a recursive and iterative solution for a finding the factorial of a number. 
# If you don't remember, the factorial of a non-negative integer n, denoted n! 
# is the product of all positive integers less than . For example, 5! = 5 * 4 * 3 * 2 * 1

def factorial_recursive(n):
	if n == 1:
		return 1
	return n * factorial_recursive(n-1)

# TESTS
# for i in range(1, 8):
# 	print factorial_recursive(i)

def factorial_iterative_1(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

def factorial_iterative_2(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

# TESTS
# for i in range(1, 8):
# 	print factorial_iterative_2(i)

# ==================================
# QUESTION 6: Binary vs. Linear Searching

# Write an example demonstrating Binary Search. Write an example demonstrating Linear Search. 
# Hint: A linear search looks down a list, one item at a time, without jumping. 
# In complexity terms this is an O(n) search - the time taken to search the list gets bigger at the same rate as the list does. 
# A binary search is when you start with the middle of a sorted list, and see whether that's greater than or less than the 
# value you're looking for, which determines whether the value is in the first or second half of the list.

def binary_search(target, l):
	if l == []:
		return False

	middle = l[len(l)/2]
	if target == middle:
		return True

	if target < middle:
		return binary_search(target, l[0:len(l)/2])
	if target > middle:
		return binary_search(target, l[(len(l)/2)+1:])

# TESTS
# for i in range(10):
# 	l = range(i)
# 	print l, binary_search(7, l)

def linear_search(target, l):
	for e in l:
		if e == target:
			return True
	return False

# TESTS
# for i in range(10):
# 	l = range(i)
# 	print l, linear_search(7, l)

# ==================================
# QUESTION 7: Fibonacci

# Implement an iterative and recursive version of the Fibonacci sequence which take an integer n as input 
# and returns the nth Fibonacci number.

# In mathematics, the Fibonacci numbers or Fibonacci series or Fibonacci sequence are the numbers in the 
# following integer sequence:[1][2] 0,1,1,2,3,5,8,13,21,34,55,89,144 
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is 
# the sum of the previous two. In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the 
# recurrence relation F_n = F_{n-1} + F_{n-2}

def fibonacci_recursive(n):
	if n <= 1:
		return n
	return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# TESTS
# for i in range(13):
# 	print fibonacci_recursive(i)

def fibonacci_iterative(n):
	l = [0]
	if n == 0:
		return l
		# return 0
	if n <= 2:
		return l + ([1] * n) 
		# return 1

	n_1 = 1
	n_2 = 1
	l.append(n_2)
	l.append(n_1)

	for i in range(3, n):
		temp = n_1
		n_1 = n_1 + n_2
		n_2 = temp
		l.append(n_1)

	l.append(n_1 + n_2)
	return l
	# return n_1 + n_2

# TESTS
# for i in range(13):
# 	print fibonacci_iterative(i)


# ==================================
# QUESTION 8: Apple Stock
# I have an array stockPricesYesterday where the indices are the number of minutes 
# into the day (starting with midnight) and the values are the price of Apple stock 
# at that time. For example, the stock cost $500 at 1am, so stockPricesYesterday[60] = 500. 

# Write an efficient algorithm for computing the best profit I could have made from 
# 1 purchase and 1 sale of an Apple stock yesterday. Note: You must buy before you sell.

def max_profit(prices):
	if prices == []:
		return None
	current_max_profit = -prices[0]
	current_lowest_buy_price = prices[0]

	for price in prices:
		profit = price - current_lowest_buy_price
		if profit > current_max_profit:
			current_max_profit = profit
		if price < current_lowest_buy_price:
			current_lowest_buy_price = price

	return current_max_profit

# TESTS
# p = [17, 16, 18, 17, 14, 16]
# print max_profit(p)
# p = [18, 16, 16, 17, 14, 16]
# print max_profit(p)
# p = [14, 16, 16, 17, 18, 16]
# print max_profit(p)

# ==================================
# QUESTION 9-1: Arrays, Unique
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def unique(l):
	for i in range(len(l)):
		if l[i] in l[:i] or l[i] in l[i+1:]:
			return False
	return True

# TESTS
# l = range(5)
# print unique(l)
# l.append(3)
# print unique(l)

def unique_d(l):
	d = {}
	for e in l:
		d[e] = d.get(e, 0) + 1
		if d[e] > 1:
			return False
	return True


# TESTS
# l = range(5)
# print unique_d(l)
# l.append(3)
# print unique_d(l)

# ==================================
# QUESTION 9-2: Arrays, C-Style String
# Write code to reverse a C-Style String. 
# (C-String means that "abcd" is represented as five characters, 
# including the null character.)

def reverse_c_string(c):
	if len(c) < 2:
		return
	for i in range(len(c)/2):
		temp = c[i]
		c[i] = c[-i - 2]
		c[-i - 2] = temp
	return

# TESTS
# c_string = range(5)
# c_string.append(None)
# print c_string
# reverse_c_string(c_string)
# print c_string

# ==================================
# QUESTION 10-1: Strings, Duplicates
# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not. Write the test cases for this method.

# Does order matter? 

def remove_duplicates(s):
	pass

# TEST
# s = 'abcde'
# remove_duplicates(s)
# print s
# s = 'abcbdaae'
# remove_duplicates(s)
# print s

# ==================================
# QUESTION 10-2: Strings, Anagrams 
# Write a method to decide if two strings are anagrams or not.

def are_anagrams(s1, s2):
	ss1 = sorted(s1)
	ss2 = sorted(s2)
	if ss1 == ss2:
		return True
	return False

# TESTS
# print are_anagrams('orchestra', 'carthorse')
# print are_anagrams('yes', 'noo')

# ==================================
# QUESTION 11: Linked and Circularly Linked Lists

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def display(self):
		node = self.head
		while node:
			print node.data
			node = node.next

	def append(self, data):
		node = Node(data)

		if self.head == None:
			self.head = node
			self.tail = node
			return

		self.tail.next = node
		self.tail = node

	def delete(self, data):
		if self.head == None:
			return

		if self.head.data == data:
			if not self.head.next:
				self.tail = None
			self.head = self.head.next
			return	
		
		prev = self.head
		node = self.head.next
		while node:
			if node.data == data:
				if not node.next:
					self.tail = prev
				prev.next = node.next
				break
			else:
				prev = node
				node = node.next
	
	def center_node(self):
		if not self.head:
			return None

		current_center = self.head
		current_tail = self.head.next

		while current_tail and current_tail.next:
			current_center = current_center.next
			current_tail = current_tail.next.next

		return current_center

	# QUESTION 11-1: Lists, Linked, Delete Middle 
	# Implement an algorithm to delete a node in the middle of a singly linked list, 
	# given only access to that node.
	# EXAMPLE Input: the node 'c' from the linked list a->b->c->d->e
	# Result: nothing is returned, but the new linked list looks like a->b->d->e
	def del_mid(self):
		m = self.center_node()
		if m == None or m.next == None:
			return False
		m.data = m.next.data
		m.next = m.next.next
		return True

# TEST
# l = LinkedList()
# for i in range(5):
# 	l.append(i)
# l.display()
# print l.center_node().data
# l.del_mid()
# l.display() 
# print l.center_node().data


# ==================================
# QUESTION 11-2: Lists, Linked, Addition
# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE Input: (3 -> 1 -> 5) + (5 -> 9 -> 2) Output: 8 -> 0 -> 8

def plus(l1, l2):
	result = LinkedList()
	carry = 0

	n1 = l1.head
	n2 = l2.head

	while n1 or n2:
		if n1 and n2:
			n_sum = n1.data + n2.data + carry
			n1 = n1.next
			n2 = n2.next
		
		elif n1:
			n_sum = n1.data + carry
			n1 = n1.next
		
		elif n2:
			n_sum = n2.data + carry
			n2 = n2.next

		if n_sum >= 10:
			carry = n_sum/10
			n_sum -= carry * 10
		else:
			carry = 0

		result.append(n_sum)
	
	if carry:
		result.append(carry)

	return result

# TESTS
# l1 = LinkedList()
# l1.append(3)
# l1.append(1)
# l1.append(5)
# l1.display()
# l2 = LinkedList()
# l2.append(1)
# l2.append(5)
# l2.display()

# l3 = plus(l1, l2)
# l3.display()

# ==================================
# QUESTION 11-3: Lists, Circular Loop
# Given a circular linked list, implement an algorithm which returns node at the beginning of the loop. 
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, 
# so as to make a loop in the linked list.
# EXAMPLE input: A -> B -> C -> D -> E -> C [the same C as earlier] output: C

def find_loop_start(l):
	visited = {}
	node = l.head
	while node:
		if visited.get(node):
			return node.data
		visited[node] = True
		node = node.next
	return None

# TESTS
# l = LinkedList()
# l.append('A')
# l.append('B')
# l.append('C')
# l.append('D')
# l.append('E')
# l.tail.next = l.head.next.next
# print find_loop_start(l)

# ==================================
# QUESTION 11-4: Lists, Intersection
# Given two different lists of objects, come up with an efficient solution to find the intersection
# of the two lists.

def intersection(l1, l2):
	result = []
	d = {}
	for e in l1:
		d[e] = True
	for e in l2:
		if d.get(e, False):
			result.append(e)
	return result

# TESTS
# l1 = [2, 3, 1, 5, 6, 4]
# l2 = [5, 7, 9, 6, 2]
# print intersection(l1, l2)

# ==================================
# QUESTION 12: TREES

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# ==================================
# QUESTION 12-1: Trees, Balanced
# Implement a function to check if a tree is balanced. For the purposes of this question, 
# a balanced tree is defined to be a tree such that no two leaf nodes differ in distance 
# from the root by more than one.

# ==================================
# QUESTION 12-2: Trees, Directed, Route
# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

# ==================================
# QUESTION 12-3: Trees, Binary, Create from Array
# Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.

# ==================================
# QUESTION 12-3: Trees, Binary Search
# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
# (i.e., if you have a tree with depth D, you’ll have D linked lists).


# ==================================
# QUESTION 13: STACKS

# ==================================
# QUESTION 13-1: Stacks, Towers of Hanoi

# In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes 
# which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size 
# from top to bottom (e.g., each disk sits on top of an even larger one).

# You have the following constraints:
# (A) Only one disk can be moved at a time. 
# (B) A disk is slid off the top of one rod onto the next rod.
# (C) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first rod to the last using Stacks.

# ==================================
# QUESTION 13-2: Stacks, Sort
# Write a program to sort a stack in ascending order.
# You should not make any assumptions about how the stack is implemented.
# The following are the only functions that should be used to write this program:
# push | pop | peek | isEmpty.

