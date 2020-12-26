import sys
input=sys.stdin.readline
# 07m 40s
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

N,M,K=map(int,input().split())
D=[]
for i in range(M):
    a,b=map(int,input().split())
    D.append((a,b,i+1))
D.sort(key=lambda x:x[2])

ans=[0]*K
for i in range(K):
    # i번째 턴에는 D[i:M]까지의 거리만 사용
    temp=0
    # 각 턴의 mst의 최소 비용
    p=[-1]*(N+1)
    for j in range(i,M):
        # D[i:M]까지의 거리만 사용하기 위해 j는 i부터 시작
        x,y=D[j][0],D[j][1]
        if not merge(x,y): continue
        temp+=D[j][2]
    if p.count(-1)>2: break
    # 두개의 컴포넌트가 있으면 break
    ans[i]=temp
    # 하나로 다 연결되었으면 ans[i]=temp
print(*ans)
