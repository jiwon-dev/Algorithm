import sys
input=sys.stdin.readline
# 30m 46s
# 규칙 찾는데 오래 걸림
N,K=map(int,input().split())
st=K*(K+1)//2
if N<st: print(-1)
elif (N-st)%K==0: print(K-1)
else: print(K)
