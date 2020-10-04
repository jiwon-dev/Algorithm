import sys
input=sys.stdin.readline
# 09m 37s
# 시작 위치에서 부터 왼쪽 오른쪽으로 dfs
# 정답은 visit에서 1의 개수
n=int(input())
r=list(map(int,input().split()))
s=int(input())
visit=[0]*n
def dfs(s,c):
    l=[s-c,s+c]
    visit[s]=1
    for i in range(2):
        if 0<=l[i]<n and not visit[l[i]]:
            visit[l[i]]=1
            dfs(l[i],r[l[i]])
dfs(s-1,r[s-1])
print(visit.count(1))
