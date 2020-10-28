import sys
from collections import deque
input=sys.stdin.readline
# 30m 41s
# 1. 에라토스테네스의 체로 1000부터 10000까지의 소수를 구한다
# 2. 네 자리 수이므로 str 형태에서 한 자리씩 수를 바꿔가며 소수 체크와 처음 방문했는지 여부 체크한 뒤, q에 넣음
# 3. q가 빌때 까지 반복(bfs)
def prime_list(n):
    check=[True]*n
    m=int(n**0.5)
    for i in range(2,m+1):
        if check[i]==True:
            for j in range(i+i,n,i):
                check[j]=False
    return [i for i in range(1000,n) if check[i]==True]

def bfs(A):
    q=deque()
    q.append(A)
    disc[A]=0
    while q:
        n=q.popleft()
        for i in range(4):
            s=str(n)[:]
            for j in range(10):
                sa=s[:i]+str(j)+s[i+1:]
                sam=int(sa)
                if 1000<=sam<=9999 and sam in prime and disc[sam]==-1:
                    disc[sam]=disc[n]+1
                    q.append(sam)

for _ in range(int(input())):
    A,B=map(int,input().split())
    prime=prime_list(10000)
    disc=[-1]*10000
    ans=bfs(A)
    print('Impossible' if disc[B]==-1 else disc[B])
