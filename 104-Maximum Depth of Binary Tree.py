# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        count = 1
        return self.treedepth(root, count)
    def treedepth(self, thenode, count):
        if thenode is None:
            return count
        if thenode.left is None and thenode.right is None:
            return count
        count += 1
        return max(self.treedepth(thenode.left, count), self.treedepth(thenode.right, count))
