

initHash = {"Mo":[1,2], "Tu":[5,6], "We":[2,3], "Th":[7,8], "Fr":[1,2], "Sa":[8,9] ,"Su":[13,14]}
#initHash = {1:[01,02], 2:[05,06], 3:[02,03], 4:[07,08], 5:[11,12], 6:[08,09] ,7:[13,14]}

newdict = {}
newlist = []
newlist2 =[]
def newHash(initHash):
	for key, val in initHash.items():
		if val not in newdict.values():
			newdict[key]=val
	for key, val in newdict.items():
		newlist.append(val)
	#print(newlist)    #[[1, 2], [5, 6], [2, 3], [7, 8], [8, 9], [13, 14]]
	m = [y[0] for y in newlist]   #[1, 5, 2, 7, 8, 13]
	#print(m)
	for key, val in newdict.items():
		#x = val[-1]    #[2,6,3,8,9,14]
		if val[-1] in m:
			for i in newlist:
				if val[-1] == i[1]:
					newlist2.append(i)
	#print(newdict)   #{'Mo': [1, 2], 'Tu': [5, 6], 'We': [2, 3], 'Th': [7, 8], 'Sa': [8, 9], 'Su': [13, 14]}
	return(newlist2)   #[[1, 2], [7, 8]]
