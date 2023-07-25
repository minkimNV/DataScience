def solution(nums):
    answer = 0
    setnum = set(nums)
    print(setnum)
    if len(nums)/2 < len(setnum):
        return len(nums)/2
    return len(setnum)