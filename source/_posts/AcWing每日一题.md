---
title: AcWing每日一题
categories:
  - 学习笔记
tags:
  - 算法刷题笔记
toc: true
---
### 前缀和

将区间求和求差,改为两个值的运算

### 差分

前缀和的逆运算,可以在$O(1)$的时间内更新区间

### 二分

下标二分

答案二分

注意边界

### 双指针

区间问题,最大最小值,但是左指针是递增(单调性)

### 递推

根据规律或者推断,找解

### 递归

树的遍历

### 并查集

集合划分与合并

### 哈希

重复值或者出现的次数

### 单调队列

之前或者之后的最大最小值

### KMP

字符串匹配

### Trie

字典树,最大的异或对

```C++
#include <iostream>
using namespace std;

int tire[3100005][3];
int index=1;
void build(int num){
    int p=0;
    for(int i=31;i>=0;i--){
        int temp=(num>>i)&1;
        if(tire[p][temp]==0){
            tire[p][temp]=index++;
        }
        p=tire[p][temp];
    }
}
int query(int num){
    int p=0,ans=0;
	for (int i=31;i>=0;i--){
        int temp=(num>>i)&1;
        if(tire[p][!temp]){
            ans+=(1<<i);
            p=tire[p][!temp];
        }else{
            p=tire[p][temp];
        }
    }
    return ans;
}

int main()
{
    int n;
    scanf("%d",&n);
    int ans=-1;
    for(int i=0;i<n;i++){
        int t;
        scanf("%d",&t);
        build(t);
        ans=max(ans,query(t));
    }
    cout<<ans<<endl;

    return 0;
}

```

### BFS

### DFS

### 拓扑排序

### Dijkstra

Dijkstra算法是一种广泛使用的最短路径算法，可以求解从单个源节点到其他所有节点的最短路径。其基本思路是维护两个集合，一个集合存储已经确定最短路径的节点，另一个集合存储未确定路径的节点。初始时，只有源节点在已确定的路径集合中，其他节点在未确定路径的集合中。每次从未确定节点中选择距离源节点最近的节点加入到已确定路径的集合中，更新该节点到其他未确定节点的最短距离。重复此步骤直到已确定的路径集合中包含所有节点。

```python
import heapq

def dijkstra(graph):
    n = len(graph)
    dist = [float('inf')] * (n)
    dist[0] = 0  
    visited = set()

    min_heap = [(0, 0)]

    for _ in range(n):
        # 找到还没确定的里面距离最小的
        if len(min_heap)==0:
            break
        temp, min_index = heapq.heappop(min_heap)
        # 已经确定了
        visited.add(min_index)
        for v in range(n):
            if v not in visited and graph[min_index][v] > 0:
                # graph[min_index][v] > 0 表示存在这个路径
                new_dist = dist[min_index] + graph[min_index][v]
                if dist[v] > new_dist:  # 表示值得被更新
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (dist[v], v))

    return dist



n,m=list(map(int,input().split()))
graph = [[0]*(n+2) for i in range(n+2)]
for i in range(m):
    a,b=list(map(int,input().split()))
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

ans=dijkstra(graph)   
for item in ans[1:n]:
	print(item)

```

### 质数问题

筛质数

1.埃氏筛 $O(NloglogN)$
`可优化`

```C++
const int N=1e6+5;
bool vis[N];
void esieve(int n){//标记0~n的数字的质数状态,并统计质数个数
	vis[0]=vis[1]=1;//0，1属于非质数
	for(int i=2;i<=n;i++){//标记剩下的2~n的数字的状态
		if(vis[i]==0){//判断i是不是质数 思考：为什么这样就能判断i是质数？
			for(int j=2*i;j<=n;j+=i){//遍历范围内的i的倍数
				vis[j]=1;//将倍数标记为1（非质数）
			}
		}
	}
}
```

`优化后`

```C++
const int N=1e6+5;
bool vis[N];
void esieve(int n){//标记0~n的数字的质数状态,并统计质数个数
    vis[0]=vis[1]=1;
	for(int i=2;i*i<=n;i++){//标记剩下的2~n的数字的状态 优化：到根号n即可停止
		if(vis[i]==0){//判断i是不是质数 
			for(int j=i*i;j<=n;j+=i){//遍历范围内的i的倍数 从i*i开始，减少重复筛选
				vis[j]=1;//将倍数标记为1（非质数）
			}
		}
	}
}
```

2.欧拉筛 $O(N)$  线性筛

```C++
const int N=1e8+5;
bool vis[N];//标记数组
int prime[N/10];//质数表，存放质数
int erla(int n){
	vis[0]=vis[1]=1;//0.1不是质数
	int cnt=0;//统计质数的个数
	for(int i=2;i<=n;i++){
		if(!vis[i]){//判断i是不是质数
			prime[cnt++]=i;//将质数存到质数表中
		}
		//遍历质数表 新序列 prime[j]*i
		for(int j=0;prime[j]*i<=n&&j<cnt;j++){
			vis[prime[j]*i]=1;//标记组成的序列为非质数
			if(i%prime[j]==0) break;//prime[j]是i的最小质因子 ，不能继续组合，避免重复
		}
	}
	return cnt;//返回质数个数
}

```

3.欧拉函数
`对正整数n欧拉函数是小于或等于n的正整数中与n互质的数的数目`

```C++
bool vis[N];//标记数组
int prime[N];//质数表，存放质数
int phi[N];
int erla(int n){
	vis[0]=vis[1]=1;//0.1不是质数
	int cnt=0;//统计质数的个数
	phi[1]=1;//1的欧拉函数值是1
	for(int i=2;i<=n;i++){
		if(!vis[i]){//判断i是不是质数
			prime[cnt++]=i;//将质数存到质数表中
			phi[i]=i-1;//性质1
		}
		//遍历质数表 新序列 prime[j]*i
		for(int j=0;prime[j]*i<=n&&j<cnt;j++){
			vis[prime[j]*i]=1;//标记组成的序列为非质数
			if(i%prime[j]==0){
				phi[i*prime[j]]=prime[j]*phi[i];//性质2
				break;//prime[j]是i的最小质因子 ，不能继续组合，避免重复
			}else{
				phi[i*prime[j]]=(prime[j]-1)*phi[i];//性质3
			}
		}
	}
	return cnt;//返回质数个数
}
```

### 最大公约数

### 最近公共祖先

### 排列组合
