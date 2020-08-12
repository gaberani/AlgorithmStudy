di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

def move(num):
    i, j, d = horses[num]
    order = 0       # 해당 말의 위치에서 몇번째 인덱스에 위치해있는지 인덱스 정보(각 위치는 리스트로 이루어져있기 때문)
    for k in range(len(horseposition[i][j])):
        if horseposition[i][j][k]==num:
            order = k
            break
    movelist = horseposition[i][j][order:]      # 현재 말과 업혀있는 말 함께 이동
    horseposition[i][j] = horseposition[i][j][:order]   # 현재 말 아래에 있는 말들은 이동X
    ni, nj = i+di[d], j+dj[d]
    if pan[ni][nj]==0:
        horseposition[ni][nj] += movelist           # 이동한 후 원래의 리스트에 더하기(업히기)
    elif pan[ni][nj]==1:
        horseposition[ni][nj] += movelist[::-1]     # 이동하는 말들의 순서를 바꾼 후 더하기
    elif pan[ni][nj]==2:
        if d in [1, 2]:         # 방향 반대로 바꿔주기
            d = 3-d
        else:
            d = 7-d
        ni, nj = i+di[d], j+dj[d]           # 방향을 바꿔주고 위의 방법 반복 진행
        if pan[ni][nj] == 0:
            horseposition[ni][nj] += movelist
        elif pan[ni][nj] == 1:
            horseposition[ni][nj] += movelist[::-1]
        elif pan[ni][nj] == 2:
            horseposition[i][j] += movelist     # 이 때의 경우엔 현재 위치에 그냥 더해준다
            ni, nj = i, j                       # 따라서 새로운 위치 좌표도 현재 위치로 변경
    if len(horseposition[ni][nj])>=4:
        return True                             # 4개 이상 쌓이면 true 리턴
    for m in horseposition[ni][nj]:
        if m==num:
            horses[m] = [ni, nj, d]             # 이동한 후 위에 업힌 말들도 위치를 바꿔준다
        else:
            horses[m][0], horses[m][1] = ni, nj

N, K = map(int, input().split())
pan = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]   # 2로 둘러싸인 배열 생성
horses = [[]]       # 각 말들 정보 저장
horseposition = [[[] for _ in range(N+2)] for _ in range(N+2)]  # 각 말이 놓이는 위치 이차원배열 생성  (각 위치는 리스트로 구성되어있다)
for k in range(1, K+1):
    i, j, d = map(int, input().split())
    horses.append([i, j, d])
    horseposition[i][j].append(k)
ans = -1
flag = False
for turn in range(1, 1001):     # 1000번 이동
    for num in range(1, K+1):
        if move(num):           # 문제조건 성립하면
            ans = turn          # 그 떄의 turn 저장
            flag = True
            break
    if flag:
        break
print(ans)