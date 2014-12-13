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

def rev_in_place(l):
	i = 0
	while i < len(l)/2:
		temp = l[i]
		l[i] = l[len(l) - 1 - i]
		l[len(l) - 1 - i] = temp
		i += 1

# TESTS
# l1 = range(4)
# l2 = range(5)

# print l1
# rev_in_place(l1)
# print l1

# print l2
# rev_in_place(l2)
# print l2

def rev_copy(l):
	result = []
	for i in range(len(l)):
		result.append(l[len(l) - 1 - i])
	return result

# TESTS
# l1 = range(4)
# l2 = range(5)

# l1r = rev_copy(l1)
# print l1
# print l1r

# l2r = rev_copy(l2)
# print l2
# print l2r


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

# ==================================
# QUESTION 10: Peasant Multiplication

def peasant_mult(x, y):
	result = 0
	sign = 1

	if x < 0:
		sign = -sign
		x *= -1

	if y < 0:
		sign = -sign
		y *= -1

	while True:
		if x % 2:
			result += y 
		x = x / 2
		if x == 0:
			break
		y *= 2

	return result * sign

# print peasant_mult(54, 96)
# print peasant_mult(96, 54)
# print peasant_mult(-54, -96)
# print peasant_mult(-54, 96)

# ==================================
# QUESTION 11: Convert a string to an integer
# consider decimals and negative numbers

def string_to_num_parse(s):
	if s == "":
		return None
	
	result = 0
	start = 0
	sign = 1

	parsed_s = s.split(".")
	left = parsed_s[0]
	
	if len(parsed_s) > 1:
		right = parsed_s[1]
	else:
		right = ""

	if left and left[0] == "-":
		sign = -1
		start = 1

	if left[start:].isdigit():
		result += int(left[start:])

	if right.isdigit():
		result += int(right) / (10.0 ** len(right))

	return result * sign

s_to_n = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

def string_to_num(s):
	if s == "":
		return None

	result = 0

	parsed_s = s.split(".")
	left = parsed_s[0]
	if len(parsed_s) > 1:
		right = parsed_s[1]
	else:
		right = ""

	sign = 1
	start = 0
	if left and left[0] == "-":
		sign = -1
		start = 1

	for i in range(start, len(left)):
		place = 10 ** (len(left) - 1 - i)
		result += s_to_n[left[i]] * place

	for i in range(len(right)):
		place = 10.0 ** (i + 1)
		result += s_to_n[right[i]] / place

	return result * sign



# TESTS
# print string_to_num('58343')
# print type(string_to_num('58343'))
# print string_to_num('-58343')
# print type(string_to_num('-58343'))
# print string_to_num('-500')
# print type(string_to_num('-500'))

# print string_to_num('0.01')
# print type(string_to_num('0.01'))
# print string_to_num('1.01')
# print type(string_to_num('1.01'))
# print string_to_num('0.01')
# print type(string_to_num('0.01'))
# print string_to_num('-.1')
# print type(string_to_num('-.1'))
# print string_to_num('-1.01')
# print type(string_to_num('-1.01'))


# ==================================
# QUESTION 12: 
"""
Find a path from S to E!
S = start
E = end
# = wall
* = path

Note: right-hand-rule won't work because of free-standing walls.
"""
maze = ["########",
        "#      E",
        "# # ####",
        "# #   ##",
        "# # ####",
        "#      S",
        "########"]
 
# example solution
solution = ["########",
            "#  ****E",
            "# #*####",
            "# #*  ##",
            "# #*####",
            "#  ****S",
            "########"]

def find_start_end(maze):
	start = None
	end = None
	for y in range(len(maze)):
		for x in range(len(maze[y])):
			if maze[y][x] == "S":
				start = (x, y)
			if maze[y][x] == "E":
				end = (x, y)
	return start, end

