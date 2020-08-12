import sys
input = sys.stdin.readline

def check(tmp):
    global ans
    used = [0] * N
    pivot = tmp[0]
    flag = 0
    cnt = 1
    while cnt < N:
        if pivot == tmp[cnt]:
            cnt += 1
        elif pivot-1 == tmp[cnt] and cnt+L <= N:
            pivot = tmp[cnt]
            for j in range(L):
                used[cnt+j] = 1
                if pivot != tmp[cnt + j]:
                    flag = 1
                    break
            if flag:
                break
            cnt += L
        elif pivot+1 == tmp[cnt] and cnt-L >= 0:
            for j in range(L):
                if pivot != tmp[cnt-j-1] or used[cnt-j-1] == 1:
                    flag = 1
                    break
            if flag:
                break
            pivot = tmp[cnt]
            if cnt == N-1:
                cnt += 1
        else:
            break
        if flag:
            break
    if cnt == N:
        ans += 1

N, L = map(int, input().split())
ramp = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ctmp = []
    tmp = ramp[i]
    check(tmp)
    for j in range(N):
        ctmp.append(ramp[j][i])
    check(ctmp)
print(ans)





import sys;input=sys.stdin.readline
def slope(x,chk):
    global ans
    cnt=1
    for y in range(n-1):
        dir=Map[x][y+1]-Map[x][y] if chk else Map[y+1][x]-Map[y][x]
        if dir==0:
            cnt+=1
        elif dir==1 and cnt>=l:cnt=1
        elif dir==-1 and cnt>=0:cnt=1-l
        else:return
    if cnt>=0:ans+=1

n,l=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    slope(i,1)
    slope(i,0)
print(ans)