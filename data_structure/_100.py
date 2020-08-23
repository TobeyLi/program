# url:https://leetcode.com/problems/same-tree/

# Main idea: 判断两棵二叉树是不是同一颗二叉树，相同的判断情况：结构相同，并且对应结点的值相同

# 解题方式：数的结构和数的结点的值进行判断，通过递归的方式去做,主要是看采用何种方式去做，如何
# 简化代码

class TreeNode:
    def __init__(self,left,right,val):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False