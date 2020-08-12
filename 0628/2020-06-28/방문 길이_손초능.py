def solution(dirs):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    dir_list = {'U':0, 'R':1, 'D':2, 'L':3}
    visit = [[[0]*4 for _ in range(11)] for _ in range(11)]
    p = [5, 5]
    answer = 0

    for i in range(len(dirs)):
        d = dir_list[dirs[i]]
        nx, ny = p[0] + dx[d], p[1] + dy[d]
        if 0<=nx<=10 and 0<=ny<=10:
            if not visit[p[0]][p[1]][d]:
                answer += 1
                visit[p[0]][p[1]][d] = 1
                visit[nx][ny][(d+2)%4] = 1
            p = [nx, ny]

    return answer