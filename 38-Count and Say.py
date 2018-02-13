class Solution(object):
    def countAndSay(self, n):
        stra = ["1", "11"]
        if n <= 0:
            return ""
        if n == 1 or n == 2:
            return stra[n - 1]
        for i in range(1, n):
            j = len(stra[i])
            num = 1
            while(1):
                if j - 1 == -1:
                    stra[i + 1] = stra[i + 1][::-1]
                    break
                elif j == len(stra[i]):
                    stra.append("")
                    stra[i + 1] += stra[i][j - 1]
                    stra[i + 1] += str(num)
                elif stra[i][j - 1] != stra[i][j]:
                    num = 1
                    stra[i + 1] += stra[i][j - 1]
                    stra[i + 1] += str(num)
                elif stra[i][j - 1] == stra[i][j]:
                    stra[i + 1] = stra[i + 1][:-1]
                    num += 1
                    stra[i + 1] += str(num)
                j -= 1
        return stra[n - 1]
