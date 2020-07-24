
# 最简单的爬楼梯问题分析
# 一次你可以爬一步，或者是两步，那么总共有多少种不同的方式爬到第n层
# 同样的，这个题目和斐波那契数列的解决方式是一样的，自己也可以采用其他的方式来解决
# 当Blog写到这里的时候，如果还没写到变态青蛙跳的话，那么自己需要在Blog种写到

# f(n)=f(n-1)+f(n-2)
class Solution:
    def climbStairs(self, n):
        """
        直接采用递归的方式，这样是会存在时间复杂度过高的情况，那么可以采用优化的方式
        :param n:
        :return:
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs_1(self, n):
        """
        递归不行，那么我们可以分析采用迭代的方式，因为第n步只是和第n-1和第n-2步想管，那么我们只是需要记录n-1和n-2这两个内容即可
        :param n:
        :return:
        """
        if n==1:
            return 1
        if n==2:
            return 2
        a,b=1,2
        step,count=3,0
        while step<=n:
            count=a+b
            step+=1
            a=b
            b=count
        return count
    def climbStairs_2(self,n):
        """
        发现，大佬还有更加高效的做法，值得去学习一波。。实际是用C++ 重写了上面的迭代方法
        :param n:
        :return:
        """
        pass