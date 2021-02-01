import sys
from math import gcd
input=sys.stdin.readline
# 24m
A,B=map(int,input().split())
tmp=B//A
# 답이 i,j일 때, lcm//gcd=(i//gcd*j//gcd)임을 활용

for i in range(int(tmp**0.5)+1,0,-1):
    # 합이 최소가 되는 i,j를 찾아야하므로 최댓값인 int(tmp**0.5)+1부터 1까지 탐색
    if tmp%i!=0: continue
    # tmp%i가 0이 아니면 탐색할 필요 없으므로 continue
    j=tmp//i
    # j는 tmp//i가 됨
    if gcd(i,j)==1: break
    # i와 j는 서로소이므로 gcd(i,j)==1이면 break
    # 작으면 작을수록 좋으니 답이 될 수 있는 가장 큰 수부터 탐색
i,j=min(i,j),max(i,j)
print(A*i,A*j)
   
