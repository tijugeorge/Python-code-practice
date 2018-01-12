class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            z = list(map(lambda x, y: x+y , res[-1] +[0], [0] + res[-1]))
            res.append(z)
        return res[:numRows]
