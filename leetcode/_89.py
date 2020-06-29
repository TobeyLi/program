#url:https://leetcode.com/problems/gray-code/

# Main idea:题目的意思是格雷码的转换，首先要弄明白的是，什么是格雷码（https://zh.wikipedia.org/wiki/%E6%A0%BC%E9%9B%B7%E7%A0%81）

# 弄明白格雷码的定义之后，那么就是可以根据题目的意义，去生成格雷码，在这里，我们可以根据最简单的通过二进制转换为格雷码，然后
# 再将格雷码生成十进制数，得到最终的结果.

# 二进制转换为格雷码的方式：二进制码 ----> 格雷码(编码)：从最右边一位起，依次将每一位与左边一位异或(XOR)，作为对应格雷码该位的值，最左边一位不变(相当于左边是0)。
# 格雷码转换为二进制的方式：其法则是保留格雷码的最高位作为自然二进制码的最高位，而次高位自然二进制码为高位自然二进制码与次高位格雷码相异或，而自然二进制码的其余各位与次高位自然二进制码的求法相类似。

class Solution:
    def grayCode(self, n):
        res=[]
        for i in range(pow(2,n)):
            # 高位不变，低位异或，很神奇的玩法
            res.append((i>>1)^i)
        return res

    def grat_2_binary(self,n):
        mask=n>>1
        res=n
        while mask!=0:
            res=res^mask
            mask=mask>>1
        return res

if __name__ == '__main__':
    solution=Solution()
    # print(solution.grayCode(2))
    print(solution.grat_2_binary(2))

