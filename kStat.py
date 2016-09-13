#Find k-th smallest element in array: one way is to find sorted array and check a[k].
import quicksort
import random

#k-th stat definition - k > 0, so we look for k-th smallest element in array: 1<= k <= n in array A

def trueK(a, k):
	return quicksort.quicksort(a)[k-1]

#O(n) algorithm to find k-th smallest element in array
def constant_time_kth(a, k):
	if len(a) == 1:
		return a[0]
	if len(a) > 1:
		less = []
		equal = []
		greater = []
		pivot = a[random.randint(0, len(a) - 1)]
		for x in a:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		if k > len(less) and k <= len(less) + len(equal): return pivot
		if k <= len(less): return constant_time_kth(less, k)
		if k > len(less) + len(equal): return constant_time_kth(greater, (k) - (len(less) + len(equal)))
	

def test():
	results = []
	for x in range(0, 100):

		a = [random.randint(0, 1000) for y in range(0, 950)]
		k = random.randint(0, 950)
		results.append(trueK(a, k) == constant_time_kth(a, k))
	print results
	return results

test()