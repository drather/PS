def solution(n, words):
    table = {}
    answer = []
    first_word = words[0]
    table[first_word] = True
    print("First: ", first_word)
    answer.append(first_word)
    turn = 1

    for i in range(1, len(words)):
        print("\n", words[i])
        # 다른 단어 말한 경우
        if first_word[-1] != words[i][0]:
            print("다른 단어 말함")
            print("turn: ", turn)

            if (i+1)% n == 0:
                return [n, turn // n + 1]
            else:
                return [(i+1) % n, turn // n +1]

        else:
            print("잘 말함")

        # 이미 말한 단어 말한 경우
        if words[i] in answer:
            print("이미 말한 단어 말함")
            print("turn: ", turn)
            if (i+1)% n == 0:
                return [n, turn // n + 1]
            else:
                return [(i+1) % n, turn // n + 1]

        else:
            print("처음 나오는 단어 말함")
            answer.append(words[i])
            print("answers: ", answer)
            first_word = words[i][-1]
            turn += 1



words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# words = ["hello", "one", "even", "never", "now", "world", "draw"]
n = 3
print("답: ", solution(n, words))
