def selectionSort(alist):
	for element in range(len(alist)-1):
	   minimum = element
	   for index in range(element+1,len(alist)):
	   	if alist[index] < alist[minimum]:
	   		minimum = index

	   alist[element], alist[minimum] = alist[minimum], alist[element] 

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

