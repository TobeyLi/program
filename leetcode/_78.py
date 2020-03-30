# url:https://leetcode.com/problems/subsets/

# Main idea:给定一个list，找到这个list中的子集合（是采用组合的方式，而不是排列）。同77 一致，本题也是需要采用
# DFS 的方式去解决这个问题，DFS解决寻找所有组合的这个方式是比较通用的。

class Solution:
    def subsets(self, nums):
        res=[]
        self.__helper(nums,0,[],res)
        return res

    def __helper(self,nums,index,path,res):
        #  终止条件,本题是直接进行添加的
        res.append(path)
        for i in range(index,len(nums)):
            self.__helper(nums,i+1,path+[nums[i]],res)


if __name__ == '__main__':
    solution=Solution()
    nums=[1,2,3]
    print(solution.subsets(nums))
