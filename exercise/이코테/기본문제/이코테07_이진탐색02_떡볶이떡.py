"""
1. 문제
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다.
동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기의 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2 cm 이다. 손님은 6cm 만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

<제한 사항>
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1<=N<=1,000,000, 1<=M<=2,000,000,000)
둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

<입력 예시>
4 6
19 15 10 17

<출력 예시>
15
"""


def cut_cake(height):
    result = 0

    for length in cake_length:
        if length > height:
            result += length - height

    return result


if __name__ == '__main__':
    cake_num, target_length = map(int, input().split())
    cake_length = list(map(int, input().split()))

    left = 1
    right = max(cake_length)

    while left <= right:
        middle = (left + right) // 2
        # print(f"left, middle, right: {left}, {middle}, {right}")

        cut_cake_sum = cut_cake(height=middle)
        # print(f"cut_cake_sum: {cut_cake_sum}")

        if cut_cake_sum >= target_length:
            # print("떡의 길이 >= target 길이 -> 따라서 middle 의 높이를 높여서 떡의 길이를 줄여야 함 -> left  = middle + 1")
            left = middle + 1

        else:
            # print("떡의 길이 < target 길이 -> 따라서 middle 의 높이를 낮춰서 떡의 길이를 늘려야  함 -> right  = middle - 1")
            right = middle - 1

        # print()
    print(right)
