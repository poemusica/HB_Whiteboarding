import random

# Coding interview questions from
# http://meetupresources.herokuapp.com/whiteboard.html
 
# ==================================
# QUESTION 1: Write a method that converts an integer to its Roman numeral equivalent, i.e., 476 => 'CDLXXVI'.

# arabic_to_roman = {
# 	1: 'I', 
# 	5: 'V', 
# 	10: 'X', 
# 	50: 'L', 
# 	100: 'C', 
# 	500: 'D', 
# 	1000: 'M'
# 	}

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
	# ones place
	# if n % 10 == 9:
	# 	numeral.append('IX')
	# elif (n / 5) % 2 and (n / 5 > 0):
	# 	numeral.append('V')
	# 	numeral.append('I' * (n % 5))
	# elif n % 5 == 4:
	# 	numeral.append('IV')
	# elif n % 10:
	# 	numeral.append( 'I' * (n % 10))

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

print eng_to_pig_latin('maple')
print eng_to_pig_latin('almond')

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
l = range(10)
print l
print shuffle(l)

# ==================================
# QUESTION 4: Anagrams
# An anagram is a word formed by rearranging the letters of another word, e.g., iceman is an anagram of cinema.
# We're going to write a method called anagrams_for that takes as its input a word and an array of words,
# representing a dictionary, and returns an array consisting of all the anagrams of the input word. 
# anagrams_for should return an empty array ([]) if no anagrams are found in the dictionary.
# You don't have to worry about the order of the returned Array.

