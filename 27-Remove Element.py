class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return len(nums)
        else:
            a = 0
            while(0 <= a < len(nums)):
                if nums[a] == val:
                    nums.pop(a)
                else:
                    a += 1
            return len(nums)
