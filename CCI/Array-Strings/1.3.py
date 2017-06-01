def URLify(string, length):
    """time: O(n) space: O(n)"""
    return string.rstrip().replace(' ', '%20')
    
print URLify('Mr John Smith    ', 13)
