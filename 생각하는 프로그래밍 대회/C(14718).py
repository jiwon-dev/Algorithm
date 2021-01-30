import sys
input=sys.stdin.readline
N,K=map(int,input().split())
S=[list(map(int,input().split())) for _ in range(N)]

res=[]
for v in S: res.append((sum(v),v))
print(res)
