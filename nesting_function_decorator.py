'''
def addOne(myFunc):
    def addOneInside():
        return myFunc() + 1
    return addOneInside

def oldFunc():
    return 3

#newFunc = addOne(oldFunc)
#print oldFunc(), newFunc()

#replace ne with old function as shown below

oldFunc = addOne(oldFunc)#instead of this use@decorator
print oldFunc()


#this entire thing can be achieved using decorator as shown below
'''
def addOne(myFunc):
    def addOneInside(*args, **kwargs):#addedd *args, **kwargs
        return myFunc(*args, **kwargs) + 1 #*args, **kwargs
    return addOneInside

@addOne
def oldFunc(x = 45677):
    return x

print oldFunc(565757)
