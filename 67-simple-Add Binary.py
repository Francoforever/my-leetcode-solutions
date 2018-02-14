class Solution(object):
    def addBinary(self, a, b):
        num = int(a,2) + int(b,2)
        return bin(num)[2:]
