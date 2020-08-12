import pprint
di = [-1, -1,  0,  1, 1, 1, 0, -1]
dj = [ 0, -1, -1, -1, 0, 1, 1,  1]

grid = [[[0, 0] for _ in range(4)] for _ in range(4)]
# 물고기 이동시키기
def fishMove(direction):
    # 1번부터 16번 순서로 이동
    for fish_num in list(range(1, 17))[::direction]:
        out_flag = 0    # break point flag
        for i in range(4):
            for j in range(4):
                # 일치하는 물고기 찾으면
                if grid[i][j][0] == fish_num:
                    d = grid[i][j][1]
                    ni, nj = i+di[d]*direction, j+dj[d]*direction
                    # 이동할 수 있을 때까지 반시계로 돌린다.
                    while not (0 <= ni < 4 and 0 <= nj < 4 and grid[ni][nj][0] != 99):
                        d += direction
                        ni, nj = i+di[d%8]*direction, j+dj[d%8]*direction
                    grid[i][j][1] = d%8
                    grid[i][j], grid[ni][nj] = grid[ni][nj], grid[i][j]
                    out_flag = 1
                    break
            if out_flag:
                break

def dfs(si, sj, cnt):
    global max_result
    fishMove(1)          # 물고기 이동
    # 맵 복사 해두기
    original_map = [[[0, 0] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            original_map[i][j][0], original_map[i][j][1] = grid[i][j][0], grid[i][j][1]
    d = grid[si][sj][1]  # 상어 자리 방향
    for d_multiple in range(1, 4):
        fi, fj = si+di[d]*d_multiple, sj+dj[d]*d_multiple
        # 2. 상어 이동
        if 0 <= fi < 4 and 0 <= fj < 4 and 0 < grid[fi][fj][0] < 17:
            fish_num = grid[fi][fj][0]
            grid[fi][fj][0] = grid[si][sj][0]  # 상어 번호만 옮김, 방향은 물고기 방향
            grid[si][sj] = [0, 0]  # 상어자리 초기화
            dfs(fi, fj, cnt+fish_num)
            # 원래로 복구 시키기
            for i in range(4):
                for j in range(4):
                    grid[i][j][0], grid[i][j][1] = original_map[i][j][0], original_map[i][j][1]
            if max_result < cnt:
                max_result = cnt

    # 상어가 이동할 수 없으면 종료 / 상어의 방향은 돌지 않는다 / 물고기를 먹을 때만 변함
    else:
        if max_result < cnt:
            max_result = cnt

# 0. 인풋 정리
for i in range(4):
    input_info = input().split()
    for j in range(4):
        # 상어 자리 표시
        if i == 0 and j == 0:
            # 상어는 99로 표시
            eaten_fishs = int(input_info[2*j])  # 처음 들어가는 자리(0, 0) 물고기 번호
            grid[i][j][0], grid[i][j][1] = 99, int(input_info[2 * j + 1]) - 1
        else:
            grid[i][j][0] = int(input_info[2 * j])     # 물고기 번호
            grid[i][j][1] = int(input_info[2 * j + 1]) - 1   # 방향

max_result = 0
sang_d = grid[0][0][1]

# 상어 출발 위치에서 보낸다.
dfs(0, 0, eaten_fishs)
print(max_result)