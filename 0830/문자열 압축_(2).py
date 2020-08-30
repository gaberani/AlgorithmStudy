# 다른 사람의 풀이 최고 추천수
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cnt = 1
    for pre, now in zip(words, words[1:] + ['']):
        if pre == now:
            cnt += 1
        else:
            res.append([cur_word, cnt])
            cur_word = now
            cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])




# *** 기존 풀이 ***
def solution(s):
    # 표현한 문자열 중 가장 짧은 것의 길이 (answer)
    answer = 0
    L = len(s)
    if L == 1:
        return L
    for l in range(1, L // 2 + 1):  # 자를 단위(절반까지 가능)
        cut_answer = ''
        word = s[:l]
        cnt = 1
        for sl in range(l, L, l):  # 단위만큼만 비교
            if word == s[sl:sl + l]:
                cnt += 1
            else:
                if cnt == 1:
                    cut_answer += word
                else:
                    cut_answer += str(cnt) + word
                    cnt = 1  # cnt 초기화
                word = s[sl:sl + l]

        # 끝난 뒤 마지막 부분에 따라 추가
        if cnt == 1:
            cut_answer += word
        else:
            cut_answer += str(cnt) + word

        if answer > len(cut_answer):
            answer = len(cut_answer)
    return answer