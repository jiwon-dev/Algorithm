import sys
input=sys.stdin.readline
# 11m 36s
# 성장 포텐셜이 제일 낮은 나무부터 자름
n=int(input())
Hi=list(map(int,input().split()))
Ai=list(map(int,input().split()))

length=[0]*n
for i in range(n):
    length[i]=(Hi[i],Ai[i])
length.sort(key=lambda x:[x[1]])

ans=0
for i in range(n):
    ans+=length[i][0]+length[i][1]*i
print(ans)
