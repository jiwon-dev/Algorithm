# 19m 57s
ans=0
N=int(input())
dic={}
for i in range(N): dic[input()]=i
tmp=[input() for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if dic[tmp[i]]>dic[tmp[j]]: ans+=1; break
        # 기준 차량(i)의 순서보다 뒷 차량의 순서(j)가 낮을 경우 추월했다는 의미이므로 ans+=1 후 break
print(ans)
