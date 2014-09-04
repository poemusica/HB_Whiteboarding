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
for i in range(13):
	print fibonacci_iterative(i)