import sys
input=sys.stdin.readline
# 12m 25s
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

N,M=map(int,input().split())
S=[0]+input().split()
# 1부터 시작하기 때문에 맞추기 위해 앞에 0을 삽입
D=[tuple(map(int,input().split())) for _ in range(M)]
D.sort(key=lambda x:x[2])
# 거리 오름차순으로 정렬

p=[-1]*(N+1)
# 유니온 파인드 부모 배열
ans=0
# 최소 경로 길이
for x,y,w in D:
    if S[x]==S[y]: continue
    # 남초->남초 or 여초->여초이면 사심 경로 조건을 만족하지 못하므로 continue
    if not merge(x,y): continue
    # 둘 다 이어져있으면 continue
    ans+=w
    # 둘 중에 하나라도 이어져있지 않다면 ans+=w
print(-1 if ans==0 or p[1:].count(-1)>1 else ans)
# 컴포넌트가 하나가 아니라 여러 개일 경우 어떤 대학교에서 모든 대학교로 이동 불가능하므로 p의 루트가 여러 개인지 확인->p[1:].count(-1)
