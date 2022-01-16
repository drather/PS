from itertools import permutations
from itertools import combinations

def check_prime(num):
    count = 0
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = []
    answer = set(answer)
    temp = (list(combinations(numbers, 2)))

    length = len(numbers)
    count = 1

    while count <= length:
        temp = list(permutations(numbers, count))
        for i in temp:
            str_num = ""
            for j in i:
                str_num += j

            print("Str_num: " , str_num)

            int_num = int(str_num)
            print("int_num: ", int_num)

            if check_prime(int_num):
                answer.add(int_num)

        count += 1

    print(answer)

    return len(answer)


numbers = "011"
print(solution(numbers))
