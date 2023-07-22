### 유사 딕셔너리 `defaultdict()`

`from collections import defaultdict` <br>
- 모듈을 먼저 import 해주어야 사용할 수 있다.
- 인자로 주어진 객체의 기본값을 딕셔너리 초기값으로 지정할 수 있다.
- defaultdict의 매개변수로는 int, list, set 등으로 초기화할 수 있다.
- key 값만 입력하고 value 입력하지 않으면 초기값인 0이 저장된다.
- value 값을 지정하면 지정한 값이 저장된다.
- defaultdict()를 이용해 특정 key에 대한 카운팅을 할 수 있다.
<br>

`test_dict = defaultdict(int)` <br>
> 디폴트 값이 int인 딕셔너리를 생성했다.<br>

`test_dict = defaultdict(lambda: defaultdict(int))`

> 디폴트 값이 int인 딕셔너리를 기본값으로 하는 딕셔너리를 생성했다.<br>
>> defaultdict( ... )         : 기본값이 괄호 안의 것인 딕셔너리를 생성하는데<br>
>> lambda:defaultdict(int)    : 그 딕셔너리의 원소/item은 기본값을 int로 하는 딕셔너리다.



<br><br>

### 해쉬 `hash`
나는 이 문제를 풀려고 defaultdict를 사용해 빈 딕셔너리를 만들어주고 각 원소가 몇 개가 있는지 카운팅을 해줬는데 이 문제를 hash로 풀 수도 있다. <br>
hash로 풀 때도 비슷하긴 했는데 hash의 경우에는 *'만약 해쉬딕셔너리에 이 원소가 없다면 어떻게 추가하겠다.'* 라는 조건(?)이 필요했다.<br>
왜 필요했는지 알고 싶은데 검색해도 안나옴 헤헤<br>
일단 해쉬 사용한 코드부터 냅다 뿌리기 

```
def topKFrequent(nums, k):
    hashbrown = {}

    for key in nums:
        if key not in hashbrown:
            hashbrown[key] = 1
        else:
            hashbrown[key] += 1

    salthashbrown = sorted(hashbrown.items(), key = lambda x: -x[1])

    mst = []
    for i in range(k):
        mst.append(salthashbrown[i][0])

    return mst
```
