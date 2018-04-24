import copy
def fibHelper(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	return fibHelper(x-1) + fibHelper(x-2)
def fib(x):
	return fibHelper(x)
def reverseStringHelper(s, reversedString):
	if len(s) >= 1:
		rs = s[0] + reversedString
		string = s[1:]
	else:
		return reversedString
	return reverseStringHelper(string, rs)
def reverseString(string):
	return reverseStringHelper(string, "")
def isSortedHelper(lst, sortedLst):
	if len(lst) >= 1:
		minimum = min(lst)
		sortedLst.append(minimum)
		lst.remove(minimum)
	else:
		return sortedLst
	return isSortedHelper(lst, sortedLst)
def isSorted(lst):
	origLst = copy.copy(lst)
	if origLst == isSortedHelper(lst, []):
		return True
	return False
def countOccHelper(lst, item, timesOccurred):
	if len(lst) >= 1:
		if lst[0] == item:
			timesOccurred += 1
		lst = lst[1:]
	else:
		return timesOccurred
	return countOccHelper(lst, item, timesOccurred)
def countOcc(lst, item):
	return countOccHelper(lst, item, 0)
def main():
	print(reverseString("hello")) #should be "olleh"
	print(isSorted([3, 5, 2])) #should be False
	print(isSorted([3, 4, 9])) #shoudl be True
	print(countOcc([4, 5, 6, 7, 8, 8, 2], 8)) #should be 2
	for i in range(10):
		print(fib(i)) #should come out as 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
	#You can run more tests if you want
main()
