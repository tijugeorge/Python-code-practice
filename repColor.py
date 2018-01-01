#return the color/s maximum happen within the 2D array of colors. Forexample, input: [['red', 'red', 'green'], 
#['yellow', 'blue']] output: ['red'] : in the array form
import collections

def repColor(arr):
	dict = {}
	max_j = -1
	max_i = len(arr)
	max_value = -1
	result = []
	for i in range(len(arr)):
		j = len(arr[i])
		if j > max_j:
			max_j = j
	#print( max_i, max_j)
	

	for i in range(max_i):
		for j in range(max_j):
			try:
				if arr[i][j] in dict:
					dict[arr[i][j]] += 1
				else:
					dict[arr[i][j]] = 1
			except IndexError:
				pass
	
	print(dict)
	dict = collections.Counter(dict)
	result.append(dict.most_common(1)[0][0])
	return result

	#return dict 

	

arr = [['red', 'red', 'green'],
		['yellow', 'blue'],
		['red', 'red', 'green']]

print(repColor(arr))
