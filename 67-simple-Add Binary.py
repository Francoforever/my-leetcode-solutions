class Solution(object):
    def addBinary(self, a, b):
        inta = int(a, 2)
        intb = int(b, 2)
        res = inta + intb
        res_str = bin(res)
        return res_str[2:]
