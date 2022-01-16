def solution(s):
    answer = True

    if not (len(s) == 4 or len(s) == 6):
        return False

    for i in range(len(s)):
        print("i: ", s[i])

        if not s[i].isnumeric():
            return False

    return answer


s = "1234"
s = "a234"
print(solution(s))