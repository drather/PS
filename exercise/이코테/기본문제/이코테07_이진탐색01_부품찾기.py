# num_stock = int(input())
# stock = list(map(int, input().split()))
#
# request_num = int(input())
# request = list(map(int, input().split()))

num_stock = 5
stock = [8, 3, 7, 9, 2]

request_num = 3
request = [5, 7, 9]

stock.sort()


def binary_search(req):
    global stock
    global num_stock

    left = 0
    right = num_stock - 1

    while left <= right:
        middle = (left + right) // 2

        if stock[middle] == req:
            return True

        elif stock[middle] > req:
            right = middle - 1

        else:
            left = middle + 1

    else:
        return False


if __name__ == '__main__':
    for r in request:
        if binary_search(r):
            print("Yes")
        else:
            print("No")
