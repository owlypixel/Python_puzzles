# Find the last element of a list.

# a = [1, 4, 6, 2, 0, -3]
# print(a[-1])

# Find the secont to last element of a list.

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

t = [1, 1, 2, 3, 3, -2, 1, 1, 1, 1, 2, 5, 6, 7, 8, -2]

def conDedup(lst):
	result = []
	sample = lst[0]
	for i in lst:
		if(i != sample):
			result.append(i)
			sample = i
	return result
print(conDedup(t))