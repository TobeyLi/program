# URL：https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Main ideas：二叉树的层次遍历，是需要z字形遍历

# 解题方式：记录层数，奇数层顺序掉头，偶数层直接加入最终的序列即可，操作方式和102 一致

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        res, cur = [], [root]
        cnt = 0
        while cur:
            temp, new = [], []
            for node in cur:
                temp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if cnt % 2 == 1:
                temp.reverse()
            res.append(temp)
            cnt += 1
            cur = new
        return res
