class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        t = [""] * numRows
        for j in range(0, len(s)):
            tmp = j % (2 * numRows - 2)
            if tmp <= numRows - 1:
                t[tmp] += s[j]
            else:
                t[2 * numRows - 2 - tmp] += s[j]
        t = "".join(t)
        return t
