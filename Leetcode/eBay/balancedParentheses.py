#Determine whether a list of parentheses "[()]{}"
import time

def f(my_string):
    x = time.time()
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
            #print(my_string)
    print(time.time()-x)
    return not my_string
    
    
my_string = "[(){()[]}]"
print(f(my_string))


def parentheses(my_string):
  y = time.time()
  brackets = ['()','[]', '{}']
  for x in brackets:
    if x in my_string:
      for br in brackets:
        my_string = my_string.replace(br, '')
        #print(my_string)
  print(time.time()-y)
  return not my_string
  

print(parentheses(my_string))
