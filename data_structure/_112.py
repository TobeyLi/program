# URL:https://leetcode.com/problems/path-sum/

# Main idea:给出一颗二叉树和一个值，判断是否存在一条由根节点到叶子节点的路径，使这条路径上的值相加等于给定的值

# 解题方式:基于先序遍历的思想，采用非递归的方式来解答，当遍历到叶子节点时，判断这个路径上面的值的和与给定值是否相同.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        借助于类似先序遍历的做法来解决
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if sum == val:
                    return True
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
        return False

    def hasPathSum_recursive(self, root, sum):
        """
        借助递归的方式来解决
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)