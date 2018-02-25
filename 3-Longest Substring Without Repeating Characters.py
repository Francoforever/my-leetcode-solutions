class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        start = 0
        maxlen = 0
        for i in range(len(s)):
            dic[s[i]] = -1
        for i in range(len(s)):
            if dic[s[i]] != -1:
                while start <= dic[s[i]]:
                    dic[s[start]] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dic[s[i]] = i
        return maxlen
