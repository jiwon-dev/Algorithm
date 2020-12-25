import sys
input=sys.stdin.readline
# 25m 44s
def find(n,p):
    if p[n]<0: return n
    p[n]=find(p[n],p)
    return p[n]

def merge(a,b,p):
    a=find(a,p);b=find(b,p)
    if a==b: return False
    p[b]=a
    return True

def mst(D,t):
    # (D=최악 or 최선의 거리,t=최선이면 0 최악이면 1)
    D.sort(key=lambda x:[x[2]])
    # mst 수행하기 전 비용을 기준으로 오름차순 정렬
    ans=0
    # 오르막길 선택 횟수
    p=[-1]*(N+1)
    # 유니온 파인드 하기 위한 부모 배열
    for x,y,w in D:
        if not merge(x,y,p): continue
        # p를 인자로 넘겨줘야 find 함수 실행 가능
        if t==0 and w==1: ans+=1
        # 최선의 경우이고 w가 1(오르막길)이면 ans+=1
        if t==1 and w==0: ans+=1
        # 최악의 경우이고 w가 0(오르막길)이면 ans+=1
    return ans

N,M=map(int,input().split())
u,v,w=map(int,input().split())
D=[tuple(map(int,input().split())) for _ in range(M)]
B=[]
# 최선의 경우 거리 배열
W=[]
# 최악의 경우 거리 배열
for x,y,t in D:
    if t==0:
        # 오르막길이면
        B.append((x,y,1))
        # 최선의 경우 오르막길을 최소한으로 선택해야하므로 가중치로 1을 줌
        W.append((x,y,0))
        # 최악의 경우 오르막길을 최대한으로 선택해야하므로 1보다 작은 0을 줌(음수를 줘도 상관없음, 1보다만 작으면 됨)
    else:
        # 내리막길이면
        B.append((x,y,0))
        # 최선의 경우 내리막길을 최대한으로 선택해야하므로 가중치로 0을 줌
        W.append((x,y,1))
        # 최악의 경우 내리막길을 최소한으로 선택해야하므로 가중치로 1을 줌

best=mst(B,0)
# 최선=mst(최선의 거리 배열,0)
worst=mst(W,1)
# 최악=mst(최악의 거리 배열,1)
if w==0:
    # 입구에서 무조건 1을 거쳤다가 가야하므로 0->1이 오르막길이면 최선, 최악의 경우의 수도 하나씩 증가해야함
    best+=1
    worst+=1
print(worst**2-best**2)
