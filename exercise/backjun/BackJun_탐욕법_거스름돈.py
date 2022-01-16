
input_value = int(input())
target = 100000 - input_value
print("target: ", target)

coins = [1, 5, 10, 50, 100, 500]
answer = 0
test = 0
while test < 10:
    test += 1
    coin_index = 0
    print("\nTest: ", test)

    for i in range(len(coins)-1, -1, -1):
        if target >= coins[i]:
            coin_index = i
            print("coins_index2: ", coin_index)
            break

    coin_value = coins[coin_index]
    coin_num = target // coin_value
    temp_result = coin_value * coin_num
    print("동전의 액면가: ", coin_value)
    print("동전의 갯수: ", coin_num)
    print("중간결과: ", temp_result)

    target -= temp_result
    answer += coin_num

    print("target: ", target)
    print("answer: ", answer)
    if target == 0:
        break

print(answer)
