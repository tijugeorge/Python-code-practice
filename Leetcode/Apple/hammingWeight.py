def hammingWeight(n, count=0):
    return hammingWeight(n & n-1, count+1) if n!=0 else count 
    
    
    
print(hammingWeight(12))
