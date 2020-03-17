# problem url:https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        Main idea：
        we shold record the index of zeroes in the matrix,then use the index to set
        the original matrix's columns and rows to be zeroes
        """
        index_zero=[]
        # 遍历matrix,记录原文中为0的坐标
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # 如果存在为0，那么将这一行以及一列全都变为0
                if matrix[i][j]==0:
                    index_zero.append((i,j))
        # 对原数组进行处理，将角标对应的行和列设置为0
        for i,j in index_zero:
            # 设置行为0
            for k in range(len(matrix[0])):
                matrix[i][k]=0
            # 设置列为0
            for l in range(len(matrix)):
                matrix[l][j]=0

    def setZeroes_1(self,matrxi):
        """
        this way of solution is from https://leetcode.com/problems/set-matrix-zeroes/discuss/541988/Python3-O(r%2Bc)-HashMap-Solution-with-Comments
        He/She is mainly use set to record zeroes,but I think the idea of solution is same as mine.
        :param matrxi:
        :return:
        """
        row = set()
        col = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)

        for r in row:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0

        for c in col:
            for r in range(len(matrix)):
                matrix[r][c] = 0

if __name__ == '__main__':
    solution=Solution()
    matrix=[[1,1,1],[1,0,1],[1,1,1]]
    matrix_2=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix_2)
