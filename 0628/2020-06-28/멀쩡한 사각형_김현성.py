def solution(w, h):
    answer = 1
    if w == h:
        return w*h - w
    # 최대공약수
    def find(x, y):
        if x < y:
            x, y = y, x
        while y:
            x, y = y, x%y
        return

    answer = w*h - (w+h-find(w,h))
    return answer



print(solution(5, 5))
print(solution(8, 12))
print(solution(100000000, 999999999))
print(solution(2, 6))



# if w != h:
#     if w > h:
#         big, small = w, h
#     elif w < h:   # 같은 경우도 있다.
#         big, small = h, w
#     mok = big//small+1
#     cut = small*mok
#     answer = w*h - cut
# else:
#     answer = w*w - w