class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lis = []
        if numRows == 0:
            return lis
        lis.append([1])
        for i in range(1, numRows):
            lis.append([])
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    lis[i].append(1)
                else:
                    lis[i].append(lis[i - 1][j - 1] + lis[i - 1][j])
        return lis
