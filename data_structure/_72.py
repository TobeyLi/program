
# 求解编辑距离
# 编辑距离的求解一般是考虑整个公式的推导过程，是采用dp的方式去求解，先开始一个一个的模拟分析
# 看最终的结果是如何进行的。
class Solution:
    def minDistance(self, word1, word2):
        """
        基于递归的方式来解决编辑距离,会遇到超时的问题
        :param word1:
        :param word2:
        :return:
        """
        if min(len(word1),len(word2))==0:
            return max(len(word1),len(word2))
        elif word1[-1]==word2[-1]:
            return self.minDistance(word1[:-1],word2[:-1])
        else:
            return min(self.minDistance(word1[:-1],word2),self.minDistance(word1,word2[:-1]),
                       self.minDistance(word1[:-1],word2[:-1]))+1

    def minDistance_1(self, word1, word2):
        """
        采用动态规划来解决问题
        :param word1:
        :param word2:
        :return:
        """
        # 建立二维矩阵dp,dp[i][j]的值为word1[:i]到word2[:j]所需要的最短的edit distance,里面是行，外面是列
        dp=[[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        # 初始化列
        for i in range(len(word1)+1):
            dp[i][0]=i
        # 初始化行
        for j in range(1,len(word2)+1):
            dp[0][j]=j
        # 更新参数,一行一行的更新
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]

if __name__ == '__main__':
    s=Solution()
    print(s.minDistance_1(word1 = "horse", word2 = "ros"))