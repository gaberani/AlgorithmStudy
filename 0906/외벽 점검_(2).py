# 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한
# 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사
# 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리
import copy
def solution(n, weak, dists):
    len_W = len(weak)
    len_D = len(dists)
    answer = len_D + 1

    # 순열
    friends = []
    def f(n, k):
        if n == k:
            friends.append(copy.deepcopy(dists))
        else:
            for i in range(n, k):
                dists[n], dists[i] = dists[i], dists[n]
                f(n + 1, k)
                dists[n], dists[i] = dists[i], dists[n]
    f(0, len(dists))

    # 길이를 두 배로 늘림(시계, 반시계 신경 안쓰기 위해)
    for i in range(len_W):
        weak.append(weak[i] + n)