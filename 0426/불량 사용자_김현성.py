# 이벤트 응모자 아이디 목록이 담긴 배열 user_id
# 불량 사용자 아이디 목록이 담긴 배열   banned_id
import re
from copy import deepcopy
# user_id는 중복이 없다.
# banned_lst는 중복이 가능하다.
answer = []
def check(idx, gyp_id, arr, length):
    global answer
    if idx == len(gyp_id):
        if len(arr) == length and arr not in answer:
            answer.append(deepcopy(arr))
        return

    for one_ban_id in gyp_id[idx]:
        if one_ban_id not in arr:
            arr.add(one_ban_id)
            check(idx+1, gyp_id, arr, length)
            arr.remove(one_ban_id)

def solution(user_id, banned_lst):
    global answer
    answer = []
    # ban_id_lst = []
    # ban_id_num = []
    gyp_id = []
    for ban_id in banned_lst:
        # if ban_id not in ban_id_lst:
        #     ban_id_lst.append(ban_id)
        #     ban_id_num.append(1)
        # else:
        #     ban_id_num[ban_id_lst.index(ban_id)] += 1
        ban_id = '^'+ban_id+'$'                   # 끝내는 표시 추가
        b = re.sub('\\*', '.', ban_id)  # *를 .으로 변환
        bc = re.compile(b)              # compile 선언
        tmp_lst = []
        for id in user_id:
            u = bc.search(id)           # ban 목록 아이디랑 user_id 겹치는지 체크
            if u:                       # 겹쳐서 u가 생기면
                tmp_lst.append(id)
        gyp_id.append(tmp_lst)
    check(0, gyp_id, set(), len(banned_lst))
    print(answer)
    return len(answer)

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "frodoc"], ["fr*d*"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))