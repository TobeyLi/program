# URL:https://leetcode.com/problems/distinct-subsequences/

# Main idea；给定两个字符串，S和T，判断T是S的子串的情况有多少种（注意顺序是不能乱的），顺序
# 乱了就不能称为子串。

# 解题方式：看到有关字符串的子序列的问题，首先应该考虑的就是用动态规划 Dynamic Programming 来求解，
# 这个应成为条件反射。分析DP状态转移方程，以题目的例子为准，找出状态转移方程得到：
#   Ø r a b b b i t
# Ø 1 1 1 1 1 1 1 1
# r 0 1 1 1 1 1 1 1
# a 0 0 1 1 1 1 1 1
# b 0 0 0 1 2 3 3 3
# b 0 0 0 0 1 3 3 3
# i 0 0 0 0 0 0 3 3
# t 0 0 0 0 0 0 0 3

# 首先是初始化第一行与第一列，定义行为S，列为T。因为空字符串是所有字符串的字串，那么可得到第一行的值为1，同理可得到第一列的值
# 为0，后续可以写出矩阵中的数字。定义dp数组，其中dp[i][j]表示为s中范围是[0, i] 的子串中能组成t中范围是[0, j] 的子串的
# 子序列的个数。
# 当更新到dp[i][j]时，当T[i-1]==S[j-1]时，dp[i][j]=dp[i][j-1]+dp[i-1][j-1]，若不等，
# dp[i][j] = dp[i][j - 1]，所以，综合以上，递推式为：
# dp[i][j] = dp[i][j - 1] + (T[i - 1] == S[j - 1] ? dp[i - 1][j - 1] : 0)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 二维数组定义
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for k in range(len(dp)):
            dp[k][0]=1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if(s[i-1] == t[j-1] and dp[i-1][j-1]):
                    dp[i][j] = max(dp[i-1][j-1] + dp[i-1][j], dp[i-1][j]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]