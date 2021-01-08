import sys
input=sys.stdin.readline
# 중복 조합 잘 봐두기
# idx 이전 값은 계산할 필요 없음
def solve(depth,result,idx):
    global ans
    if depth==N:
        if visited[result]: return
        ans+=1
        visited[result]=True
        return

    for i in range(idx,4):
        solve(depth+1,result+R[i],i)
    
N=int(input())
R=[1,5,10,50]
visited=[False]*1001
ans=0
solve(0,0,0)
print(ans)

