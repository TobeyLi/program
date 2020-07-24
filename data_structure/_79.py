# url:https://leetcode.com/problems/word-search/

# Main meaning: 给定一个二维数组以及一个字符串，当遍历到某一个字符时，可以向其上下左右寻找下一个字符，但是不能
# 去到原来的字符，问这个字符串是否可以在这个二维数组中找到

# Main idea：对于在这个二维数组中寻找给定的字符串的时候，第一想法是通过DFS进行遍历寻找，但是寻找的方向是不确定的。
# 需要自己来定义遍历的方向，然后开始DFS的过程

# PS: 本题是我在面试腾讯的时候，手撕代码的题，给20min，写出代码并且讲解具体的思路

class Solution:
    def exist(self, board, word):
        # board 二维数组判断
        if not board or not len(board[0]):
            return False
        # 遍历board，查看是否满足条件
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 第一个字符相等才进行DFS,
                if board[i][j]==word[0]:
                    if(self.__helper(board,i,j,word)):
                        return True
        return False

    def __helper(self,board,i,j,word):
        # word遍历完成
        if len(word)==0:
            return True
        # 需要从四个方向去进行判断,同时记录已经走过的路径
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        temp=board[i][j]
        # 设置已经遍历的内容成分
        board[i][j]="#"
        res=self.__helper(board, i+1, j, word[1:]) or self.__helper(board, i-1, j, word[1:]) \
            or self.__helper(board, i, j+1, word[1:]) or self.__helper(board, i, j-1, word[1:])
        # 回退
        board[i][j]=temp
        return res


if __name__ == '__main__':
    solution=Solution()
    board =[['A', 'B', 'C', 'E'],['S', 'F', 'C', 'S'],['A', 'D', 'E', 'E']]
    word = "ABCCED"
    print(solution.exist(board,word))