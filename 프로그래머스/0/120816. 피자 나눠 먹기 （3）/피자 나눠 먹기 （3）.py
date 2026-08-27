def solution(slice, n):
    answer=0
    pizza=1
    while slice < n:
            pizza+=1
            n=n-slice
    return pizza