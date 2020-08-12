import sys
n, L = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    length, flag, j = 1, 0, -1
    while 1:
        j += 1
        if j == n-1:
            cnt += 1; break
        elif abs(arr[i][j] - arr[i][j+1]) > 1: break # 높이차이가 1보다 커지는 것 제외
        elif arr[i][j] - arr[i][j+1] == 1: # 높이가 작아질 때, 
            if j + L < n: # 경사로를 놓았을 때, 범위를 넘어가는지 검사
                for k in range(1, L): # 경사로를 놓았을 때, 경사로가 놓아지는 위치들의 높이가 모두 동일한지 검사
                    if arr[i][j+1] != arr[i][j+1+k]:
                        flag = 1
                        break
                else:
                    j += L - 1 # 경사로가 놓아질 수 있으면, 검사 시작 위치를 변경
                    length = 0
                if flag: break
            else: break
        elif arr[i][j] - arr[i][j+1] == -1: # 높이가 커졌을 때,
            if length >= L: length = 1 # 뒤의 길이가 경사로의 길이보다 크거나 같은지 검사
            else: break # 크면 넘어가고, 작으면 제외
        else: # 높이가 같으면, 경사로가 높아질 때 필요한 이전 길이를 갱신
            length += 1

    length, flag, j = 1, 0, -1
    while 1:
        j += 1
        if j == n - 1:
            cnt += 1;
            break
        elif abs(arr[j][i] - arr[j+1][i]) > 1:
            break
        elif arr[j][i] - arr[j+1][i] == 1:
            if j + L < n:
                for k in range(1, L):
                    if arr[j+1][i] != arr[j+1+k][i]:
                        flag = 1
                        break
                else:
                    j += L - 1
                    length = 0
                if flag: break
            else:
                break
        elif arr[j][i] - arr[j+1][i] == -1:
            if length >= L:
                length = 1
            else:
                break
        else:
            length += 1
print(cnt)