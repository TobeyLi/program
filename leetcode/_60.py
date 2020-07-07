
# 返回第k个回文字符串
# 算法思想：首先是需要生成回文字符串，即给定数字n，按照数字可以产生回文字符串，一般的方式是采用DFS

class Solution:
    def getPermutation(self,n,k):
        """
        这种方法是可以产生所有的排列数，但是不是按照我们想要的规则来运行的，其产生的内容是比较任意的，这不是我们所想要的；
        那么怎么按照序列的要求进行产生下一个排列数呢
        :param n:
        :param k:
        :return:
        """
        res=list()
        nums=[i+1 for i in range(n)]
        def dfs(nums,path,res):
            # 边界条件判断
            if len(path)==n:
                res.append(path)
            # 循环条件
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],[nums[i]]+path,res)
        dfs(nums,[],res)
        return res[k]
    def getPermutation1(self,n,k):
        """
        这个题目的解题思路不是先一次全部生成所有的内容，而是按照生成的格式（条件），然后进行找规律进行生成
        先确定第一个数，再确定第二个数，第三个数、第四个数等等.
        本题的实现主要是找规律，然后通过这样的规律来实现。
        reference：https://www.cnblogs.com/grandyang/p/4358678.html
        :param n:
        :param k:
        :return:
        """
        ans=''
        fact=[1]*n
        # 先建立0～9 字符串
        num=[str(i) for i in range(1,10)]

        # 算阶乘，便于后面做除法
        for i in range(1,n):
            fact[i]=fact[i-1]*i
        print(fact)
        # 下标需要减少1
        k-=1
        for i in range(n,0,-1):
            # 确定第一个数字
            first=k//fact[i-1]
            k%=fact[i-1]
            ans+=num[first]
            # 在已经找到的字符串中去除这个字符,避免这个字符再次出现
            num.pop(first)
        return ans
s=Solution()
print(s.getPermutation1(3,2))

