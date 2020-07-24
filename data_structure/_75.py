#url:https://leetcode.com/problems/sort-colors/

# Main idea
# Well,the problem waiting for solving can be concluded as follow:given an array,which conclude
# 0,1,2,sort the array.
# First,we should set 3 point,for example,i,j,k;j is the working point;the number before i is zero;
# the number after k is 2。

#  the main idea behind the problem is quick sort ,I think.
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,k=0,0,len(nums)-1
        while j<=k:
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
                continue
            if nums[j]==1:
                j+=1
                continue
            elif nums[j]==2:
                nums[j], nums[k] = nums[k], nums[j]
                k-=1
if __name__ == '__main__':
    solution=Solution()
    print(solution.sortColors([2,0,2,1,1,0,0]))