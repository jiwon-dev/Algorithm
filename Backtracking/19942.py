import sys
input=sys.stdin.readline
# 17m 09s
INF=float('inf')
def solve(p,f,s,v,cost,bit,idx):
    # (단백질,지방,탄수화물,비타민,가격,선택한 식재료 비트,중복 선택 방지를 위한 idx)
    global ans
    if p>=mp and f>=mf and s>=ms and v>=mv:
        # depth와 상관없이 조건만 맞으면 갱신 후 return -> 최소 값이므로 더 탐색할 필요없으니 가지치기로 끊음
        temp=[]
        # 선택한 식재료 번호를 담는 리스트
        for i in range(N):
            if bit&(1<<i): temp.append(i+1)
            # 비트마스크로 확인해서 1이면 temp에 넣음
        ans=min(ans,[cost,temp])
        # [최소 비용, 만약 같으면 사전 순으로 가장 빠른 것]이니 min을 사용
        return
    
    for i in range(idx,N):
        # 백트래킹 과정
        # i를 idx부터 시작하는 이유: 0부터 시작하게 되면 (1,2,3,4,5)와 (1,3,2,4,5)가 같음에도 불구하고 두 번 비교하기 때문에 가지치기로 잘라줌
        if not visited[i]:
            visited[i]=True
            # i를 선택하지 않았으면 i 선택
            bit|=(1<<i)
            # i를 선택하지 않았으면 비트로 표시
            solve(p+S[i][0],f+S[i][1],s+S[i][2],v+S[i][3],cost+S[i][4],bit,i)
            # 재귀로 백트래킹 실행
            bit&=~(1<<i)
            # 한 사이클이 돌면 비트 되돌림
            visited[i]=False
            # 한 사이클이 돌았으니 방문 해제
            
N=int(input())
mp,mf,ms,mv=map(int,input().split())
S=[list(map(int,input().split())) for _ in range(N)]
visited=[False]*N
ans=[INF,[INF]*N]
solve(0,0,0,0,0,0,0)
if ans[0]==INF: print(-1)
else:
    print(ans[0])
    print(*ans[1])
