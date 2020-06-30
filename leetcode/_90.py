# url:https://leetcode.com/problems/subsets-ii/

# Main idea:给出一个list，找出它的所有的子集

# 类似题：leetcode 78

# 一般来说，找子集的问题都可以去通过DFS的方式去解决，本题首先尝试DFS的方法，然后去看看有没有什么优化的空间

# DFS过程：
# void DFS(int 当前状态){
#       if(当前状态为边界状态){
#         记录或输出
#         return;
#       }
#       //横向遍历解答树所有子节点
#       for(i=0;i<n;i++){
#            //扩展出一个子状态。
#            修改了全局变量
#            if(子状态满足约束条件){
#               dfs(子状态)
#            }
#            恢复全局变量   //回溯部分
#       }
# }
class Solution:
    def subsetsWithDup(self, nums):
        res=[]
        # 需要排序的原因主要是因为：在题目中，会存在【1，2，2】和【2，1，2】是重复的存在的情况，需要排序解决这种问题
        nums.sort()
        self.__helper(nums,0,[],res)
        return res

    def __helper(self,nums,index,path,res):
        """
        辅助DFS函数
        :return:
        """
        # 终止条件
        if path not in res:
            res.append(path)
        for i in range(index,len(nums)):
            # 遍历条件：当前元素如果使用，后面的那个元素从哪里开始，也就决定了后面的数字选择多少个。
            if i>index and nums[i]==nums[i-1]:
                continue
            self.__helper(nums,i+1,path+[nums[i]],res)