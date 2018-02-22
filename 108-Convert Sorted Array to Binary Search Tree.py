# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            head = TreeNode(nums[0])
            head.left = None
            head.right = None
            return head
        else:
            head = TreeNode(nums[len(nums)/2])
            head.left = self.sortedArrayToBST(nums[:len(nums)/2])
            head.right = self.sortedArrayToBST(nums[len(nums)/2+1:])
            return head
