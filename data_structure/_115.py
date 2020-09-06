# URL:https://leetcode.com/problems/distinct-subsequences/

# Main idea；给定两个字符串，S和T，判断T是S的子串的情况有多少种（注意顺序是不能乱的），书序
# 乱了就不能称为子串。

# 解题方式：看到有关字符串的子序列或者配准类的问题，首先应该考虑的就是用动态规划 Dynamic Programming 来求解，
# 这个应成为条件反射。分析DP状态转移方程

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass