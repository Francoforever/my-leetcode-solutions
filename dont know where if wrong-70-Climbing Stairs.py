from scipy.special import comb
class Solution(object):
    def climbStairs(self, n):
        sumup = 1
        if n == 1:
            return sumup
        num = n / 2
        for i in range(1, num + 1):
            sumup += int(comb(n - i, i))
        return sumup
