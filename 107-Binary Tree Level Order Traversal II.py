# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lis = []
        if root is None:
            return lis
        count = -1
        lisgen = self.generatelis(root, lis, count)
        return lisgen[::-1]
    def generatelis(self, thenode, thelist, count):
        if thenode is None:
            return thelist
        count += 1
        if len(thelist) < count + 1:
            thelist.append([])
        thelist[count].append(thenode.val)
        return self.generatelis(thenode.left, thelist, count) and self.generatelis(thenode.right, thelist, count)
