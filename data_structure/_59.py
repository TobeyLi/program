# 采用这样的定义方式会导致所有的内容指向一个地址
# tmp=[[0]]*6
# 第二种方法:采用列表生成式，这样就存在多个不同的指针，这样就可以进行操作了
# 第三种方式：可以采用numpy来进行操作

# 最终的目的是将mateix中的值进行改变，可以按照循环打印数组的方式进行操作
class Solution:
    def generateMatrix(self, n):
        if not n:
            return []
        # 产生数组
        res=[[0 for _ in range(n)] for _ in range(n)]
        # 四个方向的内容定义
        left,right,top,down,num=0,n-1,0,n-1,1
        while left<=right and top<=down:
            for i in range(left,right+1):
                res[top][i]=num
                num+=1
            top+=1
            for i in range(top,down+1):
                res[i][right]=num
                num+=1
            right-=1
            for i in range(right, left - 1, -1):
                res[down][i] = num
                num += 1
            down -= 1
            for i in range(down, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res
s=Solution()
s.generateMatrix(3)