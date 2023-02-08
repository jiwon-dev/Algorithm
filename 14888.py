import sys
from itertools import permutations
sets = []
cnt = 0
min_v, max_v = float('INF'), -float('INF')

def cal(d, a, b):
    if d == 0: return a + b
    elif d == 1: return a - b
    elif d == 2: return a * b
    elif a < 0: return -((-a) // b)
    else: return a // b

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(4):
    for j in range(B[i]): sets.append(i)
    cnt += B[i]

data = list(permutations(sets))

for i in range(len(data)):
    tmp = cal(data[i][0], A[0], A[1])
    for j in range(1, cnt):
        tmp = cal(data[i][j], tmp, A[j + 1])
    min_v = min(min_v, tmp)
    max_v = max(max_v, tmp)
print(max_v)
print(min_v)

