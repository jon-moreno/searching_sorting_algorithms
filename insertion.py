def insertionSort(alist):
   for index in range(1,len(alist)):
     element = alist[index]

     while index > 0 and alist[index-1] > element:
         alist[index] = alist[index-1]
         index = index - 1

     alist[index] = element

alist = [88,33,22,1,2,4,77,99]
insertionSort(alist)
print(alist)