def is_outside_or_wall(maze, pos):
	if pos[0] > len(maze[0]) - 1:
		return True
	if pos[0] < 0:
		return True
	if pos[1] > len(maze) - 1:
		return True
	if pos[1] < 0:
		return True
	if maze[pos[1]][pos[0]] == '#':
	 	return True
	return False 

def find_path(maze, start=None, end=None, visited=None, path=None):
	if not (start and end and visited):
		start, end = find_start_end(maze)
		visited = {}
		path = []
		path.append(start)

	current = start

	if is_outside_or_wall(maze, current):
		return False
	if visited.get(current, False):
		return False
	else:
		visited[current] = True
	if current == end:
		return path

	north = (current[0], current[1] + 1)
	south = (current[0], current[1] - 1)
	east = (current[0] + 1, current[1])
	west =  (current[0] - 1, current[1]) 

	if find_path(maze, north, end, visited, path) != False:
			path.append(north)
			return path
	if find_path(maze, south, end, visited, path) != False:
			path.append(south)
			return path
	if find_path(maze, east, end, visited, path) != False:
			path.append(east)
			return path
	if find_path(maze, west, end, visited, path) != False:
			path.append(west)
			return path
	return False

def print_path(maze):
	path = find_path(maze)
	print path
	if path:
		path = sorted(path, key=lambda p : p[0], reverse=True)
		path = sorted(path, key=lambda p : p[1], reverse=True)
		step = path.pop()
	else:
		step = None
	for y in range(len(maze)):
		for x in range(len(maze[y])):
			if (x, y) == step:
				print '*',
				if path:
					step = path.pop()
			else:
				print maze[y][x],
		print '\n',	

# TEST
# print_path(maze)


# ==================================
# QUESTION 13: Replace all curse words in a string with asterisks. 

bad_words = ['eff', 'effing', 'effer', 'effed', 'shizz']

punctuation = ['.', ',', ';', ':', '!', '\'', ' ', '\n']

text = "That effing effer did some really effed up shizz! I can't believe that effer."

def replace_curses(text):
	result = []
	charlist = ['']
	for char in text:
		if char in punctuation:
			word = ''.join(charlist)
			if word in bad_words:
				word = '*' * len(word)
			result.append(word)
			result.append(char)
			charlist = ['']
		else:
			charlist.append(char)
	return ''.join(result)

# TEST
# print text
# print replace_curses(text)

# ==================================
# QUESTION 14: Write a function that determines whether a number is prime.

def is_prime(n):
	if n > 0 and n < 3:
		return True
	
	f1 = 2
	f2 = n / 2
	product = f1 * f2
	mid = ((n / 2) / 2) - 1
	while f2 >= mid and f1 <= mid:
		if product == n:
			return False
		if product < n:
			f1 += 1
			product = f1 * f2
		if product > n:
			f2 -= 1
			product = f1 * f2
	return True

# print is_prime(33)
# print is_prime(36)

# ==================================
# QUESTION 15: Write a function that finds the index in a list where 
# the sum of the elements to its right equal the sum of the elements
# to its left.

def find_sum_pivot(l):
	pivot = len(l)/2
	rsum = sum(l[:pivot])
	lsum = sum(l[pivot + 1:])

	while True:
		if pivot >= len(l) - 2 or pivot < 1:
			break
		if rsum == lsum:
			return pivot
		if rsum > lsum:
			rsum -= l[pivot - 1]
			lsum += l[pivot]
			pivot -= 1
		if lsum > rsum:
			lsum -= l[pivot + 1]
			rsum += l[pivot]
			pivot += 1

def find_sum_pivot2(l):
	rsum = l[0]
	lsum = sum(l[2:])

	for i in range(1, len(l)-1):
		if rsum == lsum:
			return i
		if lsum > rsum:
			lsum -= l[i + 1]
			rsum += l[i]

# TESTS
# l = [1, 2, 3, 4, 6, 5, 5]
# print find_sum_pivot(l)

# ==================================
# QUESTION 16: Find a  word in a boggle board. 
