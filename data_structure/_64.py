
# 给定一个二维数组，数组里面每一个数都是整形，求从数组的左上方到右下方的路径中，哪一条路径和最小
# 涉及到最短路径的话，那么我们需要考虑的就是能不能采用动态规划去解决,动态规划主要是设计出状态转移方程
# 这个涉及之前的状态，是如何选择的呢？限定了每次只能向下或者向右
# 我们可以设计一个二维数组，然后开始进行赋初值操作，
# dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]


# 由于这个题目的特性，可以将二维数组进行优化成为一维数组，可以查看自己以前参考的解法
class Solution:
    def minPathSum(self, grid):
        if len(grid)==0 or len(grid[0])==0:
            return 0
        row,column=len(grid),len(grid[0])
        # 定义一个dp数组
        dp=[[0 for _ in range(column)] for _ in range(row)]
        # 初始化赋值操作
        dp[0][0]=grid[0][0]
        for i in range(1,row):
            dp[i][0]=grid[i][0]+dp[i-1][0]
        for i in range(1,column):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        for i in range(1,row):
            for j in range(1,column):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]