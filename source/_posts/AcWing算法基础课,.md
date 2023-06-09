---
title: AcWing算法基础课
categories:
  - 学习笔记
tags:
  - 算法刷题笔记
toc: true# 是否启用内容索引
---
## 基础算法

#### 快速排序

```python
def quick_sort(lst,start,end):
    # 边界条件
    if start>=end:
        return None
    # 选择哨兵点
    standby=lst[(start+end)>>1]
    # 左右指针
    left=start-1
    right=end+1
    while left<right:
        left+=1
        while lst[left]<standby:
            left+=1
        right-=1
        while lst[right]>standby:
            right-=1
        if left<right:
            lst[left],lst[right]=lst[right],lst[left]
    # if j-l+1>=m:
    #     return quick_sort(nums,l,j,m)
    # else:
    #     return quick_sort(nums,j+1,r,m-(j-l+1))
    quick_sort(lst,start,right)
    quick_sort(lst,right+1,end)

import sys
n=int(input())
nums=list(map(int,sys.stdin.read().split()))
quick_sort(nums,0,len(nums)-1)
for item in nums:
    print(item,end=" ")
```

#### 选择排序

```python
n=int(input())
lst=list(map(int,input().split()))

def merge(a,b):
    lena=len(a)
    lenb=len(b)
    i=j=0
    c=[]
    while i<lena and j<lenb:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
          # ans+=len(l)-i
            c.append(b[j])
            j+=1
    if i==lena:
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c
  
def sort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)>>1
    l=sort(nums[:mid])
    r=sort(nums[mid:])
    return merge(l,r)

ret=sort(lst)
for item in ret:
    print(item,end=" ")
```

#### 二分

```python
n,m=list(map(int,input().split()))
lst=list(map(int,input().split()))
for _ in range(m):
    q=int(input())
    l=0
    r=n-1
    while l<r:
        mid=(l+r)>>1
        if lst[mid]>=q:
            r=mid
        else:
            l=mid+1
    if lst[l]!=q:
        print("-1 -1")
    else:
        print(l,end=' ')
        l=0
        r=n-1
        while l<r:
            mid=(r+l+1)>>1
            if  lst[mid]>q:
                r=mid-1
            else:
                l=mid
        print(l)
# --------
import bisect
n,m=list(map(int,input().split()))

lst=list(map(int,input().split()))

for _ in range(m):
    q=int(input())
    l=bisect.bisect_left(lst,q)
    r=bisect.bisect_right(lst,q)
    if l>=n or r<=0:
        print("-1 -1")
    elif r!=0 and lst[r-1]!=q:
        print("-1 -1")
    else:
        r-=1
        print(f'{l} {r}')
```

#### 前缀和

```python


```

#### 差分

```python
n,m=map(int,input().split())
nums=list(map(int,input().split()))
diff=[0]*(n+1)
diff[0]=nums[0]
for i in range(1,len(nums)):
    diff[i]=nums[i]-nums[i-1]
for i in range(m):
    a,b,c=map(int,input().split())
    diff[a-1]+=c
    diff[b]-=c
temp=0
for i in range(n):
    temp+=diff[i]
    print(temp,end=' ')
```

#### 双指针

```python


```

#### 位运算

```python


```

#### 离散化

```python
n,m=map(int,input().split())
all=set()
add=[]
query=[]
for _ in range(n):
    x,c=map(int,input().split())
    all.add(x)
    add.append((x,c))
for _ in range(m):
    l,r=map(int,input().split())
    all.add(l)
    all.add(r)
    query.append((l,r))
  
all=sorted(all)
nums=[0]*len(all)
nums2index={}
for i,x in enumerate(all):
    nums2index[x]=i
  
for k,v in add:
    nums[nums2index[k]]+=v

sums=[0]*(len(all)+1)

for i in range(len(nums)):
    sums[i+1]=sums[i]+nums[i]

for l,r in query:
    indexl=nums2index[l]
    indexr=nums2index[r]

    print(sums[indexr+1]-sums[indexl])

```

#### 区间和并

