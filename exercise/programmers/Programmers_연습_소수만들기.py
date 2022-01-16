def check_prime(n):
    res = 0
    for i in range(2, n+1):
        if n % i == 0:
            res += 1

    if res == 2:
        return True
    else:
        return False


def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                if check_prime(temp):
                    answer += 1

    print("answer: ", answer)
    return answer

nums = [1,2,7,6,4]
print(solution(nums))