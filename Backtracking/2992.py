import sys
input=sys.stdin.readline
# 비트마스킹을 이용해서 선택한 인덱스를 확인
def solve(s,bit):
    global ans
    if bit==2**len(X)-1:
        if int("".join(s))>N:
            ans=min(ans,int("".join(s)))
        return

    for i in range(len(X)):
        if bit&(1<<i)==0:
            bit|=(1<<i)
            solve(s+X[i],bit)
            bit&=~(1<<i)
X=list(map(str,input().rstrip()))
N=int("".join(X))
ans=float('inf')
solve("",0)
print(0 if ans==float('inf') else ans)
