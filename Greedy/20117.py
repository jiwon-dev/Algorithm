import sys
input=sys.stdin.readline
# 06m 31s
# 정렬한 뒤, [i]와 [N-i-1]을 짝지어서 계산
# 이 때, 홀수 일 경우 [N//2]값을 한 번 더 더하므로 [N//2]를 빼줌
N=int(input())
a=sorted(map(int,input().split()))
ans=0
if N%2==0:
    for i in range(N//2):
        ans+=a[N-i-1]*2
else:
    for i in range(N//2+1):
        ans+=a[N-i-1]*2
    ans-=a[N//2]
print(ans)
