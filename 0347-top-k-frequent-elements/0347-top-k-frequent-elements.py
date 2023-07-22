'''
nums = 정수 배열
most frequent elements를 k개만큼 return
'''

'''
풀이
1. 정수 배열에 원소들이 몇개 나왔는지 세어준다
2. 많이 나온 거 순서대로 정렬한다
3. k번째까지만 반환한다
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        dict_num = defaultdict(int)
        # 기본값이 int인 딕셔너리를 만들어줘용
        for key in nums:
            dict_num[key] += 1
            # 기본값이 int인 딕셔너리에 키랑 밸류를 넣어줘용
            # 키는 nums 안에 있는 원소고
            # 밸류는 그 원소가 나올 때마다 +1씩 늘어나용
            # 그 원소 nums 배열 안에 얼마나 있나 세어주는거에용 
        # dict_num 딕셔너리가 완성됐어용
        dict_num = sorted(dict_num.items(), reverse = True, key = lambda x: x[1])
        # dict_num 키n:밸류n이 item-n으로 묶어서 정렬할건뎅
        # reverse = True 내림차순 해줘용
        # key = lambda ... lambda함수 기준으로 내림차순 하는거에용
        # lambda x: x[1]은 dict_num.items()의 원소 x.. x의 인덱스1인거 기준이에용
        mst = []
        for i in range(k):
            mst.append(dict_num[i][0])
            # 0부터 k-1번째까지 key값을 mst 배열에 추가해줘용
            # 가장 많이 있는 정수를 상위 k등까지 추리는거에용
        return mst