### 문제 요약
- 장르 별로 가장 많이 재생된 두 곡씩 베스트 앨범을 낸다.
- 노래에는 각자의 고유 번호가 있으므로 중복되지 않는다.
<br>

### 문제 해석
1. 장르 : {고유번호 - 고유번호}
2. 각 장르 별          : 총 재생 횟수를 계산해 내림차 정렬한다.
3. 각 장르 내          : 정렬 규칙 1. 재생 횟수 많은 노래 2. 고유 번호
<br>

<hr>

### 첫 번째 풀이 - 실패

```
from collections import defaultdict
```
> 기본 값을 지정할 수 있는 `defaultdict()`를 사용하기 위해 호출했다.
<br>

##### 1. 딕셔너리 = {장르: {재생횟수: 고유번호}, 장르: {재생횟수: 고유번호}}
```
def solution(genres, plays):
    zipping = [[genres[i], plays[i], i] for i in range(len(genres))]
    hashbrown = defaultdict(dict)

    for x in zipping:
        genre, play_count, id = x[0], x[1], x[2]
        hashbrown[genre][play_count] = id
```
> zipping 리스트를 만들어 장르, 재생횟수, 고유번호를 하나의 리스트로 2차원 리스트를 만든 후<br>
> 딕셔너리에 key와 value를 넣어주려는 for문<br>
> key는 장르이고, 장르 key의 values는 또다른 딕셔너리로 {재생횟수: 고유번호}가 들어간다.<br><br>
> *Output:*<br>
> `defaultdict(<class 'dict'>, {'classic': {500: 0, 150: 2, 800: 3}, 'pop': {600: 1, 2500: 4}})`
<br>

##### 2. 각 장르의 총 재생 횟수 기준으로 장르 정렬
```
    salthashbrown = dict(sorted(hashbrown.items(), key=lambda item: -sum(item[1].keys())))
```
> *Output:*<br>
> `{'pop': {600: 1, 2500: 4}, 'classic': {500: 0, 150: 2, 800: 3}}`
<br>

##### 3. 장르 내에서 재생 횟수 기준으로 내림차 정렬 
```
    for genre in salthashbrown:
        salthashbrown[genre] = sorted(salthashbrown[genre].items(), key=lambda item: -item[0])
```
> 여기까지 하고 나니 의문.. 나는 왜 정렬을 이렇게나 열심히 하고 있을까? 아직 문제 해결을 위한 단계 근처에도 안갔는데..<br>
> 어떤 장르가 총 재생횟수가 많은지 찾으면 일단 첫 번째 관문은 끝난거 아닌가?  <br>
> *Output:*<br>
> `{'pop': [(2500, 4), (600, 1)], 'classic': [(800, 3), (500, 0), (150, 2)]}`
<br>

##### 4. 상위 2곡 인덱스 추출
```
    for genre in salthashbrown:
        temp = sorted(salthashbrown[genre].items(), key=lambda item: -item[0])
        print(temp)
        answer = []
        cnt = 0
        for song in temp:
            cnt += 1
            if cnt > 2:
                break
            else:
                answer.append(song[1])
                print(answer)
```
> 이렇게 하면 각 장르마다 인덱스를 뽑고 다음 장르 상위 2 곡 뽑으려고 할 때 이전 결과가 리셋된다. <br><br>
```
  여기서부터는 갈 길을 잃었다. 정말 길을 너무 심하게 잃어서 처음에 어떤 코드로 계속 실패해댔는지도 모르겠다.
  어딘가에서 뭔가에 꽂혀버린 것 같은데 다시 시작해보자..!
```
<br>

<hr>

### 두 번째 풀이 - 성공

##### 1. 딕셔너리 = {장르: [(재생횟수, 고유번호), (재생횟수, 고유번호), ...]}
```
from collections import defaultdict

def solution(genres, plays):
    zipping = [[genres[i], plays[i], i] for i in range(len(genres))]
    hashbrown = defaultdict(list)  # 리스트를 값으로 가지는 defaultdict 생성

    for x in zipping:
        genre, play_count, unique_id = x[0], x[1], x[2]
        hashbrown[genre].append((play_count, unique_id))
```
> 첫 번째 풀이와 다른 점은 리스트를 기본값으로 갖는 딕셔너리를 만들어서 `.append(재생횟수, 고유번호)` <br>
> 딕셔너리 = {장르: [(재생횟수, 고유번호), (재생횟수, 고유번호), ...]}<br>
> *Output:* <br>
> `defaultdict(<class 'list'>, {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]})`
<br>

##### 2. 총 재생 횟수 기준 장르 정렬
```
    sorted_genres = sorted(hashbrown.keys(),
                           key=lambda genre: sum(play_count for play_count, _ in hashbrown[genre]), reverse=True)
```
> 어떤 장르가 총 재생횟수가 많은지 알면 되니까 여기서는 총 재생횟수가 많은 장르 순서대로 장르를 정렬한 리스트를 반환했다. <br>
>> `sorted(hashbrown.keys(), ...)` : hashbrown 딕셔너리의 key값을 사용해서 정렬할 건데 <br>
>> `key = lambda genre:`           : 장르를 정렬하기 위한 lambda 함수를 적용할 거고<br>
>> `sum(play_count for play_count, _ in hashbrown[genre])`    : 장르는 딕셔너리의 각 장르 내에 재생횟수들을 합산한 값으로 정렬할 것<br>
>> `reverse = True`                : 내림차순 <br>
<br>

##### 3. 상위 2곡씩 인덱스 추출
```
    answer = []
    for genre in sorted_genres:
        top_2_songs = [unique_id for _, unique_id in sorted(hashbrown[genre], key=lambda x: (-x[0], x[1]))[:2]]
        answer.extend(top_2_songs)

    return answer

# 예시 테스트
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
```
> `sorted_genres`  : <br>
> `top2`           : <br>
> `sorted(hashbrown[genre], key=lambda x: (-x[0], x[1])) [:2]`  : 장르의 원소 첫번째값(재생횟수)은 내림차순 -x[0], 두번째값(고유번호)은 오름차순 x[1]해서 정렬하고, 두번째 원소까지만 슬라이싱 [:2] <br>
> 원소의 두번째 값인 unique_id를 top_2_songs로 정의한다.<br>
>> 이때 top_2_songs에는 하나의 장르에 해당하는 노래의 고유번호가 담긴다.<br>
>> `.extend(top_2_songs)` 를 이용해 추출한 인덱스를 추가해준다.<br>
<br>
<hr>

### 세 번째 풀이 - 성공
```
'''
1. 재생횟수 많은 장르 찾기
2. 장르 내 재생횟수 많은 노래 찾기
'''
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

```
<br>
<hr>

### 네 번째 풀이 - 성공
```
def solution(genres, plays):
    answer = []

    songs = {}
    for i in range(len(genres)):
        if genres[i] in songs:
            songs[genres[i]][i] = plays[i]
        else:
            songs[genres[i]] = {i: plays[i]}
    print(songs)
    total_play = {}
    for key in songs.keys():
        total_play[key] = sum(songs[key].values())
    total_play = sorted(total_play.items(), key=lambda x: x[1], reverse=True)
    print(total_play)
    for i in total_play:
        temp = sorted(songs[i[0]].items(), key=lambda x: x[1], reverse=True)
        print(temp)
        answer.append(temp[0][0])
        if len(temp) != 1:
            answer.append(temp[1][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500,600,150,800,2500]))
```
