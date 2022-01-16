"""
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수 중에서 M개를 고른 수열

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""


def dfs(level):
    global table
    # print("\nlevel: ", level)
    if level == limit:
        for r in range(limit):
            print(result[r], end=" ")
        print()

    else:
        for i in range(length):
            # print("후보 인덱스, 값: ", (i, arr[i]))
            # if val_check[arr[i]] == 0 and idx_check[i] == 0:
            if table[arr[i]] > 0:
                # print("실제 호출 인덱스, 값: ", (i, arr[i]))
                result[level] = arr[i]
                table[arr[i]] -= 1
                # val_check[arr[i]] = 1

                dfs(level+1)
                table[arr[i]] += 1




if __name__ == "__main__":
    length, limit = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    result = [0] * limit

    val_check = [0] * (max(arr) + 1)
    idx_check = [0] * (length+1)

    table = {}
    for i in arr:
        table[i] = table.get(i, 1)

    print(table)

    dfs(0)


