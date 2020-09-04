# url:https://leetcode.com/problems/path-sum-ii/

# Main idea: 同T112，但是需要记录路径

# 解题方式：采用DFS 方式进行遍历更新，记录更新路径

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return []
        res=[]
        self.__dfs(root,sum,[],res)
        return res

    def __dfs(self, root, sum, path, res):
        if not root.left and not root.right and sum == root.val:
            path.append(root.val)
            res.append(path)
        if root.left:
            self.__dfs(root.left, sum - root.val, path + [root.val], res)
        if root.right:
            self.__dfs(root.right, sum - root.val, path + [root.val], res)
