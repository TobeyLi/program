# url:https://leetcode.com/problems/decode-ways/

# Main meaning:存在一种映射关系：A->1,B->2...Z->26,然后给你一个只包含数字的字符串，
# 判断这个字符串解析为英文字母存在多少种形式，说的比较直白一些，就是怎么去划分这个数字字符串

# 解题方式：确实，在初看这题的时候，想到的是采用类似青蛙跳的方式，但是自己分析的时候，却get不到点，学习掌握这个idea。
# 限制条件：一位数时不能为0，二位数时不能大于26
# 采用dp来解决这样的方式，其中dp[i]表示s中前i个字符组成的子串的解码方法的个数，长度比输入数组长多多1，并将 dp[0]初始化为1。
# 采用具体的情况来进行分析：
# 对于case： 2260

# s[0]=2,那么此时有一种情况，所以有：dp=[1,1,0,0,0]
# s[1]=2,那么此时，总共有两种情况：本身是不等于0的，那么就至少是和前面有一样多的情况，且s[0]和s[1]能组成一个两位数，
# 所以dp[2]=dp[i-1]+dp[i-2]=dp[0]+dp[1]=2,此时dp=[1,1,2,0,0]
# s[2]=6,同理分析：dp[3]=dp[i-1]+dp[i-2]=dp[1]+dp[2]=3,此时dp=[1,1,2,3,0]
# s[3]=0,此时是不能单独的进行解码，dp[4]=0,此时dp=[1,1,2,3,0]

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0]=1

        for i in range(1,len(dp)):
            if s[i-1]!="0":
                dp[i]=dp[i-1]
            # 更新
            if i>1 and "09"<s[i-2:i]<"27":
                dp[i]+=dp[i-2]
        return dp[-1]
if __name__ == '__main__':
    solution=Solution()
    print(solution.numDecodings("2267"))
