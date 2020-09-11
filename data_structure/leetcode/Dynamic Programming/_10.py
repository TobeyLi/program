# URL:https://leetcode.com/problems/regular-expression-matching/

# Main idea:字符串匹配，但是加入了两个通配符，其中：
# '.' 匹配任意单个字符.
# '*' 与前面的元素中的零个或多个匹配。(之前的字符存在0个、1个或者是多个)
# 注意：pattern串必须是要匹配整个输入字符串，而不单单是部分的串

# 解题方式：虽然本题分到了动态规划这个Tag下面，但是状态转移方程是比较难找的，可以采用递归的方式来解答，下面就来分析递归的方式：
# （1）若p为空，若s也为空，返回 true，反之返回 false。
# （2）若p的长度为1，若s长度也为1，且相同或是p为 '.' 则返回 true，反之返回 false。
# （3）若p的第二个字符不为*，若此时s为空返回 false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配。
# （4）若p的第二个字符为*，进行下列循环，条件是若s不为空且首字符匹配（包括 p[0] 为点），调用递归函数匹配s和去掉前两个字符的p
# （这样做的原因是假设此时的星号的作用是让前面的字符出现0次，验证是否匹配），若匹配返回 true，否则s去掉首字母（因为此时首字母
#   匹配了，我们可以去掉s的首字母，而p由于星号的作用，可以有任意个首字母，所以不需要去掉），继续进行循环。
# （5）返回调用递归函数匹配s和去掉前两个字符的p的结果（这么做的原因是处理星号无法匹配的内容，比如 s="ab", p="a*b"，
#   直接进入 while 循环后，我们发现 "ab" 和 "b" 不匹配，所以s变成 "b"，那么此时跳出循环后，就到最后的 return 来比较 "b"
#   和 "b" 了，返回 true。再举个例子，比如 s="", p="a*"，由于s为空，不会进入任何的 if 和 while，只能到最后的 return
#   来比较了，返回 true，正确）。

# reference：https://www.cnblogs.com/grandyang/p/4461713.html

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        采用递归的方式来判断两个串是否匹配
        :param s: 输入字符串
        :param p: 模式串
        :return: 是否匹配
        """
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == ".")
        if p[2] != "*":
            if len(s) == 0:
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        # p[2] = "*" 的情况
        while len(s) != 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])
