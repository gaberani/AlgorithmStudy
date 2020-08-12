from collections import deque
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 구슬 움직이는 함수
def move(i, j, d):
    # 못 움직일 때까지
    while arr[i][j]!='O' and arr[i][j]!='#':
        i += di[d]
        j += dj[d]
    # 구멍에 빠지면 좌표 -1로
    if arr[i][j]=='O':
        i, j = -1, -1
    # 아니면 한 칸 원상복귀
    else:
        i -= di[d]
        j -= dj[d]
    return i, j

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
ans = -1
# 구슬 위치 저장한 다음 빈칸으로 변경
for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            R = [i, j]
            arr[i][j] = '.'
        elif arr[i][j]=='B':
            B = [i, j]
            arr[i][j] = '.'
# 구슬이 있었던 자리 모두 저장
visited = []
visited.append([R[0], R[1], B[0], B[1]])
q = deque()
q.append([R[0], R[1], B[0], B[1], 1])
while q:
    # 빨간구슬, 파란구슬 좌표, 이동횟수
    Ri, Rj, Bi, Bj, cnt = q.popleft()
    if cnt==11:
        break
    complete = False
    for d in range(4):
        # 이동 후 좌표
        newRi, newRj = move(Ri, Rj, d)
        newBi, newBj = move(Bi, Bj, d)
        # 빨간구슬만 구멍에 빠졌을 때
        if newRi==-1 and newRj==-1 and newBi!=-1 and newBj!=-1:
            ans = cnt
            complete = True
            break
        # 두 구슬 모두 구멍에 안 빠졌을 때
        elif newRi!=-1 and newRj!=-1 and newBi!=-1 and newBj!=-1:
            # 두 구슬의 좌표가 같다면 초기 좌표 환경 및 기울인 방향에 따라 좌표 수정
            if newRi==newBi and newRj==newBj:
                if d==0:
                    if Ri > Bi:
                        newRi -= di[d]
                    else:
                        newBi -= di[d]
                elif d==1:
                    if Rj < Bj:
                        newRj -= dj[d]
                    else:
                        newBj -= dj[d]
                elif d==2:
                    if Ri < Bi:
                        newRi -= di[d]
                    else:
                        newBi -= di[d]
                elif d==3:
                    if Rj > Bj:
                        newRj -= dj[d]
                    else:
                        newBj -= dj[d]
            # 새로운 구슬 위치라면
            if [newRi, newRj, newBi, newBj] not in visited:
                q.append([newRi, newRj, newBi, newBj, cnt+1])
                visited.append([newRi, newRj, newBi, newBj])
    # 빨간 구슬만 빠지면 break
    if complete:
        break
print(ans)