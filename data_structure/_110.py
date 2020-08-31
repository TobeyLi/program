# URL ：https://leetcode.com/problems/balanced-binary-tree/

# Main idea:给定一颗二叉树，判断这个二叉树是否是平衡二叉树

# 解题方式：递归的判断每棵子树是否满足二叉平衡树的要求即可

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1