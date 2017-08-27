import copy
#recursive way to sum up the first n numbers in list

S = [1,3,4,6,7,9,4,5,6,7]



def linear_sum(T,n):
  if n == 0:
    return 0
  else:
    return linear_sum(T, n-1)+T[n-1]



m = (int(input("Please enter the number ")))
if 0 < m < len(S):
  print("The sum is :",linear_sum(S, m))
else:
  print("Number n is out of range")
  
  
#recursive way to reverse a list

def reverse(S, start, stop):
  if start < stop-1:
    S[start], S[stop-1] = S[stop-1], S[start]
    reverse(S, start+1, stop-1)
  return S
  
print(reverse(S, 0, len(S)))

#power function

def power(x, n):
  if n==0:
    return 1
  else:
    return x*power(x, n-1)
    
print(power(2,18))

#another way of power
def power2(x,n):
  if n == 0:
    return 1
  else:
    partial = power2(x, n//2)
    result = partial*partial
    if n%2==1:
      result*=x
    return result
    
print(power2(2,13))

#recursion tower of hanoi
def moveTower(height, fromPole, toPole, withPole):
  if height>=1:
    moveTower(height-1, fromPole, withPole, toPole)
    moveDisk(fromPole, toPole)
    moveTower(height-1, withPole, toPole, fromPole)
  
def moveDisk(fp, tp):
  print("moving disk from",fp,"to",tp)
  
moveTower(3, 'A','B','C')


#recursive palidrome:
#T =[1,4,6,7,3,4,7,9]
#T = [1,4,7,4,1]
T = 'georgegroeg'



arr = list(T)
SOld = copy.deepcopy(arr)
print(SOld)
print(arr)


def palindrome_check(T, start, stop):
  if start < stop-1:
    T[start], T[stop-1] = T[stop-1], T[start]
    palindrome_check(T, start+1, stop-1)
  if T == SOld:
    #print (T, SOld)
    return True
  return False

#print(palindrome_check(T, 0, len(T)))   #for numbers
print(palindrome_check(arr, 0, len(arr))) #for strings
