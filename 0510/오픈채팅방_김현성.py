def solution(record):
    answer = []
    user_name = dict()
    chat = []
    for r in record:
        info = r.split()        # cmd, id, name
        if info[0] == 'Enter':
            user_name[info[1]] = info[2]
            chat.append(["{0}님이 들어왔습니다.", info[1]])
        elif info[0] == 'Leave':
            chat.append(["{0}님이 나갔습니다.", info[1]])
        elif info[0] == 'Change':
            user_name[info[1]] = info[2]
    for c in chat:
        answer.append(c[0].format(user_name[c[1]]))
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	))

# 시간 초과
# def solution(record):
#     answer = []
#     chat_record = []
#     for r in record:
#         if r[0] == 'L':
#             id = r[6:]
#             # id만 써져있으므로 name 찾기
#             for chat in chat_record:
#                 if chat[0] == id:
#                     name = chat[1]
#             chat_record.append([id, name])
#         else:
#             cmd, id, name = r.split()
#             if cmd[0] == 'E':
#                 # 전에 들어왔던 아이디면 그 전 이름 바꿈
#                 for chat in chat_record:
#                     if chat[0] == id:
#                         chat[1] = name
#                 # 처음 들어온 아이디면 붙임
#                 else:
#                     chat_record.append([id, name])
#             elif cmd[0] == 'C':     # 기록에서 id 겹치면 name 바꿈
#                 for chat in chat_record:
#                     if chat[0] == id:
#                         chat[1] = name
#     idx = 0
#     for r in record:
#         if r[0] != 'C':
#             id = chat_record[idx][1]
#             if r[0] == 'E':
#                 answer.append(''.join(id+"님이 들어왔습니다."))
#             elif r[0] == 'L':
#                 answer.append(''.join(id+"님이 나갔습니다."))
#             idx += 1
#     return answer