import random
from time import time
import sys
sys.setrecursionlimit(100000) # 10000 is an example, try with different values

a = []
for i in range(700):
	a.append(random.randint(0,2*i))
b = a
c = a

random.shuffle(a)

old = a
# Sort that shiz yo!

def compareAndSwap(LIST):
	# print LIST
	# print 'Swappin!'
	pimpin = True
	pumpin = True
	uno = False
	# dos = False
	squeeze = 0
	index = 0
	end = len(LIST)
	fluxitup = True
	while(pimpin):
		# print 'Working', index
		# print 'Squeeze', squeeze
		# print LIST
		pumpin = True
		val = LIST[index]
		pivot = index
		while pumpin:
			if fluxitup:
				index += 1
				if val > LIST[index]:
					# print 'Swapping', pivot, 'and', index
					pimpin = True
					uno = False
					LIST[pivot] = LIST[index]
					LIST[index] = val
					pivot = index
					# print LIST
				else:
					pumpin = False
				if index >= end - (squeeze + 1):
					if uno:
						pimpin = False
					else:
						uno = True
					fluxitup = False
			else:
				index -= 1
				if val < LIST[index]:
					# print 'Swapping', pivot, 'and', index
					pimpin = True
					uno = False
					LIST[pivot] = LIST[index]
					LIST[index] = val
					pivot = index
					# print LIST
				else:
					pumpin = False
				if index <= 0 + squeeze:
					if uno:
						pimpin = False
					else:
						uno = True
					pumpin = False
					fluxitup = True
					squeeze += 1
	# squeeze += 1
	# index = squeeze
	# fluxitup = True
	# if pimpin == False:
	# 	print 'Squeeze =', squeeze
	# 	# squeeze += 1
	# 	if dos == False:
	# 		dos = True
	# 		pimpin = True
	# else:
	# 	if dos == True:
	# 		dos = False

def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

def MERGE(A,start,mid,end):
    L = A[start:mid]
    R = A[mid:end]
    i = 0
    j = 0
    k = start
    for l in range(k,end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1  

def mergeSort(A,p,r):
    if r - p > 1:
        mid = int((p+r)/2)
        mergeSort(A,p,mid)
        mergeSort(A,mid,r)
        MERGE(A,p,mid,r)

starta = time()
compareAndSwap(a)
print a
print time() - starta, 'seconds'

# startb = time()
# print qsort1(b)
# print time() - startb, 'seconds'

startb = time()
mergeSort(b,0,len(b))
print b
print time() - startb, 'seconds'

if a == b:
	print 'Clean!'