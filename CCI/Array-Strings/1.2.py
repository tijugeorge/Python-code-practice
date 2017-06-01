#Given two strings, write a method to decide if #one is a permutation of the other.
from collections import Counter

def check_permutation(a, b):
    """time: O(n) space: O(n)"""
    if len(a) != len(b): 
      return False
    #print Counter(a), Counter(b)
    return Counter(a) == Counter(b)
    
    
print check_permutation("check", "kcche")

def check_permutation_2(a, b):
    """time: O(n*logn) space: O(1). It modifies the lists in place."""
    if not isinstance(a, list): 
      a = list(a)
      print a
    if not isinstance(b, list): 
      b = list(b)
      print b
    if len(a) != len(b): 
      return False
    a.sort(); b.sort()
    return a == b
    
print check_permutation_2("check", "kcche")
