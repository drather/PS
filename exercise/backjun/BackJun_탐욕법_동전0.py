# coin_num, target = map(int, input().split())
# coins = []
#
# for _ in range(coin_num):
#     coins.append(int(input()))

# 입출력은 위에 부분
# 이 아래 coins, target은 그냥 써놓은거

coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
target = 5
length = len(coins)

answer = 0
result = 0

print("coins: ", coins)
print("초기 target: ", target)
test = 0
while test < 10:
    test += 1
    print("\ntarget: ", target)
    coin_index = 0
    if coins[-1] < target:
        coin_index = -1

    else:
        for i in range(length-1, -1, -1):
            if coins[i] <= target:
                coin_index = i
                break

    coin_value = coins[coin_index]

    print("동전의 액면가: ", coins[coin_index])

    mok = target // coin_value
    temp_result = mok * coin_value

    print("동전 갯수: ", mok)
    print("temp_result: ", temp_result)

    answer += mok
    target -= temp_result

    if target == 0:
        break

print(answer)


