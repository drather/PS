score = list(map(int, input()))

print("LUCKY") if sum(score[:len(score)//2]) == sum(score[len(score)//2:]) else print("READY")