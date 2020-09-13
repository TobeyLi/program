# URL:https://leetcode.com/problems/longest-valid-parentheses/

# Main idea:给出一个字符串，包含"（"，和"）"，找到最长的合法括号匹配

# 解题方式：涉及到有效到括号匹配问题，我们一般会借助于栈来帮助我们进行判断。
# 需要定义一个start变量来记录合法括号串的起始位置，然后开始遍历字符串，遇到左括号，那么将下标压入到栈中，如果遇到右括号，如果
# 当前栈为空，则将下一个坐标位置记录到 start，如果栈不为空，则将栈顶元素取出，此时若栈为空，则更新结果和 i - start + 1 中
# 的较大值，否则更新结果和 i - st.top() 中的较大值，

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        括号匹配有效性验证，根据栈来解答
        :param s:
        :return:
        """
        # 定义起始变量和记录最终的结果
        res,start=0,0
        stack=[]
        for index,val in enumerate(s):
            # 当前遍历的内容为左括号
            if val=="(":
                stack.append(index)
            elif val==")":
                # 当前遍历的为右括号，但是栈中已无元素，那么这个右括号是不合法的，记录下一个合法的位置
                if len(stack)==0:
                    start=index+1
                else:
                    # 弹出栈中元素，更新结果
                    stack.pop()
                    res=max(res,index-start+1) if len(stack)==0 else max(res,index-stack[-1])
        return res