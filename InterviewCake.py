import random
## InterviewCake.com practice problems ##

## As you are writing your answers, think about space and time complexity. 
# If possible, try to get your answers down to constant space and O(n) time.

## Strategies
# Greedy: Do everything in one pass by keeping track and updating as you go.
# Brute Force: Enumerate all possible solutions and check for correctness.
# Hashing: Use a dictionary. (This will cost space.)
# Memoization (Top-down): Keep track using a class or global variable. (This will cost space.)
# Dynamic (Bottom-up): Determine what you will calculate based on what you already have calculated.
#                      Start at the 'leaves' or terminal calculations. 


## QUESTION 1:
# Write a function that takes a list of numbers and returns the largest difference between any two numbers in the list.

## SOLUTION 1.1: Greedy. O(n) time. O(1) space.
def max_diff(l):
	if not l:
		return None 
	max_l = l[0]
	min_l = l[0]
	for num in l:
		if num > max_l:
			max_l = num
		if num < min_l:
			min_l = num
	return max_l - min_l

l0 = []
l1 = [4, 5, 2, 9, 22, 3, 2, 4, 1]
# print max_diff(l0)
# print max_diff(l1)

# SOLUTION 1.2: Brute Force. O(n^2) time. O(1) space.
def max_diff2(l):
	diff = 0
	for n in l:
		for m in l:
			if abs(n-m) > diff:
				diff = abs(m-n)
	return diff

## QUESTION 2: 
# Write a function that takes a list of numbers 1-1000 (with no repeats) and returns the single missing number.

# SOLUTION 2.1: Greedy. O(n) time. O(1) space.
def missing_num(l):
	list_sum = 0
	full_sum = 0
	for num in l:
		list_sum += num
	for i in range(1, len(l) + 2):
		full_sum += i
	return full_sum - list_sum

l2 = range(1, 1001)
random.shuffle(l2)
# print l2.pop(random.randint(1, 1000))
# print missing_num(l2)

# SOLUTION 2.2: Greedy, but O(n) time and O(n) space.
def missing_num2(l):
	full_list = range(1, len(l)+2)
	for num in l:
		full_list.remove(num)
	return full_list[0]

# print l2.pop(random.randint(1, 1000))
# print missing_num2(l2)

## QUESTION 3:
# Write a function that creates all possible pairs from a list without including mirror pairs.

# SOLUTION 3.1: Greedy, but can't be better than O(n^2)
def make_pairs(l):
	pairs = []
	for countdown in range(len(l) -1, -1, -1):
		for n in l[0:countdown]:
			pairs.append((n, l[countdown]))
	return pairs

l3 = range(1, 5)
# print l3
# print make_pairs(l3)


## QUESTION 4: 
# Write a function that takes an index and returns the fibonacci sequence at that index.

# SOLUTION 4.1: Bottom-up. O(n) time. O(1) space. 
def fib(n):
	prev = 1
	prev_prev = 0
	result = 0
	for num in range(n):
		result = prev + prev_prev
		prev_prev = prev
		prev = result
	return result

# print fib(1)

# SOLUTION 4.2: Memoization. O(n) time, but also O(n) space for the hashmap/dictionary.
class Fib:
	memo = {}
	def fib(self, n):
		if self.memo.get(n):
			return self.memo[n]
		if n < 2:
			self.memo[n] = 1
			return self.memo[n]
		self.memo[n] = self.fib(n-1) + self.fib(n-2)
		print self.memo
		return self.memo[n]

f = Fib()
# print f.fib(6)

# SOLUTION 4.3: Recursive. O(2^n) time. n determines the max depth of the stack frames needed. 
# Every call becomes 2 calls. Every call doubles the time.
# O(n) space. Stack frame on left side resolves before right side expands.
def fib3(n):
	if n < 2:
		return 1
	return fib3(n-1) + fib3(n-2)

# print fib3(5)

## QUESTION 5:
# Given a list of stock prices where the index indicates the relative time of sampling, 
# write a function that returns the possible maximum profit. Note: You must buy before you sell.

# SOLUTION 5.1: Greedy. O(n) time. O(1) space.
def max_profit(prices):
	buy_price = prices[0]
	current_best = prices[1] - buy_price
	for price in prices:
		profit = price - buy_price
		if profit > current_best:
			current_best = profit
		if price < buy_price:
			buy_price = price
	return current_best

# SOLUTION 5.2: Brute Force. O(n^2) time. O(1) space.
def max_profit2(prices):
	max_p = prices[1] - prices[0]
	for i in range(len(prices)):
		price1 = prices[i]
		for price2 in prices[i+1:]:
			profit = price2 - price1
			if profit > max_p:
				max_p = profit
	return max_p

l5 = [500, 455, 502, 300, 301, 499]
print max_profit(l5)



