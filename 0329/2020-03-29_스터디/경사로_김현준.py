def rotate(arr):                    # 90도 회전 후 아래 이동 반복
    arr1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr1[j][N-i-1] = arr[i][j]
    return arr1

def move():
    global ans
    for i in range(N):
        cnt = 1                 # 초기값 1로 설정
        for j in range(N-1):
            if arr[i][j]==arr[i][j+1]:      # 현재 위치와 오른쪽 위치의 값이 같으면 cnt +1
                cnt += 1
            elif arr[i][j]+1==arr[i][j+1]:      # 오른쪽 위치가 1 크고, cnt가 경사로 설치 길이보다 같거나 크면 올라가는 경사로 설치 가능
                if cnt >= L:
                    cnt = 1                     # 설치 후 다시 초기값 1로 세팅
                else:
                    break
            elif arr[i][j]-1==arr[i][j+1]:      # 오른쪽 위치가 1 작고, cnt가 0보다 크면 내려가는 경사로를 설치할 수 있다
                if cnt >= 0:
                    cnt = -L+1                  # 이 때 cnt는 -L+1로 설정
                else:
                    break
            else:                               # 그 외의 경우는 경사로를 설치할 수 없기 때문에 break
                break
        else:                                   # 문제 없이 모든 위치를 탐색하고 남아있는 cnt가 0보다 같거나 크면 ans+1 (마지막에 내려가는 경사로 설치하면 cnt가 음수일 수 있으므로)
            if cnt >= 0:
                ans += 1

N, L = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(N)]
ans = 0
move()
arr=rotate(arr)
move()
print(ans)