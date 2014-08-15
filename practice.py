# reverse a list in place

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

# produce a list of unique (or non-unique) items in a list
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

print unique_dict([3, 4, 5, 6, 4, 7, 8, 3, 2])
