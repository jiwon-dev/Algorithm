import sys
input=sys.stdin.readline
# 18m 37s
# p[i]:i의 부모노드
# 각 동맹의 우두머리는 루트 노드
# 우두머리에 모든 병력을 배치
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def union(a,b):
    # 동맹을 수행하는 함수
    a=find(a);b=find(b)
    if a==b: return
    # a==b의 의미는 서로 동맹이라는 뜻인데 동맹인 국가가 또 동맹을 맺을 수 없으니
    # if a==b: return은 필요 없긴 하지만 이해를 위해 넣음
    p[b]=a
    # 병력의 크기와 상관없이 b를 a에 합침
    A[a]+=A[b]
    # 동맹했으니 a의 병력을 b의 병력만큼 더함
    A[b]=0
    # a와 합쳤으니 b의 병력은 사라짐
    
def war(a,b):
    # 전쟁을 수행하는 함수
    a=find(a);b=find(b)
    # 각각의 우두머리를 비교하기 위해 find 사용
    if A[a]>A[b]:
        # a의 병력이 더 많을 경우
        A[a]-=A[b]
        # a가 이겼으니 b의 병력만큼 손실
        p[b]=a
        # a와 b는 a로 합쳐짐
        A[b]=0
        # b는 졌으므로 병력은 0이 됨
    elif A[a]==A[b]:
        # 둘의 병력이 같을 경우
        A[a]=0;A[b]=0
        # 둘 다 멸망하므로 병력은 없어짐
    else:
        # b의 병력이 더 많을 경우
        A[b]-=A[a]
        # b가 이겼으니 a의 병력만큼 손실
        p[a]=b
        # a를 b에 합침
        A[a]=0
        # a는 졌으니 병력은 없어짐
    
N,M=map(int,input().split())
A=[int(input()) for _ in range(N)]
p=[-1]*(N+1)
for _ in range(M):
    O,P,Q=map(int,input().split())
    if O==1: union(P-1,Q-1)
    else: war(P-1,Q-1)

ans=[]
for i in range(N):
    if p[i]==-1 and A[i]>0:
        # 각 동맹의 우두머리이고 남은 병력이 0보다 클 경우 남아 있는 국가(동맹)이므로 ans에 추가
        ans.append(A[i])
ans.sort()
print(len(ans))
print(*ans)
