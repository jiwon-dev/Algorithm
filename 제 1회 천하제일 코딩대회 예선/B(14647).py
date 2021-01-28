import sys
input=sys.stdin.readline
# 08m
n,m=map(int,input().split())
B=[input().split() for _ in range(n)]

total=0
ans=0
for i in range(n):
    tmp=0
    for j in range(m):
        tmp+=B[i][j].count('9')
        total+=B[i][j].count('9')
    ans=max(ans,tmp)

for j in range(m):
    tmp=0
    for i in range(n):
        tmp+=B[i][j].count('9')
    ans=max(ans,tmp)
print(total-ans)

