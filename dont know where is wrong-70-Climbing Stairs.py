from scipy.special import comb
class Solution(object):
    def climbStairs(self, n):
        sumup = 0
        if n == 1:
            return 1
        num = n / 2
        for i in range(0, num + 1):
            sumup += int(comb(n - i, i))
        return sumup
