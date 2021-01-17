import sys
input=sys.stdin.readline
# 59m
N=int(input())
ans=[]
for i in range(1,N+1):
    x,y,v=map(int,input().split())
    ans.append((((x**2+y**2)**0.5)/v,i))
ans.sort(key=lambda x:[x[0],x[1]])
for v,i in ans: print(i)
