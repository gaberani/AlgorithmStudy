# 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한
# 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사
# 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리
import copy
def solution(n, weak, dists):
    len_W = len(weak)
    len_D = len(dists)
    answer = len_D+1

    # 친구 순서 만들기
    friends = []
    def f(n, k):
        if n == k:
            friends.append(copy.deepcopy(dists))
        else:
            for i in range(n, k):
                dists[n], dists[i] = dists[i], dists[n]
                f(n+1, k)
                dists[n], dists[i] = dists[i], dists[n]
    f(0, len(dists))

    # 길이를 두 배로 늘림(시계, 반시계 신경 안쓰기 위해)
    for i in range(len_W):
        weak.append(weak[i] + n)

    for i in range(len_W):
        start = [weak[j] for j in range(i, i+len_W)]
        for order in friends:
            friend_idx, friend_cnt = 0, 1
            possible_length = start[0] + order[friend_idx]
            for idx in range(len_W):
                # 만약 확인할 수 있는 최대 거리를 넘으면 다음 친구 추가
                if start[idx] > possible_length:
                    friend_cnt += 1
                    if friend_cnt > len(order):
                        break
                    friend_idx += 1
                    possible_length = start[idx] + order[friend_idx]
            answer = min(answer, friend_cnt)
    if answer == len_D + 1:
        return -1
    return answer