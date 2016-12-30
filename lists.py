# Find the last element of a list.

# a = [1, 4, 6, 2, 0, -3]
# print(a[-1])

# Find the second to last element of a list.

# a = [1, 4, 6, 2, 0, -3]
# print(a[-2])

# Find all elements from the third to last element of a list to the last one.

# a = [1, 4, 6, 2, 0, -3]
# print(a[-3:])

# Find the k'th element of a list

# k = 5
# a = [1, 4, 6, 2, 0, -3]
# print(a[k - 1])

# Find the number of elements of a list.

# a = [8, 1, 3, -3, 20, -36, 0]
# print(len(a))

# Reverse a list.

# a = [8, 1, 3, -3, 20, -36, 0]
# print(a[::-1])

# Find out whether a list is a palindrome.

# a = [9, 8, 6, 8, 9]
# print(a == a[::-1])

# Flatten a nested list structure.

# list1 = [[1, 2, 3], [[0,-3], 5, 6], [7], [8, 9]]

# def flatten(lst):
# 	result = []
# 	for l in lst:
# 		if(type(l) == list):
# 			result.extend(flatten(l))
# 		else:
# 			result.append(l)
# 	return result
# print(flatten(list1))

#  Eliminate !CONSECUTIVE! duplicates from the list.

# t = [1, 1, 2, 3, 3, -2, 1, 1, 1, 1, 2, 5, 6, 7, 8, -2]
#
# def conDedup(lst):
# 	result = []
# 	sample = lst[0]
# 	for i in lst:
# 		if(i != sample):
# 			result.append(i)
# 			sample = i
# 	return result
# print(conDedup(t))

# Duplicate the elements of a list.

# t = [1, 2, 3, -2, 22, 51, 6, 87, 8, -2]
# a = []
# for i in t:
#     a.extend([i,i])
# print(a)

# Insert an element at a given position into a list.
#
# pos = 3
# el = 8
# l1 = [1, 2, 3, -2, 22, 51]
#
# def ins_in_pos(list, el, pos):
#     result = list[:(pos - 1)]
#     result.append(el)
#     result.extend(list[pos - 1:])
#     print(result)
#
# ins_in_pos(l1, el, pos)

# Create a list containing all integers within a given range.

# start = 5
# end = 32
# print(list(range(start, end)))

# ---------------------------------------------------------------
# filter the list of inventors for those who lived during 1500's
inventors = [
	{'first': 'Albert', 'last': 'Einstein', 'year': 1879, 'passed': 1955},
	{'first': 'Isaac', 'last': 'Newton', 'year': 1643, 'passed': 1727},
	{'first': 'Galileo', 'last': 'Galilei', 'year': 1564, 'passed': 1642},
	{'first': 'Marie', 'last': 'Curie', 'year': 1867, 'passed': 1934},
	{'first': 'Johannes', 'last': 'Kepler', 'year': 1571, 'passed': 1630},
	{'first': 'Nicolaus', 'last': 'Copernicus', 'year': 1473, 'passed': 1543},
];

# def func(item):
# 	if(item['year'] >= 1500 and item['year'] <= 1600):
# 		return True

# result = filter(func, inventors)
# print(list(result))

# Get an array of inventors first and last names

# def func(item):
# 	return item['first'] + ' ' + item['last']

# result = map(func, inventors)
# print(list(result))

# Sort the inventors by birthdate oldest to youngest

# def byAge(inventor):
# 	return inventor['year']

# sorted1 = sorted(inventors, key=byAge)
# print(sorted1)

# How many years did all the inventors live?

# from functools import reduce
# def func(tmp, cur):
# 	return tmp + (cur['passed'] - cur['year'])

# totalYears = reduce(func, inventors, 0)
# print(totalYears)

# Sort the inventors by years lived  -  NOT SOLVED!!!!!!!!!!!!!!!!!!!!!
# def byAge(a, b):
# 	last = a['passed'] - a['year']
# 	next = b['passed'] - b['year']
# 	return -1 if last > next else 1
# oldest = sorted(inventors, key=byAge)
# print(oldest)