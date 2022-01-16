"""
후위표기식 만들기
중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있
으면 중위표기식입니다.

후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.

만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
(3+5)*2 이면 35+2* 로 바꾸어야 합니다.
※후위 표기식이 이해가 안되면 구글링으로 공부해보는 것도 좋습니다.

▣ 입력설명
첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.

▣ 출력설명
후위표기식을 출력한다.

▣ 입력예제 1
3+5*2/(7-2)

▣ 출력예제 1
352*72-/+

▣ 입력예제 2
3*(5+2)-9

▣ 출력예제 2
352+*9-

풀이!!
- 스택을 이용해서 푼다.
- 스탁을 이용해서 푼다는 것은, 보통은
    1. 주어진 데이터를 차례대로 읽으면서 스택에 집어넣을 건데
    2. 만약 stack 의 top, 또는 stack[-1] 의 값과 계속 비교를 해서, 조건을 만족하는 위치를 찾을 경우 그곳에 push 한다.

- 이 문제에서는 사칙연산의 우선순위가 중요하다.
1). 읽은 data 가 숫자인 경우:
    - 그냥 answer 에 붙인다.
2). 읽은 data 가 연산자인 경우
    - 2-1). 곱셈, 나눗셈인 경우
        - 이미 스택에 들어가 있는 것과, 지금 읽은 연산자를 계쏙 비교해보면서 어떤 것을 연산할지 정하는 것이라 할 수 있다.
        - 현재 스택을 보면서, 곱셈과 나눗셈보다 먼저 처리해야 할 연산자가 있는 지를 찾아본다.
        - 먼저 처리할 연산자는 괄호? 가 있고, 이미 스택에 들어가 있는 곱셈과 나눗셈을 먼저 처리해야 한다.
        - 따라서, stack[-1]의 값을 보면서, 곱셈이나 나눗셈인 경우 그 연산자를 pop 해서 answer 에 붙인다.
        - 아닌 경우, 그냥 stack 에 붙인다.
    - 2-2). 덧셈, 뺄셈인 경우
        - 이미 stack 에 들어가 있는 연산자 중, 여는 괄호를 만나기 전까지 나오는 모든 연산자를 pop 한 후 answer 에 붙인다.
        - 왜냐하면, 여는 괄호 말고 모든 기호(곱셈, 나눗셈)은 덧셈, 뺄셈보다 먼저 처리해야 하기 때문이다.
        - 그 후, answer 에 붙인다.
    - 2-3). 여는 괄호일 경우
        - 그냥 stack 에 append 한다
    - 2-4). 닫는 괄호일 경우
        - 여는 괄호가 나올 때 까지 나오는 모든 연산자를 pop 해서 answer 에 붙인다.
        - 그 후, stack.pop()을 통해 여는 괄호를 제거한다.

** 느낀 점
중위 표현식에 너무 익숙하다보니, 풀기가 힘들었던 문제.
기존에 알고 있던 것은 잠시 접어두고, 문제에 집중할 필요 있음

** 배운 점
스택을 이용하는 경우, 읽은 데이터와 stack[-1]과의 지속적인 비교를 통해서
stack 에서 pop()을 한 뒤에 push()를 하는 경우가 많은 것 같다.
즉, 문제에 주어진 기준이나 조건을 가지고, 읽어온 데이터와 stack[-1]을 적절히 비교 후 push(), pop() 등 알맞은 조치를 취해라.
"""
import sys
sys.stdin = open("in2.txt", "rt")
before_exp = input()
answer = ""
stack = []

print("입력: ", before_exp)

for i in before_exp:
    print("\ni: ", i)
    if i.isdecimal():
        answer += i

    else:
        if i == "(":
            stack.append(i)

        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(i)

        elif i == "+" or i == "-":
            while stack and (stack[-1] != "("):
                answer += stack.pop()
            stack.append(i)

        elif i == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()

        print("Stack: ", stack)
        print("answer: ", answer)


while stack:
    answer += stack.pop()
print("최종 answer: ", answer)


# !!!!!!!!!! 첫 번째 풀이 !!!!!!!!!!
# before_exp = input()
# print(before_exp)
# answer = ""
# stack = []
#
# # for i in range(len(before_exp)):
#     print("\n읽은 값: ", before_exp[i])
#     if before_exp[i].isnumeric():
#         answer += before_exp[i]
#
#     else:
#         if before_exp[i] == "(":
#             stack.append(before_exp[i])
#         elif before_exp[i] == "*" or before_exp[i] == "/":
#             while stack and (stack[-1] == "*" or stack[-1] == '/'):
#                 answer += stack.pop()
#             stack.append(before_exp[i])
#
#         elif before_exp[i] == "+" or before_exp[i] == "-":
#             while stack and stack[-1] != "(":
#                 answer += stack.pop()
#             stack.append(before_exp[i])
#
#         elif before_exp[i] == ")":
#             while stack and stack[-1] != "(":
#                 answer += stack.pop()
#             stack.pop()
#
# while stack:
#     answer += stack.pop()
#
# print(answer)
