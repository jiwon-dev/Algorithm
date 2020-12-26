import sys
input=sys.stdin.readline
# 1시간 이상
INF=float('inf')
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

def dist(loc,k):
    # x좌표->0, y좌표->1, z좌표->2로 표현하기 위해 k를 인자로 받았다
    for i in range(N-1):
        x,y=loc[i][-1],loc[i+1][-1]
        if (x,y) in dic:
            dic[(x,y)]=min(dic[(x,y)],abs(loc[i][k]-loc[i+1][k]))
        else:
            dic[(x,y)]=abs(loc[i][k]-loc[i+1][k])
    
N=int(input())
loc=[]
for i in range(N):
    x,y,z=map(int,input().split())
    loc.append([x,y,z,i])
    # x좌표, y좌표, z좌표 기준으로 3번 정렬할 것이기 때문에 인덱스가 흐트러 진다
    # 따라서, 좌표 정렬을 해도 인덱스가 흐트러지지 않게 i를 넣는다

dic={}
# 처음에 리스트를 사용하니 공간복잡도가 초과되어 메모리 초과가 났다
# 리스트를 딕셔너리로 바꾸어 dic[(i,j)]=(i에서 j로 가는 최소 비용)으로 두었다

# x,y,z 좌표로 정렬하면 i와 i+1이 각 정렬된 좌표에서 최소 비용이다
loc.sort(key=lambda x:x[0])
# x좌표로 정렬
dist(loc,0)
# x좌표로 연결할 때의 비용을 구함
loc.sort(key=lambda y:y[1])
# y좌표로 정렬
dist(loc,1)
# y좌표로 연결할 때의 비용을 구함
loc.sort(key=lambda z:z[2])
# z좌표로 정렬
dist(loc,2)
# z좌표로 연결할 때의 비용을 구함

items=list(dic.items())
# 각 거리의 비용을 오름차순으로 정렬하기 위해 items로 추출
items.sort(key=lambda x:x[1])
# 비용 오름차순으로 정렬
p=[-1]*N
ans=0
for loc,w in items:
    if not merge(loc[0],loc[1]): continue
    ans+=w
print(ans)