```python
n=int(input())
nums=[]
for _ in range(n):
    a,b=list(map(int,input().split()))
    nums.append((a,b))
nums=sorted(nums)
left,right=nums[0][0],nums[0][1]
ans=1
for i in range(1,len(nums)):
    a,b=nums[i][0],nums[i][1]
    if a<=right:
        right=max(b,right)
    else:
        ans+=1
        left,right=a,b
print(ans)
```

## 数据结构

#### 单链表

#### 双链表

#### 栈

```python
s=input()

num_stack=[]
op_stack=[]
pro={'+':1,'-':1,'*':2,'/':2}

def eval():
    b=num_stack.pop()
    a=num_stack.pop()
    op=op_stack.pop()
    if op=='+':
        num_stack.append(a+b)
    elif op=='-':
        num_stack.append(a-b)
    elif op=='*':
        num_stack.append(a*b)
    else:
        num_stack.append(int(a/b))

i=0
while i<len(s):
    if s[i].isdigit():
        temp=0
        while i<len(s) and s[i].isdigit():
            temp=temp*10+int(s[i])
            i+=1
        num_stack.append(temp)
        continue
    elif s[i]=='(':
        op_stack.append('(')
    elif s[i]==')':
        while op_stack[-1]!='(':
            eval()
        op_stack.pop()
    else:
        while op_stack and op_stack[-1]!='(' and pro[s[i]]<=pro[op_stack[-1]]:
            eval()
        op_stack.append(s[i])
    i+=1

while op_stack:
    eval()
print(num_stack[0])
```

#### 队列

#### 单调栈

```python
n=int(input())

lst=list(map(int,input().split()))


stack=[lst[0]]
ans=[-1]


for i in range(1,len(lst)):
    while stack and stack[-1]>=lst[i]:
        stack.pop()
    ans.append(stack[-1] if stack else -1)
    stack.append(lst[i])
for i in ans:
    print(i,end=' ')
```

#### 单调队列

```python
from collections import deque
n,k=map(int,input().split())
lst=list(map(int,input().split()))

ans=[]
dq=deque()
ans2=[]
dq2=deque()
for i in range(n):
    while (dq and lst[dq[-1]]<lst[i]):
        dq.pop()
    while dq and i-dq[0]>=k:
        dq.popleft()
    dq.append(i)
    ans.append(lst[dq[0]])
  
for i in range(n):
    while (dq2 and lst[dq2[-1]]>lst[i]):
        dq2.pop()
    while dq2 and i-dq2[0]>=k:
        dq2.popleft()
    dq2.append(i)
    ans2.append(lst[dq2[0]])
  
for item in ans2[k-1:]:
    print(item ,end=' ')   
print()
for item in ans[k-1:]:
    print(item ,end=' ')
```

#### Tire

```python
n=int(input())

lst=list(map(int,input().split()))

tire=[[0]*2 for i in range(3000000)]
count=0
def insert(x):
    p=0
    for i in range(32,-1,-1):
        t=(x>>i)&1
        if not tire[p][t]:
            global count
            count+=1
            tire[p][t]=count
        p=tire[p][t]
  
  
def find(x):
    p=0
    res=0
    for i in range(32,-1,-1):
        t=(x>>i)&1
        if tire[p][not t]:
            res+=(1<<i)
            p=tire[p][not t]
        else:
            p=tire[p][t]
    return res
ans=-1
for i in lst:
    insert(i)
    ans=max(ans,find(i))
  
print(ans)

```

#### 并查集

```python
n,m=map(int,input().split())

size=[1]*(n+1)
p=[i for i  in range(n+1)]
def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]
def merge(a,b):
    fa=find(a)
    fb=find(b)
    p[fa]=fb
    size[fb]+=size[fa]

for _ in range(m):
    inp=input().split()
    q=inp[0]
    if q=='C':
        a,b=int(inp[1]),int(inp[2])
        if find(a)!=find(b):
            merge(a,b)
    elif q=='Q1':
        a,b=int(inp[1]),int(inp[2])
        if find(a)==find(b):
            print("Yes")
        else:
            print('No')
    else:
        a=int(inp[1])
        print(size[find(a)])
```

