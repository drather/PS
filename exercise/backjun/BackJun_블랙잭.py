# 5 21                  카드의 갯수와 합을 정하는 숫자
# 5 6 7 8 9             카드의 값

# 카드의 갯수와, 넘지 말아야 할 값을 입력받는다.
card_num, value = map(int, input().split())

# 카드의 값들을 입력받는다.
cards = list(map(int, input().split(' ')))

# 값을 저장하기 위한 answer 선언
answer = 0

# i, j, k 3개의 인덱스를 이용해서 3중 for문을 돌린다.
# (1, 2, 3)을 1번 카드, 2번카드, 3번 카드의 합이라 할 때
# 아래 for문은 (1, 2, 3) 부터 (3, 4, 5)까지 돌게 된다.
for i in range(card_num - 2):
    for j in range(i+1, card_num - 1):
        for k in range(j+1, card_num):
            temp = cards[i] + cards[j] + cards[k]
            # 지금 경우에 구한 합이 value를 넘거나
            if temp > value:
                continue;

            # 이전에 구한 값보다 작다면 다른 행동을 취하지 않는다.
            elif temp < answer:
                continue;

            # value보다 작고, 이전 결과보다 가장 큰 값이 answer에 저장된다.
            else:
                answer = temp
print(answer)