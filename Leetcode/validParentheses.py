def isValid(string):
	stack = []
	dict ={"]":"[","}":"{",")":"("}
	for char in string:
		if char in dict.values():
			stack.append(char)
		elif char in dict.keys():
			if stack == [] or dict[char] != stack.pop():
				return False
		else:
			return False
	return stack == []



s = "()"

print(isValid(s))
