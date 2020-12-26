import sys
input=sys.stdin.readline
# 12m 31s
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

dic={}
for i in range(26): dic[chr(ord('a')+i)]=i+1
for j in range(26): dic[chr(ord('A')+j)]=j+27
# 문자를 길이로 바꾸는 과정

N=int(input())
C=[input().rstrip() for _ in range(N)]
R=[]
temp=0
# 전체 랜선의 길이
for i in range(N):
    for j in range(N):
        if C[i][j] not in dic: continue
        # dic에 없으면 연결되어있지 않다는 뜻이므로 continue
        temp+=dic[C[i][j]]
        # 전체 랜선의 길이 더함
        R.append((i,j,dic[C[i][j]]))
        # mst를 위한 R에 (i,j,i->j의 길이) 추가
R.sort(key=lambda x:x[2])
# 길이 오름차순으로 정렬

p=[-1]*N
ans=0
for x,y,w in R:
    if not merge(x,y): continue
    ans+=w
print(-1 if p.count(-1)>1 else temp-ans)
# p에 -1이 2개 이상있으면 여러 개의 컴포넌트가 존재한다는 의미이므로 -1 출력
