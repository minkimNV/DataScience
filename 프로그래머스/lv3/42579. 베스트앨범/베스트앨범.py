from collections import defaultdict

def solution(genres, plays):
    zipping = [[genres[i], plays[i], i] for i in range(len(genres))]
    hashbrown = defaultdict(list)  # 리스트를 값으로 가지는 defaultdict 생성

    # 딕셔너리 = {장르: [(재생횟수, 고유번호), (재생횟수, 고유번호), ...]}
    for x in zipping:
        genre, play, id = x[0], x[1], x[2]
        hashbrown[genre].append((play, id))

    # 총 재생 횟수 기준 장르 정렬
    sorted_genres = sorted(hashbrown.keys(),
                           key=lambda genre: sum(play for play, _ in hashbrown[genre]), reverse=True)
    
    # 장르 내에서 상위 2곡의 인덱스 추출
    answer = []
    for genre in sorted_genres:
        top2 = [id for _, id in sorted(hashbrown[genre], key=lambda x: (-x[0], x[1]))[:2]]
        answer.extend(top2)

    return answer

# 예시 테스트
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))



def solution(genres, plays):

    songs = [[genre, (play, i)] for genre, (play, i) in zip(genres, enumerate(plays))]
    songs = sorted(songs, key = lambda x: (x[0], -x[1][1], x[1][0]))


    # 재생횟수 많은 장르 찾기
    gorder = {}
    for i in range(len(songs)):
        if songs[i][0] not in gorder:
            gorder[songs[i][0]] = songs[i][1][1]
        else:
            gorder[songs[i][0]] += songs[i][1][1]

    sortedgorder = sorted(gorder.items(), key=lambda x: -x[1])

    # 상위 2 곡 인덱스
    answer = []
    cnt = 0
    for genre in sortedgorder:
        cnt = 0
        for song in songs:
            if genre[0] == song[0]:
                cnt += 1
                if cnt > 2 :
                    break
                else:
                    answer.append(song[1][0])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

