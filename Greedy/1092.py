import sys
input=sys.stdin.readline
N=int(input())
L=sorted(map(int,input().split()))
M=int(input())
B=sorted(map(int,input().split()))+[1000001]
ans=0
if max(L)<max(B[:-1]): print(-1)
else:
    i=0
    while i<M:
        for l in L:
            if B[i]<=l: i+=1
        ans+=1
    print(ans)