#### 堆

```python
import heapq

```

#### 哈希表

```python
import sys
N=100010
n,m=map(int,sys.stdin.readline().split())
h=[0]*N
p=[0]*N
seed=131
Q=1<<64
s=' '+input()

def get(l,r):
    return (h[r]-h[l-1]*p[r-l+1])%Q
  
p[0]=1

for i in range(1,n+1):
    p[i]=(p[i-1]*seed)%Q
    h[i]=(h[i-1]*seed+ord(s[i]))%Q
  
while m:
    m-=1
    a,b,x,y=map(int,sys.stdin.readline().split())
    if get(a,b)==get(x,y):
        print("Yes")
    else:
        print("No")
```

## 搜索与图论

#### 深搜&广搜

#### 拓扑排序

```python
n,m=map(int,input().split())

from collections import defaultdict,deque
graph=defaultdict(list)
degr=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    degr[b]+=1

def topsort():
    ans=[]
    dq=deque()
    for i in range(1,n+1):
        if degr[i]==0:
            dq.append(i)
  
    while dq:
        cur = dq.pop()
        ans.append(cur)
        for neigh in graph.get(cur,[]):
            degr[neigh]-=1
            if degr[neigh]==0:
                dq.append(neigh)
  
    return ans if len(ans)==n else None

ans=topsort()
if ans:
    for i in ans:
        print(i,end=' ')
else:
    print(-1)
```

#### dijkstra

```python
from collections import defaultdict
import heapq
n,m=list(map(int,input().split()))

graph=[[-1]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c=list(map(int,input().split()))
    graph[a-1][b-1]=c if graph[a-1][b-1]==-1 else min(graph[a-1][b-1],c)
  

def dijkstra():

    dis=[float('inf')]*(n)
    dis[0]=0
    visited=set()
    min_heap=[(0,0)]
  
    # 依次确定n个点的距离
    for i in range(n):
        # 没有可达的点了
        if len(min_heap)==0:
            break
        # 未确定点最近的一个
        _,min_index=heapq.heappop(min_heap)
        visited.add(min_index)
        # 寻找邻居
        for v in range(n):
            # 可达且未访问
            if v not in visited and graph[min_index][v]>0:
                new_dis=dis[min_index]+graph[min_index][v]
                # 更新
                if dis[v]>new_dis:
                    dis[v]=new_dis
                    heapq.heappush(min_heap,(dis[v],v))
    return dis
d=dijkstra()
print(d[n-1] if d[n-1]!=float('inf') else -1)
```

```python
from collections import defaultdict
import heapq
import sys
n,m=map(int,input().split())

graph=defaultdict(list)

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a-1].append((b-1,c))
  
def dijkstra():

    dis=[float('inf')]*n
    dis[0]=0
    visit=set()
  
    min_heap=[(0,0)]
    while len(min_heap):
        _,node=heapq.heappop(min_heap)
        if node in visit:continue
        visit.add(node)
        for v,d in graph.get(node,[]):
            new_dis=dis[node]+d
            if dis[v]>new_dis:
                dis[v]=new_dis
                heapq.heappush(min_heap,(dis[v],v))
    return dis
d=dijkstra()
print(d[n-1] if d[n-1]!=float('inf') else -1)
```

#### bellman-ford

```python
from collections import defaultdict
import heapq
import sys
n,m,k=map(int,input().split())

graph=[]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph.append((a,b,c))
  
def bellmen_ford():
    dis=[float('inf')]*(n+1)
    dis[1]=0
    backup=[]
    for _ in range(k):
        backup=dis.copy()
        for a,b,c in graph:
            dis[b]=min(backup[a]+c,dis[b])
      
    if float(dis[n])>float('inf')/2 or dis[n]==float('inf'):
        return 'impossible'
    return dis[n]
ans=bellmen_ford()
print(ans)
```

#### spfa

