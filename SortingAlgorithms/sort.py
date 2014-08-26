import random

# Sorting Algorithms

# ========================
# 0. SHUFFLE IN PLACE
def shuffle(l):
	result = l[:]
	for i in range(len(result)):
		rand_i = random.randint(i, len(result)-1)
		temp = result[i]
		result[i] = result[rand_i]
		result[rand_i] = temp
	return result

# ========================
# 1. BUBBLE SORT
# in place
# O(nlogn) 
def bubble(l):
	for countdown in range(len(l)-1, -1, -1):
		for i in range(countdown):
			if l[i] > l[i+1]:
				temp = l[i]
				l[i] = l[i+1]
				l[i+1] = temp

# TEST
# l = shuffle(range(1, 10))
# print l
# bubble(l)
# print l

# ========================
# 2. MERGE SORT
# not in place
# recursive solution
def merge_sort(l):
	if len(l) == 1:
		return l
	middle = (len(l))/2
	left = l[:middle]
	right = l[middle:]
	left = merge_sort(left)
	right = merge_sort(right)

	result = []
	while left and right:
		if left[0] > right[0]:
			result += [right[0]]
			right.pop(0)
		else:
			result += [left[0]]
			left.pop(0)
	if left:
		result += left
	if right:
		result += right
	return result

# TEST
# l = shuffle(range(1, 11))
# print l
# print merge_sort(l)


# ========================
# 3. QUICK SORT
# recursive solution
# not in place
def quick_copy(l):
	r = l[:]
	if len(r) < 2:
		return r
	pivot = r[0]
	pivot_loc = 0
	for i in range(1, len(r)):
		if r[i] < pivot:
			pivot_loc += 1
			temp = r[i]
			r[i] = r[pivot_loc]
			r[pivot_loc] = temp
	temp = r[0]
	r[0] = r[pivot_loc]
	r[pivot_loc] = temp

	left = quick(r[:pivot_loc])
	right = quick(r[pivot_loc + 1:])

	return left + [pivot] + right

# TEST
# l = shuffle(range(1, 11))
# print l
# print quick_copy(l)
# print l


# recursive solution
# in place
def quick(l, start=0, end=None):
	if end is None:
		end = len(l)
	if end - start < 2:
		return
	pivot = l[start]
	pivot_loc = start

	for i in range(start + 1, end):
		if l[i] < pivot:
			pivot_loc += 1
			temp = l[i]
			l[i] = l[pivot_loc]
			l[pivot_loc] = temp
	temp = l[start]
	l[start] = l[pivot_loc]
	l[pivot_loc] = temp
	
	quick(l, start, pivot_loc) # left
	quick(l, pivot_loc + 1, end) # right

# TEST
# l = shuffle(range(1, 11))
# print l
# quick(l)
# print l
