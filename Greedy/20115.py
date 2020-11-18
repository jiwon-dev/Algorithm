import sys
input=sys.stdin.readline
N=int(input())
D=sorted(list(map(int,input().split())),reverse=True)
ans=max(D)
for i in range(1,N):
    ans+=D[i]/2
print(ans)