```python
from collections import defaultdict,deque

import sys
n,m=map(int,input().split())

graph=defaultdict(list)

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
  
def spfa():
    dist = [float('inf')] * (n+1)
    dist[1] = 0  
    visited = [0] * (n+1)
    q=deque()
    q.append(1)
    visited[1]=1
    while q:
        cur=q.popleft()
        visited[cur]=0
      
        for b,c in graph.get(cur,[]):
            if dist[b]>dist[cur]+c:
                dist[b]=dist[cur]+c
                if not  visited[b]:
                    visited[b]=1
                    q.append(b)
  
    return dist[n] if dist[n]!=float('inf') else 'impossible'
ans=spfa()
print(ans)
```

#### floyd

```python
import sys
n,m,k=map(int,input().split())

dist = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    dist[a][b]=min(c,dist[a][b])
  
for i in range(n+1):
    dist[i][i]=0

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

ans=floyd()

for _ in range(k):
    a,b=map(int,sys.stdin.readline().split())
    print('impossible' if dist[a][b]==float('inf') else dist[a][b])
```

#### prime

```python
import sys
n,m=map(int,input().split())
INF=float('inf')
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[b][a]=min(c,graph[b][a])
    graph[a][b]=graph[b][a]

for i in range(n+1):
    graph[i][i]=0

def prime():
    dist= [INF] * (n+1)
    visit= [False] * (n+1)
    res=0
  
    for i in range(n):
        t=-1
        for j  in range(1,n+1):
            if not visit[j] and (t==-1 or dist[t]>dist[j] ):
                t=j
      
        if i and dist[t]==INF:return INF
        if i:res+=dist[t]
        for j in range(1,n+1):
            dist[j]=min(dist[j],graph[t][j])
      
        visit[t]=True
      
    return res

ans=prime()
print(ans if ans!=INF else 'impossible')
```

#### kruskal
```python
import sys
from collections import defaultdict

n,m=map(int,input().split())
INF=float('inf')
graph = []
p = [i for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph.append((c,a,b))
    
graph=sorted(graph)

def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def kruskal():
    res=0
    cnt=0
    for w,a,b in graph:
        a=find(a)
        b=find(b)
        if a!=b:
            p[a]=b
            cnt+=1
            res+=w
    return INF if cnt<n-1 else res

ans=kruskal()

print(ans if ans!=INF else 'impossible')

```



## 数学知识

#### 筛质数

```python
def get_prime(n):
    count=0
    isprime=[1]*(n+1)
    isprime[0]=isprime[1]=0
    for i in range(2,n+1):
        if isprime[i]:
            count+=1
        for j in range(2,n+1):
            if j*i>n:
                break
            isprime[i*j]=0
    return count
# 埃式筛法
def get_prime2(n):
    count=0
    isprime=[1]*(n+1)
    isprime[0]=isprime[1]=0
    for i in range(2,n+1):
        if isprime[i]:
            count+=1
            for j in range(2,n+1):
                if j*i>n:
                    break
                isprime[i*j]=0
    return count
# 线性筛法
def get_prime3(n):

    nums=[1]*(n+1)
    isprime=[]
    for i in range(2,n+1):
        if nums[i]:
            isprime.append(i)
        for j in range(len(isprime)):
            if i*isprime[j]>n:
                break
            nums[i*isprime[j]]=0
            if i%isprime[j]==0:
                break
    return len(isprime)
n=int(input())
print(get_prime3(n))
```

#### 约数

```python
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
```

`约数定理`

$n=\prod p_i^{a_i}= p_1^{a_1}* p_2^{a_2}*...*p_k^{a_k}$

约数个数:$f(n)=\prod (a_i+1)= (a_1+1)*(a_2+1)*...*(a_k+1)$

约数和:$\sigma(n)=\left(p_{1}^{0}+p_{1}^{1}+p_{1}^{2}+\cdots p_{1}^{a_{1}}\right)\left(p_{2}^{0}+p_{2}^{1}+p_{2}^{2}+\cdots p_{2}^{a_{2}}\right) \cdots\left(p_{k}^{0}+p_{k}^{1}+p_{k}^{2}+\cdots p_{k}^{a_{k}}\right)$

