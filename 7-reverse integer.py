class Solution(object):
    def reverse(self, x):
        length = len(str(x))
        resnum = 6
        eor = 0
        if type(x) != int:
            eor = 1
        elif abs(x) > (2**31-1):
            resnum = 0
        elif x != 0:
            if x < 0:
                length -= 1
            resnum = 0
            xabs = abs(x)
            for i in range(length-1):
                resnum += (xabs / (10 ** i) - (xabs / (10 ** (i + 1))) * 10) * (10 ** (length - 1 - i))
            resnum = resnum + xabs / (10 ** (length - 1))
            if x < 0:
                resnum *= (-1)
        elif x == 0:
            resnum = 0
        if eor == 1:
            return -1
        else:
            if abs(resnum) > (2**31-1):
                resnum = 0
            return resnum
