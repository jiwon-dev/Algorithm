import sys
input=sys.stdin.readline
# 10m
N=int(input())
ans='Wa-pa-pa-pa-pa-pa-pow!'
if N!=3: ans='Woof-meow-tweet-squeek'
else:
    cnt=0
    for _ in range(3):
        a,b=map(int,input().split())
        if (a,b) in [(1,3),(3,1),(4,3),(3,4),(1,4),(4,1)]: cnt+=1
    if cnt<3: ans='Woof-meow-tweet-squeek'
print(ans)
