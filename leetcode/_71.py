
# 简化路径
# 简化规则：将双斜杠转换成单斜杠，去除没有必要的元素，. 代表当前路径，可以清楚，.. 代表上层路径
# 刚开始想的做法，使用栈来解决这样的问题。要注意空栈的处理

class Solution:
    def simplifyPath(self, path):

        s = path.replace('..', '#')
        s = s.replace('.', '')
        while "//" in s:
            s = s.replace("//", '/')
        if path=='/':
            return path
        stack = []
        for i in range(len(s)):
            if s[i] != '#':
                stack.append(s[i])
            # 只有一个斜杠
            if len(stack) <= 1 and s[i] == '#':
                continue
            if s[i] == '#':
                stack.pop()
                stack.pop()
                stack.pop()
        if len(stack)!=1 and stack[-1] == '/':
            stack.pop()
        return ''.join(stack).replace('//','/')
    def learn(self,path):
        plist = [p for p in path.split('/') if p]
        stack = []
        for p in plist:
            if p == '..':
                if stack:   stack.pop()
            elif p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    s=Solution()
    # 为什么这个测试用例是这样的结果
    print(s.learn("/..."))

