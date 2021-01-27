import sys
from collections import deque
# 09m 37s
input=sys.stdin.readline
for _ in range(int(input())):
    N,M=map(int,input().split())
    D=list(map(int,input().split()))
    q=deque()
    # 덱 사용
    for i in range(N): q.append((i,D[i]))
    # 덱에 (인덱스, 중요도) 추가

    res=[]
    while q:
        idx,doc=q[0]
        # 제일 앞에 있는 문서를 기준으로 뒤에 중요도가 높은 문서가 있다면 인쇄하지 않고 q에 다시 넣음
        # 아니면, res(정답 배열)에 넣음
        cnt=0
        for j in range(1,len(q)):
            # 제일 앞에 있는 문서를 기준으로 하기 때문에 j는 1부터 시작
            if q[j][1]>doc: cnt+=1
            # 제일 앞 문서의 중요도보다 큰 문서가 있으면 개수 증가
        if cnt>0: q.append(q.popleft())
        # 중요도가 큰 문서가 하나 이상이면 인쇄하지 않고 q에 제일 뒤에 배치
        else: res.append(q.popleft())
        # 아니면 res(정답)에 추가

    for i in range(N):
        if res[i][0]==M: print(i+1); break
        
    
