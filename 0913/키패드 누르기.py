def solution(numbers, hand):
    answer = ''
    # x, y = 3으로 나눈 몫, 3으로 나눈 나머지
    for num in numbers:
        x, y = num//3, num%3
        if y == 1:
            pass
        elif y == 0 and num != 0:
            pass
        else:
            pass
    return answer



# def solution(numbers, hand):
#     answer = ''
#     L_posi = [1, 3]
#     R_posi = [0, 3]
#     for num in numbers: # 3의 몫은 y좌표, 나머지는 x좌표로 활용
#         if num%3 == 1:      # 왼손
#             mok = num//3
#             L_posi = [1, mok]
#             answer += 'L'
#         elif num%3 == 0 and num != 0:   # 오른손
#             mok = num//3-1
#             R_posi = [0, mok]
#             answer += 'R'
#         else:
#             # 0을 구별하기 위한 몫 설정
#             if num == 0:
#                 mok = 3
#             else:
#                 mok = num//3
#             # 왼손 오른손 중 누가 가까운지 계산 (2는 가운뎃 줄의 나머지)
#             L_hand_D = abs(L_posi[0]-2) + abs(L_posi[1]-mok)
#             if R_posi[0] == 0:
#                 R_hand_D = 1 + abs(R_posi[1]-mok)
#             else:
#                 R_hand_D = abs(R_posi[0]-2) + abs(R_posi[1]-mok)
#             # 거리 따라 어떤 손을 쓸지 결정
#             if L_hand_D < R_hand_D:
#                 answer += 'L'
#                 L_posi = [2, mok]
#             elif L_hand_D > R_hand_D:
#                 answer += 'R'
#                 R_posi = [2, mok]
#             else:
#                 if hand == 'right':
#                     answer += 'R'
#                     R_posi = [2, mok]
#                 else:
#                     answer += 'L'
#                     L_posi = [2, mok]
#         print(L_posi, R_posi)
#     return answer

#               L  R  L  L  L  R  L  L  R  R  L
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))