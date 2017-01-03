'''
def Func(*args):
    for arg in args:
        print arg
l = [1,2,3,54, "ham"]
Func(*l)
'''

def Func(*args, **kwargs):
    for arg in args:
        print arg
    for item in kwargs.items():
        print item

Func(12, x = 456, y = 3)
