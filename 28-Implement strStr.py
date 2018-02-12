class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        elif len(haystack) == len(needle):
            if haystack != needle:
                return -1
            else:
                return 0
        elif len(haystack) < len(needle):
            return -1
        
        else:
            for i in range(0, len(haystack) - len(needle) + 1):
                if haystack[i] == needle[0]:
                    flag = 1
                    for j in range(0, len(needle)):
                        if haystack[i + j] != needle[j]:
                            flag = 0
                            break
                    if flag == 1:
                        return i
                    else:
                        continue
            return -1
