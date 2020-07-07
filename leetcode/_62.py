
# 给定一个二维矩阵，一个机器人怎么从左上方走到右下方，总共存在多少中方式（m行n列）
# 本题的特点：只能存在两种走的方向：向下或者是向下，所有只是需要定义两种方向即可（这种思想是采用DFS来解决的）
# 总共存在多少中不同的方式，那么我们可以采用动态规划的方式去做
# 首先比较简单的可以得到：dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 肯定是采用这两种方式去解决问题的，到达i，j处总共存在多少种距离就等于到达上一步存在的两种方式之和（这种是采用动态规划来解决的）
class Solution:
    def uniquePaths(self, m,n):
        # 采用DFS方法来解决这个问题
        # 首先建立matrix数组
        memo = [[0] * n for _ in range(m)]

        def dfs(m, n, memo):
            if m == 0 or n == 0:
                return 1
            if memo[m][n]:
                return memo[m][n]
            up = dfs(m - 1, n, memo)
            left = dfs(m, n - 1, memo)
            memo[m][n] = up + left
            return memo[m][n]
        res=dfs(m - 1, n - 1, memo)
        return res

    def uniquePaths1(self, m, n):
        """
        使用动态规划的方式来完成本类型题
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    solution=Solution()
    solution.uniquePaths(3,2)