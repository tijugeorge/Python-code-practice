#Divide two integers without using multiplication, division and mod operator.
#If it is overflow, return MAX_INT.

def divide(dividend, divisor):
  positive = (dividend < 0) is (divisor < 0)
  dividend, divisor = abs(dividend), abs(divisor)
  res = 0
  while dividend >= divisor:
    temp, i = divisor, 1
    while dividend >= temp:
      dividend-=temp
      res+=i
  if not positive:
    res = -res
  return min(max(-2147483648, res), 2147483648)
  
  
  
print(divide(-121, 11))
