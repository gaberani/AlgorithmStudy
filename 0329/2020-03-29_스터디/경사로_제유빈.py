import sys

# 경사로를 놓을 수 없을 때를 check
def road(P):
    global cnt, L
    for r in range(N):
        flag = 0  # 경사로를 놓을 수 없을 때 flag
        occ = [0]*N   # occupied(경사로 놓은 자리 표시)
        for c in range(1, N):
            # 앞의 값과 차이가 1보다 크면
            if P[r][c] > P[r][c-1]+1 or P[r][c] < P[r][c-1]-1:
                flag = 1
                break

            # 앞의 값보다 1 클 때
            if P[r][c] == P[r][c-1]+1:
                # 경사로 길이만큼 값이 일정하지 않으면 flag
                if P[r][c-L:c] != [P[r][c]-1]*L:
                    flag = 1
                # 경사로 길이 모두 조건 만족할 때
                else:
                    # 이전에 놓은 경사로와 겹쳐지지 않으면
                    if occ[c-L:c] == [0]*L:
                        occ[c-L:c] = [1]*L
                    # 겹쳐지면
                    else:
                        flag = 1
            # 앞의 값보다 1 작을 때
            if P[r][c] == P[r][c-1]-1:
                if P[r][c:c+L] != [P[r][c]]*L:
                    flag = 1
                else:
                    if occ[c:c+L] == [0]*L:
                        occ[c:c+L] = [1]*L
                    else:
                        flag = 1
            if flag:
                break
        if not flag:
            cnt += 1

N, L = map(int, sys.stdin.readline().split())
# 행 검사할 리스트
RP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 열 검사할 리스트 (행, 열 바꿈)
CP = [[RP[c][r] for c in range(N)] for r in range(N)]

cnt = 0
road(RP)
road(CP)
print(cnt)
