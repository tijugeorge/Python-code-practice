
def paintFence(n , k):   #n is no of fences and k is no of colors
	if n==0:
		return 0
	if n==1:
		return k
	same, diff = k, k*(k-1)
	for i in range(3, n+1):
		same, diff = diff, (same + diff)*(k-1)
	return same+diff



print(paintFence(2,3))
