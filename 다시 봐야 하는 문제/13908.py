import sys
input=sys.stdin.readline
# 최악일 때 7천만이므로 모든 경우를 살펴도 1초 안에 충분히 통과할 수 있다
def solve(depth):
    global ans
    if depth==n:
        res=True
        for v in num:
            if not cnt[v]: res=False
        if res: ans+=1
        return

    for i in range(10):
        cnt[i]+=1
        solve(depth+1)
        cnt[i]-=1
    
n,m=map(int,input().split())
num=list(map(int,input().split()))
cnt=[0]*10
# cnt[i]:탐색한 숫자 중 i의 개수
# i가 0이 아니면 숫자 i는 존재한다는 의미
ans=0
solve(0)
print(ans)
