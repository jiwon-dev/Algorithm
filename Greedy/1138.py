import sys
input=sys.stdin.readline
# 16m 20s
N=int(input())
H=list(map(int,input().split()))
ans=[-1]*N

for i in range(N):
    cnt=0
    for j in range(N):
        if cnt==H[i] and ans[j]==-1:
            ans[j]=i+1
            break
        elif ans[j]==-1:
            cnt+=1
print(*ans)
        
