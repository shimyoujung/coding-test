def solution(array):
    count = [0] * 1000

    for num in array:
        count[num] += 1

    max_count = max(count)

    answer = -1
    same_count = 0

    for i in range(1000):
        if count[i] == max_count:
            answer = i
            same_count += 1

    if same_count > 1:
        return -1

    return answer