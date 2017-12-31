def longestValidParentheses(s):
	s = ")"+s
	stack, ans = [], 0
	for index in xrange(len(s)):
		element = s[index]
		if element == ")" and stack and stack[-1][1] == "(":
			stack.pop()
			ans = max(ans, index-stack[-1][0])
		else:
			stack.append((index, element))
	return ans
