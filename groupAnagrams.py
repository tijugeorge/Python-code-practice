class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicti = {}
        for st in strs:
            key = ''.join(sorted(st))
            if key not in dicti:
                dicti[key] = [st]
            else:
                dicti[key] += [st]
        arr = []
        for i in dicti.values():
            arr.append(i)
        return arr
        
