import sys
from collections import deque
input=sys.stdin.readline
# 10m 38s
# 에라토스테네스의 체를 이용해 100000까지의 소수를 구하고 bfs를 실행
def prime_list(n):
    check=[True]*n
    m=int(n**0.5)
    for i in range(2,m+1):
        if check[i]==True:
            for j in range(i+i,n,i):
                check[j]=False
    return [i for i in range(2,n) if check[i]==True]

def bfs(N):
    q=deque()
    q.append(N)
    cnt=-1
    visited=[0]*1000001
    while q:
        cnt+=1
        for _ in range(len(q)):
            u=q.popleft()
            if A<=u<=B and u in prime:
                return cnt
            for v in (u//2),(u//3),(u+1),(u-1):
                if 0<=v<=1000000 and not visited[v]:
                    visited[v]=1
                    q.append(v)
    return -1

prime=prime_list(100001)
for _ in range(int(input())):
    N,A,B=map(int,input().split())
    print(bfs(N))

