class Solution(object):
    def searchInsert(self, nums, target):
        if nums == []:
            return 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif (nums[i] < target and len(nums) - i == 1) or (nums[i] < target and nums[i + 1] > target):
                return i + 1
            elif nums[i] > target:
                return i
