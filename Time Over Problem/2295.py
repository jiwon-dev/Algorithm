import sys
input=sys.stdin.readline
# 1시간 이상
# 풀이:u[i]+u[j]+u[k]=u[l]일 때, u[i]+u[j]=u[l]-u[k]로 두고 u[i],u[j] 값들을 배열에 넣고 k,l를 가지고 이분 탐색함
# u[i]+u[j]를 오름차순으로 sum_l 배열에 넣었으므로 이분 탐색 가능
n=int(input())
u=sorted([int(input()) for _ in range(n)])
# 입력받을 때 오름 차순으로 정렬해줘야 u[i]+u[j]도 정렬 없이 오름차순 가능
sum_l=[]
for i in range(n):
    for j in range(i+1):
        sum_l.append(u[i]+u[j])
        # u[i]+u[j]값들을 오름 차순으로 sum_l 배열에 넣음
        # i를 기준으로 j는 i보다 작거나 같은 인덱스이므로 u[i]보다 작은 값들임
        # [2,3,5,10,18]로 이중 포문 돌려보면 두 개의 합이 정렬하지 않아도 오름차순으로 들어감을 알 수 있음 -> 이분 탐색 가능
ans=0
for k in range(n-1,-1,-1):
    # 답을 빨리 찾기 위해 뒤에서 부터 살펴 봄
    for l in range(n-1,k-1,-1):
        start,last=0,len(sum_l)-1
        while start<=last:
            mid=(start+last)//2
            if sum_l[mid]==u[l]-u[k]:
                ans=max(ans,u[l])
                break
            elif sum_l[mid]<u[l]-u[k]:
                start=mid+1
            else:
                last=mid-1
print(ans)
