def solution(d, budget):
    answer = 0
    d.sort()

    sum_ = 0
    for b in d:
        if sum_ + b <= budget:
            sum_ += b
            answer += 1
        else:
            break

    return answer


d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d,budget))