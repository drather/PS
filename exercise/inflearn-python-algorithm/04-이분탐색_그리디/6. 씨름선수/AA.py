"""
씨름 선수(그리디)
현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습
니다. 현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
“다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자
만 뽑기로 했습니다.”
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니
다.

▣ 입력설명
첫째 줄에 지원자의 수 N(5<=N<=50)이 주어집니다.
두 번째 줄부터 N명의 키와 몸무게 정보가 차례로 주어집니다. 각 선수의 키와 몸무게는 모두
다릅니다.

▣ 출력설명
첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력하세요.

▣ 입력예제 1
5
172 67
183 65
180 70
170 72
181 60

▣ 출력예제 1
3

출력설명
(183, 65), (180, 70), (170, 72)가 선발됩니다. (181, 60)은 (183, 65) 때문에 탈락하고, (172, 67)은 (180, 70)
때문에 탈락합니다.
"""
import sys
sys.stdin = open("in5.txt", "rt")

player_num = int(input())
info = []
for _ in range(player_num):
    info.append(list(map(int, input().split())))

# player_num = 5
# info = [[172, 67], [180, 70], [170, 72], [181, 60], [183, 65]]

info.sort(reverse=True)
largest = 0
cnt = 0
print(info)
# !!!!!!!!!!!!!!! 두 번째 풀이, 이게 훨씬 좋음 !!!!!!!!!!!!!!!
for x, y in info:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)



# !!!!!!!!!!!!!!! 첫 번째 풀이 !!!!!!!!!!!!!!!
# answer = player_num
# info.sort(reverse=True)
# for i in range(len(info)-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if info[i][1] < info[j][1]:
#             answer -= 1
#             break
# print(answer)