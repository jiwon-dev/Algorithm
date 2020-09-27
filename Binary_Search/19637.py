import sys
input=sys.stdin.readline
# 08m 18s
# 이분 탐색으로 O(mlogn)에 해결 가능
# 칭호에 맞는 전투력과 캐릭 전투력이 같을 경우 칭호에 맞게 해야하므로 last=mid-1
n,m=map(int,input().split())
c=[input().split() for _ in range(n)]
g=[int(input()) for _ in range(m)]
for value in g:
    start,last=0,n-1
    while start<=last:
        mid=(start+last)//2
        if int(c[mid][1])<value:
            start=mid+1
        else:
            last=mid-1
    print(c[last+1][0])
