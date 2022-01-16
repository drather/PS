def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        temp = ""
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                temp += skill_trees[i][j]
        skill_trees[i] = temp

    for i in range(len(skill_trees)):
        for j in range(len(skill_trees[i])):
            if skill[j] != skill_trees[i][j]:
                break
        else:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))

