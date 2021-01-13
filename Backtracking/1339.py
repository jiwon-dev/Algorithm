import sys
input=sys.stdin.readline
def cal(arr):
    temp=0
    for i in range(len(arr)):
        temp+=dic[arr[i]]*(10**(len(arr)-i-1))
    return temp

def solve(depth,bit):
    global count
    global ans
    count+=1
    if depth==length:
        res=0
        for a in w: res+=cal(a)
        ans=max(ans,res)
        return

    for i in range(10):
        if bit&(1<<i)==0:
            bit|=(1<<i)
            c,v=items[depth]
            dic[c]=i
            solve(depth+1,bit)
            bit&=~(1<<i)
    
N=int(input())
dic={}
w=[]
for _ in range(N):
    s=input().rstrip()
    for v in s: dic[v]=0
    w.append(s)
    
items=list(dic.items())
length=len(dic)
ans=0
count=0
solve(0,0)
print(ans)
