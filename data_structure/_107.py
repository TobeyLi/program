# URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Main idea: 二叉树中序遍历，要求是从底部遍历到上面（自底向上）

# 解题方式：
# （1）按照最原始的自顶向下的遍历方式，然后将list进行反转即可；
# （2）或者是每次都插入到前面一个即可。本题采用第二种方式


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        res, cur = [], [root]
        while cur:
            temp, new = [], []
            for node in cur:
                temp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            cur = new
            res.insert(0, temp)
        return res
