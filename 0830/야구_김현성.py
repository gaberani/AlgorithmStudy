import sys
input = sys.stdin.readline

N = int(input())
orderList = [list(map(int, input().split())) for _ in range(N)]

def perm(cnt):
    global result
    if cnt == 9:
        batter[0], batter[3] = batter[3], batter[0]
        result = max(result, game(batter))
        batter[0], batter[3] = batter[3], batter[0]
    else:
        # 첫 번째 제외하고 돌림
        for i in range(9):
            if i not in batter:
                batter[cnt] = i
                perm(cnt+1)
                batter[cnt] = 0

def game(order):
    global N
    ining, idx, score = 0, 0, 0
    while ining < N:
        # out, base = 0, [0]*3
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            num = orderList[ining][order[idx]]
            # 히트
            if num:
                if num == 1:
                    score += base3
                    base1, base2, base3 = 1, base1, base2
                elif num == 2:
                    score += base2 + base3
                    base1, base2, base3 = 0, 1, base1
                elif num == 3:
                    score += base1 + base2 + base3
                    base1, base2, base3 = 0, 0, 1
                elif num == 4:
                    score += (1 + base1 + base2 + base3)
                    base1, base2, base3 = 0, 0, 0
            # 아웃
            else:
                out += 1
            idx = (idx+1)%9
        ining += 1
    return score

result = 0
batter = [0] * 9
perm(1)
print(result)







def game(order):
    global N
    ining, idx, score = 0, 0, 0
    while ining < N:
        # out, base = 0, [0]*3
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            num = orderList[ining][order[idx]]
            # 히트
            if num:
                if num == 1:
                    score += base3
                    base1, base2, base3 = 1, base1, base2
                elif num == 2:
                    score += base2 + base3
                    base1, base2, base3 = 0, 1, base1
                elif num == 3:
                    score += base1 + base2 + base3
                    base1, base2, base3 = 0, 0, 1
                elif num == 4:
                    # score += 4 - base.count(0)
                    score += (1 + base1 + base2 + base3)
                    base1, base2, base3 = 0, 0, 0

                    # for i in range(3):
                    #     base[i] += num
                    #     # 홈에서 이제 출발한 경우
                    #     if base[i] == num: break
                    #     # 홈으로 돌아옴
                    #     elif base[i] > 3:
                    #         base[i] = 0
                    #         score += 1
            # 아웃
            else:
                out += 1
            idx = (idx+1)%9
        ining += 1
    return score