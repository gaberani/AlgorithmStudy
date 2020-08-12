# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = list(range(1, N+1))

def team():
    global minV
    # 1. 팀 나누기
    all_lst = comb(members, N//2)
    L = len(all_lst)
    for idx in range(L//2):
        team1 ,team2 = all_lst[idx], all_lst[-idx-1]
        one, two = 0, 0
        # 2. 점수더하기
        for i1 in range(N//2-1):
            for i2 in range(i1, N//2):
                one += S[team1[i1]-1][team1[i2]-1] + S[team1[i2]-1][team1[i1]-1]
                two += S[team2[i1]-1][team2[i2]-1] + S[team2[i2]-1][team2[i1]-1]

        # 3. 차이의 최솟값 구하기
        minV = min(minV, abs(one-two))
    return minV

# 리스트에서 n개 뽑는 모든 조합 짜기
def comb(lst, n):
    comb_lst = []
    if n > len(lst):
        return comb_lst
    else:
        if n == 1:
            for i in lst:
                comb_lst.append([i])
        elif n > 1:
            for i in range(len(lst)-n+1):
                for temp in comb(lst[i+1:], n - 1):
                    comb_lst.append([lst[i]]+temp)
        return comb_lst


minV = 2**63-1
print(team())