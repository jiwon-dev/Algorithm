import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

N,M=map(int,input().split())
S,E=map(int,input().split())
D=[tuple(map(int,input().split())) for _ in range(M)]
D.sort(key=lambda x:-x[2])
# 최대 개수를 구해야하므로 비용을 내림차순으로 정렬한 뒤, 하나씩 간선을 추가하면서
# 출발점과 도착점이 이어지는 간선이 추가되면(둘의 뿌리가 같을 경우) w 출력 후 break

p=[-1]*(N+1)
for x,y,w in D:
    x=find(x);y=find(y)
    if x!=y: p[y]=x
    if find(S)==find(E):
        print(w)
        break
else: print(0)
# 중요:출발지에서 도착지까지 갈 수 없는 경우 0을 출력
