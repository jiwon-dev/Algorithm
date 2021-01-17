import sys
input=sys.stdin.readline
# 14m (3)
K,L=map(int,input().split())
dic={}
for i in range(L):
    S=input().rstrip()
    dic[S]=i
items=list(dic.items())
items.sort(key=lambda x:x[1])
if K>len(items):
    for i in range(len(items)): print(items[i][0])
else:
    for i in range(K): print(items[i][0])
    

