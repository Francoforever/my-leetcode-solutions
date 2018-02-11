class Solution(object):
    def romanToInt(self, s):
        signs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lis = []
        for char in s:
            lis.append(signs[char])
        for i in range(0, len(lis) - 1):
            if lis[i] < lis[i + 1]:
                lis[i] *= (-1)
        return sum(lis)
