class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        length = 0
        for char in range(0, len(strs[0])):
            for i in range(len(strs)):
                if len(strs[i]) - 1 < char:
                    return "" + strs[0][0:length]
                elif strs[0][char] != strs[i][char]:
                    return "" + strs[0][0:length]
            length += 1
        return "" + strs[0][0:length]
