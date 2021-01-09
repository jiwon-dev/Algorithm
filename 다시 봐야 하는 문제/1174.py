import sys
input=sys.stdin.readline
# 1시간 이상
# 최대 감소하는 수는 9876543210이라서 시간 내에 충분히 가능
# 모든 자연수에서 감소하는 수는 1023개 밖에 되지 않음
def solve(idx,res):
    for i in range(idx,-1,-1):
        ans.append(res*10+i)
        solve(i-1,res*10+i)
N=int(input())
ans=[]
solve(9,0)
ans.sort()
print(-1 if N>len(ans) else ans[N-1])
