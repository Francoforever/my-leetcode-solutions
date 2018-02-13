class Solution(object):
    def maxSubArray(self, nums):
        l = g = -1000000000000
        for n in nums:
            l = max(n,l+n)
            g = max(l,g)
        return g
