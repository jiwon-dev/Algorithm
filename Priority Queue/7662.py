import sys
from heapq import *
input=sys.stdin.readline
# 딕셔너리만을 사용하여 1일 때 del max(d), -1일 때 del min(d)로 처리해도 됨(시간 여유가 많음)
# 35m
for _ in range(int(input())):
    k=int(input())
    maxq,minq=[],[]
    # 최대힙, 최소힙 두개 사용
    dic={}
    # 'I'인 숫자의 개수를 저장하는 딕셔너리
    # 두 개의 힙을 사용하기 때문에 개수 관리 필수
    for _ in range(k):
        l,n=input().split()
        n=int(n)
        if l=='I':
            if n in dic: dic[n]+=1
            else: dic[n]=1
            # 개수 갱신
            heappush(maxq,-n)
            # 최대힙은 부호를 반대로 넣어야하기 때문에 -를 붙여 삽입
            heappush(minq,n)
        elif not maxq or not minq: continue
        # 'D'이고 최대힙이나 최소힙이 비었으면 연산 무시
        else:
            # 'D'이고 둘 중 하나가 비지않았으면
            if n==1:
                # 최대힙에서 하나를 삭제할 때
                while maxq:
                    tmp=-heappop(maxq)
                    # 최대힙은 -를 붙여서 삽입했으므로 꺼낼때도 -를 붙여야 원래 값이됨
                    if dic[tmp]>0:
                        # dic[pop한 값]이 양수이면(우선순위큐에서도 존재한다는 의미)
                        dic[tmp]-=1
                        # pop했으므로 dic[pop한 값]-=1후 break
                        break
            else:
                # 최소힙에서 하나를 삭제할 때는 최대힙과 반대
                while minq:
                    tmp=heappop(minq)
                    if dic[tmp]>0:
                        dic[tmp]-=1
                        break
    if not minq or not maxq: print('EMPTY')
    # 둘 중에 하나라도 비었으면 EMPTY 출력
    else:
        # 아니면
        items=dic.items()
        ans=[]
        for v,c in items:
            if c>0: ans.append(v)
            # c>0은 모든 명령 후에도 값이 존재한다는 의미
            # ans에 추가
        ans.sort()
        # ans 정렬
        if not ans: print('EMPTY')
        # ans가 비었다면 EMPTY 출력
        else: print(ans[-1],ans[0])
        # 아니면 최대,최솟값 출력
    
