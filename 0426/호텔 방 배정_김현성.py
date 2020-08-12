def solution(k, room_number):
    answer = []
    rooms = {}      # key: 배정받은 room 번호, value: key와 같은 room을 원할 때 다음 room 번호
    def addroom(room):
        if room in rooms:   # 이미 배정이 되어 있으면
            i = rooms[room]
            while i in rooms:   # 다음 배정 가능 방 찾기
                i = rooms[i]
            rooms[i] = i+1  # 배정가능방에 배정하고, 다음 배정방 저장
            j = i+1
            i = room    # 다시 처음으로 돌아가서
            while rooms[i]!=j:  # 지나온 방들마다 다음 배정방 바꿔주기
                k = rooms[i]
                rooms[i] = j
                i = k
        else:
            rooms[room] = room+1    # 배정이 안되어 있으면 배정
        print(rooms)
    for i in room_number:
        addroom(i)
    for key in rooms.keys():    # 딕셔너리 순서대로 key값 받기
        answer.append(key)
    return answer

print(solution(10, [1,3,4,1,3,1]))







# 딕셔너리로 해보기
# def solution(k, room_number):
#     answer = ''
#     room = list(range(1, k+1))
#     for guest in room_number:   # guest 오는 순서대로 처리
#         tmp = guest-1
#         while room[tmp] == 0:
#             tmp += 1
#         answer += str(tmp+1)
#         room[tmp] = 0
#     answer = list(map(int, answer))
#     return answer
#


'''
def solution(k, room_number):
    answer = []
    room = list(range(1, k+1))
    for guest in room_number:   # guest 오는 순서대로 처리
        tmp = guest-1
        while room[tmp] == 0:
            tmp += 1
        answer.append(tmp+1)
        room[tmp] = 0
    return answer
'''