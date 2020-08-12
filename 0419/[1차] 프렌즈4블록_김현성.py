import pprint
di = [0, 1, 1]
dj = [1, 0, 1]

def solution(m, n, board):
    answer = 0
    # 리스트 좌표화
    for i in range(m):              
        board[i] = list(board[i])

    V = []
    tmp_board = [[0] * n for _ in range(m)]
    while board != tmp_board:       # 더 이상 지워지는게 없을 때 까지
        # tmp_board에 복사
        for i in range(m):
            for j in range(n):
                tmp_board[i][j] = board[i][j]

        # 네모 찾기
        for i in range(m-1):
            for j in range(n-1):
                box_flag = 1
                if board[i][j] != '.':
                    cha = board[i][j]
                    for d in range(3):
                        ni, nj = i+di[d], j+dj[d]
                        if not cha == board[ni][nj]:    # 하나라도 기존위치와 다르면
                            box_flag = 0                # box_flag 내림
                            break                       # d-for문 종료
                    if box_flag:            # 네모완성 / 중복으로 좌표들갈 수 있다. 체크안해도될까?
                        if (i, j) not in V:
                            V.append((i, j))
                        for d in range(3):
                            ni, nj = i + di[d], j + dj[d]
                            if (ni, nj) not in V:
                                V.append((ni, nj))
        # 표시된 좌표 모두 꺼내서 board에서 없앰
        while V:
            vi, vj = V.pop()
            board[vi][vj] = '.'
            answer += 1
        # 바닥으로 내리기
        for j in range(n):
            for i in range(m-2, -1, -1):
                if board[i][j] != '.' and board[i+1][j] == '.':
                    for i2 in range(i+1, m):
                        if board[i2][j] != '.':
                            print(board[i][j], board[i2][j])
                            board[i][j], board[i2-1][j] = board[i2-1][j], board[i][j]
                            break
                        if board[i2][j] == '.' and i2 == m-1:
                            board[i][j], board[i2][j] = board[i2][j], board[i][j]

        pprint.pprint(board)
    return answer

# print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
# print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
print(solution(8, 5, ['HGNHU', 'CRSHV', 'UKHVL', 'MJHQB', 'GSHOT', 'MQMJJ', 'AGJKK', 'QULKK']))