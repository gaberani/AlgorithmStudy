# 이동은 현재 칸과 이동하려는 칸의 높이 차 <= height
# 높이 차 > height 일 경우, 사다리를 설치 이동 가능

di = [0, 1,  0, -1]
dj = [1, 0, -1,  0]

def solution(land, height):
    answer = 0
    N = len(land)
    visit = [[0]*N for _ in range(N)]
    def color(si, sj):
        visit[si][sj] = color_cnt
        q = []
        q.append((si, sj))
        tmp_q = []
        while q:
            i, j = q.pop(0)
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0 <= ni < N and 0 <= nj < N and abs(land[i][j]-land[ni][nj]) <= height and visit[ni][nj] == 0:
                    visit[ni][nj] = color_cnt
                    tmp_q.append((ni, nj))
            if not q:
                q = tmp_q
                tmp_q = []
        print(visit)

    color_cnt = 1
    now_height = 0
    cnt = 0
    # height 내 인 것 칠하기
    while cnt != N:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if visit[i][j] == 0 and land[i][j] <= now_height+height:
                    color(i, j)
                    color_cnt += 1
        # 전부 칠했는지 검사
        for i in range(N):
            if 0 not in visit[i]:
                cnt += 1
        now_height += height


    # height 넘는 부분따라 최소 비용 구하기
    # cost_map = [[10000]*N for _ in range(N)]
    cost_dic = {i:10000 for i in range(1, color_cnt-1)}
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0 <= ni < N and 0 <= nj < N and visit[i][j] == visit[ni][nj]-1:
                    if cost_dic[visit[i][j]] >= abs(land[i][j]-land[ni][nj]):
                        cost_dic[visit[i][j]] = abs(land[i][j]-land[ni][nj])
    for c in range(1,color_cnt-1):
        answer += cost_dic[c]
    print(cost_dic)
    return answer


print(solution([[ 1,  4,  8, 10],
                [ 5,  5,  5,  5],
                [10, 10, 10, 10],
                [10, 10, 10, 20]], 3))  # 15

print(solution([[10, 11, 10, 11],
                [ 2, 21, 20, 10],
                [ 1, 20, 21, 11],
                [ 2,  1,  2,  1]], 1))  # 18