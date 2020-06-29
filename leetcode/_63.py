
# 这个题目是62题的强化版本，现在我们的路上是存在障碍物的，即给定数字，有些内容被标记为1，表明此路不通，你需要换
# 另外一种方式来通过这个路，问：现在从最上方出发，走到最下方总共存在多少种不同的情况

# 问题分析：按照具体的情况来看，这个题目同样是可以采用动态规划来做，但是需要加上一定的条件判断
# 即某个位置存在1的情况的话，那么就不能从这里面过
# 状态转移方程为：d[i][j]=d[i-1][j]+d[i][j-1]
# 这个状态转移方程没有凸显出包含障碍的这个特点
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        在构建二维数组的时候，需要先构建列再构建行
        :param obstacleGrid:
        :return:
        """
        if len(obstacleGrid)==0 or len(obstacleGrid[0])==0 or obstacleGrid[0][0]==1:
            return 0
        row,column=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0 for _ in range(column+1)] for _ in range(row+1)]
        dp[0][1]=1 # 随机设置一个值为1，
        for i in range(1,row+1):
            for j in range(1,column+1):
                if obstacleGrid[i - 1][j - 1] != 0:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]
    s=Solution()
    print(s.uniquePathsWithObstacles(obstacleGrid))