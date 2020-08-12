def turn(n, direction):
    # 시계 방향
    if direction == 1:
        grid[n] = [grid[n][7]] + grid[n][:7]
    # 반시계 방향
    elif direction == -1:
        grid[n] = grid[n][1:] + [grid[n][0]]

grid = [list(map(int, input())) for _ in range(4)]
K = int(input())

# K번 만큼 회전
for _ in range(K):
    num, d = map(int, input().split())
    # print(num-1, d)
    pi, ni = num - 1, num - 1
    p2, n6 = grid[pi][2], grid[ni][6]
    # 돌리기 전에
    for _ in range(3):
        # 오른쪽 방향 영역 체크
        if 0 <= pi < 3 and p2 >= 0:
            # 극이 다르다면
            if p2 != grid[pi+1][6]:
                p2 = grid[pi + 1][2]    # 돌리기 전에 오른쪽 톱니바퀴 상태 갱신
                turn(pi+1, -d)          # 오른쪽 톱니바퀴 돌림
            # 극이 같다면 더 안도니깐 flag로 사용
            else:
                p2 = -1

        # 왼쪽 방향 영역 체크
        if 1 <= ni < 4 and n6 >= 0:
            # 극이 다르다면
            if grid[ni-1][2] != n6:
                n6 = grid[ni - 1][6]    # 돌리기 전에 왼쪽 톱니바퀴 상태 갱신
                turn(ni-1, -d)          # 왼쪽 톱니바퀴 돌림
            # 극이 같다면 더 안도니깐 flag로 사용
            else:
                n6 = -1
        # 돌릴 방향과 인덱스 갱신
        d *= -1
        pi, ni = pi+1, ni-1
    # 돌려줘야하는 톱니바퀴 돌리기
    turn(num-1, -d)

    # for g in grid:
    #     print(g)
    # print('----------------------------')

# 점수 세기
result = 0
for t in range(4):
    if grid[t][0] == 1:
        result += 2**t
print(result)