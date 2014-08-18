import random

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

# QUESTION 3: write fibonocci with O(n) time and O(1) space
def fib(n):
	prev = 1
	prev_prev = 0
	current = 1
	for i in range(n):
		current = prev + prev_prev
		prev_prev = prev
		prev = current
	return current

# for i in range(5):
# 	print i, fib(i)


# QUESTION 4: Shuffle a list in place.
def shuffle(l):
	for i in range(len(l)):
		r = random.randint(i, len(l)-1)
		temp = l[i]
		l[i] = l[r]
		l[r] = temp
l = [0, 1, 2, 3, 4, 5, 6]
shuffle(l)
print l
