import sys
input=sys.stdin.readline
# 1시간 이상
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    # (이긴 왕국, 진 왕국)으로 입력받음
    p[b]=a
    
N,M=map(int,input().split())
dic={}
name=[]
for i in range(N):
    s=input().split()
    name.append(s[-1])
name.sort()
# 사전 순으로 정렬해서 출력해야하기 때문에 이름을 정렬 후 dic에 넣음
for j in range(N): dic[name[j]]=j
# dic[이름]=인덱스

p=[-1]*N
for _ in range(M):
    s=input().rstrip().split(',')
    x,y=s[0].split()[-1],s[1].split()[-1]
    a=find(dic[x]);b=find(dic[y])
    u=dic[x];v=dic[y]
    # 같은 왕국에서 종주국과 속국 비교하는 방법:p[종주국]=-1이고 p[속국]=(종주국의 idx)
    if s[-1]=='1':
        # 왼쪽 왕국이 이길 때
        if a==b:
            # 뿌리가 같으면(같은 왕국인데 속국이 종주국을 친 경우)
            if p[u]==-1: continue
            # 종주국이 이기면 아무일도 일어나지 않으니 continue
            else:
                # 속국이 이기면
                p[u]=-1
                # p[이긴 왕국(속국)]=-1
                p[v]=u
                # p[진 왕국(종주국)]=이긴 왕국(속국) 
        else: merge(a,b)
        # 뿌리가 다르면 다른 왕국이므로 왕국-왕국 or 왕국-속국의 싸움인데
        # 왕국-속국의 싸움의 경우 속국의 왕국이 싸워야하기 때문에 뿌리끼리 합침
    else:
        # 오른쪽 왕국이 이길 때는 왼쪽 왕국이 이길 때의 반대
        if a==b:
            if p[v]==-1: continue
            else:
                p[v]=-1
                p[u]=v
        else: merge(b,a)

print(p.count(-1))
# 최종으로 살아남은 왕국은 p[idx]가 -1임 -> -1의 개수가 속국 아닌 왕국의 수
for i in range(N):
    if p[i]<0:
        # p[i]<0은 속국이 아닌 왕국이므로 이름 출력
        print(f'Kingdom of {name[i]}')
