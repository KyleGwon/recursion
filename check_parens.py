def isBalancedHelper(s, unclosedParens):
	if unclosedParens < 0:
		return False
	elif len(s) <= 0:
		if unclosedParens == 0:
			return True
		return False
	else:
		if s[0] == "(":
			unclosedParens += 1
		elif s[0] == ")":
			unclosedParens -= 1
	string = s[1:]
	return isBalancedHelper(string, unclosedParens)
def isBalanced(s):
	return isBalancedHelper(s, 0)
def fileChecker(fileName, fileLines, origLines, issues, lineNum):
	if len(fileLines) <= 0:
		if issues == 0:
			print("File %s has no unbalanced parentheses" % (fileName))
		return
	elif not isBalanced(fileLines[0]):
		print("Unbalanced parentheses on line %d of %s\n%s" % (lineNum+1, fileName, origLines[lineNum]))
		issues += 1
	lineNum += 1
	lines = fileLines[1:]
	fileChecker(fileName, lines, origLines, issues, lineNum)
def invalidFile(fileName):
	try:
		file = open(fileName, "r")
	except:
		return True
	return False
def main():
	fileName = input("Enter file name: ")
	while invalidFile(fileName):
		fileName = input("Error: file not found; enter file name: ")
	file = open(fileName, "r")
	lines = file.readlines()
	# print(isBalanced("print(hello))("))
	# print(isBalanced("print(hello)()"))
	# print(isBalanced("print('(')\n"))
	fileChecker(fileName, lines, lines, 0, 0)
main()
