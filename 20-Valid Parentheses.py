class Solution(object):
    def isValid(self, s):
        lis = []
        dic = {"(": 0, "[": 1, "{": 2, ")": 3, "]": 4,"}": 5}
        for i in range(0, len(s)):
            if 0 <= dic[s[i]] <= 2:
                lis.append(dic[s[i]])
            else:
                if lis != [] and dic[s[i]] -3 == lis[-1]:
                    lis.pop()
                else:
                    return False
        if lis != []:
            return False
        return True
