# URL: https://leetcode.com/problems/longest-palindromic-substring/

# Main idea:给出一个字符串，找到最长的回文字串

# 解题方式：需要借助双指针滑动窗口法进行比较判断，以当前遍历的为中心，开始向两边扩散，以测试用例为标准："cbbd"
# （1）遍历到c，左边没有位置，那么最长的回文字串就是c；
# （2）遍历到b（第一个b），向两边扩散，此时最长的为bb，无回文，结束；
# （3）同理，得到遍历第三个位置，第四个位置...
# 注意：在遍历的时候需要考虑到原始字符串的长度是奇数还是偶数
#  本题是分在了DP下面，那么可以尝试使用DP去解答，首先是要分析出状态转移方程：首先定义一个DP数组，dp[i][j]代表原始字符串s
# 从i到j是否回文。当 i = j 时，只有一个字符，肯定是回文串，如果 i = j + 1，说明是相邻字符，此时需要判断 s[i] 是否等于 s[j]，如果i和j不相邻，
# 即 i - j >= 2 时，除了判断 s[i] 和 s[j] 相等之外，dp[i + 1][j - 1] 若为真，就是回文串，通过以上分析，可以写出递推式如下：
# dp[i, j] = 1                                   if i == j
#          = s[i] == s[j]                        if j = i + 1
#          = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1

class Solution:
    def longestPalindromeSlideWindows(self, s: str) -> str:
        """
        采用双指针滑动窗口法进行比较判断
        :param s: 给定的字符串
        :return: 最长的回文字符串
        """
        res = ""
        for i in range(len(s)):
            odd = self.__getPalindrome(s, i, i)
            even = self.__getPalindrome(s, i, i + 1)
            res = max(res, odd, even, key=len)
        return res

    def __getPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]


    def longestPalindromeDynamicProgramming(self, s: str) -> str:
        """
        本题最终是划在了动态规划的tag下，那么可以尝试使用动态规划去解题，找到状态转移方程, 但是比较遗憾，时间比滑动窗口时间还长
        :param s: 给定的字符串
        :return: 最长的回文字符串
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = ''
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                # palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if len(ans) < end - start + 1:  # changed to reuse ans
                            ans = s[start: end + 1]
        return ans