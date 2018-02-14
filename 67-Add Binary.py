#submitted many times because of some small mistakes. Please take care! And of course, there is a 2-line code, which will be submitted later. 
class Solution(object):
    def addBinary(self, a, b):
        inta = intb = 0
        if len(a) == 1:
            inta = int(a)
        else:
            for i in range(0, len(a)):
                inta += (2 ** i) * int(a[len(a) - 1 - i])
        if len(b) == 1:
            intb = int(b)
        else:
            for j in range(0, len(b)):
                intb += (2 ** j) * int(b[len(b) - 1 - j])
        res = inta + intb
        if res == 0 or res == 1:
            return str(res)
        power = 0
        res_str = ""
        while(res > 2 ** power):
            power += 1
        if res != 2 ** power:
            power -= 1
        for i in range(0, power + 1):
            res_str += str(res % 2)
            res /= 2
        res_str = res_str[::-1]
        return res_str
