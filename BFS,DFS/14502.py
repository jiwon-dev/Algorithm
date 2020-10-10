import sys
from collections import deque
input=sys.stdin.readline
# 53m 06s
# bfs,브루트 포스 이용
# 원리:0의 위치를 모두 리스트에 담아서 3중 for문을 이용해 펜스 설치할 수 있는 3개의 위치에 펜스를 설치하고
# 바이러스를 다 퍼트린 뒤, 0의 개수의 최댓값이 답이다
# 모든 경우의 수를 다 살펴봐야하기 때문에 초기화가 중요하다
# 최대 8x8이기 때문에 O(n*m*64C3)에 해결 가능
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
memory=[]
# grid를 초기 입력받은 값으로 초기화 하기 위해 memory라는 리스트를 이용
dx,dy=[-1,1,0,0],[0,0,-1,1]
virus=deque()
# 모든 바이러스의 위치를 담는 deque -> 모든 바이러스가 증식하기 때문에 bfs 이용
c_virus=deque()
# virus를 초기 바이러스의 위치로 초기화 하기 위해 c_virus라는 deque를 이용
zero=[]
# 모든 0의 위치를 담는 리스트(펜스 설치를 위해 모든 0의 위치를 살펴봐야하기 때문에 필요)
for i in range(n):
    sam=[]
    for j in range(m):
        if grid[i][j]==2:
            # 2이면 바이러스이므로 virus,c_virus에 담음
            virus.append([i,j])
            c_virus.append([i,j])
        elif not grid[i][j]:
            # 0이면 안전지역이므로 zero에 담음
            zero.append([i,j])
        sam.append(grid[i][j])
    memory.append(sam)
    # 초기 입력받은 값과 같게 만들기 위해 memory에 담음

def initiate():
    # virus,grid를 초기값으로 초기화 하기 위한 함수
    for i in range(n):
        for j in range(m):
            grid[i][j]=memory[i][j]
    # grid를 memory를 이용해 초기값으로 초기화
    for v in c_virus:
        virus.append(v)
    # virus를 c_virus를 이용해 초기값으로 초기화

def cal():
    # bfs한 뒤, 0의 개수(안전지역)를 세는 함수
    cnt=0
    for i in range(n):
        for j in range(m):
            if not grid[i][j]:
                cnt+=1
    return cnt

def bfs(visited):
    # 모든 바이러스 위치에서 상하좌우로 퍼짐
    while virus:
        for _ in range(len(virus)):
            a,b=virus.popleft()
            for i in range(4):
                aa,bb=a+dx[i],b+dy[i]
                if 0<=aa<n and 0<=bb<m and not visited[aa][bb] and not grid[aa][bb]:
                    visited[aa][bb]=1
                    grid[aa][bb]=2
                    # 바이러스가 퍼졌으므로 2로 수정
                    virus.append([aa,bb])
                    # 퍼진 바이러스가 또 퍼질 수 있으므로 virus에 추가

ans=0       
for i in range(len(zero)):
    for j in range(i+1,len(zero)):
        for k in range(j+1,len(zero)):
            # 3중 for문으로 모든 펜스 설치할 수 있는 곳에 설치하면서 cal()로 안전지역의 최댓값 찾음
            grid[zero[i][0]][zero[i][1]]=1
            grid[zero[j][0]][zero[j][1]]=1
            grid[zero[k][0]][zero[k][1]]=1
            # 3개의 펜스 설치
            visited=[[0]*m for _ in range(n)]
            # 방문한지 체크하는 리스트
            bfs(visited)
            # bfs 시작(모든 바이러스를 퍼트림)
            ans=max(ans,cal())
            # 최댓값 찾는 과정
            initiate()
            # 3개의 펜스를 설치했을 때 안전지역을 살펴봤으므로 다음 펜스를 치기위해 virus,grid를 초기화해줌
print(ans)
            
