def bubblesort(mylist):
    for iternum in range(len(mylist)-1, 0, -1):
        for idx in range(iternum):
            if mylist[idx] > mylist[idx+1]:
                mylist[idx], mylist[idx+1] = mylist[idx+1], mylist[idx]
    return mylist

mylist = [40, 23, 7, 49, 32, 98, 76, 48, 87]

print(bubblesort(mylist))
