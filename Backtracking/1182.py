import sys
input=sys.stdin.readline
N,S=map(int,input().split())
seq=list(map(int,input().split()))
ans=0
total=0
def dfs(cnt):
    global ans
    global total
    if cnt==N: return
    if total+seq[cnt]==S: ans+=1
    
    dfs(cnt+1)
    total+=seq[cnt]
    dfs(cnt+1)
    total-=seq[cnt]
dfs(0)
print(ans)
