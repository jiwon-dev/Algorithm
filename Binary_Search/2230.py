import sys
input=sys.stdin.readline
# 23m 20s
# 이분 탐색
N,M=map(int,input().split())
S=[int(input()) for _ in range(N)]
S.sort()

ans=float('inf')
for i in range(N):
    s,e=i,N-1
    # s를 0에서 하면 같은 수가 나왔을 때, 여러 번 계산될 수 있으므로 i로 설정
    while s<=e:
        mid=(s+e)//2
        if abs(S[mid]-S[i])<M: s=mid+1
        else: e=mid-1; ans=min(ans,abs(S[mid]-S[i]))

# 투 포인터
s,e=0,0
S.sort()
ans=float('inf')
while s<N and e<N:
    # 포인터 둘다 N 미만일 때만 반복문 돌면 됨
    if S[e]-S[s]>=M: ans=min(ans,S[e]-S[s]); s+=1
    else: e+=1
print(ans)
