---
title: 快速傅里叶变换(FFT)求多项式乘法
categories:
  - 学习笔记
tags:
  - 多项式乘法
  - 快速傅里叶变换
  - FFT
toc: true# 是否启用内容索引
---
[toc]

推荐一篇写的很好的[课件](https://www.renrendoc.com/paper/201816620.html)


## 多项式的表示与乘法
1. 系数表示法
多项式$A(x)=\sum_{i=0}^{n} a_ix^i$的系数表示就是
$a=(a_0,a_1,...,a_n)^T$

>如果用系数表示,多项式乘法的复杂度是$O(n^2)$,就是和平时手算过程一样


2. 点值表示法
n+1个不同的点能唯一确定n次多项式系数

对于多项式$A(x),B(x)$
$A(x):\left\{\left(x_{0}, y_{0}\right),\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \ldots,\left(x_{n}, y_{n}\right)\right\},$

$B(x):\left\{\left(x_{0}, y_{0}^{\prime}\right),\left(x_{1}, y_{1}^{\prime}\right),\left(x_{2}, y_{2}^{\prime}\right), \ldots,\left(x_{n}, y_{n}^{\prime}\right)\right\}$


>设 $C(x) = A(x) B(x)$,因为$C(x)$的系数是2n,所以要在$A(x)和B(x)$上取2n个不同的点才行,$C(x)$的点值表示为
$\left\{\left(x_{0}, y_{0} y_{0}^{\prime}\right),\left(x_{1}, y_{1} y_{1}^{\prime}\right),\left(x_{2}, y_{2} y_{2}^{\prime}\right), \ldots,\left(x_{2 n}, y_{2 n} y_{2 n}^{\prime}\right)\right\}$
点值表示的多项式乘法复杂度为$O(n)$


## 系数表示法与点值表示法的转换
![](https://image.yayan.xyz/20221119121436.png)
系数到点(也叫求值):$Xa=y$
因为系数矩阵行列式不为0,所以可逆.
点到系数(也叫插值):$a=X^{-1}y$

## 单位复数根
n次单位复数根满足$w^n=1$,n次单位复数根敲好有n个
复杂证明略过,n次单位根的所有根,作为计算点值的$x$

## 离散傅里叶变换

对于  n  次多项式  $A(x)=\sum_{i=0}^{n} a_{i} x^{i}$ ,

其系数形式为  $a=\left(a_{0}, a_{1}, \ldots, a_{n}\right)^{T}$ .

设 $ y_{k}=A\left(\omega_{n}^{k}\right)=\sum_{i=0}^{n} a_{i} \omega_{n+1}^{k i}, 0 \leq k \leq n, k \in N $,

则向量 $ y=\left(y_{0}, y_{1}, \ldots, y_{n}\right)^{T} $

就是系数向量 $ a=\left(a_{0}, a_{1}, \ldots, a_{n}\right)^{T} $ 的离散傅里叶变换.

但是离散傅里叶变换的复杂度仍是$O(n^2)$

## 快速傅里叶变换(FFT)

FFT 将$A(x)$拆分为奇数下标与偶数下标的系数


$A^{[0]}(x)=a_{0}+a_{2} x+a_{4} x^{2}+\cdots+a_{n-1} x^{\frac{n-1}{2}},$


$A^{[1]}(x)=a_{1}+a_{3} x+a_{5} x^{2}+\cdots+a_{n} x^{\frac{n-1}{2}} .$

 $A^{[0]}(x)$  包含  A  所有偶数下标的系数, $ A^{[1]}(x)$  数下标的系数, 于是有:

$A(x)=A^{[0]}\left(x^{2}\right)+x A^{[1]}\left(x^{2}\right) .$

所以, 求 $ A(x)$  在  $\omega_{n+1}^{0}, \omega_{n+1}^{1}, \ldots, \omega_{n+1}^{n}$  处的值的问题转化为:
a. 求次数为 $ \frac{n}{2}$  的多项式 $ A^{[0]}(x), A^{[1]}(x) $ 
在点 $\left(\omega_{n+1}^{0}\right)^{2},\left(\omega_{n+1}^{1}\right)^{2}, \ldots,\left(\omega_{n+1}^{n}\right)^{2}$  处的取值.

递归即可得到结果.


>复杂度
$T(n)=2 T\left(\frac{n}{2}\right)+\Theta(n)$

然后进行点值乘法,得到点值的结果,再利用逆变换为系数表达.


## 具体流程

1. 加倍多项式次数
通过加入  $n$  个系数为 0 的高阶项, 把多项式 $ A(x)  和  B(x)$  变为次数为  $2 n$  的 多项式, 并构造其系数表达.
2. 求值
通过应用 $ 2(n+1) $ 阶的 $FFT $计算出  $A(x)  和  B(x) $ 长度为 $ 2(n+1) $ 的点值表达. 这些点值表达中包含了两个多项式在 $ 2(n+1) $ 次单位根处的取值.
3. 逐点相乘
把  $A(x)  的值与  B(x) $的值逐点相乘, 可以计算出  $C(x)=A(x) B(x) $ 的点值表 达, 这个表示中包含了 $ C(x)  在每个  2(n+1) $ 次单位根处的值.
4. 揷值
通过对  $2(n+1) $ 个点值应用 FFT, 计算其逆 DFT, 就可以构造出多项式$C(x)$的系数表达

由于 $ 1 、 3 $ 的时间复杂度为 $ \Theta(n)$, $2 、 4 $ 的时间复杂度为  $\Theta\left(n \log _{2} n\right)$ ,
因此整个算法的时间复杂度为 $ \Theta\left(n \log _{2} n\right)$ .


## python 代码

```python
import math
# 定义Π
PI = 3.1415926
# 定义复数
class complex:
    def __init__(self,real=0,virtual=0) -> None:
        self.real=real
        self.virtual=virtual
    
    def __str__(self) -> str:
        return f'real:{self.real}  virtual:{self.virtual}\n'
    
# 复数的乘法加法减法
def complex_mut(a,b):
    ret=complex()
    ret.real = a.real * b.real - a.virtual * b.virtual
    ret.virtual = a.real * b.virtual + a.virtual * b.real
    return ret
    
    
def complex_add(a,b):
    ret=complex()
    ret.real = a.real + b.real
    ret.virtual = a.virtual + b.virtual
    return ret


def complex_sub(a,b):
    ret=complex()
    ret.real = a.real - b.real
    ret.virtual = a.virtual - b.virtual
    return ret
    
# 获取i次n复根
def get_w(n,k,inverse):
    w=complex()
    # 根据欧拉函数获得w
    accy=round(PI*2*k/n,6)
    # 逆傅里叶变换sin前面要有-
    if inverse:
        w.real=round(math.cos(accy),6)
        w.virtual=round(-math.sin(accy),6)
    else:
        w.real=round(math.cos(accy),6)
        w.virtual=round(math.sin(accy),6)
    return w

# 快速傅里叶变换
def FFT(coefficient,n,inverse):
    # 如果n==1了直接返回系数
    if n==1:
        return coefficient
    # 用于存放奇偶次项
    odd,even=[],[]
    for index in range(n):
        if index&1:
            odd.append(coefficient[index])
        else:
            even.append(coefficient[index])
    # 对奇偶次项分别计算快速傅里叶变换
    e_k=FFT(even,n//2,inverse)
    d_k=FFT(odd,n//2,inverse)
    # 计算第k个点和第k+n//2个点的y坐标
    y_k,y_k_2=[],[]
    for i in range(n//2):
        w=get_w(n,i,inverse)
        y_k.append(complex_add(e_k[i],complex_mut(w,d_k[i])))
        y_k_2.append(complex_sub(e_k[i],complex_mut(w,d_k[i])))
    # 返回n个点的y坐标
    return y_k+y_k_2
    
        
def polynomial_mul(coefficient_a,coefficient_b):
    # 本来是坐标代表高位
    # 现在反过来,左边代表地位,索引就是x的项数
    coefficient_a=coefficient_a[::-1]
    coefficient_b=coefficient_b[::-1]
    # 计算乘积的最高次项是多少
    length=len(coefficient_a)-1+len(coefficient_b)-1
    # 取乘积的此项大的 2的n次方 方便后面FFT计算
    digitnum = 1
    while length>0:
        length>>=1
        digitnum+=1
    length = 1
    while digitnum>0:
        length<<=1
        digitnum-=1
    # 把系数变为复数,方便后面和n复根计算
    a,b=[complex() for _ in range(length+1)],[complex() for _ in range(length+1)]
    for index,item in enumerate(coefficient_a):
        a[index].real=item
    for index,item in enumerate(coefficient_b):
        b[index].real=item
    # 对系数a,b进行快速傅里叶变换
    FFT_a=FFT(a,length,inverse=False)
    FFT_b=FFT(b,length,inverse=False)
    c=[]
    # 对变换得到的y坐标进行点值乘法
    for index in range(length):
        c.append(complex_mut(FFT_a[index],FFT_b[index]))
    # 对c进行逆傅里叶变换
    FFT_c=FFT(c,length,inverse=True)
    # 取c的实部才是结果
    ans=[]
    for item in FFT_c:
        # 控制精度,因为float计算会有误差
        if item.real/length>0.05 or item.real/length<-0.05:
            # 小数点后保留2位
            # 得到的结果还需要除以n
            ans.append(round(item.real/length,2))
        else:
            ans.append(0)
    return ans
# (x2+x+1)^2
# x4+x3+x2+x3+x2+x+x2+x+1
# x4+2*x3+3*x2+2*x+1
# 0 0 0 1 2 3 2 1
if __name__=='__main__':
    # 左边代表高次项,右边代表低次项
    a=[0,3,2]
    b=[2,1,1]
    # O(nlogn)的多项式乘法
    c=polynomial_mul(a,b)
    # 打印
    astr=' + '.join([f'{item}*x^{index} ' for index,item in enumerate(a[::-1])][::-1])
    bstr=' + '.join([f'{item}*x^{index} ' for index,item in enumerate(b[::-1])][::-1])
    print(f"    {astr}")
    print(f"*   {bstr}")
    cstr=' + '.join([f'{item}*x^{index} ' for index,item in enumerate(c) if item !=0  ][::-1]  )
    print(f"=   {cstr}")

```
## C++代码
来自[知乎](https://zhuanlan.zhihu.com/p/411082641)
```C++
#include<iostream>
#include<vector>
#include<iomanip>
#include<math.h>
using namespace std;
const double PI = 3.1415926;
struct _complex{
    double x;
    double y;
};//手动封装的复数结构体，x为实部，y为虚部
_complex a[4096], b[4096];//用于存储两个多项式的系数
bool is_output[4096];//后面会用到的用于判断是否输出的一串变量
_complex omega(const int& n, const int& k,bool inverse)
{
	_complex r;
	if (!inverse)
	{
	r.x = cos(PI * 2 * k / n);
	r.y = sin(PI * 2 * k / n);
	}
	else
	{
		r.x = cos(PI * 2 * k / n);
		r.y = -sin(PI * 2 * k / n);
	}
	return r;
}//用于插复根
inline _complex operator*(_complex a, _complex b)
{
	_complex r;
	r.x = a.x * b.x - a.y * b.y;
	r.y = a.x * b.y + a.y * b.x;
	return r;
}
inline _complex operator+(_complex a, _complex b)
{
	_complex r;
	r.x = a.x + b.x;
	r.y = a.y + b.y;
	return r;
}
inline _complex operator-(_complex a, _complex b)
{
	_complex r;
	r.x = a.x - b.x;
	r.y = a.y - b.y;
	return r;
}
//因为没有用到除法，这里我就没有重载除的函数
void Real_DFT(_complex* a, bool inverse, int anum)//这个inverse表示是否为反变换，false为否，true表示是
{
	if (anum == 1)
		return;
	vector<_complex> buf1, buf2;//buf1和buf2为两个缓冲数组，用于暂存变换中各项系数
	for (int i = 0; i < anum ; i++)
	{
		if (i & 1)
		{
			buf2.push_back(a[i]);//奇数项
		}
		else
		{
			buf1.push_back(a[i]);//偶数项
		}
	}
	for (int i = 0; i < anum / 2; i++)
	{
		a[i] = buf1[i];
		a[i + anum / 2] = buf2[i];
	}//拆分排序后重新赋值回a，为下一步排序准备
	Real_DFT(a, inverse, anum / 2);
	Real_DFT(a + anum / 2, inverse, anum / 2);//奇偶数项拆开后迭代继续拆分
	int armlength = anum / 2;
	for (int i = 0; i < armlength; i++)
	{
		_complex t = omega(anum, i, inverse);
		buf1[i] = a[i] + t * a[i + anum / 2];//低次复根走这边插
		buf2[i] = a[i] - t * a[i + anum / 2];//高次复根走这边插
	}//这里继续用到了buf数组只是为了暂存，没有别的意思
	for (int i = 0; i < anum / 2; i++)
	{
		a[i] = buf1[i];
		a[i + anum / 2] = buf2[i];
	}//重新赋值回去
	return;
}
int main()
{
//inport data
	int numa = 0, numb = 0;//numa是a多项式的项数，numb同理
	cin >> numa;
	int ptr0 = 0, maxa = 0, sum = 0, ptr1 = 0,maxb=0;//maxa存储a多项式中的最高次幂，maxb同理
	for (int i = 0; i<numa; i++)
	{
		int id = 0;
		cin >> id;
		maxa = maxa > id ? maxa : id;
		cin >> a[id].x;
	}
	cin >> numb;
	for (int i = 0; i < numb; i++)
	{
		int id = 0;
		
		cin >> id;
		maxb = maxb > id ? maxb : id;
		cin >> b[id].x;
	}
	sum = maxa + maxb;
//decide complete num
	int digitnum = 1;
	for (; sum > 0; sum >>= 1, digitnum++);
	sum = 1;
	for (; digitnum > 0; sum <<= 1, digitnum--);//由于傅里叶变换要求插值数为2的整数次幂
//这里首先确定多项式相乘后最多的项数也就是sum然后找到第一个比sum大的2的整数次幂的数，将sum重置为这个2的整数次幂
//Fast Fourier Transform
	Real_DFT(a, false, sum);
	Real_DFT(b, false, sum);
	for (int i = 0; i < sum; i++)
		a[i] = a[i] * b[i];//这一步就是上文没有细讲的点值表达式相乘，还是挺好搞的
	Real_DFT(a, true, sum);
//export data
	int num=0;
	for (int i = 0; i <= sum; i++)
	{
		if (a[i].x / sum > 0.05||a[i].x/sum<-0.05)//遍历得到的结果，如果这个数的绝对值大于0.05（题目要求的0.1精度，根据四舍五入原则判断），则准备输出
		{
			num++;
			is_output[i] = 1;
		}
	}
	cout  << num;
	for (int i = sum; i >=0; i--)
	{
		if(is_output[i]==1)
			cout << " " <<i<<" "<< std::fixed << setprecision(1) << (a[i].x / sum);
	}
	return 0;
}

输入
2 1 2.4 0 3.2
2 2 1.5 1 0.5

输出
3 3 3.6 2 6.0 1 1.6
```