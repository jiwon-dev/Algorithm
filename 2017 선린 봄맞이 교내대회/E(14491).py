import sys
input=sys.stdin.readline
# 19m
T=int(input())
ans=''
while T>0:
    ans+=str(T%9)
    T//=9
print(ans[::-1])
