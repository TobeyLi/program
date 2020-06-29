#url:https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Main meaning:给出一个已经排好序的数组，但是这个数组以其中的某一个值为中心，进行了旋转，如[0,0,1,2,2,5,6] 变成 [2,5,6,0,0,1,2]
# 给出一个数字，判断这个数字是否在这个数组中。注意，这个数组中可能存在重复的数字\

# awesome solution
class Solution:
    def search(self, nums, target):
        if len(nums)<1:
            return False
        # split nums into two list
        index=len(nums)
        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) < 0:
                index = i
        l1 = nums[:index]
        l2 = nums[index:]

        l1_index = self.__binary_search(l1, target)
        l2_index = self.__binary_search(l2, target)

        if l1_index >= 0 or l2_index >= 0:
            return True
        else:
            return False

    def __binary_search(self,arr,target):
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)>>1
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1

if __name__ == '__main__':
    solution=Solution()
    nums=[2,5,6,0,0,1,2]
    res=solution.search(nums,1)
    print(res)