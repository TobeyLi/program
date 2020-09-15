# URL:https://leetcode.com/problems/zigzag-conversion/

# Main ideas:将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING"  行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，如"PAHNAPLSIIGYIR"

# 算法思想：本题实际是一个规律题
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        ans = ""
        interval = 2 * (numRows - 1)
        # 最上面一层的边界值
        for i in range(0, len(s), interval):
            ans += s[i]
        # 中间z的输出
        for row in range(1, numRows - 1):
            inter = 2 * row
            i = row
            while i < len(s):
                ans += s[i]
                inter = interval - inter
                i += inter
        # 最下面一层的边界值
        for i in range(numRows - 1, len(s), interval):
            ans += s[i]
        return ans




if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
