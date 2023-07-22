### 유사 딕셔너리 `defaultdict()`

`from collections import defaultdict` <br>
- 모듈을 먼저 import 해주어야 사용할 수 있다.
- 인자로 주어진 객체의 기본값을 딕셔너리 초기값으로 지정할 수 있다.
- defaultdict의 매개변수로는 int, list, set 등으로 초기화할 수 있다.
<br>
`test_dict = defaultdict(int)`<br>
>> 디폴트 값이 int인 딕셔너리를 생성했다.<br>
<br>
`test_dict = defaultdict(lambda: defaultdict(int))`<br>
>> 디폴트 값이 int인 딕셔너리를 기본값으로 하는 딕셔너리를 생성했다.<br>
>>>> defaultdict( ~ : 기본값이 괄호 안의 것인 딕셔너리를 생성하는데<br>
>>>> lambda:defaultdict(int) : 그 딕셔너리의 원소/item은 기본값을 int로 하는 딕셔너리다.<br>
<br>
- key 값만 입력하고 value 입력하지 않으면 초기값인 0이 저장된다.
- value 값을 지정하면 지정한 값이 저장된다.
<br>
- defaultdict()를 이용해 특정 key에 대한 카운팅을 할 수 있다.
<br>​
