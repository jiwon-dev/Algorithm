import sys
input=sys.stdin.readline
# X좌표, Y좌표를 오름차순으로 정렬한 뒤, 그 중 중앙값이 편의점의 위치(모든 고객의 최소 거리의 합)
N=int(input())
X=[]
Y=[]
for _ in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
sx,sy=X[(N-1)//2],Y[(N-1)//2]
ans=0
for i in range(N):
    ans+=abs(sx-X[i])+abs(sy-Y[i])
print(ans)
