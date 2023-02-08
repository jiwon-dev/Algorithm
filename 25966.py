import sys
input = sys.stdin.readline
N, M, q = map(int, input().split())
ans = []

for i in range(N):
    tmp = list(map(int, input().split()))
    ans.append(tmp)

sam = [i for i in range(N)]
for _ in range(q):
    tmp = list(map(int, input().split()))
    if tmp[0]: ex = sam[tmp[1]]; sam[tmp[1]] = sam[tmp[2]]; sam[tmp[2]] = ex
    else: ans[sam[tmp[1]]][tmp[2]] = tmp[3]

for i in range(N):
    for j in range(M):
        print(ans[sam[i]][j], end = ' ')
    print()
    
