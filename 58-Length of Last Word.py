class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        flag = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
                flag = 1
            elif s[i] == ' ' and flag == 1:
                return length
        return length
