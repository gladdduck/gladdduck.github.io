---
title: LeecCode剑指offer1
categories:
  - 学习笔记
tags:
  - 算法刷题笔记
toc: true# 是否启用内容索引
---


## LeecCode剑指offer1刷题记录

### 第一天

[剑指 Offer 09. 用两个栈实现队列](https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:一个栈1用于进,一个栈2用于出,当2空了,就把1里面的元素全部放进2,如果此时1也空了,那就是都空了

```python
class CQueue:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)
    def deleteHead(self) -> int:
        if len(self.stack_out):
            return self.stack_out.pop()
        else:
            if len(self.stack_in):
                while len(self.stack_in):
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()
            else:
                return -1
```
[剑指 Offer 30. 包含min函数的栈](https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:一个单独的栈x存最小值,如果进栈的元素小于等于x最顶元素就进x,如果出栈元素等于x顶层元素,x出栈

```python
class MinStack:
    def __init__(self):
        self.stack=[]
        self.minnums=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not len(self.minnums) or x<=self.minnums[-1]:
            self.minnums.append(x)
    def pop(self) -> None:
        if self.stack[-1]==self.minnums[-1]:
            self.stack.pop()
            self.minnums.pop()
        else:
            self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def min(self) -> int:
        return self.minnums[-1]
```

### 第二天

[剑指 Offer 06. 从尾到头打印链表](https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.遍历一遍链表,用数组存每个元素,然后返回数组的逆序 2.递归

```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans=[]
        while head:
            ans.append(head.val)
            head=head.next
        return ans[::-1]
        # return self.reversePrint(head.next) + [head.val] if head else []
```


[剑指 Offer 24. 反转链表](https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.三个指针,模拟列表断开向后连接的情景,2.把链表元素都存在数组里,当作一个个单独的节点,反过来连接

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:return head
        re=[]
        while head:
            re.append(head)
            temp=head.next
            head.next=None
            head=temp
        re.reverse()
        print(re)
        ret=None
        for i in range(len(re)):
            if ret is None:
                ret=re[i]
            else:
                ret.next=re[i]
                ret=ret.next
        return re[0]
```


[剑指 Offer 35. 复杂链表的复制](https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

错误思路:不能像普通链表一样遍历重新连接,因为random指针的节点可能还没遍历到

思路:1.递归  2.把A-B-C的链表  改造成A-A'-B-B'-C-C',然后模仿原指针的下一个位置,主要各个边界条件的判断

```python
# 拼接+拆分
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None :return None
        temphead=head
        while head:
            temp=Node(head.val)
            temp.next=head.next
            head.next=temp
            head=head.next.next
        head=temphead
        while head:
            if head.random:
                head.next.random=head.random.next
            head=head.next.next
        orighead=head=temphead.next
        ans=head
        while head:
            if head.next is None:
                break
            temp=orighead.next.next
            head.next=orighead.next.next
            head=head.next
            orighead=temp
        return ans
```

```C++
// Hash表+递归
class Solution {
public:
    unordered_map<Node*, Node*> cachedNode;

    Node* copyRandomList(Node* head) {
        if (head == nullptr) {
            return nullptr;
        }
        if (!cachedNode.count(head)) {
            Node* headNew = new Node(head->val);
            cachedNode[head] = headNew;
            headNew->next = copyRandomList(head->next);
            headNew->random = copyRandomList(head->random);
        }
        return cachedNode[head];
    }
};
```



### 第三天
[剑指 Offer 05. 替换空格](https://leetcode.cn/problems/ti-huan-kong-ge-lcof/description/)

思路:先用数组比直接返回str.replace时间空间上都要快不少

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)
```

[剑指 Offer 58 - II. 左旋转字符串](https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:.

```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]
```


### 第四天

[剑指 Offer 03. 数组中重复的数字](https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.字典存 2.排序 3.一直交换到已有

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        m=dict()
        for i in nums:
            if i in m:
                return i
            m[i]=1

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

```



[剑指 Offer 53 - I. 在排序数组中查找数字 I](https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/description/)

思路:二分,然后下标加到不是这个数

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index=bisect_left(nums,target)
        length=len(nums)
        ans=0
        while index<length and nums[index]==target:
            ans+=1
            index+=1
        return ans
```

[剑指 Offer 53 - II. 0～n-1中缺失的数字](https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.直接遍历 2.hash 3.位运算 4.应该的和-实际的和=差的数字 5.二分

```python
# 后面加n个数 一起异或,缺的数只会出现一次,相同的数异或两次为-
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # ans=0
        # for index,num in enumerate(nums):
        #     ans^=index
        #     ans^=num
        # return ans^len(nums)
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)>>1
            if nums[mid]==mid:
                left=mid+1
            else:
                right=mid-1
        return left
```



### 第五天

[剑指 Offer 11. 旋转数组的最小数字](https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:根据凹的性质一次遍历,如果找不到那么就是递增的,直接返回numbers[0]

```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(1,len(numbers)):
            if numbers[i]<numbers[i-1]:
                return numbers[i]
        return numbers[0]
```


[剑指 Offer 50. 第一个只出现一次的字符](https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.OrderedDict   2.Counter

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        m=OrderedDict()
        for i in s:
            m[i]=m.get(i,0)+1
        for k,v in m.items():
            if v==1:
                return k
        return ' '
        # frequency = collections.Counter(s)
        # for i, ch in enumerate(s):
        #     if frequency[ch] == 1:
        #         return ch
        # return ' '

```


[剑指 Offer 04. 二维数组中的查找](https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.对每一行二分$O(N*log(N))$ 2.把矩阵向左旋转90度就是一个搜索树,从底向上搜索,
每次可消去一行或者一列 $O(N+M)$

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:return False
        m=len(matrix[0])
        n=len(matrix)
        i,j=n-1,0
        while i>=0 and j<m:
            if matrix[i][j]>target:
                i-=1
            elif matrix[i][j]<target:
                j+=1
            else:
                return True
        return False
```




### 第六天

[剑指 Offer 32 - I. 从上到下打印二叉树](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:广搜

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:return []
        stack=collections.deque([root])
        ans=[]
        while len(stack):
            cur=stack.popleft()
            ans.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        return ans
```

[剑指 Offer 32 - II. 从上到下打印二叉树 II](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.广搜存节点的时候新增一个layer表示在第几层 2.每一次遍历完队列中的所有节点 3.记录每一层的最后一个节点
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        stack=collections.deque([(root,1)])
        ans=[]
        temp=[root.val]
        lastlayer=-1
        while len(stack):
            (cur,layer)=stack.popleft()
            if layer!=lastlayer:
                ans.append(temp)
                temp=[]
            if cur.left:
                stack.append((cur.left,layer+1))
                temp.append(cur.left.val)
            if cur.right:
                stack.append((cur.right,layer+1))
                temp.append(cur.right.val)
            lastlayer=layer
        return ans

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
```

[剑指 Offer 32 - III. 从上到下打印二叉树 III](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:在上面一题的基础上,在新增每一层的时候,用一个标志,奇数正加,偶数反加

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        stack=collections.deque([(root,1)])
        ans=[]
        temp=[root.val]
        lastlayer=0
        while len(stack):
            (cur,layer)=stack.popleft()
            if layer!=lastlayer:
                if layer&1:
                    ans.append(temp)
                else:
                    ans.append(temp[::-1])
                temp=[]
            if cur.left:
                stack.append((cur.left,layer+1))
                temp.append(cur.left.val)
            if cur.right:
                stack.append((cur.right,layer+1))
                temp.append(cur.right.val)
            lastlayer=layer
        return ans
```


### 第七天


[剑指 Offer 26. 树的子结构](https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1. 先找到子树的根节点,然后对比剩下的部分是否一样,判断条件比较多  2.三种情况,一个是从当前节点比,一个是左子树的子树,一个是右子树的子树

```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
```
[剑指 Offer 27. 二叉树的镜像](https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/description/)

思路:递归交换左右子树

```python
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:return None
        l,r=None,None
        if root.left:
            r=self.mirrorTree(root.left)
        if root.right:
            l=self.mirrorTree(root.right)
        root.right,root.left=r,l
        return root
```


[剑指 Offer 28. 对称的二叉树](https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

错误思路:只比较了左右子树,没有从全局对比

题解:1.两个指针,反过来比(一个从左往右走,一个从右往左走)  2.交换左右子树再递归查询

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(a,b):
            if a is None and b is None:
                return True
            if a is None and b :
                return False
            if b is None and a:
                return False
            if a.val != b.val:
                return False
            return check(a.left,b.right) and check(a.right,b.left)
        
        return check(root,root)
```
### 第八天

[剑指 Offer 10- I. 斐波那契数列](https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)
[剑指 Offer 10- II. 青蛙跳台阶问题](https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.递归  2.记忆递归 3.动态规划 4.空间优化的动态规划

```python
class Solution:
    def fib(self, n: int) -> int:
        if n==0:return 0
        a=0
        b=1
        for i in range(2,n+1):
            a,b=b,a+b
            a%=1e9+7
            b%=1e9+7
        return int(b)
```

[剑指 Offer 63. 股票的最大利润](https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:保存最小的价格 一次遍历,比较答案和今天减去最小价格,更新最小价格

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices)==0:
        #     return 0
        # ans=0
        # leftprofit=0
        # buyprice=prices[0]
        # for index in range(1,len(prices)):
        #     if prices[index]-prices[index-1]+leftprofit>=0:
        #         leftprofit=prices[index]-prices[index-1]+leftprofit
        #         ans=max(ans,leftprofit)
        #     else:
        #         buyprice=prices[index]
        #         leftprofit=0
        # return ans
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
```


### 第九天


[剑指 Offer 42. 连续子数组的最大和](https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:如果之前的加上当前的是负数,那就把当前的当作开始

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     nums[i] += max(nums[i - 1], 0)
        # return max(nums)
        pre = 0
        maxAns = nums[0]
        for x in nums:
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)
        return maxAns
```

[剑指 Offer 47. 礼物的最大价值](https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:二维DP基础

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # n=len(grid)
        # m=len(grid[0])
        # dp=[[0]*m for _ in range(n)]
        # dp[0][0]=grid[0][0]
        # for i in range(1,n):
        #     dp[i][0]=dp[i-1][0]+grid[i][0]
        # for i in range(1,m):
        #     dp[0][i]=dp[0][i-1]+grid[0][i]
        # for i in range(1,n):
        #     for j in range(1,m):
        #         dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        # return dp[n-1][m-1]
        m, n = len(grid), len(grid[0])
        for j in range(1, n): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
```

### 第十天

[剑指 Offer 46. 把数字翻译成字符串](https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:如果和当前的数和前面的数组合小于26,当前的情况就可以由前一个数的情况加上前两个数的情况得到,如果大于25,那就只是能前面的情况

```python
class Solution:
    def translateNum(self, num: int) -> int:
        num=str(num)
        length=len(num)
        if length==1:
            return 1
        a=1
        b=0
        if int(num[0])*10+int(num[1])<=25 and int(num[0])*10!=0:
            b=2
        else:
            b=1
        for index,item in enumerate(num[2:],2):
            if int(num[index-1])*10+int(num[index])<=25  and int(num[index-1])*10!=0:
                b,a=a+b,b
            else:
                b,a=b,b
        return b
        '''
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a
        '''
```



[剑指 Offer 48. 最长不含重复字符的子字符串](https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:双指针维护当前不含重复字符的区间,用字典存区间里的字符,如果当前区间新增了一个不重复的,就更新答案,如果加了一个重复的,左指针一直移到不重复的点

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        length=len(s)
        ans=0
        count=dict()
        
        while right<length:
            if count.get(s[right],-1)==-1:
                count[s[right]]=1
                right+=1
                ans=max(ans,right-left)
            else:
                count[s[left]]=-1
                left+=1
        return ans 
```

### 第十一天

[剑指 Offer 22. 链表中倒数第k个节点](https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:遍历一遍得到长度,然后找到length-k的节点


[剑指 Offer 18. 删除链表的节点](https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:存好前一个节点

### 第十二天

[剑指 Offer 25. 合并两个排序的链表](https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:归并排序的合并

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=ListNode(-1)
        pre=ans
        while l1 and l2:
            if l1.val<l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2=l2.next
            pre=pre.next
        pre.next=l1 if l1 else l2
        return ans.next
```


[剑指 Offer 52. 两个链表的第一个公共节点](https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:A链表一个指针A,B链表一个指针B,如果A指针遍历完A了,就指向B链表,B同理,这两相当于把两个链表拼接了,AB-BA,这样解决了长度不一致的问题

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA,pB=headA,headB
        while pA or pB:
            if pA==pB:
                return pA
            if pA:
                pA=pA.next
            else:
                pA=headB
            if pB:
                pB=pB.next
            else:
                pB=headA
        return None
```



### 第十三天

[剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:双指针,类似快排

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        length=len(nums)
        left,right=0,length-1
        while left<right:
            flag=False
            while  left<length and  nums[left]&1:
                left+=1
                flag=True
            while right>=0 and  nums[right]&1==0:
                right-=1
                flag=True
            if left>right:
                return nums
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums
```
[剑指 Offer 57. 和为s的两个数字](https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:双指针,一个从左一个从右,根据当前和的大小,移动指针


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        left,right=0,length-1
        while left<right:
            if nums[left]+nums[right]>target:
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                return [nums[left],nums[right]]
        return None
```
[剑指 Offer 58 - I. 翻转单词顺序](https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:分词转置,用队列手动实现


```python
class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        return " ".join(word[::-1])
```
### 十四天
[剑指 Offer 12. 矩阵中的路径](https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:从每一个格子dfs搜索


```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length=len(word)
        n=len(board)
        m=len(board[0])
        visited=[[0]*m for _ in range(n)]

        def dfs(cur,x,y):
            if board[x][y]!=word[cur]:
                return False
            if cur==length-1:
               return True
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                x_,y_=x+i,y+j
                if 0<=x_<n and 0<=y_<m and not visited[x_][y_]:
                    visited[x_][y_]=1
                    if dfs(cur+1,x_,y_):
                        return True
                    visited[x_][y_]=0
        
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    visited[i][j]=1
                    if dfs(0,i,j):
                        return True
                    visited[i][j]=0
        return False
```

[面试题13. 机器人的运动范围](https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:1.dfs搜索  2.两个for循环遍历,用字典存已访问


```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def check(a,b):
            t=0
            for num in chain(str(a),str(b)):
                t+=int(num)
            if t<=k:
                return True
            return False
        # visited={}
        # ans=0
        # def dfs(x,y):
        #     for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        #         x_,y_=x+i,y+j
        #         if 0<=x_<n and 0<=y_<m and (x_,y_) not in visited:
        #             visited[(x_,y_)]=1
        #             if check(x_,y_):
        #                 nonlocal ans
        #                 ans+=1
        #                 dfs(x_,y_)
        # if k>=0:
        #     ans+=1
        #     visited[(0,0)]=1
        #     dfs(0,0)
        # return ans
        visited={}
        visited[(0,0)]=1
        for i in range(n):
            for j in range(m):
                if ((i-1,j) in visited or (i,j-1) in visited) :
                    if check(i,j):
                        visited[(i,j)]=1
        return len(visited)
```
### 第十五天
[剑指 Offer 34. 二叉树中和为某一值的路径](https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:dfs搜索并存储路径

题解:广搜,存节点的父节点,找到和之后反着找路径


```python
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:return []
        ans=[]
        def dfs(curnode,cursum,path):  # s起点，e终点
            if not curnode.left and not curnode.right:
                if cursum == target:
                    nonlocal ans
                    ans.append(path[:])
                return 
            if curnode.left:
                path.append(curnode.left.val)
                dfs(curnode.left,cursum+curnode.left.val,path)
                path.pop()
            if curnode.right:
                path.append(curnode.right.val)
                dfs(curnode.right,cursum+curnode.right.val,path)
                path.pop()
        dfs(root,root.val,[root.val])
        return ans
```

[剑指 Offer 36. 二叉搜索树与双向链表](https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:类似线索二叉树的构造,一个指针存上一个节点,注意的是第一个节点和最后一个节点的处理

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:return root
        self.pre=None
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            if not self.pre:
                self.head=cur
            else:
                self.pre.right,cur.left=cur,self.pre
            self.pre=cur
            dfs(cur.right)
        dfs(root)
        self.head.left=self.pre
        self.pre.right=self.head
        return self.head
```

[剑指 Offer 54. 二叉搜索树的第k大节点](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:1.中序遍历,输出数组的k大节点  2.在遍历二叉树的时候,先搜右子树,再搜左子树,记录当前节点是第几大


```python
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        cnt=0
        ans=-1
        def dfs(curnode):  # s起点，e终点
            nonlocal cnt
            if cnt>k:return 
            if curnode.right:
                dfs(curnode.right)
            if cnt+1==k:
                nonlocal ans
                ans=curnode.val
            cnt+=1
            if cnt>k:return 
            if curnode.left:
                dfs(curnode.left)
        dfs(root)
        return ans
```
### 第十六天
[面试题45. 把数组排成最小的数](https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:根据数字排序,具体的,A,B两个数, 转为字符串拼接成AB和BA,逐个比较两个的大小,小的放前面,为什么转为AB,不同的数字不影响,比如123,124,主要防止这种情况1230和123,或者123和1234 ,这两个数字应该是在答案中挨在一起的,组合成AB,BA就是答案需要的最小数


```python
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(a,b):
            a=str(a)
            b=str(b)
            tempa=a
            a+=b
            b+=tempa
            for i,j in zip(a,b):
                if i<j:
                    return -1
                if i>j:
                    return 1
            return 0


        nums.sort(key=functools.cmp_to_key(cmp))
        print(nums)
        return "".join(map(str,nums))
```

[面试题61. 扑克牌中的顺子](https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路：没读懂题目

题解: 就是判断五个数是不是连着的,但是大小王可以当作任何数. 判断不能有重复且最大值-最小值+大小王的数量应该小于5


```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子 
```
### 第十七天
[剑指 Offer 40. 最小的k个数](https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:1.排序  2.堆排序  3.快速排序:如果当前作为基数的这个值下标正好是k,那么他左边的就是前k小的数,否则分开排序左右两边


```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # if k==0:return []
        # a=[-arr[i] for i in range(k)]
        # heapq.heapify(a)
        # for item in arr[k:]:
        #     if -item > a[0]:
        #         heapq.heappushpop(a,-item)
        # return list(map(lambda x:-x,a))
        if k==0:return []
        if k>=len(arr):return arr
        def quick_sort(l,r):
            i,j=l,r
            while i<j:
                while i<j and arr[j]>=arr[l]:j-=1
                while i<j and arr[i]<=arr[l]:i+=1
                
                arr[i],arr[j]=arr[j],arr[i]
            arr[i],arr[l]=arr[l],arr[i]
            if k<i:return quick_sort(l,i-1)
            if k>i:return quick_sort(i+1,r)
            return arr[:k]
        
        return quick_sort(0,len(arr)-1)

```

[剑指 Offer 41. 数据流中的中位数](https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:1.二分查找插入位置,保持数组有序  2.两个优先队列,一个存左半部分一个存右半部分,固定一个是奇数,或者两个都是偶数,这样取值的时候固定取一个一个队列或者两个一起取,存值的时候,也要注意奇偶数


```python
from heapq import *
class MedianFinder:
    def __init__(self):
        # self.list=[]
        # self.length=0
        # 存小  /大项堆
        self.A=[]
        # 存大   /小项堆
        self.B=[]

    def addNum(self, num: int) -> None:
        # if self.length==0:
        #     self.list.append(num)
        # else:
        #     index=bisect.bisect_left(self.list,num)
        #     self.list.insert(index,num)
        # self.length+=1

        if (len(self.A)+len(self.B))&1:
            heappush(self.A,-heappushpop(self.B,num))
        else:
            heappush(self.B,-heappushpop(self.A,-num))

    def findMedian(self) -> float:
        # if self.length&1:
        #     return self.list[self.length//2]
        # else:
        #     return (self.list[self.length//2-1]+self.list[self.length//2])/2
        if (len(self.A)+len(self.B))&1:
            return self.B[0]
        return (self.B[0]-self.A[0])/2
```
### 第十八天
[剑指 Offer 55 - I. 二叉树的深度](https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:广搜的层次遍历,深搜也行


```python
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        ans=0
        que=deque()
        que.append(root)

        while que:
            length=len(que)
            for i in range(length):
                cur=que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans+=1
        
        return ans 

```

[剑指 Offer 55 - II. 平衡二叉树](https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:和上面一题同理,都是计算树的深度,这题递归求比较方便


```python
class Solution:
    ans=True
    def isBalanced(self, root: TreeNode) -> bool:
        def aaa(cur):
            if not cur:return 0
            if not cur.left and not cur.right:
                return 1
            left=self.isBalanced(cur.left)
            right=self.isBalanced(cur.right)
            if abs(left-right)>1:
                print(left,right)
                self.ans=False
            return max(left,right)+1
        aaa(root)
        return self.ans
```


### 第十九天

[剑指 Offer 64. 求1+2+…+n](https://leetcode.cn/problems/qiu-12n-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:无,

题解:利用逻辑运算的短路性质当作if判断,n>1的时候 执行递归,否则就是直接短路了


```python
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
```

[剑指 Offer 68 - I. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:如果两个值都小于当前节点,则递归搜索左子树,如果都大于当前节点,递归搜索右子树,否则当前节点就是公共祖先


```python
class Solution:
    def __init__(self):
        self.ans=None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return root
        def do(cur):
            if p.val<cur.val and q.val<cur.val:
                do(cur.left)
            elif p.val>cur.val and q.val > cur.val:
                do(cur.right)
            else:
                self.ans=cur
        do(root)
        return self.ans
```



[剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode.cn/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.dfs搜索一遍存父节点 然后用字典存一个节点的父节点,搜另一个节点时,如果父节点存在就是祖先  2.在深搜的时候,分条件,如果 节点分别在左右子树  或者 一个节点在子树,另一个节点就是当前节点,那么就是答案

```python
class Solution:
    ans=None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def dfs(cur):
        #     if not cur :return False
        #     left=dfs(cur.left)
        #     right=dfs(cur.right)
        #     if (left and right) or ((left or right) and (cur==p or cur == q)):
        #         self.ans=cur
        #     return left or right or cur==p or cur == q
        # dfs(root)
        # return self.ans
        fa={}
        def dfs(cur):
            if cur.left:
                fa[cur.left.val]=cur
                dfs(cur.left)
            if cur.right:
                fa[cur.right.val]=cur
                dfs(cur.right)
        fa[root.val]=None
        dfs(root)
        vis={}
        while p:
            vis[p]=1
            p=fa[p.val]
        while q:
            if q in vis:
                return q
            q=fa[q.val]
        return None
```

### 第二十天

[剑指 Offer 07. 重建二叉树](https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)
思路:根据两个遍历顺序,画图分析一下,递归的建树就行


```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre,ino):
            if len(pre)==0:
                return None
            root=TreeNode(pre[0])
            root_index=ino.index(pre[0])
            root.left=build(pre[1:1+root_index],ino[:root_index])
            root.right=build(pre[1+root_index:],ino[root_index+1:])
            return root
        return build(preorder,inorder)

```

[剑指 Offer 33. 二叉搜索树的后序遍历序列](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)
思路:二叉搜索树,中序遍历是顺序的,有了后序遍历,排序一下就得到了中序遍历,看看这两个序列能不能建成一个树,能建成就是正确的后续遍历,否则就不是,用了一下上一题的代码


```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        inorder=sorted(postorder)
        flag=True
        def build(pre,ino):
            if len(pre)==0:
                return None
            root=TreeNode(pre[-1])
            try:
                root_index=ino.index(pre[-1])
                root.left=build(pre[:root_index],ino[:root_index])
                root.right=build(pre[root_index:-1],ino[root_index+1:])
            except:
                nonlocal flag
                flag=False
            return root
        a=build(postorder,inorder)
        print(a)
        return flag
```


[剑指 Offer 16. 数值的整数次方](https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)
思路:快速幂,但是要注意的是n的正负数,奇数就单独乘一次x,偶数就乘x的平方


```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n>0:
            while n > 0:
                if n & 1:  
                    res *= x
                x *= x
                n >>= 1  
        else:
            n=abs(n)
            while n > 0:
                if n & 1:  
                    res /= x
                x *= x
                n >>= 1  
        return res
```

### 第二十一天

[剑指 Offer 15. 二进制中1的个数](https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)
思路:位移与1


```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while n:
            if n&1:
                ans+=1
            n>>=1
        
        return ans 
```



[剑指 Offer 65. 不用加减乘除做加法](https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)
思路:位运算,我选择不做


```python
MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1

class Solution:
    def add(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a
```

### 第二十二天

[剑指 Offer 56 - I. 数组中数字出现的次数](https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)
思路:两个相同的数异或为0,但是数据里面有两个只出现一次的数,把数据全部异或一遍之后,结果就是这两个数异或的结果,从后往前遍历这个结果,遇见的第一个1,就是这两个数不同的位置,然后根据这个位置把数组分成两份,这两份里面的数字异或完就剩下只出现一次的数字


```python
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        n,x,y,m=0,0,0,1

        for item in nums:
            n^=item
        while n&m==0:
            m<<=1
        for item in nums:
            if item&m:
                x^=item
            else:
                y^=item
        return [x,y]
```



[剑指 Offer 56 - II. 数组中数字出现的次数 II](https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:统计每一位上1出现的次数,然后对3取余,剩下位置上的1组成的数字就是只出现一次的


```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        counts=list(map(lambda x:x%3,counts))
        ans=0
        for j in range(32):
            if counts[j]:
                temp=1<<j
                ans^=temp
        return ans
```

### 第二十三天

[剑指 Offer 39. 数组中出现次数超过一半的数字](https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:1.常规排序或者计数  2.使用投票,随机选取一个数字,如果后面的数字等于他,票数加1,否则票数-1,如果票数为0,就重新换一个数字选择


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        # 验证 x 是否为众数
        # for num in nums:
        #     if num == x: count += 1
        # return x if count > len(nums) // 2 else 0 # 当无众数时返回 0
        return x

```


[剑指 Offer 66. 构建乘积数组](https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:正过来乘一遍,乘上之前的数,反过来乘一遍,乘上之后的数


```python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        length=len(a)
        ans=[]
        temp=1
        for index,item in enumerate(a):
            ans.append(temp)
            temp*=item
        temp=1
        for index in range(length-1,-1,-1):
            ans[index]*=temp
            temp*=a[index]
        return ans
```


### 第二十四天

[剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:双指针维护一个区间

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans=[]
        cursum=0
        left,right=1,1
        while left<target:
            if cursum>target:
                cursum-=left
                left+=1
            elif cursum<target:
                cursum+=right
                right+=1
            else:
                ans.append(list(range(left,right)))
                cursum-=left
                left+=1
        return ans

```




[剑指 Offer 14- I. 剪绳子](https://leetcode.cn/problems/jian-sheng-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:dp,当前的数字,可以由比他小的任意两个数的乘积得到,这两个数同样可以由比他们小的乘积得到


```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:return 1
        if n==3:return 2
        dp=[0]*(n+1)
        dp[2]=2
        dp[3]=3
        dp[4]=4
        for i in range(5,n+1):
            for j in range(2,i):
                dp[i]=max(dp[i],dp[i-j]*dp[j])
        return dp[n]
        # 只考虑2,3就行,证明略
        #  dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])
        # 只考虑分成2,3
```



[剑指 Offer 62. 圆圈中最后剩下的数字](https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:模拟会超时,每次删除一个数字,就相当于把后面的数字挪到前面了,根据这个性质,逆着推,在前面加上m个数,然后对当前的数据量取余,就得到了这个数字的原始位置


```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # nums=list(range(n))
        # start=0
        # while len(nums)!=1:
        #     length=len(nums)
        #     num=nums[(start+m-1)%length]
        #     nums.remove(num)
        #     start=(start+m-1)%length
        # return nums[0]
        x=0
        for i in range(1,n+1):
            x=(x+m)%i
        return x
```
### 第二十五天

[剑指 Offer 29. 顺时针打印矩阵](https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:一圈圈的模拟,从左往右,从上往下,从右往左,从下往上,坐标在左上角和右下角,每次走完一行都修改边界


```python
class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res
```



[剑指 Offer 31. 栈的压入、弹出序列](https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:如果是正确的顺序,那么一进一出,肯定是正好的,两个队列一起操作,遇到出栈顺序的数字就出栈,模拟,不正确的顺序栈内最后会剩下元素

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, j = [], 0
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return len(st) == 0
```

### 第二十六天

[剑指 Offer 20. 表示数值的字符串](https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:根据题目要求分别实现判断是不是小数,是不是整数,是不是科学计数(根据e分开,然后利用前两个函数),然后一起判断

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        def isint(a):
            if len(a)==0:
                return False
            if a[0]=='-' or a[0]=='+':
                a=a[1:]
            if len(a)==0:
                return False
            for item in a:
                if not item.isdecimal():
                    return False
            return True
        
        def isfloat(a):
            if len(a)==0:
                return False
            if a[0]=='-' or a[0]=='+':
                a=a[1:]
            if len(a)==0:
                return False
            if a=='.':
                return False
            flag=True
            for index,item in enumerate(a):
                if not item.isdecimal():
                    if item =='.' and flag:
                        flag=False
                        continue
                    return False
            return True

        def isnum(a):
            if len(a)==0:
                return False
            if a[0]=='-' or a[0]=='+':
                a=a[1:]
            if len(a)==0:
                return False
            index=0
            if 'e' in a:
                index=a.index('e')
            elif 'E' in a:
                index=a.index('E')
            else:
                return False
            front=a[:index]
            end=a[index+1:]
            return (isfloat(front) or isint(front)) and isint(end)

        return isint(s) or isfloat(s) or isnum(s)
```

[面试题67. 把字符串转换成整数](https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:一个个字符遍历转为int,要判断是否越界了

```python
class Solution:
    def strToInt(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        flag=1
        if s[0]=='-':
            s=s[1:]
            flag=-1
        elif s[0]=='+':
            s=s[1:]
        if len(s)==0:
            return 0
        if s[0].isalpha():
            return 0
        index=0
        ans=0
        while index<len(s) and s[index].isdecimal() :
            ans=ans*10+int(s[index])
            index+=1
        INT_MAX=(1<<31)-1
        INT_MIN=-(1<<31)
        if ans*flag>INT_MAX:
            return INT_MAX
        if ans*flag<INT_MIN:
            return INT_MIN
        return ans*flag
```
### 第二十七天

[面试题59 - II. 队列的最大值](https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:利用一个单调栈(递减栈)记录队列里的最大值,出栈的时候判断是不是单调栈的第一个元素,进栈的时候判断一下和栈顶元素的大小关系,把小于他的都弹出来(因为只要他在,前面的数的最大值都是他)

```python
import queue

class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.maxqueue = queue.deque()
    def max_value(self) -> int:
        if len(self.maxqueue)==0:
            return -1
        return self.maxqueue[0]
    def push_back(self, x: int) -> None:
        self.queue.put(x)
        while self.maxqueue and x>self.maxqueue[-1]:
            self.maxqueue.pop()
        self.maxqueue.append(x)
    def pop_front(self) -> int:
        if not self.maxqueue:
            return -1
        temp=self.queue.get()
        if temp==self.maxqueue[0]:
            self.maxqueue.popleft()
        return temp
```

[剑指 Offer 59 - I. 滑动窗口的最大值](https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)

思路:可以直接用上一题的代码,维护一个区间,队列的长度就是区间的长度,每次进一个就弹出一个,获取队列,里面的最大值

题解:单调队列实现

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq=MaxQueue()
        for item in nums[:k-1]:
            deq.push_back(item)
        
        ans=[]
        for item in nums[k-1:]:
            deq.push_back(item)
            ans.append(deq.max_value())
            deq.pop_front()
        return ans

```

### 第二十八天

[剑指 Offer 38. 字符串的排列](https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:深搜,全排列,但是不能重复,用位运算来表示访问标识符

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        length=len(s)
        visited=0
        ans=set()
        def dfs(index,cur):
            if index==length:
                ans.add("".join(cur))
                return
            for i in range(length):
                nonlocal visited
                if not (1<<i)&visited:
                    visited|=(1<<i)
                    dfs(index+1,cur+[s[i]])
                    visited^=(1<<i)
        dfs(0,[])
        return list(ans)

```

[剑指 Offer 37. 序列化二叉树](https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:就是用某种方式存树,然后再把存的树还原成原本的树

题解:层次遍历(深搜的三种遍历树不唯一),把一层的所有节点都存起来,包括空节点

```python
import collections
class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            cur=queue.popleft()
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append('null')
        return '['+",".join(res)+']'
        

    def deserialize(self, data):
        if data=='[]':return 
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur=queue.popleft()
            if vals[i]!='null':
                temp = TreeNode(int(vals[i]))
                cur.left=temp
                queue.append(temp)
            i+=1
            if vals[i]!='null':
                temp = TreeNode(int(vals[i]))
                cur.right=temp
                queue.append(temp)
            i+=1
        return root

```

### *第二十九天

[剑指 Offer 19. 正则表达式匹配](https://leetcode.cn/problems/zheng-ze-biao-da-shi-pi-pei-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:类似字符串最短编辑距离,$dp[i][j] $代表 $s[:i]$ 与 $p[:j]$ 是否可以匹配。s是字符串,p是模式串

- 当p[j]=='*'时:
  1. dp[i][j-2]:不记这个字符,当作他出现0次  s='' p="c*"
  2. dp[i-1][j] and s[i]==p[j-1]:  *前面的字符和s这个位置上的字符一样
  3. dp[i-1][j] and '*'==p[j-1]:  *前面的字符是.,随意匹配 (这两种情况可以视作,当前的p和s已经匹配了,s又加入了一个新字符,看这个新字符和p的最后一个是不是一样)

- 当p[j]!='*'时:
  1. dp[i-1][j-1] and s[i-1]==p[j-1]:前面的都能匹配,看当前位置的两个字符是不是一样
  2. dp[i-1][j-1] and '.'==p[j-1]: .随意匹配

实现的时候注意,dp的下标是从1开始,但是s,p的下标是从0开始,公式里面的sp下标要多减个1


```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1,m):
            for j in range(1,n):
                if p[j-1]=='*':
                    if dp[i][j-2] or ( s[i-1]==p[j-2] and dp[i-1][j]) or  ( p[j-2]=='.' and dp[i-1][j]):
                        dp[i][j]=True
                else:
                    if ( p[j-1]=='.' and dp[i-1][j-1]) or (( p[j-1]==s[i-1] and dp[i-1][j-1])):
                        dp[i][j]=True

        return dp[m-1][n-1]


```

[剑指 Offer 49. 丑数](https://leetcode.cn/problems/chou-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:当前的数位x,下一个数一定是$(a*2,b*3,c*5)$之中最小的一个,而且$(a,b,c)$一定是之前的某个丑数:用三个指针,如果下一个是当前的指针指的数,这个指针加1指向下一个数,刚开始都指向1

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 最小堆
        dp=[0]*n
        dp[0]=1
        a,b,c=0,0,0
        for i in range(1,n):
            dp[i]=min(dp[a]*2,dp[b]*3,dp[c]*5)
            if dp[i]==dp[a]*2:
                a+=1
            if dp[i]==dp[b]*3:
                b+=1
            if dp[i]==dp[c]*5:
                c+=1
        
        return dp[n-1]
```

[剑指 Offer 60. n个骰子的点数](https://leetcode.cn/problems/nge-tou-zi-de-dian-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:首先要知道,n个筛子可以扔出多少个点:[n,6n],共5*n+1个点,每个点,可以从少一个筛子的情况下得到,f(n,x)表示n个筛子得到x点
![](https://image.yayan.xyz/20230327180014.png)


$f(n,x)=f(n-1,x)+f(n-1,x-2)+,..,f(n-1,x-6)$得到,但是这样会越界

上一层的x,可以贡献给这一层的6个数字
$f(n,x+k)=f(n-1,x),k \in [1,2,3,4,5,6]$

```python
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp=[[0]*(5*(n+1)+1) for _ in range(n+1)]
        for k in range(6):
            dp[1][k]=1/6
        for i in range(2,n+1):
            for j in range(5*i+1):
                for k in range(6):
                    dp[i][j+k]+=(dp[i-1][j])/6
        print(dp)
        return dp[n][:5*n+1]
```
### 第三十天

[剑指 Offer 17. 打印从1到最大的n位数](https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:一行代码,但是考虑大整数的情况下,可以用深搜

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        right=pow(10,n)
        return [i for i in range(1,right)]
```

[剑指 Offer 51. 数组中的逆序对](https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=fa86zc7)


思路:快排,统计逆序对,用之前的代码

```python

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans=0
        def mergesort(seq):
            """归并排序"""
            if len(seq) <= 1:
                return seq
            mid = len(seq) // 2  # 将列表分成更小的两个列表
            # 分别对左右两个列表进行处理，分别返回两个排序好的列表
            left = mergesort(seq[:mid])
            right = mergesort(seq[mid:])
            # 对排序好的两个列表合并，产生一个新的排序好的列表
            return merge(left, right)

        def merge(left, right): 
            """合并两个已排序好的列表，产生一个新的已排序好的列表"""
            result = []  # 新的已排序好的列表
            i = 0  # 下标
            j = 0
            # 对两个列表中的元素 两两对比。
            # 将最小的元素，放到result中，并对当前列表下标加1
            while i < len(left) and j < len(right):
                # 左边的小,正常
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                # 右边的小 ,是逆序,并且左边的往后也构成逆序
                else:
                    result.append(right[j])
                    j += 1
                    nonlocal ans
                    ans+=len(left)-i
            result += left[i:]
            result += right[j:]
            return result
        mergesort(nums)
        return ans 
```

### 第三十一天
[剑指 Offer 14- II. 剪绳子 II](https://leetcode.cn/problems/jian-sheng-zi-ii-lcof/)


题解思路:根据证明,把n长的划分为长度为3的段时,乘积最大,利用剪绳子1的方法不行,因为$max(dp[i],dp[i-j]*dp[j])$,取模之后没法用,不取模又不准

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:return 1
        if n==3:return 2
        if n==4:return 4
        MOD=1e9+7
        ans=1
        while n>4:
            ans*=3
            n-=3
            ans%=MOD
        return int((ans*n)%MOD)

```
[剑指 Offer 43. 1～n 整数中 1 出现的次数](https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)


题解思路:主要是数学推到,对于123456这个数字,假设当前的位是百位他的前面一定就有123*100次1出现,但是他的后面要分情况,456还是会出现100次1,156只出现了56次,056不出现1.后面三种情况可以总结位$min(max(n-100+1,0),100)$,循环遍历每一位数字就行

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        k=0
        ans=0
        # ppp=pow(10,k)
        ppp=1
        while n>=ppp:
            temp=0
            front=n//(ppp*10)
            temp+=(front*ppp)

            back=n%(ppp*10)
            temp+=min(max(back-ppp+1,0),ppp)
            ans+=temp
            k+=1
            ppp*=10
        return ans 

```
[剑指 Offer 44. 数字序列中某一位的数字](https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)


思路:根据规律,前面是1位数长度是10个,2位数长度是$2*10*9$,三位数是$3*100*9$,...,根据这个规律,可以找到n应该是在几位数上,然后除以位数的长度,就找到了在哪个数字上,在对长度取余就是这个数字的第几位

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<10:return n
        # 10
        # 20*9
        # 300*9
        # 4000*9
        n-=10
        index=2
        while n:
            temp=index*pow(10,index-1)*9
            if n<temp:
                break
            n-=temp
            index+=1
        a=n//index
        b=n%index
        # 找到所在的数字
        num=pow(10,index-1)+a
        return int(str(num)[b])

```

### 总结



