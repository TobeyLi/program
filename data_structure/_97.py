# URL:https://leetcode.com/problems/interleaving-string/

# Main Idea: 给定三个字符串s1,s2,s3，判断s3是否是可以由s1,s2错序组成

# 解题方式：
# 更加普遍的做法时：当遇到字符串匹配或者是子序列的时候，需要做的时候采用动态规划去解题，主要的就是找到状态转移方程。
# 首先是二维数组初始化，按照题目给出的用例来作为例子。
#   Ø d b b c a
# Ø T F F F F F
# a T F F F F F
# a T T T T T F
# b F T T F T F
# c F F T T T T
# c F F F T F T
# 二维数组建立方式：首先是边缘的建设，当s1和s2为空时，s3为空时为True，然后按位进行比较，然后若 s1 和 s2 其中的一个为空串的话，
# 那么另一个肯定和 s3 的长度相等，则按位比较，若相同且上一个位置为 True，赋 True，其余情况都赋 False。在任意非边缘位置[i,j]，
# 只要其左边或者是上面有True，那么就可以更新到下一个位置。因为是存在两个字符串比较，所以需要分开进行比较：如果左边的为 True，那么我们取出当前
# 对应的 s2 中的字符串 s2[j - 1] 和 s3 中对应的位置的字符相比（计算对应位置时还要考虑已匹配的s1中的字符），为 s3[j - 1 + i], 如果相等，
# 则赋 True，反之赋 False。 而上边为 True 的情况也类似，所以可以求出状态转移方程为：
# dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i - 1 + j]) || (dp[i][j - 1] && s2[j - 1] == s3[j - 1 + i]);

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        DFS 方式去解题
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        # 建立二维数组与初始化
        dp=[[True for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])
        for j in range(1,len(s2)+1):
            dp[0][j]=dp[0][j-1] and (s2[j-1]==s3[j-1])

        # 遍历
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i - 1][j] and s1[ -1] == s3[i-1+j]) or (dp[i][j - 1] and s2[j - 1] == s3[j - 1 + i]);
        return dp[-1][-1]

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1,s2,s3))