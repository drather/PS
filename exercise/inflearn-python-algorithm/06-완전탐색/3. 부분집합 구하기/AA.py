"""
▣ 입력설명
부분집합 구하기(DFS)
자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램
을 작성하세요.

첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.

▣ 출력설명
첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제와 같은 순서로 출력한다.
단 공집합은 출력하지 않습니다.

▣ 입력예제 1
3

▣ 출력예제 1
1 2 3
1 2
1 3
1
2 3
2
3

"""
import sys
sys.stdin = open("in1.txt", "r")


def dfs(n):
    if n == num + 1:
        for i in range(1, num+1):
            if check[i] == 1:
                print(i, end=" ")
        print()
    else:
        check[n] = 1
        dfs(n+1)
        check[n] = 0
        dfs(n+1)


if __name__ == '__main__':
    num = int(input())
    check = [0]*(num+1)

    dfs(1)








