import sys
input=sys.stdin.readline
# 07m 58s
# 각 시간을 0~49로 1씩 줄여서 비트에 마킹
N=int(input())
sub=[]
for _ in range(N):
    k,*s=input().split()
    temp=0
    for v in s:
        x=int(v)-1
        temp|=(1<<x)
    sub.append(temp)

M=int(input())
for _ in range(M):
    p,*q=input().split()
    temp=0
    ans=0
    for v in q:
        x=int(v)-1
        temp|=(1<<x)
    for v in sub:
        if temp&v==v: ans+=1
    print(ans)
