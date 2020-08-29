def check(ans):
    for x, y, frame in ans:
        # 기둥
        if frame == 0:
            # 바닥 위 / 보의 한쪽 끝 부분 위 /다른 기둥 위
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            else:
                return False
        # 보
        elif frame == 1:
            # 한쪽 끝 부분이 기둥 위 / 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for info in build_frame:
        x, y, frame, work = info
        # 설치
        if work == 1:
            # 미리 설치하고 체크하러 가기
            answer.append([x, y, frame])
            if check(answer) == False:
                answer.remove([x, y, frame])
        # 삭제
        else:
            # 미리 제거하고 체크하러 가기
            answer.remove([x, y, frame])
            if check(answer) == False:
                answer.append([x, y, frame])

    answer.sort()
    return answer