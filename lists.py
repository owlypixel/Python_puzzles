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

boulevards = ["Boulevard de l'Amiral-Bruix", "Boulevard Strasbourg", "Boulevard des Capucines", "Boulevard la Chapelle", "Boulevard de Clichy", "Boulevard de lital", "Boulevard des Italiens", "Boulevard la Madeleine", "Boulevard de Magenta", "Boulevard Rochechouart", "Boulevard Sbastopol", "Boulevard la Zone"]

guitarists = ['Jason, Becker', 'Marty, Friedman', 'Paul, Gilbert', 'Chick, Corea', 'Aldi, Meola', 'John, McLauglin', 'Chris, Impelliterri', 'Yngwie, Malmsteen', 'Randy, Rhoads', 'David, Micic', 'Paul, Wardingham']

guitars = ['Ibanez', 'Fender', 'Suhr', 'Mayones', 'Suhr', 'Rickenbecker', 'Caparison', 'Laguna', 'Fender', 'Suhr', 'Ibanez'];

comments = [
	{'text': 'Love this!', 'id': 523423},
	{'text': 'Super good', 'id': 823423},
	{'text': 'You are the best', 'id': 2039842},
	{'text': 'Nice Nice Nice!', 'id': 542328}
];

people = [
	{'name': 'Wes', 'year': 1988},
	{'name': 'Kait', 'year': 1986},
	{'name': 'Irv', 'year': 1970},
	{'name': 'Lux', 'year': 2015}
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

# Sort the inventors by years lived 
# def byAge(a):
# 	return a['passed'] - a['year']
# oldest = sorted(inventors, key=byAge)
# print(oldest)

# from a list of boulevards select those that contain 'de' anywhere in the name

# variant 1
# def func(a):
# 	return 'de' in a
# de = filter(func, boulevards)
# print(list(de))

# variant 2 - using lambda function
# de = filter(lambda x: 'de' in x, boulevards)
# print(list(de))

# variant 3 - using list comprehension
# de = [k for k in boulevards if 'de' in k]
# print(list(de))

# sort guitarists alphabetically by last name  -  NOT SOLVED!!!!!!!!!!!!!!!!!!!!!
# def byLastName():

# sorted1 = sorted(guitarists, key=byLastName)

# sum up the instances of each guitar model

# from functools import reduce
# def func(tmp, cur):
# 	if(not cur in tmp.keys()):
# 		tmp[cur] = 0
# 	tmp[cur] += 1
# 	return tmp
# result = reduce(func, guitars, {})
# print(result)

# s at least one person 19?
# import datetime
# now = datetime.datetime.now()
# isAdult = any(now.year - x['year'] >= 19 for x in people)
# print(isAdult);

# is everyone 19?
# import datetime
# now = datetime.datetime.now()
# allAdults = all(now.year - x['year'] >= 19 for x in people)
# print(allAdults)

# find the comment with the id 823423
# comment = filter(lambda comment: comment['id'] == 823423, comments)
# print(list(comment))

# find the comment with the id 823423 and delete it 
# comments = [c for c in comments if c['id'] != 823423]
# print(comments)