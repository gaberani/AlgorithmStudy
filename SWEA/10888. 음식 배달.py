# 0은 빈칸 / 1은 집 / 2이상은 배달음식집의 위치 및 운영비
from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    L = int(input())
    grid = [list(map(int, input().split())) for _ in range(L)]
    candidate, home = [], []
    differential_dic = {}
    # 집과 배달 후보 체크
    for i in range(L):
        for j in range(L):
            if grid[i][j] > 1:
                candidate.append([i, j])
            elif grid[i][j] == 1:
                home.append([i, j])

    min_answer = (L*L)**2
    for num in range(1, len(candidate)+1):
        for combi in combinations(candidate, num):
            dis_map = [[L*L**2]*L for _ in range(L)]
            tmp_answer = 0
            for c in combi:
                tmp_answer += grid[c[0]][c[1]]
                for h in home:
                    dis_map[h[0]][h[1]] = min(dis_map[h[0]][h[1]], abs(c[0]-h[0])+abs(c[1]-h[1]))

            for i in range(L):
                for j in range(L):
                    if dis_map[i][j] != L*L**2:
                        tmp_answer += dis_map[i][j]
            min_answer = min(min_answer, tmp_answer)
    print('#{} {}'.format(tc, min_answer))