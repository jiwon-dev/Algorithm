import sys
input=sys.stdin.readline
# 15m 35s
# 규칙 찾기(다이나믹 프로그래밍)
N=int(input())
q,r=divmod(N,7)
if r==0 or r==2: print('CY')
else: print('SK')
