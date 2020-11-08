from copy import deepcopy
N = int(input())
# 격자의 각 칸에 있는 모래
grid = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1] # 서남동북 순서
dj = [-1, 0, 1, 0]

# 모래 흩날릴 그림 만들기
dust_maps = []
original_map = [[0, 0, 2, 0, 0],
                [0, 10, 7, 1, 0],
                [5, -1, 0, 0, 0],
                [0, 10, 7, 1, 0],
                [0, 0, 2, 0, 0]]
dust_maps.append(original_map)
for _ in range(3):
    tmp = [[0]*5 for __ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[i][j] = original_map[i][j]
    for i in range(5):
        for j in range(5):
            original_map[i][j] = tmp[j][4-i]
    dust_maps.append(deepcopy(original_map))
    # for m in original_map: print(m)
    # print('------------')
for dust_map in dust_maps: print(dust_map)

# 토네이도 움직일 거리 만들기
tona_cnt, tona_lst = 1, []
for i in range(1, N):
    tona_lst.append(tona_cnt)
    tona_lst.append(tona_cnt)
    tona_cnt += 1
tona_lst.append(i)
# print(tona_lst)

# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작
# 위의 그림은 토네이도가 왼쪽으로 이동할 때이고,
# 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.
tona_d, tona_p = 0, [N//2,  N//2]
for L in tona_lst:
    tona_p[0], tona_p[1] = tona_p[0] + di[tona_d]*L, tona_p[0] + di[tona_d]*L
