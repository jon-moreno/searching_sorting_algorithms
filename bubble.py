l = [54,26,93,17,77,31,44,55,20]

def bubbleSort(alist):
	for a in range(len(alist)):
		for b in range(len(alist)-1):
			if alist[b]>alist[a]:
				
				alist[a], alist[b] = alist[b], alist[a]

	print(alist)

bubbleSort(l)

def swap():
	a,b =1,2
	temp = a
	a = b
	b = temp
	print(a,b)
swap()

def swap_two():
	a,b = 1,2
	a,b = b,a
	print(a,b)
swap_two()












