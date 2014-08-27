import random

# ==================================
# QUESTION 1: reverse a list in place
def cust_reverse(l):
	mid = (len(l) - 1) /2
	for i in range(mid):
		temp = l[i]
		l[i] = l[-1-i]
		l[-1-i] = temp
	return l

def cust_reverse2(l):
	end = len(l) -1
	mid = (len(l) - 1) /2
	for i in range(mid):
		temp = l[i]
		l[i] = l[end-i]
		l[end-i] = temp
	return l

# print cust_reverse([9, 8, 7, 6, 5, 4, 3, 2, 1])

# print cust_reverse2([9, 8, 7, 6, 5, 4, 3, 2, 1])

# ==================================
# QUESTION 2: produce a list of unique (or non-unique) items in a list
# in this case, run-time is n^2

def unique(l):
	results = []
	for i in range(len(l)):
		if l[i] not in l[:i] and l[i] not in l[i+1:]:
			results.append(l[i])
	return results

# print unique([3, 4, 5, 6, 4, 7, 8, 3, 2])

# dictionary solution. 
# in thise case run-time is linear
# dictionary lookups are O(1).
def unique_dict(l):
	d = {}
	results = []
	for item in l:
		d[item] = d.get(item, 0) + 1
	for key in d:
		if d[key] == 1:
			results.append(key)
	return results

# print unique_dict([3, 4, 5, 6, 4, 7, 8, 3, 2])

# ==================================
# QUESTION 4: Shuffle a list in place.
def shuffle(l):
	for i in range(len(l)):
		r = random.randint(i, len(l)-1)
		temp = l[i]
		l[i] = l[r]
		l[r] = temp
# l = [0, 1, 2, 3, 4, 5, 6]
# shuffle(l)
# print l

# ==================================
# QUESTION 5: Compress and decompress string.

def compress(s):
	if not s:
		return None
	result = []
	count = 1
	current = s[0]
	for char in s[1:]:
		if current == char:
			count += 1
		else:
			result.append(current + str(count))
			count = 1
			current = char
	result.append(current + str(count))
	return "".join(result)

# s = 'aaaaaaaaaabcccaddddddddddd'
# compressed_s = compress(s)
# print compressed_s

def compress_lite(s):
	if not s:
		return None
	result = []
	count = 1
	current = s[0]
	for char in s[1:]:
		if current == char:
			count += 1
		else:
			result.append(current)
			if count > 1:
				result.append(str(count))
			count = 1
			current = char
	result.append(current)
	if count > 1:
		result.append(str(count))
	return "".join(result)


# r = 'aaaaaaaaaabcccaddddddddddd'
# cr = compress_lite(r)
# print cr


def decompress(s):
	if not s:
		return None

	result = []
	char = s[0]
	num = []

	for i in range(len(s)):
		current = s[i]

		if current.isalpha():
			if i > 0 and s[i - 1].isalpha():
				result.append(char)
			elif i > 0:
				result.append( char * int(''.join(num)))
			char = current
			num = []
		else:
			num.append(current)

	if num:
		result.append(char * int(''.join(num)))
	else:
		result.append(char)

	return "".join(result)

# print decompress(compressed_s)
# print s == decompress(compressed_s)

# print decompress(cr) == r

# ==================================
# QUESTION 6: How many numerical palindromes between 1 and 10,000?

def numerical_palindromes(start, end):
	count = 0
	for i in range(start, end + 1):
		if str(i) == str(i)[::-1]:
			count += 1
			print count, i
	return count

# print numerical_palindromes(1, 10000)

# ==================================
# QUESTION 7: How many chimes?
# A clock chimes every half hour and x times every x hour.
# The chime for the hour completes at the start of that hour.
# How many chimes are there between 2am and 8am the next day?

def chimes(start, hours_later):
	count = 0
	for i in range(hours_later):
		hour = start + 1 + i
		count += (hour % 12) + 1
	return count

# print chimes(2, 30)

# ==================================
# QUESTION 8:
# Algorithm that inputs a string and returns first duplicate character.

def get_first_duplicate(s):
	d = {}
	for char in s:
		d[char] = d.get(char, 0) + 1
		if d[char] > 1:
			return char

# print get_first_duplicate('abcdcefgg')

# ==================================
# QUESTION 9: Fizzbuzz!
# Write an algorithm that prints 'fizz' instead of multiples of 3, 'buzz' instead of multiples of 5, and 'fizzbuzz' instead of multiples of both 3 and 5.
def fizzbuzz(n):
	for i in range(1, n+1):
		result = []
		if not i % 3:
			result.append("fizz")
		if not i % 5:
			result.append("buzz")
		if result:
			print "".join(result)
		else:
			print i