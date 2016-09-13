import random


def mergeSort(a):
	if len(a) == 1: return a
	left, right = partition(a)
	mleft = mergeSort(left)
	mright = mergeSort(right)
	new = merge(mleft, mright)
	return new

def partition(a):
	return a[:len(a)/2], a[len(a)/2:]

def merge(a, b):
	i = 0
	j = 0
	k = 0
	a_b = []
	while (i < len(a) and j < len(b)):
		if a[i] <= b[j]:
			a_b.append(a[i])
			i += 1
			k += 1
		else:
			a_b.append(b[j])
			j += 1
			k += 1
	while(j < len(b)):
		a_b.append(b[j])
		j += 1
	while(i < len(a)):
		a_b.append(a[i])
		i += 1
		k += 1
	return a_b


