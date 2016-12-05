#range(10)[::1]def palindrome(a):
import time
#start_time = time.time()



def palindrome(a):
     a=raw_input('Enter :')
     start_time = time.time()
     a=a.lower()
     b=a[::-1]
     if a==b:
       return True #and (start_time-time.time())
     else:
       return False #and (start_time-time.time())
       
       
print palindrome(0)

#print("--- %s seconds ---" % (time.time() - start_time))