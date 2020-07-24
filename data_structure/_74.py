# url:https://leetcode.com/problems/search-a-2d-matrix/
# Main idea:
# You should write a algorithm to find whether the target in the matrix.
# the matrix has flowing properties:
#   Integers in each row are sorted from left to right.
#   The first integer of each row is greater than the last integer of the previous row.

# when I see the row and columns are sorted,I think of binary search,so I should try to
# solve it with binary search

class Solution:
    def searchMatrix(self, matrix, target):
        """
        Find the target whether in the matrix,use binary search
        :param matrix:
        :param target:
        :return: bool
        """
        if not matrix or not matrix[0] or target is None:
            return False
        # record the len of colunms and row
        row,column=len(matrix),len(matrix[0])
        for i in range(row):
            first_num=matrix[i][0]
            last_num=matrix[i][column-1]
            if target<first_num:
                return False
            if target>last_num:
                continue
            else:
                return self.__binarySearch(matrix[i],target)

    def __binarySearch(self,array,target):
        low,high=0,len(array)-1
        while low<=high:
            mid=(low+high)//2
            if array[mid]==target:
                return True
            elif array[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False

if __name__ == '__main__':
    solution=Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    matrix_1=[[1]]
    target_1=1
    print(solution.searchMatrix(matrix_1,target_1))