#url:https://leetcode.com/problems/search-in-rotated-sorted-array/

# Main meaning:给出一个已经排好序的数组，但是这个数组以其中的某一个值为中心，进行了旋转，如[0,1,2,5,6] 变成 [2,5,6,0,1]
# 给出一个数字，判断这个数字是否在这个数组中。注意，这个数组中不可能存在重复的数字，
# 每次进行一个binary search操作会得到一个排完序的数组
# 不存在相同值保证了一个规律：如果中间的数小于最右边的数，那么右边是有序的，如果中间的数大于最右边数，则左半段是有序的

class Solution:
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            # 右边是有序的
            if nums[mid]<nums[high]:
                if target>nums[mid] and nums[high]>target:
                    low=mid+1
                else:
                    high=mid-1
            # 左边是有序的
            else:
                if nums[low]<=target and nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        return -1

if __name__ == '__main__':
    solution=Solution()
    nums=[2,5,6,0,1]
    target=0
    print(solution.search(nums,target))

