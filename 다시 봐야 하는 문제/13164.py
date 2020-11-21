import sys
input=sys.stdin.readline
# 1시간 이상
# 둘 사이의 차이를 D에 담고 정렬 후, D에 있는 값을 N-K번 더함
N,K=map(int,input().split())
G=list(map(int,input().split()))
D=[]
for i in range(N-1):
    D.append(G[i+1]-G[i])
D.sort()
ans=0
for j in range(N-K):
    ans+=D[j]
print(ans)
