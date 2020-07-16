# URL:https://leetcode.com/problems/interleaving-string/

# Main Idea: 给定三个字符串s1,s2,s3，判断s3是否是可以由s1,s2错序组成

# 解题方式：
# 先按照字母的排列书序采用两个栈的方式，判断第三个字符是否可以采取栈弹出的方式最后和s3相等.
# 更加普遍的做法时：当遇到字符串匹配或者是子序列的时候，需要做的时候采用动态规划去解题，主要的就
# 是扎到状态转移方程

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        DFS 方式去解题
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        if not s1:
            return s2==s3
        elif not s2:
          return s1==s3
        if len(s1)+len(s2)!=len(s3):
            return False
        s1,s2=list(s1),list(s2)
        # 当s1遍历的当前位置和s2遍历的当前位置不一致时，可以通过，但是相同时，需要添加其他的判断条件
        for k in s3:
            if len(s1)!=0 and len(s2)!=0 and s1[0]==s2[0]:
                # 可以采用DFS去做，但是这种方式不推荐，也需要实现一下
                pass
            if len(s1)!=0 and s1[0]==k:
                s1.pop(0)
            elif len(s2)!=0 and s2[0]==k:
                s2.pop(0)
            else:
                return False
        return True

    def isInterleave_1(self, s1: str, s2: str, s3: str) -> bool:
        """
        采用DP去解题
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        pass

if __name__ == '__main__':
    s1 = "bcc"
    s2 = "bbca"
    s3 = "bbcbcac"
    print(Solution().isInterleave(s1,s2,s3))