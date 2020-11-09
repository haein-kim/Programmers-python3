# 내가 처음 시도한 답
def solution(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)

# 스터디원 코드
def solution(arr):
	return sum(arr)/len(arr)