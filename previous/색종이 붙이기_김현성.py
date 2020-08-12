import pprint

def attach(n):
    global result
    pn = 0
    for i in range(10):
        for j in range(10):
            # if paper[i][j] == 1 and visit[i][j] == 0:
            if paper[i][j]:
                cnt = 1
                ni, nj = i, j
                for a in range(n-1):      # 색종이 크기만큼 반복해서 확인
                    ni += 1
                    nj += 1
                    if 0 <= ni <= 9 and 0 <= nj <= 9:
                        if paper[ni][j] == 1 and paper[i][nj] == 1:
                            cnt += 1        # 색종이 범위 안이면 cnt+=1
                        else:
                            break           # 중간에 색종이 크기 벗어나면 빠져나옴
                if cnt == n:            # 색종이 크기만큼 붙일 수 있으면
                    result += 1         # 색종이 붙였으니깐 result+1
                    pn += 1
                    if pn > 5:
                        result = -1
                        break
                    for pi in range(i, i+n):
                        for pj in range(j, j+n):
                            # visit[pi][pj] = 1       # 방문 표시
                            paper[pi][pj] = 0

paper = [list(map(int, input().split())) for _ in range(10)]
# visit = [[0]*10 for _ in range(10)]
result = 0
for n in range(5, 0, -1):  # 5~1
    attach(n)
    pprint.pprint(paper)
    if result == -1:
        break
print(result)
# pprint.pprint(visit)