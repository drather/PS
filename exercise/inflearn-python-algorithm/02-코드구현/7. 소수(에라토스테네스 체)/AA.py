import sys
# sys.stdin = open("in1.txt", "rt")

num = int(input())

sieve = [-1, -1] + [1]*(num-1)


for i in range(2, len(sieve)):
    if sieve[i] == 1:
        for j in range(2*i, len(sieve), i):
            sieve[j] = 0
sum = 0
for i in sieve:
    if i == 1:
       sum += 1

print(sum)


