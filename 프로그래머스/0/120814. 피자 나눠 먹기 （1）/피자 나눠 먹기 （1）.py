def solution(n):
    answer = 0
    pizza=0
    if n % 7 ==0:
        pizza=int(n/7)
    else:
        pizza=int((n/7))+1
    return pizza