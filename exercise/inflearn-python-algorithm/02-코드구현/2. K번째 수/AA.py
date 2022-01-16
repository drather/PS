"""
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
"""
import sys
# sys.stdin = open("in1.txt", "rt")

case_num = int(input())

for c in range(1, case_num+1):
    num, start, end, k = (map(int, (input().split())))
    arr = list(map(int, input().split()))

    my_list = arr[start-1:end]
    my_list.sort()

    print("#%d %d" %(c, my_list[k-1]))


