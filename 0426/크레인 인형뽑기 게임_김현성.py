def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for m in moves:
        for n in range(N):
            if board[n][m-1] != 0:
                if len(stack) == 0:
                    stack.append(board[n][m-1])
                else:
                    if board[n][m-1] == stack[-1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[n][m-1])
                board[n][m-1] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
               ,[1,5,3,5,1,2,1,4]))