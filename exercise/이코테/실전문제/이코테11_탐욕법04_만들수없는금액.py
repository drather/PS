"""
문제
동네 편의점의 주인인 velmash는 N개의 동전을 가지고 있습니다.
이때 N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.

입력조건
첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어집니다. (1 <= N <= 1,000)
둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며,
각 자연수는 공백으로 구분합니다. 이때, 각 화폐 단위는 1,000,000 이하의 자연수 입니다.

출력조건
첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력합니다.
"""
coin_cnt = int(input())
coin_values = list(map(int, input().split()))

# coin_cnt = 7
# coin_values = [3, 1, 6, 2, 7, 30, 1]


if __name__ == '__main__':
    coin_values.sort()

    coin_sum = 0

    for cv in coin_values:
        if cv - coin_sum > 1:
            break
        else:
            coin_sum += cv

    # for cv in coin_values:
    #     if coin_sum + 1 >= cv:
    #         coin_sum += cv
    #     else:
    #         break

    print(coin_sum + 1)

# if __name__ == '__main__':
#     coin_values.sort()
#
#     possible_values = set()
#     answer = 0
#
#     for i in range(len(coin_values)):
#         if possible_values and coin_values[i] - prev_max > 1:
#             answer = max(possible_values) + 1
#             break
#
#         possible_values.add(coin_values[i])
#
#         if i == 0:
#             continue
#
#         temp = [pv + coin_values[i] for pv in possible_values]
#         prev_max = temp[-1]
#         possible_values.update(temp)
#
#     print(answer)
