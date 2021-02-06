import sys
input=sys.stdin.readline
# 2h 33m(오일러 회로)
N=int(input())
graph=[[False]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(i+1,N+1):
        graph[i][j]=True
graph[1][N]=False

idx=1
ans=[1]
while True:
    for i in range(1,N+1):
        if i<idx and graph[i][idx]:
            graph[i][idx]=False
            ans.append(i)
            idx=i
            break
        if i>idx and graph[idx][i]:
            graph[idx][i]=False
            ans.append(i)
            idx=i
            break
    if len(ans)==N*(N-1)//2:
        ans.append(1)
        for v in ans: print('a'+str(v),end=' ')
        break
