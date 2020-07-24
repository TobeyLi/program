# url:https://leetcode.com/problems/unique-binary-search-trees-ii/

# Main idea:给出一个数字n，要求使用1，...n建造出不同的二叉树，返回这样二叉树的序列

# 解题方式：我们知道总共的计算方式为卡特兰数：c(2n, n)/(n+1)，那么是怎么统计出所有的可能的结果呢？
# 这道题的主要的方式就是建树，对于[1,2,3...n],以每个节点作为根节点，然后其划分开了左右两个子区间，然后分别调用递归函数，
# 会得到两个结点数组，接下来要做的就是从这两个数组中每次各取一个结点，当作当前根结点的左右子结点，
# 然后将根结点加入结果 res 数组中即可.注意题目中都是先序遍历的结果
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        if n==0:
            return []
        return self.__helper(1,n)

    def __helper(self,start,end):
        if start>end:
            return [None]
        res=[]
        for i in range(start,end+1):
            left=self.__helper(start,i-1)
            right=self.__helper(i+1,end)
            for m in left:
                for n in right:
                    node=TreeNode(i)
                    node.left=m
                    node.right=n
                    res.append(node)
        return res
