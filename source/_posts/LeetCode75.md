---
title: LeetCode75
categories:
  - 学习笔记
tags:
  - 算法刷题笔记
toc: true# 是否启用内容索引
---

## LeetCode75学习计划

### 第一天
[1480.一维数组的动态和](https://leetcode.cn/problems/running-sum-of-1d-array/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

思路:前缀和

```python
# python的内置数据方法
# https://docs.python.org/3/library/itertools.html
# accumulate([1,2,3,4,5]) --> 1 3 6 10 15

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))

```

[724.寻找数组的中心下标](https://leetcode.cn/problems/find-pivot-index/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

思路: 先求前缀和,然后遍历下标,利用前缀和计算下标两边的和,左右两端的位置需要判断一下

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum=list(accumulate(nums))
        length=len(nums)
        if pre_sum[length-1]-pre_sum[0]==0:
            return 0

        for index in range(1,length-1):
            if pre_sum[index-1]==pre_sum[length-1]-pre_sum[index]:
                return index
        # 返回最左边下标,防止有x,x,x,x,..0,0,0,0的情况
        if pre_sum[length-2]==0:
            return length-1
        return -1
```

### 第二天

[205. 同构字符串](https://leetcode.cn/problems/isomorphic-strings/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

思路:每个字符串对应位置的字母是一一对应的,用字典.
两个方向,一个是s对t的字母是一一对应,一个是t对s的字母是一一对应

```python
class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        dic=defaultdict(str)
        for index,item in enumerate(s):
            # 检查s对t
            if item not in dic:
                # 检擦t对s
                if t[index] not in dic.values():
                    dic[item]=t[index]
                else:
                    return False
            else:
                if dic[item]!=t[index]:
                    return False
        return True

    
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s,t):
            dic=defaultdict(str)
            for index,item in enumerate(s):
                if item not in dic:
                    dic[item]=t[index]
                else:
                    if dic[item]!=t[index]:
                        return False
            return True
        return check(s,t) and check(t,s)

```

[392. 判断子序列](https://leetcode.cn/problems/is-subsequence/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

思路:判断子序列,两个字符串不同位置的比较,双指针,ab指针,如果对应字符一样,都前进,如果不一样,指向母字符串的前进


```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length=len(s)
        if length==0:return True
        index=0
        for item in t:
            if item==s[index]:
                index+=1
            if index==length:
                return True
        return False
```

>332周赛

[6355. 统计公平数对的数目](https://leetcode.cn/problems/count-the-number-of-fair-pairs/)
思路:对数组排序,对每一个数,用二分找到大小在lower和upper之间的下标,如果这个数也在下标中就-1,最后结果除2,(i,j)(j,i)都算了

bilibili:两个数的和,枚举一个数,用其他方法处理另一个数

[6356. 子字符串异或查询](https://leetcode.cn/problems/substring-xor-queries/)
思路:对每一个查询,a^b=c => a=c^b,然后把a转换成二进制字符串,剩下的就是在字符串中找子字符串在起始位置

bilibili:预处理s中的二进制,把子字符串转换成数字存进dict,直接找a

[6357. 最少得分子序列](https://leetcode.cn/problems/subsequence-with-the-minimum-score/)
没做出来思路:计算最长公共子序列,统计不在最长公共子序列中的下标,就是要删除的下标(可能错在需要找到最左边的最长子序列)



bilibili:
1.删除[left,right]中间的几个和删除全部是一样的
2.枚举s,把s从中间划分,前面匹配t的前部分,后面匹配t的后部分
3.中间就是可以删掉的部分,找到最小的
4.实现的时候,先从后往前匹配s和t(全部匹配),然后从前往后,找到相应的答案


### 第三天


[21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

思路:双指针比较交替,问题就是开头的细节,一种是用一个空链表头,一种就是先比较ab的大小直接赋值ab的头


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a:return b
        if not b:return a
        # 空表头
        prehead=ListNode(0)
        pre=prehead
        while a and b:
            if a.val>b.val:
                pre.next=b
                b=b.next
            else:
                pre.next=a
                a=a.next
            pre=pre.next
        pre.next=a if a else b
        return prehead.next
```

[206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

思路:反转链表需要标记连续的三个节点,a,b,c  把b指向a,然后a,b,c依次向后移动一个,注意边界情况


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, a: Optional[ListNode]) -> Optional[ListNode]:
        if not a:return a
        if not a.next:return a 
        b=a.next
        c=a.next.next
        # 这个地方不断掉会死循环
        a.next=None
        while b:
            b.next=a
            if not c:break
            a=b
            b=c
            c=c.next
        return b

```



### 第四天

[876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

思路:把链表存成数组,找数组长度一半的节点


```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        while head:
            nums.append(head)
            head=head.next
        length=len(nums)
        return nums[length//2]
```
其他解法:1.第一次计算长度,第二次找节点  2.快慢指针

[142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)

自己错误思路:快慢指针,只能检查是否有环,找不到入口

思路:1.字典存已经走过的  2.快慢指针经过数学推导计算

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=dict()
        while head:
            if head in nums.keys():
                return head
            else:
                nums[head]=1
                head=head.next
        return head
```



### 第五天

[121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:如果今天减去昨天的利润,加上之前的利润小于0,说明今天是巨亏的,不如之前的不买,买今天的,如果今天减去昨天的利润,加上之前的利润仍然大于0,记录一下,继续往后加,说不定会涨

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        profit=0
        for index in range(1,len(prices)):
            if prices[index]-prices[index-1]+profit<0:
                profit=0
            else:
                profit+=prices[index]-prices[index-1]
            ans=max(ans,profit)
        return ans
```


[409. 最长回文串](https://leetcode.cn/problems/longest-palindrome/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:统计字符的数量,注意加上一个奇数就行

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m=defaultdict(int)
        for item in s:
            m[item]+=1
        ans=0
        flag=0
        for k,v in m.items():
            if v&1:
                 flag=1
                 v-=1
            ans+=v
        return ans+flag
```

### 第六天

[589. N 叉树的前序遍历](https://leetcode.cn/problems/n-ary-tree-preorder-traversal/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:二叉树的深搜,变成了多叉树的深搜

```python
class Solution:
    def preorder(self, a: 'Node') -> List[int]:
        ans=[]

        def dfs(root):
            if not root:return ans
            ans.append(root.val)
            for chi in root.children:
                dfs(chi)
        dfs(a)
        return ans 
```

[102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:广搜,用一个额外的层数变量标记当前节点在第几层

其他思路:记录当前栈内有几个节点,然后遍历完这些节点,这些节点之后的就是下一层的节点

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        deq=[]
        if not root:return []
        deq.insert(0,(root,0))
        last=0
        curlayer=[]
        while len(deq):
            (temp,layer)=deq.pop()
            if layer!=last:
                ans.append(curlayer)
                last=layer
                curlayer=[]
            curlayer.append(temp.val)
            if temp.left:
                deq.insert(0,(temp.left,layer+1))
            if temp.right:
                deq.insert(0,(temp.right,layer+1))
        ans.append(curlayer)
        return ans
```

### 第七天


[704. 二分查找](https://leetcode.cn/problems/binary-search/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:正常二分,right要到能遍历到的边界

[二分的细节&边界](https://leetcode.cn/problems/binary-search/solutions/8337/er-fen-cha-zhao-xiang-jie-by-labuladong/)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)>>1
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
        return -1 if nums[mid]!=target else mid
```




[278. 第一个错误的版本](https://leetcode.cn/problems/first-bad-version/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:二分查找的变换版,区别在于要记录mid量,纯二分是找到mid直接返回,这个找到的可能不是需要的

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=1,n
        ans=1
        while left<=right:
            mid=(left+right)>>1
            if isBadVersion(mid):
                right=mid-1
                ans=mid
            else:
                left=mid+1
        return ans
```

### 第八天


[98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


错误思路:不能判断当前节点之后,然后再去分别判断左右子树

正确×思路: 每棵左右子树节点的大小范围应该都是low-up,初始low=-inf,up=inf,左子树的范围是(low,root.val) 右子树是(root.val,up)  **官方题解也是错的**

其他:二叉搜素树中序遍历一定是升序的

[树的几种遍历](https://www.bilibili.com/video/BV14G411P7C1/?vd_source=602787b9249cd70cfca4def5e041f060)

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=1,n
        ans=1
        while left<=right:
            mid=(left+right)>>1
            if isBadVersion(mid):
                right=mid-1
                ans=mid
            else:
                left=mid+1
        return ans
```


[235. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:1.寻找祖先路径,找到第一个不同的位置  2.一次遍历,如果都小就都找左边,如果都大就都找右边,如果有小有大就找到了分界点

```python
class Solution:
    def lowestCommonAncestor(self, r: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if r.val>p.val and r.val>q.val:
                r=r.left
            elif r.val<p.val and r.val < q.val:
                r=r.right
            else:
                return r
```




### 第九天
[733. 图像渲染](https://leetcode.cn/problems/flood-fill/description/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:广搜/深搜找同颜色的,上下左右判断边界,访问数组

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:       
        n=len(image) 
        m=len(image[0])
        visited=[[0]*m for _ in range(n)]
        dq=deque()
        dq.append((sr,sc))
        oldcolor=image[sr][sc]
        while dq:
            x,y=dq.popleft()
            image[x][y]=color
            visited[x][y]=1
            for x_,y_ in [(0,1),(0,-1),(-1,0),(1,0)]:
                if x_+x>=0 and x_+x<n and y_+y>=0 and y_+y<m:
                    if visited[x_+x][y_+y]:
                        continue
                    if image[x_+x][y_+y]==oldcolor:
                        dq.append((x_+x,y_+y))
            
        return image
```

[200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/description/)


思路:深搜/广搜,从某点开始把连在一起的都访问一次,记录一共从几个点开始,这些点都是不同的岛屿

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid) 
        m=len(grid[0])
        visited=[[0 if grid[i][j]=='1' else 1  for j in range(m)] for i in range(n)]
        ans=0
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    ans+=1
                    dq=deque()
                    dq.append((i,j))
                    while dq:
                        x,y=dq.popleft()
                        visited[x][y]=1
                        for x_,y_ in [(0,1),(0,-1),(-1,0),(1,0)]:
                            if x_+x>=0 and x_+x<n and y_+y>=0 and y_+y<m:
                                if not visited[x_+x][y_+y]:
                                    visited[x_+x][y_+y]=1
                                    dq.append((x_+x,y_+y))
            
        return ans
```


>333周赛

[6365. 将整数减少到零需要的最少操作数]()
思路1:刚开始以为要转成二进制的01传,看0多还是1多,如果0多直接返回1的数量,但是668错了
思路2:打表100000之内2的次方,然后二分查找n在那两个数中间,找距离近的这个数的插值,然后+1递归下去,54->64-54=10->10-8=2->0

bilibili:找到最低为的1,考虑这个1 是直接减掉还是加上同位置的1 ,枚举这两种可能.

`判断一个数是不是2的幂:(x & ( x-1 ))==0`

`找到最低位的1:lowbit: x & -x`

[☆6364. 无平方子集计数]()

没思路:题型重灾区,应该是用dp做,但是毫无思路

bilibili:对不起,等我学有所成再来看,什么jb玩意那么难

[6363. 找出对应 LCP 矩阵的字符串]()

没思路



### 第十天

[509. 斐波那契数](https://leetcode.cn/problems/fibonacci-number/description/)


思路:.

```python
# 1.自顶向下,记忆化搜索
# 2.自底向上,dp数组
# 3.用a,b两个变量,空间复杂度降到O(1)
# 4.矩阵快速幂,时间复杂度降到O(logn)
```



[70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)


思路:.

```python
# 斐波那契数列模板题
```


### 第十一天

[746. 使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/description/)


思路:爬到今天的费用只能有两个来源,前一个和前两个,但是顶楼数组里没有,所以追加一个0,第一层第二层的费用就是本身,第二层为什么不是min(第一层,第二层)呢,因为如果是从第一层上到的第二层,第二层还要继续向上上,那么还得加上第二层的费用,就变成了(第一层+第二层)的费用了

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n=len(cost)
        # dp=[99999]*(n)
        a=cost[0]
        b=cost[1]
        c=b
        for i in range(2,n):
            c=min(a,b)+cost[i]
            a,b=b,c
            # dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return c

```

[62. 不同路径](https://leetcode.cn/problems/unique-paths/description/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:深搜和广搜的复杂度应该是$O(2^n)$,会超时,还是dp,当前位置只能从左边或者上边来到,就把左边和上边的方案数加起来就行,第一行第一列的方案数都是1

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=[1 for j in range(n) ]
        b=[1 for j in range(n) ]
        for i in range(1,m):
            for j in range(1,n):
                b[j]=a[j]+b[j-1]
            a=b[:]
        return b[-1]

        # dp=[[0 for j in range(n) ]  for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j==0:
        #             dp[i][j]=1
        #         else:
        #             dp[i][j]=dp[i][j-1]+dp[i-1][j]
        # return dp[m-1][n-1]

        # dq=deque([(0,0)])
        # ans=0
        # while dq:
        #     x,y=dq.pop()
        #     if x==m-1 and y==n-1:
        #         ans+=1
        #     for x_,y_ in  [(x+1,y),(x,y+1)]:
        #         if x_>=0 and x_<m and y_>=0 and y_<n:
        #             dq.append((x_,y_))
        # return ans 
```



### 第十二天


[438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:双指针维护长度为第二个字符串的区间,对区间内的数字统计数量,数量一致答案加1,右移的时候,右侧字符加1,左侧字符减1

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def val(a,b):
            for i,j in zip(a,b):
                if i!=j:
                    return False
            return True
        pnums=[0]*26
        snums=[0]*26
        constant=ord('a')
        for item in p:
            pnums[ord(item)-constant]+=1
        left=right=0
        lengths=len(s)
        lengthp=len(p)
        ans=[]
        while right<lengths:
            snums[ord(s[right])-constant]+=1
            if val(snums,pnums):
                ans.append(left)
            right+=1
            if right>=lengthp:
                snums[ord(s[left])-constant]-=1
                left+=1
        return ans 
```


[424. 替换后的最长重复字符](https://leetcode.cn/problems/longest-repeating-character-replacement/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:没有思路,考虑到了应该是用双指针

题解:双指针加一个maxhistory记录最多的相同字符个数,如果当前区间长度大于了k+maxhistory,说明不可能变成一样的,左边右移1,否则说明当前区间不是最大长度,还可增加新元素

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        constant=ord('A')
        length=len(s)
        # 左右指针
        left=right=0
        # 用于记录left-right区间每个字母的个数
        nums=[0]*26
        # 用于记录区间内出现的 最多的相同字符的个数
        historymax=0
        while right<length:
            # 新加的字符个数加1
            nums[ord(s[right])-constant]+=1
            # 更新一下区间内最长的字符个数
            historymax=max(historymax,nums[ord(s[right])-constant])
            # historymax+k 是目前可以达到的最长长度,已经包含了右节点了
            # 小于说明现在这个区间长度还小于最大长度
            # 大于说明把其它不是最多出现的字符替换以后，都不能填满这个滑动的窗口，说明此时 k 不够用
            # 这个时候须要考虑左边界向右移动
            if right-left+1>historymax+k:
                nums[ord(s[left])-constant]-=1
                left+=1
            right+=1
        return right-left
```

### 第十三天

[1. 两数之和](https://leetcode.cn/problems/two-sum/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:数组排序,然后对每个数字,二分查找target减去她的值

题解:用字典存储每个target-num的值,如果当前数字在字典中存在,找到答案,否则把target减他存进去

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=[(i,n) for i,n in enumerate(nums)]
        # nums=sorted(nums,key=lambda x:x[1])
        # length=len(nums)
        # for i in range(length):
        #     ttt=target-nums[i][1]
        #     index=bisect_left(nums,ttt,key=lambda x:x[1])
        #     if index==i:continue
        #     if index<0 or index>=length:continue
        #     if nums[index][1]==ttt:
        #         return [nums[i][0],nums[index][0]]
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
```


[299. 猜数字游戏](https://leetcode.cn/problems/bulls-and-cows/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:A数字好统计,对于B数字,分别存A,B中数字出现的个数,加入对他们重新排序,一定是只能匹配个数少的,所以直接取每个数字二者中的最小值,求和就是B.


```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hasA=[0]*10
        hasB=[0]*10
        A=0
        for i,j in zip(secret,guess):
            if i==j:
                A+=1
            else:
                hasA[int(j)]+=1
                hasB[int(i)]+=1

        ans=sum([min(a,b) for a,b in zip(hasA,hasB)])

        return f'{A}A{ans}B'
```


### 第十四天


[844. 比较含退格的字符串](https://leetcode.cn/problems/backspace-string-compare/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:忘记用栈了，从后往前遍历数组，cnt记录当前#的数量，然后跳过cnt个字母。

题解:用栈，遇见#退一个字符

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(a):
            length=len(a)
            ans=[]
            cnt=0
            for i in range(length-1,-1,-1):
                if a[i]=='#':
                    cnt+=1
                else:
                    if cnt==0:
                        ans.append(a[i])
                    else:
                        cnt-=1
            return ans
        return check(s)==check(t)
```


[394. 字符串解码](https://leetcode.cn/problems/backspace-string-compare/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:栈操作，一个数组存数字，一个栈用来弹字符，遇见]一直弹，直到弹出[。然后复制数字数组的最后一个数字便，在加入栈中，数字的处理有一点点麻烦

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        nums=[]
        length=len(s)
        i=0
        while i<length:
            if s[i]==']':
                temp=[]
                while stack[-1]!='[':
                    temp.append(stack.pop())
                stack.pop()
                temp="".join(temp[::-1])
                stack.append(temp*nums[-1])
                nums.pop()
                i+=1
            elif s[i].isnumeric():
                n=0
                while i<length  and s[i].isnumeric():
                    n*=10
                    n+=int(s[i])
                    i+=1
                nums.append(n)

            else:
                stack.append(s[i])
                i+=1
        return "".join(stack)
```


### 第十五天

[1046. 最后一块石头的重量](https://leetcode.cn/problems/last-stone-weight/description/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:大项堆，但是python的heapq只能实现小项堆，大项堆的实现要加负号


```python
class Solution:
    def lastStoneWeight(self, x: List[int]) -> int:
        x=list(map(lambda x:-x,x))
        # 这一步的作用不是很明确
        # 注意heapify(包括heapq封装的其他操作)都不会更改数据结构(仍为list)，只会以堆的操作规范对其进行处理。
        # 虽然类型仍为list，但元素的顺序已经满足了堆的规范，所以从线性的角度看结果列表并非是有序的(是[1, 3, 7, 9, 5]而非[1, 3, 5, 7, 9])
        heapq.heapify(x)
        while len(x)>1:
            a=heapq.heappop(x)
            b=heapq.heappop(x)
            if a!=b:
                newstore=abs(max(a,b)-min(a,b))
                heapq.heappush(x,-newstore)
            
        return -x[0] if len(x) else 0
```

[692. 前K个高频单词](https://leetcode.cn/problems/top-k-frequent-words/?envType=study-plan&id=leetcode_75_level_1&plan=leetcode_75&plan_progress=jr2hbvs)


思路:Counter统计单词数量，然后按照数量降序，字典序升序排列，返回k个

题解：优先队列，元组（单词，词频）

知识点：1.Counter的most_common()在计数相同的情况下是按出现顺序返回
2.python多关键字排序：

```python 
arr=[(1,4,3),(1,3,3),(2,1,4),(3,5,1)]
arr.sort(key=lambda s:(s[0],-s[1])) 
#两个关键字排序,在需要倒序排列的关键字前加`-`号

```

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words).items()
        c = sorted(c,key=lambda x:(-x[1],x[0]))
        return list(map(lambda x:x[0],c[:k]))
        # return sorted((cnt := Counter(words)).keys(), key=lambda key: (-cnt[key], key))[:k]
```

### 总结