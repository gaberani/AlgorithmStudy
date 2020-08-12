def start(arr):
    global result
    visit = [[0] * N for _ in range(N)]
    for i in range(N):  # 각 줄을 체크(N번)
        idx = 0
        flag = 0
        while idx < N - 1:
            diff = arr[i][idx] - arr[i][idx+1]
            if diff == 0:       # 같은높이
                idx += 1
            elif diff == 1:     # 내리막길
                if idx+L < N-1:
                    cnt = 0
                    for a in range(idx+1, idx+1+L):
                        if arr[i][a] == arr[i][idx+1]:
                            cnt += 1
                            visit[i][a] = 1
                        else:
                            break
                    if cnt == L:
                        idx += L
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            elif diff == -1:    # 오르막길
                cnt = 0
                for b in range(idx+1-L, idx+1):
                    if arr[i][b] == arr[i][idx] and visit[i][b] == 0:
                        cnt += 1
                        visit[i][b] = 1
                    else:
                        break
                if cnt == L:
                    idx += 1
                else:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if not flag:
            # print(arr[i])
            result += 1

N, L= map(int,input().split())
road = [list(map(int, input().split())) for _ in range(N)]

result = 0
road2 = [[] for _ in range(N)]
for i in range(N):
    for idx in range(N):
        road2[i].append(road[idx][i])
start(road)
start(road2)

print(result)