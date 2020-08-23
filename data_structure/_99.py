# https://leetcode.com/problems/recover-binary-search-tree/

# Main idea:二叉排序树的两个节点的值被错误的替换了，复原这棵二叉排序树

# 解题方式：二叉排序树的特点：左<根<右，找到不符合条件的两个结点，将他们的值进行替换即可，
# 树的结构是不变的，只是需要将值替换一下即可,那么在遍历的时候保存值且保存树的结构，直接遍历即可

class TreeNode:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes,vals=[],[]
        self.__inOrder(root,nodes,vals)
        vals.sort()
        for i,node in enumerate(nodes):
            node.val=vals[i]


    def __inOrder(self,root:TreeNode,nodes,vals):
        if root is None:
            return
        self.__inOrder(root.left,nodes,vals)
        nodes.append(root)
        vals.append(root.val)
        self.__inOrder(root.right,nodes,vals)
