import math


def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1 ):
        if n % i == 0:
            return False
    return True

# 오답
def solution1(n):
    answer = 0

    for i in range(2, n+1):
        if check_prime(i):
            print("i: ", i)
            answer += 1

    return answer

# 정답
def solution(n):
    arr = [0] * (n+1)
    arr[0] = -1
    arr[1] = -1

    print("arr: ", arr)
    for i in range(len(arr)):
        print("\ni: ", i)
        if arr[i] < 0:
            continue
        else:
            if check_prime(i):
                arr[i] = 1
                j = i
                temp = j * 2
                print("처음 temp: ", temp)
                while temp <= n:
                    print("temp: ", temp)
                    arr[temp] = -1
                    temp = temp + j

                print("arr: ", arr)

    answer = arr.count(1)
    return answer


n = 10
print(solution(n))

