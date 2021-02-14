import sys
input=sys.stdin.readline
N=int(input())
F=list(map(int,input().split()))
S=[0]*N
cnt=0
for i in range(N-2):
    if S[i]!=F[i]:
        for j in range(i,i+3): S[j]=1-S[j]
        cnt+=1
print(cnt)
