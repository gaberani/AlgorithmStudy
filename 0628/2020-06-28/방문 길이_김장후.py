def solution(dirs):
    answer = 0
    N = 11
    visited = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
    i, j = 5, 5
    for dir in dirs:
        pivot = 0
        if dir == 'U':
            di, dj = -1, 0
        elif dir == 'L':
            pivot = 1
            di, dj = 0, 1
        elif dir == 'D':
            pivot = 2
            di, dj = 1, 0
        else:
            pivot = 3
            di, dj = 0, -1
        x = i + di
        y = j + dj
        # U: 0, L: 1, D: 2, R: 3
        if 0 <= x < N and 0 <= y < N:
            if not visited[x][y][pivot]:
                visited[x][y][pivot] = 1
                visited[i][j][(pivot+2)%4] = 1
                answer += 1
            i, j = x, y
    return answer



dirs = 'ULURRDLLU'
print(solution(dirs))
dirs = 'LULLLLLLU'
print(solution(dirs))