互质个数:$\phi(n)=n \times \frac{p_{1}-1}{p_{1}} \times \frac{p_{2}-1}{p_{2}} \times \ldots \times \frac{p_{k}-1}{p_{k}}$

```python
# 约数个数


# 约数之和


# 1~n中与n互质的数的个数(欧拉函数)

```

#### 欧拉函数

```python
# 筛法求欧拉函数
n=int(input())

def oula():
    nums=[1]*(n+1)
    oula=[0]*(n+1)
    oula[1]=1
    prime=[]
    for i in range(2,n+1):
        if nums[i]:
            prime.append(i)
            oula[i]=i-1
        for j in range(len(prime)):
            if i*prime[j]>n:
                break
            nums[i*prime[j]]=0
            if i%prime[j]==0:
                oula[i*prime[j]]=oula[i]*prime[j]
                break
            oula[i*prime[j]]=oula[i]*(prime[j]-1)

    return sum(oula)
print(oula())
```

#### 快速幂

```python
n=int(input())

for _ in range(n):
    a,b,c=list(map(int,input().split()))
    ans=1
    while b:
        if b&1:
            ans*=a
            ans%=c
        a*=a
        a%=c
        b//=2
    print(int(ans))
```

#### 求组合数
|数据量|数据范围|方法|复杂度|
|----|----|-----|----|
|十万|1<=b<=a<=2000|递推|$N^2$|
|一万|1<=b<=a<=$10^5$|预处理打表|$NlogN$|
|二十|1<=b<=a<=$10^18$|卢卡斯定理(Lucas)|$Plog_pm$|

```python 
# 1<=b<=a<=2000
n=int(input())
MOD=10**9+7
C=[[0]*(2005+1) for _ in range(2005+1)]
def init():
    for i in range(2005+1):
        for j in range(i+1):
            if j==0:
                C[i][j]=1
            else:
                C[i][j]=(C[i-1][j]+C[i-1][j-1])%MOD
init()
for _ in range(n):
    a,b=map(int,input().split())
    print(C[a][b])


# 1<=b<=a<=$10^5$
n=int(input())
MOD=10**9+7
N=100010
fact=[0]*(N)
infact=[0]*N
def qmi(a,b,m):
    res=1
    while b :
        if b&1:
            res=(res*a)%MOD
        a=(a*a)%MOD
        b>>=1
    return res

def init():
    fact[0]=infact[0]=1
    for i in range(1,N):
        fact[i]=(fact[i-1]*i)%MOD
        infact[i]=infact[i-1]*qmi(i,MOD-2,MOD)%MOD

init()
for _ in range(n):
    a,b=map(int,input().split())
    print(fact[a]*infact[a-b]%MOD*infact[b]%MOD)


# 1<=b<=a<=$10^18$
n=int(input())
p=0
def qmi(x,q):
    res=1
    while q:
        if q&1:
            res=res*x%p
        x=(x*x)%p
        q>>=1
    return res

def C(a,b):
    res=1
    i=1
    j=a
    for _ in range(1,b+1):
        res=(res*j)%p
        res=(res*qmi(i,p-2))%p
        i+=1
        j-=1
    return res

def lucas(a,b):
    if a<p and b<p:
        return C(a,b)
    else:
        return C(a%p,b%p)*lucas(a//p,b//p)%p

for _ in range(n):
    a,b,p=map(int,input().split())
    print(lucas(a,b))
```



#### 容斥原理

```python
n,m=map(int,input().split())
lst=list(map(int,input().split()))
res=0
for num in range(1,1<<m):
    t=1
    s=0
    for i in range(m):
        if num>>i&1:
            if t*lst[i]>n:
                t=-1
                break
            s+=1
            t*=lst[i]
    
    if t!=-1:
        if s&1:
            res+=(n//t)
        else:
            res-=(n//t)
print(res)
```

#### 博弈论
```python
n=int(input())

count=list(map(int,input().split()))

m=int(input())

store=list(map(int,input().split()))

memory=[-1]*10005

def sg(x):
    if memory[x]!=-1:
        return memory[x]
    mex=set()
    for i in count:
        if x>=i:
            mex.add(sg(x-i))
    i=0
    while True:
        if i not in mex:
            memory[x]=i
            return memory[x]
        i+=1

res=0
for num in store:
    res^=sg(num)
print('Yes' if res else 'No')
```



