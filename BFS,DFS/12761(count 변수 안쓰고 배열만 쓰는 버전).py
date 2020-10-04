import sys
from collections import deque
input=sys.stdin.readline
# visit를 -1로 초기화 해놓고 8방향 돌 때마다 수를 늘려감
a,b,n,m=map(int,input().split())
visit=[-1]*100001
# 초기 횟수는 -1로 지정
visit[n]=0
# n에서 시작하므로 0으로 초기화
def bfs(s):
    # bfs와 비슷하나 visit 배열은 방문 표시 뿐만 아니라 횟수도 저장하게 끔 바꿈
    q=deque([s])
    while q:
        if visit[m]!=-1:
            # visit[m]이 -1이 아니라는 뜻은 n에서 m까지 도달하는 최소 방법이 나왔다는 뜻이므로 visit[m] 출력하고 탈출
            print(visit[m])
            break
        n=q.popleft()
        # 일반적인 bfs 방법
        for nx in n-1,n+1,n-a,n+a,n-b,n+b,n*a,n*b:
            # 8가지 이동하는 경우의 수를 탐색
            if 0<=nx<=100000 and visit[nx]==-1:
                # nx가 돌의 개수에 맞고 아직 방문하지 않았다면
                visit[nx]=visit[n]+1
                # visit[n]에서 visit[nx]로 한 번에 가므로 visit[nx]=visit[n]+1
                # 이게 쌓이면 3,4,5... 이렇게 늘어남
                q.append(nx)
                # nx를 방문하지 않았고 0에서 10만 사이이므로 q에 넣음
bfs(n)
