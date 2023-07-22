from collections import defaultdict

def solution(genres, plays):
    zipping = [[genres[i], plays[i], i] for i in range(len(genres))]
    hashbrown = defaultdict(list)  # 리스트를 값으로 가지는 defaultdict 생성

    # 딕셔너리 = {장르: [(재생횟수, 고유번호), (재생횟수, 고유번호), ...]}
    for x in zipping:
        genre, play_count, unique_id = x[0], x[1], x[2]
        hashbrown[genre].append((play_count, unique_id))
    # print(hashbrown)
    # 총 재생 횟수 기준 장르 정렬
    sorted_genres = sorted(hashbrown.keys(),
                           key=lambda genre: sum(play_count
                                                 for play_count, _ in hashbrown[genre]),
                           reverse=True)
    # print(sorted_genres)
    
    # 장르 내에서 상위 2곡의 인덱스 추출
    answer = []
    for genre in sorted_genres:
        # print(genre)
        top_2_songs = [unique_id for _, unique_id
                       in sorted(hashbrown[genre],
                                 key=lambda x: (-x[0], x[1]))[:2]]
        # print(top_2_songs)
        answer.extend(top_2_songs)

    return answer

# 예시 테스트
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
