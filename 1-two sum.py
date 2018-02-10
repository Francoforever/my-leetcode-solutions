class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                resultlists = []
                sumup = nums[i] + nums[j]
                if sumup == target:
                    resultlists.append(i)
                    resultlists.append(j)
                    return resultlists
                    break
            else:
                continue
            break

res = Solution()
res.twoSum([2,7, 11, 15], 9)