## 动态规划
#### 0-1背包
```python
n,m=map(int,input().split())

weight=[0]
value=[0]
for _ in range(n):
    a,b=map(int,input().split())
    weight.append(a)
    value.append(b)

def dp1():
    dp=[[0]*1005 for i in range(1005)]
    for i in range(1,n+1):
        for j in range(m+1):
            dp[i][j]=dp[i-1][j]
            if j>=weight[i]:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
    print(dp[n][m])

def dp2():
    dp=[0]*1005
    for i in range(1,n+1):
        for j in range(m,-1,-1):
            if j>=weight[i]:
                dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
    print(dp[m])
dp2()
```

#### 完全背包
```python
n,m=map(int,input().split())

weight=[0]
value=[0]
for _ in range(n):
    a,b=map(int,input().split())
    weight.append(a)
    value.append(b)

def dp1():
    dp=[[0]*1005 for i in range(1005)]
    for i in range(1,n+1):
        for j in range(m+1):
            dp[i][j]=dp[i-1][j]
            if j>=weight[i]:
                # dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i],dp[i][j-weight[i]]+value[i])

                # dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value,dp[i-1][j-2*weight]+2*value,...)
                # dp[i][j-weight]=max(dp[i-1][j-weight],dp[i-1][j-2*weight]+value,dp[i-1][j-3*weight]+2*value,...)
                # dp[i][j]=max(dp[i-1][j],dp[i][j-weight]+value)
                dp[i][j]=max(dp[i-1][j],dp[i][j-weight[i]]+value[i])
    print(dp[n][m])

def dp2():
    dp=[0]*1005
    for i in range(1,n+1):
        for j in range(m+1):
            if j>=weight[i]:
                dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
    print(dp[m])
dp2()
```

#### 多重背包
```python
n,m=map(int,input().split())

weight=[0]
value=[0]
nums=[0]
for _ in range(n):
    a,b,c=map(int,input().split())
    weight.append(a)
    value.append(b)
    nums.append(c)

def dp1():
    dp=[[0]*1005 for i in range(1005)]
    for i in range(1,n+1):
        for j in range(m+1):
            dp[i][j]=dp[i-1][j]
            for k in range(nums[i]+1):
                if j<k*weight[i]:
                    break
                dp[i][j]=max(dp[i][j],dp[i-1][j-k*weight[i]]+k*value[i])

                # dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value,dp[i-1][j-2*weight]+2*value,...)
                # dp[i][j-weight]=max(dp[i-1][j-weight],dp[i-1][j-2*weight]+value,dp[i-1][j-3*weight]+2*value,...)
                # dp[i][j]=max(dp[i-1][j],dp[i][j-weight]+value)
                # dp[i][j]=max(dp[i-1][j],dp[i][j-weight[i]]+value[i])
    print(dp[n][m])

def dp2():
    dp=[0]*1005
    for i in range(1,n+1):
        for j in range(m+1,-1,-1):
            for k in range(nums[i]+1):
                if j<k*weight[i]:
                    break

                dp[j]=max(dp[j],dp[j-k*weight[i]]+k*value[i])
    print(dp[m])
dp2()
```

#### 分组背包
```python
n,m=map(int,input().split())
from collections import defaultdict
weight=defaultdict(list)
value=defaultdict(list)

for i in range(1,1+n):
    nums=int(input())
    for j in range(nums):
        a,b=map(int,input().split())
        weight[i].append(a)
        value[i].append(b)


def dp1():
    dp=[[0]*105 for i in range(10005)]
    for i in range(1,1+n):
        for j in range(m+1):
            dp[i][j]=dp[i-1][j]
            for k in range(len(weight[i])):
                if j>=weight[i][k]:

                    dp[i][j]=max(dp[i][j],dp[i-1][j-weight[i][k]]+value[i][k])

    print(dp[n][m])

def dp2():
    dp=[0]*10005
    for i in range(1,n+1):
        for j in range(m+1,-1,-1):
            for k in range(len(weight[i])):
                if j>=weight[i][k]:
                    dp[j]=max(dp[j],dp[j-weight[i][k]]+value[i][k])
    print(dp[m])
dp2()
```

