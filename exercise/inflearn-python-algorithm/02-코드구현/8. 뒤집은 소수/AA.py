"""
뒤집은 소수
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
여 프로그래밍 한다.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000를 넘지 않는다.

▣ 출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

▣ 입력예제 1
5
32 55 62 3700 250

▣ 출력예제 1
23 73
"""
import sys


def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x+1):
            if i != x and x % i == 0:
                return False

        else:
            return True


def reverse(x):
    ch_num = list(str(x))

    target = ""
    for i in range(len(ch_num)-1, -1, -1):
        target += ch_num[i]

    return int(target)


# sys.stdin = open("in1.txt", "rt")

num = int(input())
arr = list(map(int, input().split()))

for i in arr:
    temp = reverse(i)
    if isPrime(temp):
        print(temp, end=" ")





