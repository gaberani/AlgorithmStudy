# 가능한 다리 놓기
def bridge(n, k):
    global flag
    if n == k:
        endflag = go()     # 모든 세로선이 알맞게 오면 0
        if not endflag:
            flag = 1
            return
    else:
        for i in range(1, H+1):
            for j in range(1, N+1):
                if ladder[i][j] != 1 and ladder[i][j-1] != 1 and ladder[i][j+1] != 1:
                    ladder[i][j] = 1
                    bridge(n+1, k)
                    ladder[i][j] = 0
                    if flag:
                        return

# bridge 에서 가짓수 뽑아서 실행
def go():
    endflag = 0
    for j in range(1, N+1):  # 각 세로선이 자기 자신으로 끝나는지 체크
        x, y = 1, j
        while x != H + 1:
            if ladder[x][y]:
                y += 1
            elif ladder[x][y - 1]:
                y -= 1
            x += 1
        if y != j:      # 중간에 틀리면
            endflag = 1
            break       # break해서 나머지 세로선은 안봄
    return endflag

# N: 세로선 수, M: 놓여진 가로선 수, H: 가로선 수
N, M, H = map(int, input().split())
ladder = [[0]*(N+2) for _ in range(H+2)]
for s in range(M):
    si, sj = map(int, input().split())
    ladder[si][sj] = 1

flag = 0
result = -1
for bg in range(4):     # 가로선 놓을 수 있는 갯수: 0~3
    bridge(0, bg)
    if flag:            # 모든 세로선이 자기 자신으로 가면 flag = 1이므로 더 안하고 break
        result = bg     # 결과값 갱신
        break
print(result)