#### 最长递增子序列
```python
n=int(input())

nums=list(map(int,input().split()))

dp=[0]*n
ans=float('-inf')
for i in range(n):
    dp[i]=1
    for j in range(i):
        if nums[j]<nums[i]:
            dp[i]=max(dp[i],dp[j]+1)

    ans=max(ans,dp[i])
print(ans)
# ----------
import bisect
n=int(input())
nums=list(map(int,input().split()))

INF=float('inf')
length=[INF]*(n+1)
ans=1
length[0]=-INF
for index,num in enumerate(nums):
    i=bisect.bisect_left(length,num)
    length[i]=num
    ans=max(ans,i)
print(ans)
```
#### 最长公共子序列
```python
n,m=map(int,input().split())

s=' '+input()
t=" "+input()

dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i]==t[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m]) 
```
#### 最短编辑距离

```python
n=int(input())
s=' '+input()
m=int(input())
t=" "+input()

dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=i
for j in range(m+1):
    dp[0][j]=j

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i]==t[j]:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
        else:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
print(dp[n][m])
```

## 贪心

#### 区间覆盖
```python
s,t=map(int,input().split())
n=int(input())
pair=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a>t or b<s:
        continue
    pair.append([a,b])

pair=sorted(pair)
start=s
end=float('-inf')
count=1
i=0
while end<t and i <len(pair):
    a,b=pair[i]
    if a<=start:
        end=max(end,b)
        i+=1
    elif a>start:
        if i==0:
            break
        start=end
        count+=1
        if end>=t:
            break
        if a>end:
            end=float('-inf')
            break
print(count if end>=t else -1)
```
#### 区间分组
```python
n=int(input())
pair=[]
for _ in range(n):
    pair.append(list(map(int,input().split())))
pair=sorted(pair)

import heapq
count=[]
for i in range(len(pair)):
    a,b=pair[i]
    if len(count)==0 or a<=count[0]:
        heapq.heappush(count,b)
    else:
        heapq.heappop(count)
        heapq.heappush(count,b)

print(len(count))
```
#### 最大不相交区间
```python
n=int(input())
pair=[]
for _ in range(n):

    pair.append(list(map(int,input().split())))

pair=sorted(pair,key=lambda x:x[1])

start=pair[0][0]
end=pair[0][1]
count=1
for i in range(1,len(pair)):
    a,b=pair[i]

    if a<=end and b>end:
        continue
    elif a<=end and b<=end:
        continue
    elif a>end:
        start=a
        end=b
        count+=1
print(count)
```
#### 区间选点

```python
n=int(input())
pair=[]
for _ in range(n):

    pair.append(list(map(int,input().split())))

pair=sorted(pair)

start=pair[0][0]
end=pair[0][1]
count=1
for i in range(1,len(pair)):
    a,b=pair[i]

    if a<=end and b>end:
        start=a
    elif a<=end and b<=end:
        start=a
        end=b
    elif a>end:
        start=a
        end=b
        count+=1
print(count)
```
#### 哈夫曼树
```python
n=int(input())
nums=list(map(int,input().split()))

import heapq

heapq.heapify(nums)

ans=0
for i in range(n-1):
    a=heapq.heappop(nums)
    b=heapq.heappop(nums)
    ans+=(a+b)
    heapq.heappush(nums,a+b)

print(ans)
```
#### 耍杂技的牛
```python
n=int(input())
pair=[]
for _ in range(n):
    a,b=list(map(int,input().split()))

    pair.append((a,b))
pair=sorted(pair,key=lambda x:x[0]+x[1])


ans=float('-inf')
weight=0
for i in range(len(pair)):
    temp=weight-pair[i][1]
    ans=max(ans,temp)
    weight+=pair[i][0]
print(ans)
```

