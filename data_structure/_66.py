
import math

# 将一个数加1
class Solution:
    def plusOne(self, digits):
        """
        直接这样做会遇到科学计数法的问题，那么会存在错误，直接转换成成大整数的话会存在问题，这个是需要注意的
        我们需要做的是一边处理一边转换，而不是一起转换
        :param digits:
        :return:
        """
        if len(digits)==0:
            return 0
        n=len(digits)
        count=0
        num=0
        while count<n:
           num+=math.pow(10,count)*digits[-count-1]
           count+=1
        num+=1
        num=str(num)
        print(float(num))
        res=[]

        return res

    def plusOne1(self,digits):
        return map(int, str(int(''.join(map(str, digits))) + 1))

if __name__ == '__main__':
    s=Solution()
    print(list(s.plusOne1([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3])))