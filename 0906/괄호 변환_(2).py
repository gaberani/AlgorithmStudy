



































# 기존 정답 코드
# # '(' 의 개수와 ')' 의 개수가 같다, 균형잡힌 괄호 문자열
# # '('와 ')'의 괄호의 짝도 모두 맞을 경우, 올바른 괄호 문자열
# import sys
# sys.setrecursionlimit(10000)
#
# def solution(p):
#     answer = ''
#     # 괄호 방향 뒤집는 함수
#     def change(word):
#         change_word = ''
#         for w in word:
#             change_word += ')' if w == '(' else '('
#         return change_word
#     # 올바른 괄호인지 검사하는 함수
#     def right(word):
#         if len(word) == 0: return 0
#         left, right = 0, 0
#         for i in word:
#             if i == '(':
#                 left += 1
#             elif i == ')':
#                 right += 1
#             if right >= left:
#                 break
#         return 1 if left+right == len(word) else 0
#     # 주어진 규칙(3, 4)대로 검사하는 함수
#     def go(u, v):
#         if right(u):            # 조건 3, u가 올바른 괄호 문자열이면
#             u += solution(v)    # 조건 3-1, 결과를 u에 붙인 후
#             return u            # 조건 3-1, 반환
#         else:                           # 조건 4, u가 올바른 괄호 문자열아니면
#             a = '('                     # 조건 4-1, 빈 문자열에 (
#             a += solution(v)            # 조건 4-2, v에 1단계부터 재귀적으로 수행한 결과 붙임
#             a += ')'                    # 조건 4-3, )를 다시 붙임
#             a += change(u[1:len(u)-1])  # 조건 4-4, u의 첫번째와 마지막 문자 제거, 뒤집어서 붙임
#             return a                    # 조건 4-5, 반환
#     # 균형잡힌 괄호인지 확인
#     def balance(word):
#         cnt = 0
#         idx = 0
#         while 1:
#             if word[idx] == ')':
#                 cnt -= 1
#             else:
#                 cnt += 1
#             if cnt == 0:
#                 return idx
#             idx += 1
#
#     L = len(p)
#     if L == 0:  # 조건 1
#         return answer
#     # 조건 2
#     if right(p):
#         return p
#     else:
#         idx = balance(p)
#
#         if idx == L-1:  # 끝까지 가야 right면
#             # print('end')
#             answer = go(p, '')
#         else:           # 중간에 나눌 수 있으면
#             # print('middle')
#             print(p[:idx+1], p[idx+1:])
#             answer = go(p[:idx+1], p[idx+1:])
#
#
#     # lg, rg = '', ''
#     # left, right = 0, 0
#     # while 1:
#     return answer
#
# # print(solution("(()())()"))
# # print(solution(")("))
# print(solution("()))((()"))
# # print(solution("))((()"))