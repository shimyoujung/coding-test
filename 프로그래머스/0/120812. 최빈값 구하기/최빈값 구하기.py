def solution(array):
    scores = [0] * 1001
    
    for i in range(0, len(array)):
        scores[array[i]] = scores[array[i]] + 1
        
    max = scores[0]
    mode = 0
    
    if len(array) == 1:
        return array[0]
    
    for i in range(1, len(scores)):
        if scores[i] > max:
            max = scores[i]
            mode = i
            
        elif scores[i] == max:
            mode = -1
            
            
    return mode