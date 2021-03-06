# n명의 권투선수가 권투 대회 각각 1번부터 n번까지 번호를 받았습니다.
# 만약 A 선수가 B 선수보다 실력이 좋다면 A는 B를 항상 이깁니다. => 실력순이다.
# 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다.

# 선수의 수 n
# 경기 결과를 담은 2차원 배열 results
# 정확하게 순위를 매길 수 있는 선수의 수를 return
def solution(n, results):
    answer = 0
    winners = {i:set() for i in range(1, n+1)}
    losers = {i:set() for i in range(1, n+1)}

    for r1, r2 in results:
        winners[r1].add(r2)
        losers[r2].add(r1)
    # print(winners)
    # print(losers)
    # print('----------')
    for i in range(1, n+1):
        # i에게 진 사람들은 i를 이긴 사람에게 짐
        for loser in winners[i]:
            losers[loser].update(losers[i])
        # i를 이긴 사람들은 i에게 진 사람도 이김
        for winner in losers[i]:
            winners[winner].update(winners[i])

    # print(winners)
    # print(losers)
    for i in range(1, n+1):
        if len(winners[i]) + len(losers[i]) == n-1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))