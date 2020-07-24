
# 实现开平方操作
import math
class Solution:
    def mySqrt(self, x):
        """
        直接使用python相关的工具包
        :param x:
        :return:
        """
        return int(math.sqrt(x))
    def mySqrt1(self,x):
        """
        通过自己实现的方法来开平方操作，可以采用二分查找的方式来实现
        :param x:
        :return:
        """
        if x<=1:
            return x
        left,right=0,x
        while left<right:
            mid=left+(right-left)//2
            if mid*mid<=x:
                left=mid+1
            else:
                right=mid
        return right-1


if __name__ == '__main__':
    s=Solution()
    print(s.mySqrt1(8))
