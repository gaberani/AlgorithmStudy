def solution(words):
    return



# def solution(words):
#     words.sort() # 학습된 단어이므로 정렬해도 무방
#     n, answer = len(words), 0
#     arr = [0]*n
#     for i in range(n-1):
#         cnt1, cnt2 = find(words[i], words[i+1])
#         arr[i], arr[i+1] = max(arr[i], cnt1), max(arr[i+1], cnt2)
#     return sum(arr)
#
# def find(s1, s2): # 두 개의 글자를 비교하는 함수
#     cnt, i = 0, 0
#     while 1:
#         cnt += 1
#         if i == s1.__len__(): return cnt-1, cnt # 한 쪽 길이가 짧고, 그때까지 단어가 모두 같을 때
#         elif i == s2.__len__(): return cnt, cnt-1
#         else:
#             if s1[i] != s2[i]: return cnt, cnt # 다른 문자를 가질 때
#         i += 1