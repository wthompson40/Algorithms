import random

a = [random.randint(0, 100) for x in range(0, 1000)]


def quicksort(a):
	less = []
	equal = []
	greater = []
	if len(a) > 1:
		pivot = a[random.randint(0, len(a)-1)]
		for x in a:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		return quicksort(less) + equal + quicksort(greater)
	return a

def test():
	results = []
	for x in range(0, 100):

		a = [random.randint(0, 1000) for x in range(0, 950)]
		results.append(sorted(a) == quicksort(a))
	print results
	return results

test()