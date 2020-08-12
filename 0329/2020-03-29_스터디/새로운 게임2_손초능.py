import sys
def move(x):
    global n, di, dj, arr, nums, visit
    for i in range(n):
        for j in range(n):
            if visit[i][j]: # 돌이 있는 곳을 발견
                flag, move_list = 0, []
                for k in range(len(visit[i][j])):
                    if visit[i][j][k] == x: # 원하는 순번의 돌이 들어있는지 검사
                        idx, flag = k, 1
                        move_list.append(visit[i][j][k])
                    elif flag: move_list.append(visit[i][j][k]) # 이후 원하는 순번의 돌 위의 돌들을 move_list에 함께 담는다.
                if flag:
                    cnt = 0
                    temp = visit[i][j][0:idx] # 이동하지 않고 남아있는 돌들을 저장
                    visit[i][j], nx, ny = temp, i + di[nums[x]], j + dj[nums[x]]
                    while 1:
                        if 0 <= nx < n and 0 <= ny < n: # 이동 위치가 배열의 범위안에 드는 경우
                            if arr[nx][ny] == 1: # 붉은색일 때,
                                visit[nx][ny] += move_list[::-1] # 이동한 돌들의 순서를 뒤집어서 배열에 추가한다.
                                return len(visit[nx][ny])
                            elif arr[nx][ny] == 0: # 흰색일 때,
                                visit[nx][ny] += move_list # 이동한 돌들을 순서의 변경 없이 배열에 추가한다.
                                return len(visit[nx][ny])
                            elif arr[nx][ny] == 2: # 파란색일 때,
                                if cnt == 1: break # 이미 한 번 범위를 벗어났거나, 파란색에 닿아서 방향이 변경되었을 경우, 이동을 멈춘다
                                nx, ny = i-di[nums[x]], j-dj[nums[x]]
                                if cnt == 0: # 배열의 범위를 벗어난 적이 없고, 파란색에 닿은 것이 처음일 때,
                                    nums[x] = (nums[x] + 2) % 4 # 방향을 변경
                                cnt += 1
                        else: # 이동위치가 배열의 범위를 벗어난 경우
                            if cnt == 1: break # 이미 한 번 범위를 벗어났거나, 파란색에 닿아서 방향이 변경되었을 경우, 이동을 멈춘다
                            nx, ny = i - di[nums[x]], j - dj[nums[x]]
                            if cnt == 0: # 파란색에 닿은 적이 없고, 배열의 범위를 벗어난 것이 처음일 때,
                                nums[x] = (nums[x] + 2) % 4 # 방향을 변경
                            cnt += 1
                    visit[i][j] += move_list # 이동을 하지 않고, 방향한 변경된 경우 다시 원래의 위치 배열에 추가.
                    return 1 # 길이는 4만 넘으면 되기 때문에 이동하지 않은 위치의 돌의 수는 4이하의 임의의 값으로 출력.
                             # 원래 길이가 4이상이었으면, 이미 게임이 끝났음.

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
n, num = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[[] for _ in range(n)] for _ in range(n)]
nums, flag = [0] * num, 0
for i in range(num):
    x, y, d = map(int, sys.stdin.readline().split())
    visit[x-1][y-1].append(i)
    if d == 1: nums[i] = 0 # 방향을 방향이동 배열에 맞게 바꾸어 저장
    elif d == 2: nums[i] = 2 # nums 라는 배열에 각 돌의 이동 방향만 저장
    elif d == 3: nums[i] = 1
    elif d == 4: nums[i] = 3
for case in range(1, 1001):
    for c in range(num):
        length = move(c) # 돌이 이동했을 때, 이동한 최종 위치에서 쌓여진 돌의 수를 출력
        if length >= 4:
            print(case)
            flag = 1
            break
    if flag: break
else:
    print(-1)