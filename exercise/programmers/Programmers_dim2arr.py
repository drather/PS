# 행렬 곱
def solution(arr1, arr2):
    # 두 행렬을 파라미터로 받아서, 곱셈을 한 결과값의 형태를 가지고, 모든 값이 0인 행렬을 만든다.
    answer = [len(arr2[0]) * [0] for i in range(len(arr1))]

    # 정답 행렬을 2중 for문을 통해 순회하면서, 각 요소의 값을 채운다.
    for i in range(len(answer)):
        for j in range(len(answer[i])):

            # 아래에 for문이 가장 핵심이다.
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


def matrix_multiplication(mat1, mat2):
    matR = [len(mat2[0]) * [0] for i in range(len(mat1))]
    print(matR)

    for i in range(len(matR)):
        for j in range(len(matR[i])):
            for k in range(len(mat1[i])):
                matR[i][j] += mat1[i][k] * mat2[k][j]

    return matR

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print("결과: ", solution(arr1, arr2))




