class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1 or s[::-1] == s:
            return s
        if len(s) == 2:
            return s[0]
        maxlen = [0]
        start = [0]
        for i in range(0, len(s)):
            while ((i - maxlen[-1]/2) >= 0 and (i + 1 + maxlen[-1]/2) <= (len(s) - 1)):
                if s[i - maxlen[-1]/2] == s[i + 1 + maxlen[-1]/2]:
                    if maxlen[-1] == 0:
                        start[-1] = i + 1
                    maxlen[-1] += 2
                    start[-1] -= 1
                else:
                    if maxlen[-1] != 0:
                        maxlen.append(0)
                        start.append(0)
                    break
            maxlen.append(0)
            start.append(0)
        if maxlen[-1] == 0:
            maxlen[-1] = 1
        else:
            maxlen.append(1)
            start.append(0)
        for i in range(1, len(s)):
            while ((i - ((maxlen[-1] - 1)/2 + 1)) >= 0 and (i + ((maxlen[-1] - 1)/2 + 1)) <= (len(s) - 1)):
                if (s[i - ((maxlen[-1] - 1)/2 + 1)] == s[i + ((maxlen[-1] - 1)/2 + 1)]):
                    if maxlen[-1] == 1:
                        start[-1] = i
                    maxlen[-1] += 2
                    start[-1] -= 1
                else:
                    if maxlen[-1] != 1:
                        maxlen.append(1)
                        start.append(0)
                    break
            maxlen.append(1)
            start.append(0)
        themax = max(maxlen)
        if themax == 1:
            return s[0]
        else:
            staind = maxlen.index(themax)
            return s[start[staind]:themax + start[staind]]
