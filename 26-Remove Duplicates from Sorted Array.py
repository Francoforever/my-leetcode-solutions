class Solution(object):
    def removeDuplicates(self, nums):
        if nums == [] or len(nums) == 1:
            return len(nums)
        a = 1
        while(0 < a < len(nums)):
            if nums[a] > nums[a - 1]:
                a += 1
            else:
                nums.pop(a)
        return len(nums)
