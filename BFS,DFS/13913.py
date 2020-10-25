import sys
from collections import deque
input=sys.stdin.readline
# 33m 48s
# visited 리스트는 idx의 값을 만드는데 거쳐온 이전 값을 담음
# disc 리스트는 최소 방법
n,k=map(int,input().split())
visited=[0]*100001
disc=[-1]*100001
disc[n]=0

if n==k:
    # 주어진 두 값이 같다면 예외 처리
    print(0)
    print(n)
    sys.exit()
q=deque()
q.append(n)
while q:
    u=q.popleft()
    for v in (2*u),(u-1),(u+1):
        if 0<=v<=100000 and disc[v]==-1:
            # 100000 사이고 처음 방문했다면 visited에 이전 값(u)를 추가하고 disc를 1 늘림
            disc[v]=disc[u]+1
            visited[v]=u
            if disc[k]!=-1:
                # 목표 값에 방문했다면 visited[k]부터 n까지 거꾸로 거쳐온 값들을 구함
                print(disc[k])
                ans=[k]
                # 거쳐온 값 저장 리스트
                s=k
                while True:
                    if s==n or visited[s]==n:
                        ans.append(n)
                        break
                    ans.append(visited[s])
                    s=visited[s]
                print(*ans[::-1],sep=' ')
                # 거꾸로 구했으니 출력할 때는 반대로 출력
                sys.exit()
            q.append(v)
    
