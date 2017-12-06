#reverseVowels

def reverseVowels(s):
	vowel = 'aeiouAEIOU'
	s = list(s)
	i, j = 0, len(s)-1
	while i<j:
		while s[i] not in vowel and i<j:
			i += 1
		while s[j] not in vowel and i<j:
			j -= 1
		s[i], s[j]= s[j], s[i]
		i, j = i+1, j-1
	return ''.join(s)


s = 'Hello'

print(reverseVowels(s))


import re

def reverseVowels1(s):
	vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
	return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)    #(?i)regex" matches regex case insensitively.

print(reverseVowels1(s))
