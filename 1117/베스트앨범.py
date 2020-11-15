# 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시

# 노래를 수록하는 기준은 다음과 같습니다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

def solution(genres, plays):
    # 노래의 장르를 나타내는 문자열 배열 genres
    # 노래별 재생 횟수를 나타내는 정수 배열 plays
    # 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
    # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
    answer = []
    genre_dict = {}
    for genre, val in zip(genres, plays):
        if genre_dict.get(genre) == None:
            genre_dict[genre] = val
        else:
            genre_dict[genre] += val
    print(genre_dict)
    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))