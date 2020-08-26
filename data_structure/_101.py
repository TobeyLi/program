# URL:https://leetcode.com/problems/symmetric-tree/

# Main idea: 给出一棵树，判断其是否是根据自身对称的

# 解题方式:

class TreeNode:
    def __init__(self,left,right,val):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        基于层次遍历的方式来做
        :param root: 树的根节点
        :return: 是否是对称的树
        """
        if not root:
            return True
        stack=[(root.left,root.right)]

        while stack:
            lNode,rNode=stack.pop()
            if lNode is None and rNode is None:
                continue
            if lNode is None or rNode is None:
                return False
            if lNode.val!=rNode.val:
                return False
            stack.append((lNode.right, rNode.left))
            stack.append((lNode.left, rNode.right))
        return True