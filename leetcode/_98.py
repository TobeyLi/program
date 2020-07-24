# URL:https://leetcode.com/problems/validate-binary-search-tree/

# Main idea:给定一颗树，判断树是否是二叉排序树

# 解题方式：
# 可以按照二叉排序树的性质来做，即左<根<右
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
         直接通过树来进行判断
        :param root:
        :return:
        """
        if not root:
            return True
        return self.isValidNode(root, float('-inf'), float('inf'))

    def isValidNode(self, root, left, right):
        if not root:
            return True
        return left < root.val < right and self.isValidNode(root.left, left, root.val) and \
               self.isValidNode(root.right, root.val, right)



    def isValidBST_1(self,root:TreeNode)->bool:
        """
        借助一个数组来实现判断，判断其是否是有序即可
        :param root:
        :return:
        """
        treeNoneVal=[]
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            treeNoneVal.append(node.val)
            inOrder(node.right)
        inOrder(root)
        for i in range(1, len(treeNoneVal)):
            if treeNoneVal[i-1] >= treeNoneVal[i]:
                return False

        return True