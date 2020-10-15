# ROR 게임은 두 팀으로 나누어서 진행하며,
# 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다.
# 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

# 지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다.
# 다음은 5 x 5 크기의 맵에,
# 당신의 캐릭터가 (행: 1, 열: 1) 위치에 있고,
# 상대 팀 진영은 (행: 5, 열: 5) 위치에 있는 경우의 예시입니다.

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def solution(maps):
    N, M = len(maps), len(maps[0])
    visit = [[0]*M for _ in range(N)]
    visit[0][0] = 1
    s = []
    bi, bj = 0, 0
    s.append((bi, bj, 1))
    while 1:
        tmp = []
        while s:
            bi, bj, cnt = s.pop()
            for d in range(4):
                ni, nj = bi+di[d], bj+dj[d]
                if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and maps[ni][nj] == 1:
                    visit[ni][nj] = cnt+1
                    tmp.append((ni, nj, cnt+1))
                if ni == N-1 and nj == M-1:
                    bi, bj = N-1, M-1
                    s, tmp = [], []
                    break
            # for v in visit: print(v)
            # print('----------------')

        if tmp:
            s, tmp = tmp, []
        else:
            break

    if bi == N-1 and bj == M-1:
        answer = cnt + 1
    else:
        answer = -1

    return answer


print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,1],
                [0,0,0,0,1]]))

print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,0],
                [0,0,0,0,1]]))

print(solution([[1, 0]]))