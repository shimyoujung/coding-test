def solution(n):
    answer = 0
    pizza=1
    while True:
        if (n*pizza)%6 == 0:
            answer=(n*pizza)/6
            return answer
        else:
            pizza+=1