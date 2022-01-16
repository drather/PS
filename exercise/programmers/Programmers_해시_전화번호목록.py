# 해쉬 사용 안함.
def solution(phone_book):
    answer = True
    # phone_book을 원소의 길이가 짧은 순서대로 정렬한다.
    phone_book.sort(key=len)

    # 2중 while문을 돌린다.
    i = 0
    while i < len(phone_book):
        j = i + 1

        # i번째 원소와, i+1, i+2, ... , N번째 원소를 비교한다.
        # i번째 원소의 길이를 length에 저장해두고, j번째 원소의 0~length-1 까지의 값을 비교한다
        # 즉, i번째 원소가 "123"인데, j번째 요소가 "12345"라면,
        # i번째 원소인 "123"과 j번째 원소의 0 ~ 2번째까지의 값인 "123을 비교한다. 같다면 False를 리턴한다.
        while j < len(phone_book):
            length = len(phone_book[i])
            if phone_book[i] == phone_book[j][0:length]:
                return False
            else:
                j += 1
        i += 1

    return answer


phone_book = ["12", "123", "1235", "567", "88"]
print(solution(phone_book))