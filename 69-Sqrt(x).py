class Solution(object):
    def mySqrt(self, x):
        val = x
        a = 0
        b = x
        while(x > 2):
            if val ** 2 > x:
                b = val
                val = (a + b) / 2
            elif val ** 2 <= x < (val + 1) ** 2:
                return val
            elif (val + 1) ** 2 < x:
                a = val + 1
                val = (a + b) / 2
            elif (val + 1) ** 2 == x:
                return (val + 1)
            else:
                break
        if x == 2 or x == 1:
            return 1
        else:
            return 0
