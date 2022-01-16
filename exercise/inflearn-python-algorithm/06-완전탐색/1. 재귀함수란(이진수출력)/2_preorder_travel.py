"""
이진트리 순회(깊이우선탐색)
아래 그림과 같은 이진트리를 전위순회와 후위순회를 연습해보세요.
1
2 3
4 5 6 7
전위순회 출력 : 1 2 4 5 3 6 7
중위순회 출력 : 4 2 5 1 6 3 7
후위순회 출력 : 4 5 2 6 7 3 1

"""


def pre_order(n):
    if n > 7:
        return

    print(n, end=" ")
    pre_order(n*2)
    pre_order(n*2 + 1)


def in_order(n):
    if n > 7:
        return

    in_order(n*2)
    print(n, end=" ")
    in_order(n*2+1)


def post_order(n):
    if n > 7:
        return

    post_order(n*2)
    post_order(n*2+1)
    print(n, end=" ")


if __name__ == "__main__":
    num = 1
    pre_order(num)
    print("\n")
    in_order(num)
    print("\n")

    post_order(num)

