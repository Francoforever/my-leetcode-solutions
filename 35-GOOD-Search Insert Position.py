class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)
        while low < high:
            mid = (low+high) / 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
