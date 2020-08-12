def solution(board):
    def move_list(p1, p2, direction):
        nonlocal board, dx, dy
        result = []
        for i in range(4):
            np1 = [p1[0]+dx[i], p1[1]+dy[i]]
            np2 = [p2[0]+dx[i], p2[1]+dy[i]]
            if board[np1[0]][np1[1]] == 0 and board[np2[0]][np2[1]] == 0:
                result.append((np1[:], np2[:], direction))
        rot = [1, -1]
        rot_direction = (direction+1) % 2
        if p1[0] == p2[0]:
            for i in rot:
                if board[p1[0]+i][p1[1]] or board[p2[0]+i][p2[1]]: continue
                result.append(([p1[0]+i, p1[1]], p1[:], rot_direction))
                result.append(([p2[0]+i, p2[1]], p2[:], rot_direction))
        else:
            for i in rot:
                if board[p1[0]][p1[1]+i] or board[p2[0]][p2[1]+i]: continue
                result.append(([p1[0], p1[1]+i], p1[:], rot_direction))
                result.append(([p2[0], p2[1]+i], p2[:], rot_direction))
        return result

    n, INF = len(board), float('inf')
    board = [[1]*(n+2)]+[[1]+board[i]+[1] for i in range(n)]+[[1]*(n+2)]
    visited = [[[INF]*(2) for _ in range(n+2)] for _ in range(n+2)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visited[1][1][0] = visited[1][2][0] = 0
    q = [([1, 1], [1, 2], 0)]
    while q:
        p1, p2, direction = q.pop(0)
        length = max(visited[p1[0]][p1[1]][direction], visited[p2[0]][p2[1]][direction])+1
        for np1, np2, rot in move_list(p1, p2, direction):
            len_np1, len_np2 = visited[np1[0]][np1[1]][rot], visited[np2[0]][np2[1]][rot]
            if max(len_np1, len_np2) > length:
                if len_np1 > length: visited[np1[0]][np1[1]][rot] = length
                if len_np2 > length: visited[np2[0]][np2[1]][rot] = length
                q.append((np1[:], np2[:], rot))
    return min(visited[n][n])

# print(solution(
#     [
#         [0, 0, 0, 0, 0,],
#         [0, 0, 0, 0, 0,],
#         [0, 0, 0, 0, 0,],
#         [0, 0, 0, 0, 0,],
#         [0, 0, 0, 0, 0,],
#     ]
# ))
# print(solution(
# [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# ))
print(solution(
    [
        [0, 0, 0, 0, 0, 1, 0, 0,],
        [0, 0, 1, 0, 0, 1, 0, 0,],
        [0, 0, 1, 0, 0, 1, 0, 0,],
        [0, 0, 1, 0, 0, 0, 0, 0,],
        [0, 0, 1, 0, 0, 1, 0, 0,],
        [0, 0, 1, 0, 0, 0, 0, 1,],
        [0, 0, 1, 0, 0, 1, 0, 0,],
        [0, 0, 0, 0, 0, 1, 0, 0,],
    ]
))
# print(solution(
#     [
#         [0, 0, 0, 0, 0, 0, 0, 0,],
#         [0, 0, 1, 1, 1, 1, 0, 0,],
#         [0, 0, 1, 0, 0, 1, 0, 0,],
#         [0, 0, 1, 0, 0, 1, 0, 0,],
#         [0, 0, 1, 0, 0, 1, 0, 0,],
#         [0, 0, 1, 0, 0, 1, 0, 0,],
#         [0, 0, 1, 1, 1, 1, 0, 0,],
#         [1, 1, 0, 0, 0, 0, 0, 0,],
#     ]
# ))