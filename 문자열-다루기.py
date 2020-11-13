def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False

# 람다에 꽂힌 요즘
solution = lambda num : True if (len(num) == 4 or len(num) == 6) and num.isdigit() else False

# 다른 사람 풀이 보고 감동 받아서 조합해본 답
def solution(num):
    return num.isdigit() and len(num) in (4,6)