def binary(alist, item):
	start = 0
	end = len(alist) - 1
	found = False

	while  start <= end and not found:
		midpoint = (start + end) //2

		if alist[midpoint] == item:
			print(alist[midpoint])
			found = True

		else:
			if item < alist[midpoint]:
				end = midpoint - 1

			else:
				start = midpoint + 1
	return found


alist = [1,2,3,4,5,6,7]
print(binary(alist, 3))