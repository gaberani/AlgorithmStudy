# You are given a 2D char matrix representing the game board.
# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines,
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
di = [1, 1, 1, 0, 0, -1, -1, -1]
dj = [1, 0, -1, 1, -1, 1, 0, -1]
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        def bfs(bi, bj):
            cnt = 0
            answer = []
            for d in range(8):
                ni, nj = bi+di[d], bj+dj[d]
                if 0 <= ni < board_i and 0 <= nj < board_j:
                    # 폭탄일 경우 수를 셈
                    if board[ni][nj] == 'M':
                        cnt += 1
                    # 아직 안 밝혀진 공간
                    elif board[ni][nj] == 'E':
                        answer.append((ni, nj))

            if cnt == 0:
                return cnt, answer
            else:
                return cnt, []

        board_i, board_j = len(board), len(board[0])
        si, sj = click

        if board[si][sj] == 'M':
            board[si][sj] = 'X'
            return board
        elif board[si][sj] == 'E':
            s = [(si, sj)]
            visit = set()
            while s:
                i, j = s.pop(0)
                if (i, j) not in visit:
                    visit.add((i, j))
                    mine, empty_space = bfs(i, j)
                    if mine:
                        board[i][j] = str(mine)
                    else:
                        board[i][j] = 'B'
                    s += empty_space
                else:
                    continue
        return board


# Input:
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# Click : [3,0]

# Output:
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]