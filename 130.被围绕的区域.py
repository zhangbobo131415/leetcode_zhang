#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (37.08%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 25.4K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0 or len(board[0])==0:
            return
        res = [['X' for i in board[0]] for ii in board]
        visited = [[0 for i in board[0]] for ii in board]
        l = len(board)
        w = len(board[0])
        while True:
            start_index_i, start_index_j = self.get_first_O(board, visited, l, w)
            if start_index_i == None or start_index_j == None:
                break
            self.writte_X_to_O(start_index_i, start_index_j, res, visited, board, l, w)
        board[:] = res[:]
        # for i in board:
        #     print(i)
        # print('--------------------------')
   
    def get_first_O(self, board, visited, l, w):
        for i in range(l):
            if board[i][0] == 'O' and visited[i][0] == 0:
                return i, 0
            if board[i][w - 1] == 'O' and visited[i][w - 1] == 0:
                return i, w - 1
        for j in range(w):
            if board[0][j] == 'O' and visited[0][j] == 0:
                return 0, j
            if board[l - 1][j] == 'O' and visited[l - 1][j] == 0:
                return l - 1, j
        return None,None
    def writte_X_to_O(self, i, j, res, visited, board, l, w):
        res[i][j] = 'O'
        visited[i][j] = 1
        if self.legal_i_j(i - 1, j, visited, board, res, l, w):
            self.writte_X_to_O(i-1, j, res, visited, board, l, w)
        if self.legal_i_j(i + 1, j, visited, board, res, l, w):
            self.writte_X_to_O(i+1, j, res, visited, board, l, w)
        if self.legal_i_j(i, j + 1, visited, board, res, l, w):
            self.writte_X_to_O(i, j+1, res, visited, board, l, w)
        if self.legal_i_j(i, j - 1, visited, board, res, l, w):
            self.writte_X_to_O(i, j-1, res, visited, board, l, w)
        
    def legal_i_j(self,m, n, visited, board, res, l, w):
        if 0 <= m < l and 0 <= n < w and visited[m][n] == 0 and board[m][n] == 'O':
            # res[m][n] = 'O'
            # visited[m][n] = 1
            return True
        else:
            return False
if __name__ == '__main__':
    test = Solution()
    data = [["O","O","O"],["O","O","O"],["O","O","O"]]
    test.solve(data)
    for i in data:
        print(i)

