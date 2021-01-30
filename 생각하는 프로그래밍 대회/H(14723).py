import sys
input=sys.stdin.readline
# 14m
N=int(input())
tmp,cnt=2,0

while True:
    for i in range(tmp-1,0,-1):
        cnt+=1
        if cnt==N:
            print(i,tmp-i)
            sys.exit()
    tmp+=1
