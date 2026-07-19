# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):

        def isMirror(left, right):
            # Both nodes are None
            if not left and not right:
                return True

            # One node is None
            if not left or not right:
                return False

            # Values are different
            if left.val != right.val:
                return False

            # Check mirror condition
            return (
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)