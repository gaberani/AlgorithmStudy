
# 출발지점부터 도착지점까지의 거리 distance,
# 바위들이 있는 위치를 담은 배열 rocks,
# 제거할 바위의 수 n
def solution(distance, rocks, n):
    # 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return
    answer = 0
    # 거리를 기준으로 이분탐색
    left, right = 1, distance
    # 거리순으로 정렬
    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        pre_rock = 0
        num_rock = 0
        m_min = 1000000001
        for rock in rocks:
            if rock - pre_rock < mid:
                num_rock += 1
            else:
                # 최소거리
                m_min = min(m_min, rock - pre_rock)
                pre_rock = rock

        if num_rock > n:
            right = mid - 1
        else:
            answer = m_min
            left = mid + 1

    return answer