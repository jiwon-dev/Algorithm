import sys
from collections import deque
input=sys.stdin.readline
# 30m 38s
# 브루트 포스 형식으로 두 그룹을 선택해서 바꾼 뒤, 남은 값을 넣어 새로운 그룹을 만들고 q에 넣는다
# 방문한 노드들을 체크 안해주면 무한 루프에 빠지기 때문에 vis라는 집합을 만들어 방문 체크 한다
A,B,C=sorted(map(int,input().split()))

q=deque()
q.append((A,B,C))
vis=set((A,B,C))
while q:
    A,B,C=q.popleft()
    if A==B==C:
        print(1)
        sys.exit()
    for i in [(2*A,B-A,C),(A,2*B,C-B),(2*A,B,C-A)]:
        i=tuple(sorted(i))
        if i not in vis:
            vis.add(i)
            q.append(i)
    '''
    u=q.popleft()
    if len(set(u))==1: print(1);sys.exit()
    for i in range(3):
        for j in range(i+1,3):
            if u[i]==u[j]: continue
            sam=(u[i],u[j])
            min_value=min(sam)+min(sam)
            max_value=max(sam)-min(sam)
            sam=(min_value,max_value,u[3-(i+j)])
            if sam in vis: continue
            q.append(sam)
            vis.add(sam)
    '''
print(0)
            
